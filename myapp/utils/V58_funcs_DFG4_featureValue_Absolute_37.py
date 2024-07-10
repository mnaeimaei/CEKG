

###################Graph Functions"""""""""""""""""""""""""""""""""""

def DFC_based_on_Origins (final_DFG_List, ID_Colors, ListEnDFSHow, count, case_selector, case_selector_activation, c_white, c_black, dot, driver,activityScenario, colTitle, case_selector2, graphviz_QueryLocation):
    for EntityOrgValue_list, Show in zip(final_DFG_List, ListEnDFSHow):
        print("model_entities_derived_list=", EntityOrgValue_list)
        print("Show=", Show)
        if Show == 1:
            for model_entities in EntityOrgValue_list:
                print(model_entities)
                #print(color)
                En1 = model_entities[0]
                En1_ID = model_entities[1]
                Color_ID = model_entities[2]
                color=ID_Colors[Color_ID]

                number=count

                Node_Color = c_white
                Edge_Color = color
                edge_font_color = color

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
                    actExpression1 =  " AND " + case_selector
                    actExpression2 = " AND " + case_selector2


                dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
                             fontsize="8", margin="0")


                query1 = f'''     
                        match (f: Feature) -[r: DF_C{{En1:"{En1}", Category:"wProperty" }}]-> (c2:ActivityPropery)
                        MATCH (c1:ActivityPropery {{Type:"ActivityPropery"}}) -[df:DF_C {{Category:"wProperty"}}]-> (c2:ActivityPropery {{Type:"ActivityPropery"}})
                        match (c1:ActivityPropery){asExpression1}
                        match (c2:ActivityPropery){asExpression2}
                        WHERE df.count >= {number} and df.Type = "AbsoluteProperty" and df.En1="{En1}" and df.En1_ID="{En1_ID}" and  c1.Syn=f.Synonym and f.ID in c1.featureID {actExpression1}  
                        return distinct f, c1,df,c2{asExpression3}  
                        '''


                print(query1)
                with open(graphviz_QueryLocation, 'a') as file:
                    file.write(f'''//DFC_based_on_Origins''')
                    file.write(f'''\n{query1}\n\n''')




                with driver.session() as session:
                    record1 = session.run(query1).values()



                if record1:
                    f_Neo4J_ID = [item[0].id for item in record1]
                    f_ID = [item[0]["ID"] for item in record1]
                    f_edge= [item[0]["label"] for item in record1]
                    f_node= [item[0]["Value"] for item in record1]

                    c1_Neo4J_ID = [item[1].id for item in record1]
                    c1_feature = [item[1]["featureID"] for item in record1]
                    c1_Syn = [item[1]["Syn"] for item in record1]

                    c2_Neo4J_ID = [item[3].id for item in record1]
                    c2_feature = [item[3]["featureID"] for item in record1]

                    df_En1 = [item[2]["En1"] for item in record1]
                    df_En1_ID = [item[2]["En1_ID"] for item in record1]
                    df_count = [item[2]["count"] for item in record1]


                    if activityScenario == "Activity_Label":
                        c1_Activity = [item[1][colTitle] for item in record1]
                        c2_Activity = [item[3][colTitle] for item in record1]
                    else:
                        c1_Activity = [item[4][colTitle] for item in record1]
                        c2_Activity = [item[5][colTitle] for item in record1]


                    f_Activity = [item[0]["label"] + "=" + item[0]["Value"] for item in record1]
                    print("f_Activity=", f_Activity)

                    f1_Neo4J_ID_new = [[activity, str(ID), Syn] for activity, ID, Syn in
                                       zip(f_Activity, c1_Neo4J_ID, c1_Syn)]
                    print("f1_Neo4J_ID_new =", f1_Neo4J_ID_new)
                    f1_Neo4J_ID_new_2nd = []
                    for sublist in f1_Neo4J_ID_new:
                        sublist[0] = '_'.join(sublist)
                        f1_Neo4J_ID_new_2nd.append(sublist[0])
                    print("f1_Neo4J_ID_new_2nd =", f1_Neo4J_ID_new_2nd)

                    print("f_ID=", f_ID)
                    print("c1_Activity=", c1_Activity)
                    print("c1_Neo4J_ID=", c1_Neo4J_ID)
                    print("c2_Activity=", c2_Activity)
                    print("c2_Neo4J_ID=", c2_Neo4J_ID)
                    print("df_count=", df_count)

                    for i in range(len(record1)):
                        #print(i)

                        c1_label = c1_Activity[i].replace(' ', '\n')
                        c2_label = c2_Activity[i].replace(' ', '\n')





                        Rel_label = '#' + str(df_count[i])

                        pen_width = Edge_width

                        #print("c1_label=", c1_label)
                        #print("c2_label=", c2_label)
                        #print("Rel_label=", Rel_label)



                        dot.node(str(f1_Neo4J_ID_new_2nd[i]), str(f_node[i]), color=Node_Around_Color, penwidth="2", style="filled",
                                 fillcolor=Node_Color)
                        dot.node(str(c2_Neo4J_ID[i]), c2_label, color=Node_Around_Color, penwidth="2", style="filled",
                                 fillcolor=Node_Color)
                        dot.edge(str(f1_Neo4J_ID_new_2nd[i]), str(c2_Neo4J_ID[i]), label=Rel_label, color=Edge_Color,
                                 penwidth=pen_width,  fontname="Helvetica", fontsize="8",
                                 fontcolor=edge_font_color)



                query2 = f'''     
                        match (f: Feature) <-[ : Assign ]- (e1:Event) -[ : MONITORED] -> (c1:ActivityPropery {{Type:"ActivityPropery"}})
                        match (e1)-[:CORR]->(n1:{En1} {{ID:"{En1_ID}"}} )
                        match (c1:ActivityPropery){asExpression1}
                        WHERE  c1.Syn=f.Synonym and f.ID in c1.featureID {actExpression2}  
                        return distinct f, c1 {asExpression4}  
                        '''

                print(query2)
                with open(graphviz_QueryLocation, 'a') as file:
                    file.write(f'''//DFC_based_on_Origins''')
                    file.write(f'''\n{query2}\n\n''')

                with driver.session() as session:
                    record2 = session.run(query2).values()

                if record2:
                    f_Neo4J_ID = [item[0].id for item in record2]
                    f_ID = [item[0]["ID"] for item in record2]
                    f_edge = [item[0]["label"] for item in record2]
                    f_node = [item[0]["Value"] for item in record2]

                    c1_Neo4J_ID = [item[1].id for item in record2]
                    c1_feature = [item[1]["featureID"] for item in record2]
                    c1_Syn = [item[1]["Syn"] for item in record2]

                    if activityScenario == "Activity_Label":
                        c1_Activity = [item[1][colTitle] for item in record2]
                    else:
                        c1_Activity = [item[2][colTitle] for item in record2]


                    f_Activity = [item[0]["label"] + "=" + item[0]["Value"] for item in record2]
                    print("f_Activity=", f_Activity)

                    f1_Neo4J_ID_new = [[activity, str(ID), Syn] for activity, ID, Syn in
                                       zip(f_Activity, c1_Neo4J_ID, c1_Syn)]
                    print("f1_Neo4J_ID_new =", f1_Neo4J_ID_new)
                    f1_Neo4J_ID_new_2nd = []
                    for sublist in f1_Neo4J_ID_new:
                        sublist[0] = '_'.join(sublist)
                        f1_Neo4J_ID_new_2nd.append(sublist[0])
                    print("f1_Neo4J_ID_new_2nd =", f1_Neo4J_ID_new_2nd)
                    print("f_ID=", f_ID)
                    print("c1_Activity=", c1_Activity)
                    print("c1_Neo4J_ID=", c1_Neo4J_ID)


                    for i in range(len(record2)):
                        # print(i)

                        c1_label = c1_Activity[i].replace(' ', '\n')


                        pen_width = Edge_width

                        # print("c1_label=", c1_label)
                        # print("c2_label=", c2_label)
                        # print("Rel_label=", Rel_label)

                        dot.node(str(f1_Neo4J_ID_new_2nd[i]), str(f_node[i]), color=Node_Around_Color, penwidth="2", style="filled",
                                 fillcolor=Node_Color)
                        dot.node(str(c1_Neo4J_ID[i]), c1_label, color=Node_Around_Color, penwidth="2", style="filled",
                                 fillcolor=Node_Color)
                        dot.edge(str(c1_Neo4J_ID[i]), str(f1_Neo4J_ID_new_2nd[i]), label=f_edge[i], color=Edge_Color,
                                 penwidth=pen_width, fontname="Helvetica", fontsize="8",
                                 fontcolor=edge_font_color)



