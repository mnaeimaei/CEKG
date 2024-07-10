
def DFC_based_on_Origins1(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,AdmissionColor,multiMorbidityColor, graphviz_QueryLocation):
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
        match (p:Patient)-[r1:INCLUDED]->(a:Admission) -[r2:INCLUDED]->(m:Multimorbidity) 
        {sourceExpression1} 
        RETURN a,p,m
    '''

    print(query1)
    with open(graphviz_QueryLocation, 'a') as file:
        file.write(f'''//DFC_based_on_Origins1''')
        file.write(f'''\n{query1}\n\n''')

    with driver.session() as session:
        record1 = session.run(query1).values()
        print(record1)

    if record1:
        a_node= [item[0]["Value"] for item in record1]
        a_Neo4J_ID = [item[0].id for item in record1]

        m_node = [item[2]["Value"] for item in record1]
        m_Neo4J_ID = [item[2].id for item in record1]

        p_Type = [item[1]["Type"] for item in record1]
        p_ID = [item[1]["ID"] for item in record1]

        print("n1_node=", a_node)
        print("n1_Neo4J_ID=", a_Neo4J_ID)

        print("n2_node=", m_node)
        print("n2_Neo4J_ID=", m_Neo4J_ID)

        print("p_Type=", p_Type)
        print("p_ID=", p_ID)


        for i in range(len(record1)):
            n1_label = a_node[i].replace(' ', '\n')
            n2_label = m_node[i].replace(' ', '\n')

            Rel_label = str(p_Type[i]+p_ID[i])

            pen_width = Edge_width

            # print("c1_label=", c1_label)
            # print("c2_label=", c2_label)
            # print("Rel_label=", Rel_label)


            if dfgType==1:
                node1 = str(a_Neo4J_ID[i])
                node2 = str(m_Neo4J_ID[i])
            else:
                node1 = str(a_node[i])
                node2 = str(m_node[i])


            dot.node(node1, str(n1_label), color=AdmissionColor, penwidth="2", style="filled",
                     fillcolor=AdmissionColor ,fontcolor=c_white)
            dot.node(node2, str(n2_label), color=multiMorbidityColor, penwidth="2", style="filled",
                     fillcolor=multiMorbidityColor, fontcolor=c_white)

            dot.edge(node1, node2, label=Rel_label, color='#e31a1c',
                     penwidth=pen_width, fontname="Helvetica", fontsize="8",
                     fontcolor='#e31a1c')


def DFC_based_on_Origins2(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,multiMorbidityColor,TreatedColor, graphviz_QueryLocation):
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
        match (p:Patient)-[r1:INCLUDED]->(a:Admission) -[r2:INCLUDED]->(m:Multimorbidity) -[r3:INCLUDED]->(n:treatedMorbids) 
        {sourceExpression1} 
        RETURN m,p,n
    '''

    print(query1)
    with open(graphviz_QueryLocation, 'a') as file:
        file.write(f'''//DFC_based_on_Origins2''')
        file.write(f'''\n{query1}\n\n''')

    with driver.session() as session:
        record1 = session.run(query1).values()
        print(record1)

    if record1:
        a_node= [item[0]["Value"] for item in record1]
        a_Neo4J_ID = [item[0].id for item in record1]

        m_node = [item[2]["Value"] for item in record1]
        m_Neo4J_ID = [item[2].id for item in record1]

        p_Type = [item[1]["Type"] for item in record1]
        p_ID = [item[1]["ID"] for item in record1]

        print("n1_node=", a_node)
        print("n1_Neo4J_ID=", a_Neo4J_ID)

        print("n2_node=", m_node)
        print("n2_Neo4J_ID=", m_Neo4J_ID)

        print("p_Type=", p_Type)
        print("p_ID=", p_ID)


        for i in range(len(record1)):
            n1_label = a_node[i].replace(' ', '\n')
            n2_label = m_node[i].replace(' ', '\n')

            Rel_label = str(p_Type[i]+p_ID[i])

            pen_width = Edge_width

            # print("c1_label=", c1_label)
            # print("c2_label=", c2_label)
            # print("Rel_label=", Rel_label)


            if dfgType==1:
                node1 = str(a_Neo4J_ID[i])
                node2 = str(m_Neo4J_ID[i])
            else:
                node1 = str(a_node[i])
                node2 = str(m_node[i])


            dot.node(node1, str(n1_label), color=multiMorbidityColor, penwidth="2", style="filled",
                     fillcolor=multiMorbidityColor ,fontcolor=c_white)
            dot.node(node2, str(n2_label), color=TreatedColor, penwidth="2", style="filled",
                     fillcolor=TreatedColor ,fontcolor=c_white)

            dot.edge(node1, node2, label=Rel_label, color='#e31a1c',
                     penwidth=pen_width, fontname="Helvetica", fontsize="8",
                     fontcolor='#e31a1c')

