

###################Graph Functions"""""""""""""""""""""""""""""""""""

def DFC_based_on_Origins (EntityOrgValue, ID_Colors, count, c_white, c_black, dot, driver,activityScenario, colTitle,case_selector_activation1,case_selector_list1,case_selector1,case_selector_activation2,case_selector_list2,case_selector2,case_selector3, case_selector4, graphviz_QueryLocation ):
    for model_entities in EntityOrgValue:
        # print(model_entities)
        # print(color)
        En1 = model_entities[0]
        En2 = model_entities[1]
        En1_ID = model_entities[2]

        Color_ID = model_entities[3]
        # print(Color_ID)
        color = ID_Colors[Color_ID]

        number = count

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

        if case_selector_activation1 == False:
            actExpression1 = " "
            actExpression3 = " "
        if case_selector_activation1 == True:
            actExpression1 = " AND " + case_selector1
            actExpression3 = " AND " + case_selector3

        if case_selector_activation2 == False:
            actExpression2 = " "
            actExpression4 = " "
        if case_selector_activation2 == True:
            actExpression2 = " AND " + case_selector2
            actExpression4 = " AND " + case_selector4

        dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
                 fontsize="8", margin="0")


        query1 = f'''     
                match (f: Feature) -[r: DF_C{{En1:"{En1}", Category:"wProperty" }}]-> (c2:ActivityPropery)
                MATCH (c1:ActivityPropery {{Type:"ActivityPropery"}}) -[df:DF_C {{Category:"wProperty"}}]-> (c2:ActivityPropery {{Type:"ActivityPropery"}})
                match (c1:ActivityPropery){asExpression1}
                match (c2:ActivityPropery){asExpression2}
                WHERE df.count >= {number} and df.Type = "RelativeProperty" and df.En1="{En1}" and df.En2="{En2}" and df.En1_ID="{En1_ID}" and  c1.Syn=f.Synonym and f.ID in c1.featureID {actExpression1} {actExpression2} 
                return distinct f, c1,df,c2 {asExpression3}     
                '''


        print(query1)
        with open(graphviz_QueryLocation, 'a') as file:
            file.write(f'''//DFC_based_on_Origins''')
            file.write(f'''\n{query1}\n\n''')

        # dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
        #        fontsize="8", margin="0")

        with driver.session() as session:
            record1 = session.run(query1).values()
            print(record1)

        if record1:
            f_Neo4J_ID = [item[0].id for item in record1]
            f_ID = [item[0]["ID"] for item in record1]
            f_edge = [item[0]["label"] for item in record1]
            f_node = [item[0]["Value"] for item in record1]

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
                # print(i)

                c1_label = c1_Activity[i].replace(' ', '\n')
                c2_label = c2_Activity[i].replace(' ', '\n')

                Rel_label = '#' + str(df_count[i])

                pen_width = Edge_width


                dot.node(str(f1_Neo4J_ID_new_2nd[i]), str(f_node[i]), color=Node_Around_Color, penwidth="2", style="filled",
                         fillcolor=Node_Color)
                dot.node(str(c2_Neo4J_ID[i]), c2_label, color=Node_Around_Color, penwidth="2", style="filled",
                         fillcolor=Node_Color)
                dot.edge(str(f1_Neo4J_ID_new_2nd[i]), str(c2_Neo4J_ID[i]), label=Rel_label, color=Edge_Color,
                         penwidth=pen_width, fontname="Helvetica", fontsize="8",
                         fontcolor=edge_font_color)

        query2 = f'''     
                match (f: Feature) <-[ : Assign ]- (e1:Event) -[ : MONITORED] -> (c1:ActivityPropery {{Type:"ActivityPropery"}})
                match (e1)-[:CORR]->(n2:{En2} )
                match (e1)-[:CORR]->(n1:{En1} {{ID:"{En1_ID}"}} )
                match (c1:ActivityPropery){asExpression1}
                WHERE c1.Syn=f.Synonym and f.ID in c1.featureID {actExpression3} {actExpression4} 
                return distinct f, c1 {asExpression4}     
                '''

        print(query2)
        with open(graphviz_QueryLocation, 'a') as file:
            file.write(f'''//DFC_based_on_Origins''')
            file.write(f'''\n{query2}\n\n''')

        # dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
        #        fontsize="8", margin="0")

        with driver.session() as session:
            record2 = session.run(query2).values()
            print(record2)

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

                dot.node(str(f1_Neo4J_ID_new_2nd[i]), str(f_node[i]), color=Node_Around_Color, penwidth="2",
                         style="filled",
                         fillcolor=Node_Color)
                dot.node(str(c1_Neo4J_ID[i]), c1_label, color=Node_Around_Color, penwidth="2", style="filled",
                         fillcolor=Node_Color)
                dot.edge(str(c1_Neo4J_ID[i]), str(f1_Neo4J_ID_new_2nd[i]), label=f_edge[i], color=Edge_Color,
                         penwidth=pen_width, fontname="Helvetica", fontsize="8",
                         fontcolor=edge_font_color)

