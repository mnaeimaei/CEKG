import os

import pandas as pd
import time, csv
from neo4j import GraphDatabase

import A5_EntryCol_Step3_Step as cl1
import B02_base as cl2
import I06_Step19_OCTrel_Prepare as cl2b
import I07_funcs20_OCTrel_importingNeo4J as cl3c
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
outDir = downD + "/" +  '07_OCT_REL'
if not os.path.exists(outDir):
    os.mkdir(outDir)

svgLocDir = "../Data/0_svgLocation"
tempLoc = os.path.realpath(svgLocDir)
svgLog = tempLoc + "/" + '07_OCT_REL'
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

    relationTypesI = ["ANCESTOR_OF"]

    ############PART DK2 ##########################################

    relationTypesDK2 = [f'''INCLUDED {{Type:"last"}}''']

    ############PART DK ##########################################
    relationTypesDK = ["ASSOCIATED", "LINKED_TO", "CONNECTED_TO", "MAPPED_TO", "TIED", "TYPE_OF"]
    relTypePartially = ["CORR", "Scenario", "2"]

    ############PART V ##########################################
    relationTypesV = ["REL", "DF", "DF_C", "DF_E"]


    relationTypes = relationTypesI + relationTypesDK + relationTypesV + relationTypesDK2

    fileName = "Q1"
    graphviz_QueryLocationQ1 = outDir + "/" + fileName + ".txt"
    with open(graphviz_QueryLocationQ1, 'w') as file:
        file.write(f'''''')

    with driver.session() as session:
        session.execute_write(cl3c.deleteRelation, relationTypes, graphviz_QueryLocationQ1)
        session.execute_write(cl3c.deletePartiallyRel, relTypePartially[0], relTypePartially[1], relTypePartially[2], graphviz_QueryLocationQ1)




    end = time.time()
    cl2.add_row_to_csv(Perf_file_path, start, end, stepName)



print(" ")
print("---------------------------------------- Step H5 -----------------------------------------------------------------------------------")

OCPS_REL_MappingRelation=cl2b.OCT_REL_MappingRelation
length = len(OCPS_REL_MappingRelation)

step_link_Concepts=True
if step_link_Concepts:
    stepName='StepH5 - Creating Relationship between all Concepts ....'
    print('                      ')
    print(stepName)
    start = time.time()

    fileName = "Q2"
    graphviz_QueryLocationQ2 = outDir + "/" + fileName + ".txt"
    with open(graphviz_QueryLocationQ2, 'w') as file:
        file.write(f'''''')

    print("OCPS_REL_MappingRelation=", OCPS_REL_MappingRelation)

    for item, k in zip(OCPS_REL_MappingRelation, range(length)) :
        with driver.session() as session:
            session.execute_write(cl3c.link_Concepts, item[0], item[1], item[2], item[3], graphviz_QueryLocationQ2)
        formatted_number = "{:.2f}".format(100 * k / length)
        print("Completed: ", formatted_number, "%")

    svgFunction.truncate_file(graphviz_QueryLocationQ2)

    if selenium==True:
        print("\n Neo4J Query to SVG:")
        runingQuery = f'''
        match p=( n1 ) -[:ANCESTOR_OF]-> ( n2 )  return p limit 25;
        '''
        svgFunction.exportNeo4jSVG(runingQuery, driverUserName, driverPassword)
        svgFunction.moveSVG(outDir, fileName)
        savingTxt4 = svgLog + "/" + fileName + "_svg_location.txt"
        with open(savingTxt4, 'w') as file:
            file.write(f'''{outDir}/{fileName}.svg''')
        print("\n SVG File was created")

    end = time.time()
    cl2.add_row_to_csv(Perf_file_path, start, end, stepName)

print(" ")
print("---------------------------------------- Step H6 -----------------------------------------------------------------------------------")


step_modify_concepts=True
if step_modify_concepts:
    stepName='StepH6 - Modifying Concept ....'
    print('                      ')
    print(stepName)
    start = time.time()

    fileName = "Q3"
    graphviz_QueryLocationQ3 = outDir + "/" + fileName + ".txt"
    with open(graphviz_QueryLocationQ3, 'w') as file:
        file.write(f'''''')

    with driver.session() as session:
        session.execute_write(cl3c.modify_concept, graphviz_QueryLocationQ3)


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



