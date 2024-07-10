


###################Graph Functions"""""""""""""""""""""""""""""""""""

def DF_based_on_Entities(entityList, entityIDlists, EntOrgAbrNum, EntitiesColors, ListEnDFSHow, case_selector1,
                         case_selector2, case_selector_activation, c_white, c_black, dot, driver,activityScenario, colTitle, graphviz_QueryLocation):
    for eachEntity, EntityIDList, Color, Show in zip(entityList, entityIDlists, EntitiesColors, ListEnDFSHow):
        if Show == 1:
            for eachID in EntityIDList:

                Node_Color = c_white
                Edge_Color = Color
                edge_font_color = Color

                Node_Around_Color = c_black
                Edge_width = "1"
                show_lifecycle = False

                if activityScenario == "Activity_Label":
                    asExpression1 = " "
                    asExpression2 = " "
                    asExpression3 = " "
                    asExpression4 = " "
                if activityScenario == "Concept_Label" or activityScenario == "Concept_Label_Level":
                    asExpression1 = "-[:MAPPED_TO]->(m1)"
                    asExpression2 = "-[:MAPPED_TO]->(m2)"
                    asExpression3 = ",m1,m2"
                    asExpression4 = ",m1"


                if case_selector_activation == False:
                    actExpression1 =  " "
                    actExpression2 = " "
                if case_selector_activation == True:
                    actExpression1 =  " AND " + case_selector1
                    actExpression2 = " AND " + case_selector2


                query1 = f'''     

                    match (n1:{eachEntity}{{Type:\"{eachEntity}\"}})<-[:CORR]-(e1: Event) -[df: DF{{Type:\"{eachEntity}\"}}]-> (e2:Event) -[: CORR]-> (n2:{eachEntity} {{Type:\"{eachEntity}\"}})
                    match (e1)-[:OBSERVED]->(a1){asExpression1}
                    match (e2)-[:OBSERVED]->(a2){asExpression2}
                    WHERE n1.ID="{eachID}" AND n2.ID="{eachID}"  and df.ID="{eachID}" {actExpression2} 
                    return distinct a1,e1, df, e2,a2 {asExpression3}  

                                    '''


                print(query1)
                with open(graphviz_QueryLocation, 'a') as file:
                    file.write(f'''//DF_based_on_Entities''')
                    file.write(f'''\n{query1}\n\n''')

                dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
                         fontsize="8", margin="0")

                with driver.session() as session:
                    record1 = session.run(query1).values()

                if record1:
                    e1_Neo4J_ID = [item[1].id for item in record1]
                    e2_Neo4J_ID = [item[3].id for item in record1]
                    df_EntityType = [item[2]["Type"] for item in record1]
                    df_Entity_ID = [item[2]["ID"] for item in record1]

                    if activityScenario == "Activity_Label":
                        e1_Activity = [item[0][colTitle] for item in record1]
                        e2_Activity = [item[4][colTitle] for item in record1]
                    else:
                        e1_Activity = [item[5][colTitle] for item in record1]
                        e2_Activity = [item[6][colTitle] for item in record1]

                    print("e1_Activity=", e1_Activity)
                    print("e1_Neo4J_ID=", e1_Neo4J_ID)
                    print("e2_Activity=", e2_Activity)
                    print("e2_Neo4J_ID=", e2_Neo4J_ID)
                    print("df_Entity_ID=", df_EntityType)
                    print("df_EntityType=", df_Entity_ID)

                    if show_lifecycle:
                        e1_lifecycle = [item[1]["lifecycle"] for item in record1]

                    for i in range(len(record1)):
                        # print(i)

                        if show_lifecycle:
                            e1_name = e1_Activity[i] + '\n' + e1_lifecycle[i][0:5]
                        else:
                            e1_label = e1_Activity[i].replace(' ', '\n')
                            e2_label = e2_Activity[i].replace(' ', '\n')

                        Rel_label = str((df_EntityType[i])[:EntOrgAbrNum]) + '_' + str(df_Entity_ID[i])
                        pen_width = Edge_width

                        # print("e1_label=", e1_label)
                        # print("e2_label=", e2_label)
                        # print("Rel_label=", Rel_label)

                        dot.node(str(e1_Neo4J_ID[i]), e1_label, color=Node_Around_Color, penwidth="2", style="filled",
                                 fillcolor=Node_Color)
                        dot.node(str(e2_Neo4J_ID[i]), e2_label, color=Node_Around_Color, penwidth="2", style="filled",
                                 fillcolor=Node_Color)
                        dot.edge(str(e1_Neo4J_ID[i]), str(e2_Neo4J_ID[i]), label=Rel_label, color=Edge_Color,
                                 penwidth=pen_width, fontname="Helvetica", fontsize="8",
                                 fontcolor=edge_font_color)

                if not record1:



                    query2 = f'''     
                                                match(e1: Event) -[: CORR]-> (n1:{eachEntity} {{Type:\"{eachEntity}\"}})
                                                match (e1)-[:OBSERVED]->(a1){asExpression1}
                                                WHERE n1.ID="{eachID}"   {actExpression1} 
                                                return distinct e1,a1{asExpression4}  
                                         '''



                    print(query2)
                    with open(graphviz_QueryLocation, 'a') as file:
                        file.write(f'''//DF_based_on_Entities''')
                        file.write(f'''\n{query2}\n\n''')

                    dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
                             fontsize="8", margin="0")

                    with driver.session() as session:
                        record2 = session.run(query2).values()
                        print(record2)

                        e1_Neo4J_ID = [item[0].id for item in record2]

                        if activityScenario == "Activity_Label":
                            e1_Activity = [item[1][colTitle] for item in record2]
                        else:
                            e1_Activity = [item[2][colTitle] for item in record2]

                        print(e1_Activity)
                        print(e1_Neo4J_ID)

                        if show_lifecycle:
                            e1_lifecycle = [item[1]["lifecycle"] for item in record2]

                        for i in range(len(record2)):
                            # print(i)

                            if show_lifecycle:
                                e1_name = e1_Activity[i] + '\n' + e1_lifecycle[i][0:5]
                            else:
                                e1_label = e1_Activity[i].replace(' ', '\n')

                            dot.node(str(e1_Neo4J_ID[i]), e1_label, color=Node_Around_Color, penwidth="2",
                                     style="filled",
                                     fillcolor=Node_Color)