def DFC_based_on_Origins3(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,multiMorbidityColor,NotTreatedColor, graphviz_QueryLocation):
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
        match (p:Patient)-[r1:INCLUDED]->(a:Admission) -[r2:INCLUDED]->(m:Multimorbidity) -[r3:INCLUDED]->(n:untreatedMorbids) 
        {sourceExpression1} 
        RETURN m,p,n
    '''

    print(query1)
    with open(graphviz_QueryLocation, 'a') as file:
        file.write(f'''//DFC_based_on_Origins3''')
        file.write(f'''\n{query1}\n\n''')

    with driver.session() as session:
        record1 = session.run(query1).values()
        print(record1)

    if record1:
        a_node= [item[0]["Value"] for item in record1]
        a_Neo4J_ID = [item[0].id for item in record1]

        m_node = [item[2]["Value"] for item in record1]
        m_Neo4J_ID = [item[2].id for item in record1]

        p_Type = [item[1]["Type"] for item in record1]
        p_ID = [item[1]["ID"] for item in record1]

        print("n1_node=", a_node)
        print("n1_Neo4J_ID=", a_Neo4J_ID)

        print("n2_node=", m_node)
        print("n2_Neo4J_ID=", m_Neo4J_ID)

        print("p_Type=", p_Type)
        print("p_ID=", p_ID)


        for i in range(len(record1)):
            n1_label = a_node[i].replace(' ', '\n')
            n2_label = m_node[i].replace(' ', '\n')

            Rel_label = str(p_Type[i]+p_ID[i])

            pen_width = Edge_width

            # print("c1_label=", c1_label)
            # print("c2_label=", c2_label)
            # print("Rel_label=", Rel_label)


            if dfgType==1:
                node1 = str(a_Neo4J_ID[i])
                node2 = str(m_Neo4J_ID[i])
            else:
                node1 = str(a_node[i])
                node2 = str(m_node[i])


            dot.node(node1, str(n1_label), color=multiMorbidityColor, penwidth="2", style="filled",
                     fillcolor=multiMorbidityColor ,fontcolor=c_white)
            dot.node(node2, str(n2_label), color=NotTreatedColor, penwidth="2", style="filled",
                     fillcolor=NotTreatedColor ,fontcolor=c_white)

            dot.edge(node1, node2, label=Rel_label, color='#e31a1c',
                     penwidth=pen_width, fontname="Helvetica", fontsize="8",
                     fontcolor='#e31a1c')


