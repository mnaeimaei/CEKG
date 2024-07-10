

###################Graph Functions"""""""""""""""""""""""""""""""""""

def DFC_based_on_Origins (EntityOrgValue, ID_Colors, count, c_white, c_black, dot, driver,DomainColors,domainColTitle,activityScenario, colTitle,case_selector_activation1,case_selector_list1,case_selector1,case_selector_activation2,case_selector_list2,case_selector2,Type5_Domain_selection, Type5_Domain_ID, graphviz_QueryLocation):
    for EntityOrgValue_list in EntityOrgValue:
        for model_entities in EntityOrgValue_list:
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
                asExpression1 = "MATCH (c1)-[:MAPPED_TO]->(m1)"
                asExpression2 = "MATCH (c2)-[:MAPPED_TO]->(m2)"
                asExpression3 = ",m1,m2"
                asExpression4 = ",m1"


            if case_selector_activation1 == False:
                actExpression1 = " "
            if case_selector_activation1 == True:
                actExpression1 = " AND " + case_selector1

            if case_selector_activation2 == False:
                actExpression2 = " "
            if case_selector_activation2 == True:
                actExpression2 = " AND " + case_selector2

            if Type5_Domain_selection == False:
                domExpression1 = " "
                domExpression2 = " "
                domExpression3 = " "

            if Type5_Domain_selection == True:
                domExpression1 = " and d1." + domainColTitle + " in " + str(
                    Type5_Domain_ID) + " and d2." + domainColTitle + " in " + str(Type5_Domain_ID)
                domExpression2 = " and d1." + domainColTitle + " in " + str(Type5_Domain_ID)
                domExpression3 = " and d." + domainColTitle + " in " + str(Type5_Domain_ID)

            print(case_selector_activation1)
            print(case_selector_activation2)

            dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
                     fontsize="8", margin="0")


            query1 = f'''     
                    MATCH (c1:Activity {{Type:"Activity"}}) -[df:DF_C {{Category:"woProperty"}}]-> (c2:Activity {{Type:"Activity"}})
                    MATCH (d1)<-[:TYPE_OF]-(c1:Activity {{Type:"Activity"}})
                    MATCH (c2:Activity {{Type:"Activity"}})-[:TYPE_OF]->(d2)
                    MATCH (c1)-[:TYPE_OF]->(d1) 
                    MATCH (c2)-[:TYPE_OF]->(d2)
                    {asExpression1}
                    {asExpression2}
                    WHERE df.count >= {number} and df.Type = "Relative" and df.En1="{En1}" and df.En2="{En2}" and df.En1_ID="{En1_ID}" {actExpression1} {actExpression2}  {domExpression1}
                    return c1,df,c2,d1,d2 {asExpression3} 
            '''
            print(query1)
            with open(graphviz_QueryLocation, 'a') as file:
                file.write(f'''//DFC_based_on_Origins''')
                file.write(f'''\n{query1}\n\n''')


            # dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
            #        fontsize="8", margin="0")

            with driver.session() as session:
                record1 = session.run(query1).values()

            if record1:
                c1_Neo4J_ID = [item[0].id for item in record1]
                c2_Neo4J_ID = [item[2].id for item in record1]
                df_En1 = [item[1]["En1"] for item in record1]
                df_En1_ID = [item[1]["En1_ID"] for item in record1]
                df_count = [item[1]["count"] for item in record1]
                c1_domain = [item[3][domainColTitle] for item in record1]
                c2_domain = [item[4][domainColTitle] for item in record1]

                if activityScenario == "Activity_Label":
                    c1_Activity = [item[0][colTitle] for item in record1]
                    c2_Activity = [item[2][colTitle] for item in record1]
                else:
                    c1_Activity = [item[5][colTitle] for item in record1]
                    c2_Activity = [item[6][colTitle] for item in record1]

                # print("c1_Activity=", c1_Activity)
                # print("c1_Neo4J_ID=", c1_Neo4J_ID)
                # print("c2_Activity=", c2_Activity)
                # print("c2_Neo4J_ID=", c2_Neo4J_ID)
                # print("df_count=", df_count)
                # print("c1_domain=", c1_domain)
                # print("c2_domain=", c2_domain)

                if show_lifecycle:
                    c1_lifecycle = [item[1]["lifecycle"] for item in record1]

                for i in range(len(record1)):
                    # print(i)

                    if show_lifecycle:
                        c1_name = c1_Activity[i] + '\n' + c1_lifecycle[i][0:5]
                    else:
                        c1_label = c1_Activity[i].replace(' ', '\n')
                        c2_label = c2_Activity[i].replace(' ', '\n')

                    Rel_label = '#' + str(df_count[i])

                    pen_width = Edge_width

                    # print("c1_label=", c1_label)
                    # print("c2_label=", c2_label)
                    # print("Rel_label=", Rel_label)
                    Node_Color1 = Node_Color
                    Node_Color2 = Node_Color

                    for Value in DomainColors:
                        if c1_domain[i] == Value[0]:
                            Node_Color1 = Value[1]
                        if c2_domain[i] == Value[0]:
                            Node_Color2 = Value[1]

                    dot.node(str(c1_Neo4J_ID[i]), c1_label, color=Node_Around_Color, penwidth="2", style="filled",
                             fillcolor=Node_Color1)
                    dot.node(str(c2_Neo4J_ID[i]), c2_label, color=Node_Around_Color, penwidth="2", style="filled",
                             fillcolor=Node_Color2)
                    dot.edge(str(c1_Neo4J_ID[i]), str(c2_Neo4J_ID[i]), label=Rel_label, color=Edge_Color,
                             penwidth=pen_width, fontname="Helvetica", fontsize="8",
                             fontcolor=edge_font_color)