def DF_based_on_ID(entityList, refEntityIDlists, ListEnOrgRelDFShow, case_selector1, case_selector2,
                   case_selector_activation, c_white, c_black, SubEntities_Color, dot, driver, graphviz_QueryLocation):
    for eachEntity, EntityIDList, Show in zip(entityList, refEntityIDlists, ListEnOrgRelDFShow):
        print("EntityIDList=", EntityIDList)
        if Show == 1 and EntityIDList:
            for eachID in EntityIDList:

                edge_color = SubEntities_Color
                fontcolor = SubEntities_Color
                edge_width = "1"


                if case_selector_activation == True:
                    query = f'''
                                        MATCH (n3:{eachEntity}{{Type:\"{eachID}\"}})<-[:CORR]-(e1) -[df:DF{{Type:\"{eachID}\"}}]-> (e2:Event) -[:CORR]-> (n4:{eachEntity}{{Type:\"{eachID}\"}})
                                        MATCH (n1:{eachEntity}{{Type:\"{eachEntity}\"}})<-[:CORR]-(e1) -[df:DF{{Type:\"{eachID}\"}}]-> (e2:Event) -[:CORR]-> (n2:{eachEntity}{{Type:\"{eachEntity}\"}})  
                                        WHERE {case_selector2}
                                        RETURN distinct e1,df,e2
                                        '''

                else:
                    query = f'''
                                        MATCH (n3:{eachEntity}{{Type:\"{eachID}\"}})<-[:CORR]-(e1) -[df:DF{{Type:\"{eachID}\"}}]-> (e2:Event) -[:CORR]-> (n4:{eachEntity}{{Type:\"{eachID}\"}})
                                        MATCH (e1) -[df:DF{{Type:\"{eachID}\"}}]-> (e2:Event)
                                        RETURN distinct e1,df,e2
                                        '''
                print(query)
                with open(graphviz_QueryLocation, 'a') as file:
                    file.write(f'''//DF_based_on_ID''')
                    file.write(f'''\n{query}\n\n''')

                dot.attr("node", shape="square", fixedsize="true", width="0.4", height="0.4", fontname="Helvetica",
                         fontsize="8", margin="0")

                with driver.session() as session:
                    record = session.run(query).values()

                e1_Neo4J_ID = [item[0].id for item in record]
                e2_Neo4J_ID = [item[2].id for item in record]
                df_EntityType = [item[1]["Type"] for item in record]

                print("e1_Neo4J_ID=", e1_Neo4J_ID)
                print("e2_Neo4J_ID=", e2_Neo4J_ID)
                print("df_EntityType=", df_EntityType)

                for i in range(len(record)):
                    Rel_label = (df_EntityType[i])[0:]
                    pen_width = edge_width

                    dot.edge(str(e1_Neo4J_ID[i]), str(e2_Neo4J_ID[i]), label=Rel_label, color=edge_color,
                             penwidth=pen_width, fontname="Helvetica", fontsize="8", fontcolor=fontcolor)