def DFC_based_on_Origins4(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,multiMorbidityColor,NewDisordersColor, graphviz_QueryLocation):
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
        match (p:Patient)-[r1:INCLUDED]->(a:Admission) -[r2:INCLUDED]->(m:Multimorbidity) -[r3:INCLUDED]->(n:newMorbids) 
        {sourceExpression1} 
        RETURN m,p,n
    '''

    print(query1)
    with open(graphviz_QueryLocation, 'a') as file:
        file.write(f'''//DFC_based_on_Origins4''')
        file.write(f'''\n{query1}\n\n''')

    with driver.session() as session:
        record1 = session.run(query1).values()
        print(record1)

    if record1:
        a_node= [item[0]["Value"] for item in record1]
        a_Neo4J_ID = [item[0].id for item in record1]

        m_node = [item[2]["Value"] for item in record1]
        m_Neo4J_ID = [item[2].id for item in record1]

        p_Type = [item[1]["Type"] for item in record1]
        p_ID = [item[1]["ID"] for item in record1]

        print("n1_node=", a_node)
        print("n1_Neo4J_ID=", a_Neo4J_ID)

        print("n2_node=", m_node)
        print("n2_Neo4J_ID=", m_Neo4J_ID)

        print("p_Type=", p_Type)
        print("p_ID=", p_ID)


        for i in range(len(record1)):
            n1_label = a_node[i].replace(' ', '\n')
            n2_label = m_node[i].replace(' ', '\n')

            Rel_label = str(p_Type[i]+p_ID[i])

            pen_width = Edge_width

            # print("c1_label=", c1_label)
            # print("c2_label=", c2_label)
            # print("Rel_label=", Rel_label)


            if dfgType==1:
                node1 = str(a_Neo4J_ID[i])
                node2 = str(m_Neo4J_ID[i])
            else:
                node1 = str(a_node[i])
                node2 = str(m_node[i])


            dot.node(node1, str(n1_label), color=multiMorbidityColor, penwidth="2", style="filled",
                     fillcolor=multiMorbidityColor ,fontcolor=c_white)
            dot.node(node2, str(n2_label), color=NewDisordersColor, penwidth="2", style="filled",
                     fillcolor=NewDisordersColor ,fontcolor=c_white)

            dot.edge(node1, node2, label=Rel_label, color='#e31a1c',
                     penwidth=pen_width, fontname="Helvetica", fontsize="8",
                     fontcolor='#e31a1c')


def DFC_based_on_Origins5(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,TreatedColor,AdmissionColor, graphviz_QueryLocation):
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
        match (p:Patient)-[r1:INCLUDED]->(a:Admission) -[r2:INCLUDED]->(m:Multimorbidity) -[r3:INCLUDED]->(n:treatedMorbids) -[r4:DF_E]->(a2:Admission) 
        {sourceExpression1} 
        RETURN n,p,a2
    '''

    print(query1)
    with open(graphviz_QueryLocation, 'a') as file:
        file.write(f'''//DFC_based_on_Origins5''')
        file.write(f'''\n{query1}\n\n''')

    with driver.session() as session:
        record1 = session.run(query1).values()
        print(record1)

    if record1:
        a_node= [item[0]["Value"] for item in record1]
        a_Neo4J_ID = [item[0].id for item in record1]

        m_node = [item[2]["Value"] for item in record1]
        m_Neo4J_ID = [item[2].id for item in record1]

        p_Type = [item[1]["Type"] for item in record1]
        p_ID = [item[1]["ID"] for item in record1]

        print("n1_node=", a_node)
        print("n1_Neo4J_ID=", a_Neo4J_ID)

        print("n2_node=", m_node)
        print("n2_Neo4J_ID=", m_Neo4J_ID)

        print("p_Type=", p_Type)
        print("p_ID=", p_ID)


        for i in range(len(record1)):
            n1_label = a_node[i].replace(' ', '\n')
            n2_label = m_node[i].replace(' ', '\n')

            Rel_label = str(p_Type[i]+p_ID[i])

            pen_width = Edge_width

            # print("c1_label=", c1_label)
            # print("c2_label=", c2_label)
            # print("Rel_label=", Rel_label)


            if dfgType==1:
                node1 = str(a_Neo4J_ID[i])
                node2 = str(m_Neo4J_ID[i])
            else:
                node1 = str(a_node[i])
                node2 = str(m_node[i])


            dot.node(node1, str(n1_label), color=TreatedColor, penwidth="2", style="filled",
                     fillcolor=TreatedColor ,fontcolor=c_white)
            dot.node(node2, str(n2_label), color=AdmissionColor, penwidth="2", style="filled",
                     fillcolor=AdmissionColor ,fontcolor=c_white)

            dot.edge(node1, node2, label=Rel_label, color='#e31a1c',
                     penwidth=pen_width, fontname="Helvetica", fontsize="8",
                     fontcolor='#e31a1c')