def DFC_Adding_Entities (final_DFG_List, count, ID_Colors, c_white, c_black, dot, driver,case_selector_activation1,case_selector_list1,case_selector1,case_selector_activation2,case_selector_list2,case_selector2 , graphviz_QueryLocation):
    if case_selector_activation2:
        Entity2ID=",".join(case_selector_list2)
        print(Entity2ID)
    else:
        Entity2ID=" "

    list3 = []
    for model_entities in final_DFG_List:
        list2 = []
        En1 = model_entities[0]
        En2 = model_entities[1]
        En1_ID = model_entities[2]
        number = count
        if case_selector_activation1 == False:
            actExpression1 = " "
        if case_selector_activation1 == True:
            actExpression1 = " AND " + case_selector1

        if case_selector_activation2 == False:
            actExpression2 = " "
        if case_selector_activation2 == True:
            actExpression2 = " AND " + case_selector2

        dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
                 fontsize="8", margin="0")


        query1 = f'''     
                            MATCH (c1:ActivityPropery {{Type:"ActivityPropery"}}) -[df:DF_C {{Category:"wProperty"}} ]-> (c2:ActivityPropery {{Type:"ActivityPropery"}})
                            WHERE df.count >= {number} and df.Type = "RelativeProperty" and df.En1="{En1}" and df.En2="{En2}" and df.En1_ID="{En1_ID}" {actExpression1} {actExpression2} 
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
            # print("df_En1_ID=",df_En1_ID)
            list2.extend(df_En1_ID)

        list3.extend(list2)
    list3 = list(dict.fromkeys(list3))


    for model_entities, posit in zip(final_DFG_List, range(1, 700)):
        # print(model_entities)
        # print(color)
        # print("posit=", posit)
        En1 = model_entities[0]
        #print(En1)
        En2 = model_entities[1]
        En1_ID = model_entities[2]
        Color_ID = model_entities[3]
        color = ID_Colors[Color_ID]
        Node_Around_Color = c_white
        Node_Color = color
        Node_fontcolor = c_black
        NodeColorStriped = f"{Node_Around_Color}:{Node_Around_Color}:{Node_Around_Color}:{Node_Color}"

        if En1_ID in list3:
            #print(En1_ID)

            with dot.subgraph(name="cluster_0", comment='name2') as subDot:
                subDot.attr(style='filled', color=Node_Around_Color)
                subDot.attr(label=f"\n#{En2} {Entity2ID} for {En1}:")

                subDot.node_attr.update(shape="rectangle", fixedsize="True", width="0.8", height="0.2",
                                        fontname="Helvetica",
                                        fontsize="8", margin="0")

                if case_selector_activation1 == True:

                    if En1_ID in case_selector_list1:
                        Node_label = f"{En1_ID}        "
                        subDot.node(str(posit + 999), Node_label, color=Node_Around_Color, style="striped",
                                    fillcolor=NodeColorStriped,
                                    fontcolor=Node_fontcolor)


                else:
                    Node_label = f"{En1_ID}        "
                    subDot.node(str(posit + 999), Node_label, color=Node_Around_Color, style="striped",
                                fillcolor=NodeColorStriped,
                                fontcolor=Node_fontcolor)





