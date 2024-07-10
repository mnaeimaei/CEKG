

###################Graph Functions"""""""""""""""""""""""""""""""""""

def DF_based_on_Entities (entityList,entityIDlists, EntOrgAbrNum, EntitiesColors, ListEnDFSHow, c_white, c_black, dot, driver,case_selector,
                         case_selector_activation,activityScenario,  colTitle, graphviz_QueryLocation):
    for eachEntity,EntityIDList, Color, Show in zip(entityList, entityIDlists, EntitiesColors, ListEnDFSHow):
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
                    asExpression5 = " "
                if activityScenario == "Concept_Label" or activityScenario == "Concept_Label_Level":
                    asExpression1 = "-[:MAPPED_TO]->(m1)"
                    asExpression2 = "-[:MAPPED_TO]->(m2)"
                    asExpression3 = ",m1,m2"
                    asExpression4 = ",m1"
                    asExpression5 = ",m2"


                if case_selector_activation == False:
                    actExpression1 =  " "
                if case_selector_activation == True:
                    actExpression1 =  " AND " + case_selector

                dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
                         fontsize="8", margin="0")

                query1 = f'''     
                    match(f: Feature) -[r: DF{{Type:\"{eachEntity}\", Category:"wProperty" }}]-> (e2:Event) -[: CORR]-> (n1:{eachEntity} {{Type:\"{eachEntity}\"}})
                    match (n1:{eachEntity} {{Type:\"{eachEntity}\"}}) <- [: CORR] -(e1: Event) -[df: DF{{Type:\"{eachEntity}\", Category:"woProperty" }}]-> (e2:Event) -[: CORR]-> (n1:{eachEntity} {{Type:\"{eachEntity}\"}})
                    match (e1)-[:OBSERVED]->(a1) {asExpression1}
                    match (e2)-[:OBSERVED]->(a2) {asExpression2}
                    WHERE n1.ID="{eachID}" and df.ID="{eachID}" and r.ID="{eachID}" {actExpression1}
                    return distinct f, a1,e1, df, e2,a2 {asExpression3}                   
                    '''

                print(query1)
                with open(graphviz_QueryLocation, 'a') as file:
                    file.write(f'''//DF_based_on_Entities''')
                    file.write(f'''\n{query1}\n\n''')

                with driver.session() as session:
                    record1 = session.run(query1).values()
                    # print(record1)

                if record1:

                    f_Neo4J_ID = [item[0].id for item in record1]
                    f_ID = [item[0]["ID"] for item in record1]
                    f_edge= [item[0]["label"] for item in record1]
                    f_node= [item[0]["Value"] for item in record1]
                    e1_Neo4J_ID = [item[2].id for item in record1]
                    e2_Neo4J_ID = [item[4].id for item in record1]
                    df_EntityType = [item[3]["Type"] for item in record1]
                    df_Entity_ID = [item[3]["ID"] for item in record1]
                    e1_Event = [item[2]["Event"] for item in record1]
                    e2_Event = [item[4]["Event"] for item in record1]
                    # print(e1_Neo4J_ID)
                    # print(e2_Neo4J_ID)

                    if activityScenario == 'Activity_Label':
                        e1_Activity = [item[1][colTitle] for item in record1]
                        e2_Activity = [item[5][colTitle] for item in record1]
                    else:
                        e1_Activity = [item[6][colTitle] for item in record1]
                        e2_Activity = [item[7][colTitle] for item in record1]

                    f_Activity = [item[0]["Value"] + "=" + item[0]["label"] for item in record1]
                    print("f_Activity=", f_Activity)

                    f1_Neo4J_ID_new = [[activity, str(ID), e3] for activity, ID, e3 in
                                       zip(f_Activity, e1_Neo4J_ID, e1_Event)]
                    print("f1_Neo4J_ID_new =", f1_Neo4J_ID_new)
                    f1_Neo4J_ID_new_2nd = []
                    for sublist in f1_Neo4J_ID_new:
                        sublist[0] = '_'.join(sublist)
                        f1_Neo4J_ID_new_2nd.append(sublist[0])

                    print("e2_Neo4J_ID=", e2_Neo4J_ID)
                    print("e2_Activity=", e2_Activity)
                    print("e2_Neo4J_ID=", e2_Neo4J_ID)
                    print("df_Entity_ID=", df_EntityType)
                    print("df_EntityType=", df_Entity_ID)

                    for i in range(len(record1)):
                        f1_name = f1_Neo4J_ID_new_2nd[i].replace(' ', '\n')
                        e2_label = e2_Activity[i].replace(' ', '\n')

                        Rel_label = str((df_EntityType[i])[:EntOrgAbrNum]) + '_' + str(df_Entity_ID[i])
                        pen_width = Edge_width

                        # print("e1_label=", e1_label)
                        # print("e2_label=", e2_label)
                        # print("Rel_label=", Rel_label)

                        #print(str(f1_Neo4J_ID_new_2nd[i]))
                        #print(str(e2_Event[i]))

                        dot.node(str(f1_Neo4J_ID_new_2nd[i]), str(f_node[i]), color=Node_Around_Color, penwidth="2",
                                 style="filled",
                                 fillcolor=Node_Color)

                        dot.node(str(e2_Neo4J_ID[i]), e2_label, color=Node_Around_Color, penwidth="2", style="filled",
                                 fillcolor=Node_Color)

                        dot.edge(str(f1_Neo4J_ID_new_2nd[i]), str(e2_Neo4J_ID[i]), label=Rel_label, color=Edge_Color,
                                 penwidth=pen_width, fontname="Helvetica", fontsize="8",
                                 fontcolor=edge_font_color)