def DFC_based_on_Origins6(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,NotTreatedColor,AdmissionColor, graphviz_QueryLocation):
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
        match (p:Patient)-[r1:INCLUDED]->(a:Admission) -[r2:INCLUDED]->(m:Multimorbidity) -[r3:INCLUDED]->(n:untreatedMorbids) -[r4:DF_E]->(a2:Admission) 
        {sourceExpression1} 
        RETURN n,p,a2
    '''

    print(query1)
    with open(graphviz_QueryLocation, 'a') as file:
        file.write(f'''//DFC_based_on_Origins6''')
        file.write(f'''\n{query1}\n\n''')

    with driver.session() as session:
        record1 = session.run(query1).values()
        print(record1)

    if record1:
        a_node= [item[0]["Value"] for item in record1]
        a_Neo4J_ID = [item[0].id for item in record1]

        m_node = [item[2]["Value"] for item in record1]
        m_Neo4J_ID = [item[2].id for item in record1]

        p_Type = [item[1]["Type"] for item in record1]
        p_ID = [item[1]["ID"] for item in record1]

        print("n1_node=", a_node)
        print("n1_Neo4J_ID=", a_Neo4J_ID)

        print("n2_node=", m_node)
        print("n2_Neo4J_ID=", m_Neo4J_ID)

        print("p_Type=", p_Type)
        print("p_ID=", p_ID)


        for i in range(len(record1)):
            n1_label = a_node[i].replace(' ', '\n')
            n2_label = m_node[i].replace(' ', '\n')

            Rel_label = str(p_Type[i]+p_ID[i])

            pen_width = Edge_width

            # print("c1_label=", c1_label)
            # print("c2_label=", c2_label)
            # print("Rel_label=", Rel_label)


            if dfgType==1:
                node1 = str(a_Neo4J_ID[i])
                node2 = str(m_Neo4J_ID[i])
            else:
                node1 = str(a_node[i])
                node2 = str(m_node[i])


            dot.node(node1, str(n1_label), color=NotTreatedColor, penwidth="2", style="filled",
                     fillcolor=NotTreatedColor ,fontcolor=c_white)
            dot.node(node2, str(n2_label), color=AdmissionColor, penwidth="2", style="filled",
                     fillcolor=AdmissionColor ,fontcolor=c_white)

            dot.edge(node1, node2, label=Rel_label, color='#e31a1c',
                     penwidth=pen_width, fontname="Helvetica", fontsize="8",
                     fontcolor='#e31a1c')



def DFC_based_on_Origins7(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,NewDisordersColor,AdmissionColor, graphviz_QueryLocation):
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
        match (p:Patient)-[r1:INCLUDED]->(a:Admission) -[r2:INCLUDED]->(m:Multimorbidity) -[r3:INCLUDED]->(n:newMorbids) -[r4:DF_E]->(a2:Admission) 
        {sourceExpression1} 
        RETURN n,p,a2
    '''

    print(query1)
    with open(graphviz_QueryLocation, 'a') as file:
        file.write(f'''//DFC_based_on_Origins7''')
        file.write(f'''\n{query1}\n\n''')

    with driver.session() as session:
        record1 = session.run(query1).values()
        print(record1)

    if record1:
        a_node= [item[0]["Value"] for item in record1]
        a_Neo4J_ID = [item[0].id for item in record1]

        m_node = [item[2]["Value"] for item in record1]
        m_Neo4J_ID = [item[2].id for item in record1]

        p_Type = [item[1]["Type"] for item in record1]
        p_ID = [item[1]["ID"] for item in record1]

        print("n1_node=", a_node)
        print("n1_Neo4J_ID=", a_Neo4J_ID)

        print("n2_node=", m_node)
        print("n2_Neo4J_ID=", m_Neo4J_ID)

        print("p_Type=", p_Type)
        print("p_ID=", p_ID)


        for i in range(len(record1)):
            n1_label = a_node[i].replace(' ', '\n')
            n2_label = m_node[i].replace(' ', '\n')

            Rel_label = str(p_Type[i]+p_ID[i])

            pen_width = Edge_width

            # print("c1_label=", c1_label)
            # print("c2_label=", c2_label)
            # print("Rel_label=", Rel_label)


            if dfgType==1:
                node1 = str(a_Neo4J_ID[i])
                node2 = str(m_Neo4J_ID[i])
            else:
                node1 = str(a_node[i])
                node2 = str(m_node[i])


            dot.node(node1, str(n1_label), color=NewDisordersColor, penwidth="2", style="filled",
                     fillcolor=NewDisordersColor ,fontcolor=c_white)
            dot.node(node2, str(n2_label), color=AdmissionColor, penwidth="2", style="filled",
                     fillcolor=AdmissionColor ,fontcolor=c_white)

            dot.edge(node1, node2, label=Rel_label, color='#e31a1c',
                     penwidth=pen_width, fontname="Helvetica", fontsize="8",
                     fontcolor='#e31a1c')