def DFC_Adding_Entities (final_DFG_List, ID_Colors, ListEnDFSHow, count, case_selector, case_selector_activation, case_selector_list, c_white, c_black, dot, driver, graphviz_QueryLocation):
    list3 = []
    for EntityOrgValue_list, Show in zip(final_DFG_List, ListEnDFSHow):
        if Show == 1:
            list1 = []
            for model_entities in EntityOrgValue_list:
                list2 = []
                En1 = model_entities[0]
                En1_ID = model_entities[1]
                number=count
                if case_selector_activation == False:
                    actExpression1 =  " "
                if case_selector_activation == True:
                    actExpression1 =  " AND " + case_selector


                query1 = f'''     
                        MATCH (c1:ActivityPropery {{Type:"ActivityPropery"}}) -[df:DF_C {{Category:"wProperty"}}]-> (c2:ActivityPropery {{Type:"ActivityPropery"}})
                        WHERE df.count >= {number} and df.Type = "AbsoluteProperty" and df.En1="{En1}" and df.En1_ID="{En1_ID}"  {actExpression1} 
                        return c1,df,c2
                        '''

                print(query1)
                with open(graphviz_QueryLocation, 'a') as file:
                    file.write(f'''//DFC_Adding_Entities''')
                    file.write(f'''\n{query1}\n\n''')

                with driver.session() as session:
                    record1 = session.run(query1).values()


                if record1:
                    df_En1_ID = [item[1]["En1_ID"] for item in record1]
                    list2.extend(df_En1_ID)


                list1.extend(list2)
            list3.extend(list1)
        #print("list3=",list3)
        list3 = list(dict.fromkeys(list3))
        #print("list3=",list3)

    for final_DFG, Show in zip(final_DFG_List, ListEnDFSHow):
        #print("final_DFG=", final_DFG)
        #print("Color=", Color)
        #print("Show=", Show)

        if Show == 1 :
            #print("final_DFG=", final_DFG)
            for model_entities, posit in zip(final_DFG, range(1,700)):
                #print(model_entities)
                #print(color)
                #print("posit=", posit)
                En1 = model_entities[0]
                En1_ID = model_entities[1]
                Color_ID = model_entities[2]
                color=ID_Colors[Color_ID]


                Node_Around_Color = c_white
                Node_Color = color
                Node_fontcolor = c_black
                NodeColorStriped = f"{Node_Around_Color}:{Node_Around_Color}:{Node_Around_Color}:{Node_Color}"

                if En1_ID in list3:
                    #print(En1_ID)
                    with dot.subgraph(name="cluster_0", comment='name2') as subDot:
                        subDot.attr(style='filled', color=Node_Around_Color)
                        subDot.attr(label=f"\n{En1}:")

                        subDot.node_attr.update(shape="rectangle", fixedsize="True", width="0.8", height="0.2",
                                                fontname="Helvetica",
                                                fontsize="8", margin="0")

                        if case_selector_activation == True:

                            if En1_ID in case_selector_list:
                                Node_label = f"{En1_ID}        "
                                subDot.node(str(posit + 999), Node_label, color=Node_Around_Color, style="striped",
                                            fillcolor=NodeColorStriped,
                                            fontcolor=Node_fontcolor)


                        else:
                            Node_label = f"{En1_ID}        "
                            subDot.node(str(posit + 999), Node_label, color=Node_Around_Color, style="striped",
                                        fillcolor=NodeColorStriped,
                                        fontcolor=Node_fontcolor)