def Adding_Entities_ID_ForFirstEvent(entityList, entityIDlists, EntitiesColors, ListEnDFSHow, case_selector1,
                                     case_selector_activation, c_white, c_black, dot, driver, graphviz_QueryLocation):
    for eachEntity, EntityIDList, Color, Show in zip(entityList, entityIDlists, EntitiesColors, ListEnDFSHow):
        if Show == 1:
            for eachID in EntityIDList:

                Node_Around_Color = Color
                Node_Color = Color
                Edge_Color = Color
                fontcolor = c_white

                if case_selector_activation == False:
                    actExpression1 =  " "
                if case_selector_activation == True:
                    actExpression1 =  " AND " + case_selector1


                query2 = f'''
                        MATCH(e: Event) -[corr: CORR]-> (n1:{eachEntity})
                        WHERE n1.Type = "{eachEntity}" and n1.ID="{eachID}"  {actExpression1}
                        return e, n1
                        order by e.timestamp, e.idx
                        limit 1
                         '''

                print(query2)
                with open(graphviz_QueryLocation, 'a') as file:
                    file.write(f'''//Adding_Entities_ID_ForFirstEvent''')
                    file.write(f'''\n{query2}\n\n''')

                dot.attr("node", shape="circle", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
                         fontsize="8", margin="0")

                with driver.session() as session:
                    record2 = session.run(query2).values()

                if record2:
                    n_Neo4J_ID = [item[1].id for item in record2]
                    e_Neo4J_ID = [item[0].id for item in record2]

                    ID_Value = eachID

                    # print(n_Neo4J_ID)
                    # print(e_Neo4J_ID)

                    Entity_Node_label = str(ID_Value)
                    Event_Node_ID = str(e_Neo4J_ID[0])
                    Entity_Node_ID = str(n_Neo4J_ID[0])

                    dot.node(Entity_Node_ID, Entity_Node_label, color=Node_Around_Color, style="filled",
                             fillcolor=Node_Color,
                             fontcolor=fontcolor)
                    dot.edge(Entity_Node_ID, Event_Node_ID, style="dashed", arrowhead="none",
                             color=Edge_Color)


def Adding_Entities(entityList, entityIDlists, EntitiesColors, ListEnDFSHow, c_white, c_black, dot, driver,
                    case_selector2, case_selector_activation, graphviz_QueryLocation):
    list3 = []
    for eachEntity, EntityIDList, Show in zip(entityList, entityIDlists, ListEnDFSHow):
        if Show == 1:
            list1 = []
            for eachID in EntityIDList:
                list2 = []
                if case_selector_activation == False:
                    actExpression2 =  " "
                if case_selector_activation == True:
                    actExpression2 =  " AND " + case_selector2


                query1 = f'''     

                    match (n1:{eachEntity}{{Type:\"{eachEntity}\"}})<-[:CORR]-(e1: Event) -[df: DF{{Type:\"{eachEntity}\"}}]-> (e2:Event) -[: CORR]-> (n2:{eachEntity} {{Type:\"{eachEntity}\"}})
                    match (e1)-[:OBSERVED]->(a1)
                    match (e2)-[:OBSERVED]->(a2)
                    WHERE n1.ID="{eachID}" AND n2.ID="{eachID}"  {actExpression2} 
                    return a1,e1, df, e2,a2

                                    '''


                print(query1)
                with open(graphviz_QueryLocation, 'a') as file:
                    file.write(f'''//Adding_Entities''')
                    file.write(f'''\n{query1}\n\n''')

                with driver.session() as session:
                    record1 = session.run(query1).values()

                if record1:
                    df_EntityType = [item[2]["Type"] for item in record1]
                    # print("df_EntityType=", df_EntityType)
                    list2.extend(df_EntityType)

                list1.extend(list2)
            list3.extend(list1)
        print("list3=", list3)
        list3 = list(dict.fromkeys(list3))
        print("list3=", list3)

    for Entity_Alias, Color, posit in zip(entityList, EntitiesColors, range(1, 70)):
        print(posit)

        Node_Around_Color = c_white
        Node_Color = Color
        Node_fontcolor = c_black
        Node_label = f"{Entity_Alias}"
        NodeColorStriped = f"{Node_Around_Color}:{Node_Around_Color}:{Node_Around_Color}:{Node_Color}"

        if Entity_Alias in list3:
            print(Entity_Alias)

            with dot.subgraph(name="cluster_0", comment='name2') as subDot:
                subDot.attr(style='filled', color=Node_Around_Color)
                subDot.attr(label='\nEntities:')

                subDot.node_attr.update(shape="rectangle", fixedsize="True", width="0.8", height="0.2",
                                        fontname="Helvetica",
                                        fontsize="8", margin="0")

                subDot.node(str(posit + 99999), Node_label, color=Node_Around_Color, style="striped",
                            fillcolor=NodeColorStriped,
                            fontcolor=Node_fontcolor)