def DFC_Adding_Entities (final_DFG_List, count, ID_Colors, c_white, c_black, dot, driver,case_selector_activation1,case_selector_list1,case_selector1,case_selector_activation2,case_selector_list2,case_selector2, domainColTitle,Type5_Domain_selection, Type5_Domain_ID, graphviz_QueryLocation):
    list3=[]
    for EntityOrgValue_list in final_DFG_List:
        list1 = []
        for model_entities in EntityOrgValue_list:
            list2 = []
            En1 = model_entities[0]
            En2 = model_entities[1]
            En1_ID = model_entities[2]
            number = count

            dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
                     fontsize="8", margin="0")

            if case_selector_activation1 == False:
                actExpression1 = " "
            if case_selector_activation1 == True:
                actExpression1 = " AND " + case_selector1

            if case_selector_activation2 == False:
                actExpression2 = " "
            if case_selector_activation2 == True:
                actExpression2 = " AND " + case_selector2

            if Type5_Domain_selection == False:
                domExpression1 = " "
                domExpression2 = " "
                domExpression3 = " "

            if Type5_Domain_selection == True:
                domExpression1 = " and d1." + domainColTitle + " in " + str(
                    Type5_Domain_ID) + " and d2." + domainColTitle + " in " + str(Type5_Domain_ID)
                domExpression2 = " and d1." + domainColTitle + " in " + str(Type5_Domain_ID)
                domExpression3 = " and d." + domainColTitle + " in " + str(Type5_Domain_ID)

            query1 = f'''     
                        MATCH (c1:Activity {{Type:"Activity"}}) -[df:DF_C {{Category:"woProperty"}}]-> (c2:Activity {{Type:"Activity"}})
                        MATCH (d1)<-[:TYPE_OF]-(c1:Activity {{Type:"Activity"}})
                        MATCH (c2:Activity {{Type:"Activity"}})-[:TYPE_OF]->(d2)
                        WHERE df.count >= {number} and df.Type = "Relative" and df.En1="{En1}" and df.En2="{En2}" and df.En1_ID="{En1_ID}" {actExpression1} {actExpression2} {domExpression1}
                        return c1,df,c2,d1,d2
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

            list1.extend(list2)
        list3.extend(list1)
        # print("list3=",list3)
    list3 = list(dict.fromkeys(list3))
    # print("list3=",list3)


    for Entity_Alias in final_DFG_List:
        #print("model_entities_derived_list=", Entity_Alias)
        #print("Color=", Color)
        #print("Show=", Show)

        for model_entities, posit in zip(Entity_Alias, range(1, 700)):
            # print(model_entities)
            # print(color)
            # print("posit=", posit)
            En1 = model_entities[0]
            print(En1)
            En2 = model_entities[1]
            En1_ID = model_entities[2]
            Color_ID = model_entities[3]
            color = ID_Colors[Color_ID]
            Node_Around_Color = c_white
            Node_Color = color
            Node_fontcolor = c_black
            NodeColorStriped = f"{Node_Around_Color}:{Node_Around_Color}:{Node_Around_Color}:{Node_Color}"

            if En1_ID in list3:
                print(En1_ID)

                with dot.subgraph(name="cluster_0", comment='name2') as subDot:
                    subDot.attr(style='filled', color=Node_Around_Color)
                    subDot.attr(label=f"\n#{En2} for {En1}:")

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




def Adding_Domains_Colors_Hint (EntityOrgValue, count, DomainColors, c_white, c_black, dot, driver,domainColTitle,case_selector_activation1,case_selector_list1,case_selector1,case_selector_activation2,case_selector_list2,case_selector2,Type5_Domain_selection, Type5_Domain_ID, graphviz_QueryLocation):
    list3=[]
    for EntityOrgValue_list in EntityOrgValue:
        list1 = []
        for model_entities in EntityOrgValue_list:
            list2 = []
            # print(model_entities)
            # print(color)
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

            if Type5_Domain_selection == False:
                domExpression1 = " "
                domExpression2 = " "
                domExpression3 = " "

            if Type5_Domain_selection == True:
                domExpression1 = " and d1." + domainColTitle + " in " + str(
                    Type5_Domain_ID) + " and d2." + domainColTitle + " in " + str(Type5_Domain_ID)
                domExpression2 = " where d1." + domainColTitle + " in " + str(Type5_Domain_ID)
                domExpression3 = " and d." + domainColTitle + " in " + str(Type5_Domain_ID)

            query1 = f'''     
                                MATCH (c1:Activity {{Type:"Activity"}}) -[df:DF_C {{Category:"woProperty"}}]-> (c2:Activity {{Type:"Activity"}})
                                MATCH (d1)<-[:TYPE_OF]-(c1:Activity {{Type:"Activity"}})
                                MATCH (c2:Activity {{Type:"Activity"}})-[:TYPE_OF]->(d2)
                                WHERE df.count >= {number} and df.Type = "Relative" and df.En1="{En1}" and df.En2="{En2}" and df.En1_ID="{En1_ID}" {actExpression1} {actExpression2}  {domExpression1}
                                return c1,df,c2,d1,d2
                                '''

            print(query1)
            with open(graphviz_QueryLocation, 'a') as file:
                file.write(f'''//Adding_Domains_Colors_Hint''')
                file.write(f'''\n{query1}\n\n''')

            with driver.session() as session:
                record1 = session.run(query1).values()

            if record1:
                c1_domain = [item[3][domainColTitle] for item in record1]
                list2.extend(c1_domain)
                c2_domain = [item[4][domainColTitle] for item in record1]
                list2.extend(c2_domain)

            query2 = f'''     
                MATCH (d1)<-[:TYPE_OF]-(c1:Activity {{Type:"Activity"}})
               {domExpression2}
                return c1,d1
                                    '''
            print(query2)
            with open(graphviz_QueryLocation, 'a') as file:
                file.write(f'''//Adding_Domains_Colors_Hint''')
                file.write(f'''\n{query2}\n\n''')

            with driver.session() as session:
                record2 = session.run(query2).values()

            if record2:
                d1_domain = [item[1][domainColTitle] for item in record2]
                list2.extend(d1_domain)

            list1.extend(list2)
        list3.extend(list1)
        # print("list3=",list3)
    list3 = list(dict.fromkeys(list3))
    # print("list3=",list3)



    for DomainColors, posit in zip(DomainColors, range(1,700)):
        #print(posit)
        DomainLabel = DomainColors[0]
        DomainColorCode = DomainColors[1]
        #print(DomainLabel)
        #print(DomainColorCode)
        Node_Around_Color = c_white
        Node_fontcolor = c_black

        Node_label = f"{DomainLabel}"
        NodeColorStriped = f"{Node_Around_Color}:{Node_Around_Color}:{Node_Around_Color}:{DomainColorCode}"

        if DomainLabel in list3:
            print(DomainLabel)
            #print(DomainColorCode)
            with dot.subgraph(name="cluster_1", comment='name2') as subDot:
                subDot.attr(style='filled', color=Node_Around_Color)
                subDot.attr(label='\nDomains:')

                subDot.node_attr.update(shape="rectangle", fixedsize="True", width="0.8", height="0.2",
                                        fontname="Helvetica",
                                        fontsize="8", margin="0")

                subDot.node(str(posit + 9999999), Node_label, color=Node_Around_Color, style="striped",
                            fillcolor=NodeColorStriped,
                            fontcolor=Node_fontcolor)