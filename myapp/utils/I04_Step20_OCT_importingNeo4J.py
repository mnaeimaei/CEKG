import os

import pandas as pd
import time, csv
from neo4j import GraphDatabase

import A5_EntryCol_Step3_Step as cl1
import B02_base as cl2
import I02_Step19_OCT_Prepare as cl2b
import I03_funcs20_OCT_importingNeo4J as cl3c
import B02_svg as svgFunction
import A5_EntryCol_Step3_Step as cla

from tqdm import tqdm

print("************************** From cl1: ****************************************************************************")


driver = cl1.driver
OCTdataSet=cl1.OCTdataSet

Neo4JImport=cl2b.Neo4JImport
Perf_file_path = cl2b.Perf_file_path



downloadDir = "../../media/download/dfgTool"
downD = os.path.realpath(downloadDir)
outDir = downD + "/" + '06_OCT_Node'
if not os.path.exists(outDir):
    os.mkdir(outDir)

svgLocDir = "../Data/0_svgLocation"
tempLoc = os.path.realpath(svgLocDir)
svgLog = tempLoc + "/" + '06_OCT_Node'
if not os.path.exists(svgLog):
    os.mkdir(svgLog)


driverUserName = cla.driverUserName
driverPassword = cla.driverPassword
selenium = cla.selenium

print(" ")
print("---------------------------------------- Step H1 -----------------------------------------------------------------------------------")



step_Clear_OCT_DB=True
if step_Clear_OCT_DB:
    stepName='StepH1 - Clearing DB ....'
    print('                      ')
    print(stepName)
    start = time.time()



    ############PART I ##########################################
    nodeTypesI = ["Concept"]
    relationTypesI = ["ANCESTOR_OF"]

    ############PART DK2 ##########################################

    relationTypesDK2 = [f'''INCLUDED {{Type:"last"}}''']

    ############PART DK ##########################################
    relationTypesDK = ["ASSOCIATED", "LINKED_TO", "CONNECTED_TO", "MAPPED_TO", "TIED", "TYPE_OF"]
    relTypePartially = ["CORR", "Scenario", "2"]

    ############PART V ##########################################
    relationTypesV = ["REL", "DF", "DF_C", "DF_E"]

    nodeTypes = nodeTypesI
    relationTypes = relationTypesI + relationTypesDK + relationTypesV + relationTypesDK2

    fileName = "Q1"
    graphviz_QueryLocationQ1 = outDir + "/" + fileName + ".txt"
    with open(graphviz_QueryLocationQ1, 'w') as file:
        file.write(f'''''')

    with driver.session() as session:
        session.execute_write(cl3c.deleteRelation, relationTypes, graphviz_QueryLocationQ1)
        session.execute_write(cl3c.DeleteNodes, nodeTypes, graphviz_QueryLocationQ1)
        session.execute_write(cl3c.DeleteAllNodesRels, nodeTypes, graphviz_QueryLocationQ1)
        session.execute_write(cl3c.deletePartiallyRel, relTypePartially[0], relTypePartially[1], relTypePartially[2], graphviz_QueryLocationQ1)




    end = time.time()
    cl2.add_row_to_csv(Perf_file_path, start, end, stepName)

print(" ")
print("---------------------------------------- Step H2 -----------------------------------------------------------------------------------")


step_Clear_OCT_Constraints=True
if step_Clear_OCT_Constraints:
    stepName='StepD2 - Dropping Constraint...'
    print('                      ')
    print(stepName)
    start = time.time()

    fileName = "Q2"
    graphviz_QueryLocationQ2 = outDir + "/" + fileName + ".txt"
    with open(graphviz_QueryLocationQ2, 'w') as file:
        file.write(f'''''')

    with driver.session() as session:
        session.execute_write(cl3c.clearConstraint, None, driver, nodeTypes, graphviz_QueryLocationQ2)




    end = time.time()
    cl2.add_row_to_csv(Perf_file_path, start, end, stepName)

print(" ")
print("---------------------------------------- Step H3 -----------------------------------------------------------------------------------")



step_createConstraint=True
if step_createConstraint:
    stepName='StepD3 - Creating Constraint...'
    print('                      ')
    print(stepName)
    start = time.time()

    fileName = "Q3"
    graphviz_QueryLocationQ3 = outDir + "/" + fileName + ".txt"
    with open(graphviz_QueryLocationQ3, 'w') as file:
        file.write(f'''''')

    with driver.session() as session:
        session.execute_write(cl3c.createConstraint, nodeTypesI, graphviz_QueryLocationQ3)





    end = time.time()
    cl2.add_row_to_csv(Perf_file_path, start, end, stepName)

print(" ")
print("---------------------------------------- Step H4 -----------------------------------------------------------------------------------")

header_OCT_Node=cl2b.header_OCT_Node
OCT_Neo4JImport_OCT_Node_FileName=cl2b.OCT_Neo4JImport_OCT_Node_FileName

step_load_OCPS_Concepts=True
if step_load_OCPS_Concepts :
    stepName='StepH4 - Creating OCPS Concepts Nodes ....'
    print('                      ')
    print(stepName)
    start = time.time()

    fileName = "Q4"
    graphviz_QueryLocationQ4 = outDir + "/" + fileName + ".txt"
    with open(graphviz_QueryLocationQ4, 'w') as file:
        file.write(f'''''')


    cl3c.loadOCPSConcepts(driver, graphviz_QueryLocationQ4, header_OCT_Node, OCT_Neo4JImport_OCT_Node_FileName, OCTdataSet)  # generate query to create all events with all log columns as properties

    if selenium==True:
        print("\n Neo4J Query to SVG:")
        runingQuery = f'''
        MATCH (s:Concept)               return s limit 25;
        '''
        svgFunction.exportNeo4jSVG(runingQuery, driverUserName, driverPassword)
        svgFunction.moveSVG(outDir, fileName)
        savingTxt4 = svgLog + "/" + fileName + "_svg_location.txt"
        with open(savingTxt4, 'w') as file:
            file.write(f'''{outDir}/{fileName}.svg''')
        print("\n SVG File was created")

    end = time.time()
    cl2.add_row_to_csv(Perf_file_path, start, end, stepName)



print("-------------------------------------------------------------------------------------------------------------------------")




driver.close()