###################################################

                query2 = f'''                
                    match (f: Feature)<-[r:Assign]- (e1:Event) -[: CORR]-> (n1:{eachEntity} {{Type:\"{eachEntity}\"}})
                    match (e1)-[:OBSERVED]->(a1) {asExpression1}
                    WHERE n1.ID="{eachID}"  {actExpression1}
                    return distinct f, a1,e1 {asExpression4}                          
                                    '''

                print(query2)
                with open(graphviz_QueryLocation, 'a') as file:
                    file.write(f'''//DF_based_on_Entities''')
                    file.write(f'''\n{query2}\n\n''')

                with driver.session() as session:
                    record2 = session.run(query2).values()
                    # print(record1)

                if record2:

                    f_Neo4J_ID = [item[0].id for item in record2]
                    f_edge= [item[0]["label"] for item in record2]
                    f_node= [item[0]["Value"] for item in record2]
                    f_ID = [item[0]["ID"] for item in record2]
                    e1_Neo4J_ID = [item[2].id for item in record2]
                    e1_Event = [item[2]["Event"] for item in record2]


                    # print(e1_Neo4J_ID)
                    # print(e2_Neo4J_ID)

                    if activityScenario == 'Activity_Label':
                        e1_Activity = [item[1][colTitle] for item in record2]
                    else:
                        e1_Activity = [item[3][colTitle] for item in record2]


                    f_Activity = [item[0]["Value"] + "=" + item[0]["label"] for item in record2]
                    print("f_Activity=", f_Activity)

                    f1_Neo4J_ID_new = [[activity, str(ID), e3] for activity, ID, e3 in
                                       zip(f_Activity, e1_Neo4J_ID, e1_Event)]
                    print("f1_Neo4J_ID_new =", f1_Neo4J_ID_new)
                    f1_Neo4J_ID_new_2nd = []
                    for sublist in f1_Neo4J_ID_new:
                        sublist[0] = '_'.join(sublist)
                        f1_Neo4J_ID_new_2nd.append(sublist[0])

                    print("f1_Neo4J_ID_new_2nd=", f1_Neo4J_ID_new_2nd)



                    for i in range(len(record2)):
                        f1_name = f1_Neo4J_ID_new_2nd[i].replace(' ', '\n')
                        e1_label = e1_Activity[i].replace(' ', '\n')


                        pen_width = Edge_width

                        # print("e1_label=", e1_label)
                        # print("e2_label=", e2_label)
                        # print("Rel_label=", Rel_label)

                        #print(str(f1_Neo4J_ID_new_2nd[i]))

                        dot.node(str(f1_Neo4J_ID_new_2nd[i]), str(f_node[i]), color=Node_Around_Color,
                                 penwidth="2", style="filled",
                                 fillcolor=Node_Color)
                        dot.node(str(e1_Neo4J_ID[i]), e1_label, color=Node_Around_Color, penwidth="2", style="filled",
                                 fillcolor=Node_Color)

                        dot.edge(str(e1_Neo4J_ID[i]), str(f1_Neo4J_ID_new_2nd[i]), label=f_edge[i], color=Edge_Color,
                                 penwidth=pen_width, fontname="Helvetica", fontsize="8",
                                 fontcolor=edge_font_color)


def Adding_Entities_ID_ForFirstEvent(entityList,entityIDlists, EntitiesColors, ListEnDFSHow, c_white, c_black, dot, driver,case_selector,
                         case_selector_activation, graphviz_QueryLocation):
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
                    actExpression1 =  " AND " + case_selector



                query2 = f'''     
                            MATCH(e: Event) -[corr: CORR]-> (n1:{eachEntity})
                            WHERE n1.Type = "{eachEntity}" and n1.ID="{eachID}" {actExpression1}
                            return e, n1
                            order by e.timestamp, e.idx
                            limit 1
                         '''

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

                    ID_Value=eachID

                    #print(n_Neo4J_ID)
                    #print(e_Neo4J_ID)


                    Entity_Node_label = str(ID_Value)
                    Event_Node_ID = str(e_Neo4J_ID[0])
                    Entity_Node_ID = str(n_Neo4J_ID[0])

                    dot.node(Entity_Node_ID, Entity_Node_label, color=Node_Around_Color, style="filled",
                             fillcolor=Node_Color,
                             fontcolor=fontcolor)
                    dot.edge(Entity_Node_ID, Event_Node_ID, style="dashed", arrowhead="none",
                             color=Edge_Color)



def Adding_Entities (entityList,entityIDlists, EntitiesColors, ListEnDFSHow, c_white, c_black, dot, driver,case_selector,
                         case_selector_activation, graphviz_QueryLocation):
    list3 = []
    for eachEntity, EntityIDList, Show in zip(entityList, entityIDlists, ListEnDFSHow):
        if Show == 1:
            list1 = []
            for eachID in EntityIDList:
                list2 = []
                if case_selector_activation == False:
                    actExpression1 =  " "
                if case_selector_activation == True:
                    actExpression1 =  " AND " + case_selector


                query1 = f'''     
                        match(e1: Event) -[df: DF{{Type:\"{eachEntity}\" , Category:"woProperty"}}]-> (e2:Event) -[: CORR]-> (n1:{eachEntity} {{Type:\"{eachEntity}\"}})
                        match (e1)-[:OBSERVED]->(a1)
                        match (e2)-[:OBSERVED]->(a2)
                        WHERE n1.ID="{eachID}" {actExpression1} 
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
                    #print("df_EntityType=", df_EntityType)
                    list2.extend(df_EntityType)

                list1.extend(list2)
            list3.extend(list1)
        print("list3=",list3)
        list3 = list(dict.fromkeys(list3))
        print("list3=",list3)


    for Entity_Alias, Color, posit in zip(entityList, EntitiesColors, range(1,70)):
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