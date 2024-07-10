

def DFC_based_on_Origins (case_selector, mainEntity_selection, c_white, c_black, dot, driver,mainEntity,otherEntity,dfgType, graphviz_QueryLocation):

    # print(color)

    Node_Color = c_white
    Edge_Color = c_black
    edge_font_color = c_black

    Node_Around_Color = c_black
    Edge_width = "1"
    show_lifecycle = False

    dot.attr("node", shape="square", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
             fontsize="8", margin="0")

    if mainEntity_selection == False:
        sourceExpression1 = " "
    if mainEntity_selection == True:
        sourceExpression1 = case_selector


    query1 = f'''     
        match p1=( a1 ) -[r:DF_E {{Type:"One" , Base:"{otherEntity}",  Source:"{mainEntity}"   }}]-> ( a2 )
        {sourceExpression1} 
        return a1,r,a2;
    '''

    print(query1)
    with open(graphviz_QueryLocation, 'a') as file:
        file.write(f'''//DFC_based_on_Origins''')
        file.write(f'''\n{query1}\n\n''')

    with driver.session() as session:
        record1 = session.run(query1).values()

    if record1:
        n1_node= [item[0]["Value"] for item in record1]
        n1_Neo4J_ID = [item[0].id for item in record1]

        n2_node = [item[2]["Value"] for item in record1]
        n2_Neo4J_ID = [item[2].id for item in record1]

        rel_Source = [item[1]["Source"] for item in record1]
        rel_sourceID = [item[1]["sourceID"] for item in record1]


        print("n1_node=", n1_node)
        print("n1_Neo4J_ID=", n1_Neo4J_ID)

        print("n2_node=", n2_node)
        print("n2_Neo4J_ID=", n2_Neo4J_ID)

        print("rel_Source=", rel_Source)
        print("rel_sourceID=", rel_sourceID)


        for i in range(len(record1)):
            n1_label = n1_node[i].replace(' ', '\n')
            n2_label = n2_node[i].replace(' ', '\n')

            Rel_label = str(rel_Source[i]) + str(rel_sourceID[i])

            pen_width = Edge_width

            # print("c1_label=", c1_label)
            # print("c2_label=", c2_label)
            # print("Rel_label=", Rel_label)

            if dfgType==1:
                node1 = str(n1_Neo4J_ID[i])
                node2 = str(n2_Neo4J_ID[i])
            else:
                node1 = str(n1_node[i])
                node2 = str(n2_node[i])


            dot.node(node1, str(n1_label), color='#1f78b4', penwidth="2", style="filled",
                     fillcolor='#1f78b4',fontcolor=c_white)
            dot.node(node2, str(n2_label), color='#1f78b4', penwidth="2", style="filled",
                     fillcolor='#1f78b4',fontcolor=c_white)
            dot.edge(node1, node2, label=Rel_label, color='#e31a1c',
                     penwidth=pen_width, fontname="Helvetica", fontsize="8",
                     fontcolor='#e31a1c')

def Adding_Entities_ID_ForFirstEvent (ID_Colors, case_selector, mainEntity_selection, c_white, c_black, dot, driver,EntitiesColors,mainEntity,otherEntity,dfgType, graphviz_QueryLocation):
    # print(model_entities)
    # print(color)


    Node_Color = c_white
    Edge_Color = c_black
    edge_font_color = c_black
    fontcolor = c_white

    Node_Around_Color = c_black
    Edge_width = "1"
    show_lifecycle = False

    if mainEntity_selection == False:
        sourceExpression1 = " "
    if mainEntity_selection == True:
        sourceExpression1 = case_selector.replace("where", "AND")

    dot.attr("node", shape="circle", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
             fontsize="8", margin="0")

    query1=f'''
    
        match p1=( a1 ) -[r:DF_E {{Type:"One" , Base:"{otherEntity}",  Source:"{mainEntity}"   }}]-> ( a2 )
        WHERE NOT EXISTS {{(a1)<-[:DF_E]-()}}
        {sourceExpression1} 
        RETURN a1,r
    '''

    print(query1)
    with open(graphviz_QueryLocation, 'a') as file:
        file.write(f'''//Adding_Entities_ID_ForFirstEvent''')
        file.write(f'''\n{query1}\n\n''')

    with driver.session() as session:
        record1 = session.run(query1).values()

    if record1:
        a1_node= [item[0]["Value"] for item in record1]
        a1_Neo4J_ID = [item[0].id for item in record1]


        rel_Source = [item[1]["Source"] for item in record1]
        rel_sourceID = [item[1]["sourceID"] for item in record1]
        rel_Neo4J_ID = [item[1].id for item in record1]

        print("a1_node=", a1_node)
        print("a1_Neo4J_ID=", a1_Neo4J_ID)


        print("rel_Source=", rel_Source)
        print("rel_sourceID=", rel_sourceID)

        for i in range(len(record1)):
            node_label = str(rel_sourceID[i])

            pen_width = Edge_width

            if dfgType == 1:
                node1 = str(a1_Neo4J_ID[i])
            else:
                node1 = str(a1_node[i])


            dot.node(str(rel_Neo4J_ID[i]), str(node_label), color='#e31a1c', penwidth="2", style="filled",
                     fillcolor='#e31a1c',fontcolor=c_white)
            dot.edge(str(rel_Neo4J_ID[i]), node1, label="", color='#e31a1c',style="dashed",
                     penwidth=pen_width, fontname="Helvetica", fontsize="8",
                     fontcolor='#e31a1c')



def Adding_Entities (ID_Colors, case_selector, mainEntity_selection, c_white, c_black, dot, driver,EntitiesColors,node1,Entity_Show, graphviz_QueryLocation):

    Node_Around_Color = c_white
    Node_Color = "#e31a1c"
    Node_fontcolor = c_black
    NodeColorStriped = f"{Node_Around_Color}:{Node_Around_Color}:{Node_Around_Color}:{Node_Color}"

    with dot.subgraph(name="cluster_0", comment='name2') as subDot:
        subDot.attr(style='filled', color=Node_Around_Color)
        subDot.attr(label='\nEntities:')

        subDot.node_attr.update(shape="rectangle", fixedsize="True", width="0.8", height="0.2",
                                fontname="Helvetica",
                                fontsize="8", margin="0")

        subDot.node(str(1 + 99999), node1, color=Node_Around_Color, style="striped",
                    fillcolor=NodeColorStriped,
                    fontcolor=Node_fontcolor)



def Adding_otherEntities (ID_Colors, case_selector, mainEntity_selection, c_white, c_black, dot, driver,EntitiesColors,node1,Entity_Show, graphviz_QueryLocation):

    Node_Around_Color = c_white
    Node_Color = "#1f78b4"
    Node_fontcolor = c_black
    NodeColorStriped = f"{Node_Around_Color}:{Node_Around_Color}:{Node_Around_Color}:{Node_Color}"

    with dot.subgraph(name="cluster_1", comment='name2') as subDot:
        subDot.attr(style='filled', color=Node_Around_Color)
        subDot.attr(label='\nOther Entities:')

        subDot.node_attr.update(shape="rectangle", fixedsize="True", width="0.8", height="0.2",
                                fontname="Helvetica",
                                fontsize="8", margin="0")

        subDot.node(str(1 + 9999999), Entity_Show, color=Node_Around_Color, style="striped",
                    fillcolor=NodeColorStriped,
                    fontcolor=Node_fontcolor)