def Adding_Entities_ID_ForFirstEvent (ID_Colors, case_selector, mainEntity_selection, c_white, c_black, dot, driver
                                     ,EntitiesColors ,mainEntity,dfgType,patientColor, graphviz_QueryLocation):
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
        sourceExpression1 = case_selector.replace("where p.ID", "and r.sourceID")

    dot.attr("node", shape="circle", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
             fontsize="8", margin="0")

    query1 =f'''

        match p1=( a1 ) -[r:DF_E {{Type:"One" , Base:"Admission",  Source:"Patient"   }}]-> ( a2 )
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


            # print("c1_label=", c1_label)
            # print("c2_label=", c2_label)
            # print("Rel_label=", Rel_label)

            dot.node(str(rel_Neo4J_ID[i]), str(node_label), color=patientColor, penwidth="2", style="filled",
                     fillcolor=patientColor ,fontcolor=c_white)
            dot.edge(str(rel_Neo4J_ID[i]), node1, label="", color='#e31a1c' ,style="dashed",
                     penwidth=pen_width, fontname="Helvetica", fontsize="8",
                     fontcolor='#e31a1c')



def Adding_Entities_Hint (c_white, c_black, dot, patientColor ,AdmissionColor,multiMorbidityColor, TreatedColor ,NewDisordersColor,NotTreatedColor, graphviz_QueryLocation):

    Node_Around_Color = c_white
    Node_Color = "#e31a1c"
    Node_fontcolor = c_black
    NodeColorStriped = f"{Node_Around_Color}:{Node_Around_Color}:{Node_Around_Color}:{Node_Color}"

    with dot.subgraph(name="cluster_0", comment='name2') as subDot:
        subDot.attr(style='filled', color=Node_Around_Color)
        subDot.attr(label='\nColor Description:')

        subDot.node_attr.update(shape="rectangle", fixedsize="True", width="0.4", height="0.2",
                                fontname="Helvetica",
                                fontsize="8", margin="0")

        subDot.node(str(1 + 99999), "                            Patient", color=patientColor, style="striped",
                    fillcolor=patientColor,
                    fontcolor=Node_fontcolor)

        subDot.node(str(2 + 99999), "                                       Admission ID", color=AdmissionColor, style="striped",
                    fillcolor=AdmissionColor,
                    fontcolor=Node_fontcolor)


        subDot.node(str(3 + 99999), "                                                    Admission Disorders", color=multiMorbidityColor, style="striped",
                    fillcolor=multiMorbidityColor,
                    fontcolor=Node_fontcolor)

        subDot.node(str(4 + 99999), "                                                                  Admission Treated Disorders", color=TreatedColor, style="striped",
                    fillcolor=TreatedColor,
                    fontcolor=Node_fontcolor)


        subDot.node(str(5 + 99999), "                                                                          Admission Not Treated Disorders", color=NewDisordersColor, style="striped",
                    fillcolor=NewDisordersColor,
                    fontcolor=Node_fontcolor)

        subDot.node(str(6 + 99999), "                                                             Admission New Disorders", color=NotTreatedColor, style="striped",
                    fillcolor=NotTreatedColor,
                    fontcolor=Node_fontcolor)


