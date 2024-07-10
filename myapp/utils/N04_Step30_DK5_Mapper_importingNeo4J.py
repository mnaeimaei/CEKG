import os

import pandas as pd
import time, csv
from neo4j import GraphDatabase

import A5_EntryCol_Step3_Step as cl1
import B02_base as cl2
import N02_Step29_DK5_Mapper_prepare as cl2b
import N03_funcs30_DK5_Mapper_importingNeo4J as cl3f
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
outDir = downD + "/" + '12_DK5'
if not os.path.exists(outDir):
    os.mkdir(outDir)

svgLocDir = "../Data/0_svgLocation"
tempLoc = os.path.realpath(svgLocDir)
svgLog = tempLoc + "/" + '12_DK5'
if not os.path.exists(svgLog):
    os.mkdir(svgLog)


driverUserName = cla.driverUserName
driverPassword = cla.driverPassword
selenium = cla.selenium

print(" ")
print("---------------------------------------- Step M1 -----------------------------------------------------------------------------------")




step_Clear_OCT_DB=True
if step_Clear_OCT_DB:
    stepName='StepM1 - Clearing DB ....'
    print('                      ')
    print(stepName)
    start = time.time()


    ############PART DK ##########################################
    relationTypesDK = ["MAPPED_TO", "TIED","TYPE_OF"]
    relTypePartially = ["CORR", "Scenario", "2"]

    ############PART V ##########################################
    relationTypesV = ["REL", "DF", "DF_C", "DF_E"]

    relationTypes = relationTypesDK + relationTypesV


    fileName = "Q1"
    graphviz_QueryLocationQ1 = outDir + "/" + fileName + ".txt"
    with open(graphviz_QueryLocationQ1, 'w') as file:
        file.write(f'''''')


    with driver.session() as session:
        session.execute_write(cl3f.deleteRelation, relationTypes, graphviz_QueryLocationQ1)
        session.execute_write(cl3f.deletePartiallyRel, relTypePartially[0], relTypePartially[1], relTypePartially[2], graphviz_QueryLocationQ1)



    end = time.time()
    cl2.add_row_to_csv(Perf_file_path, start, end, stepName)



print(" ")
print("---------------------------------------- Step M2 -----------------------------------------------------------------------------------")

Activity_OCT_MappingRelation=cl2b.final_Activity_OCT_MappingRelation


step_link_Activity_OCPS=True
if step_link_Activity_OCPS:
    stepName='StepM2 - Creating Relationship between Activity and Concepts  ....'
    print('                      ')
    print(stepName)
    start = time.time()

    fileName = "Q2"
    graphviz_QueryLocationQ2 = outDir + "/" + fileName + ".txt"
    with open(graphviz_QueryLocationQ2, 'w') as file:
        file.write(f'''''')

    for item in Activity_OCT_MappingRelation:
        with driver.session() as session:
            session.execute_write(cl3f.Activity_OCPS, item[0], item[1], item[2], item[3], graphviz_QueryLocationQ2)

    if selenium==True:
        print("\n Neo4J Query to SVG:")
        runingQuery = f'''
        match  p=( c:Activity ) -[:MAPPED_TO]-> ( s: Concept ) return p limit 25;
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

print(" ")
print("---------------------------------------- Step M3 -----------------------------------------------------------------------------------")

Activity_OCT_MappingRelation=cl2b.final_Activity_OCT_MappingRelation


step_link_ActivityProperty_OCPS=True
if step_link_ActivityProperty_OCPS:
    stepName='StepM2 - Creating Relationship between Activity Property and Concepts  ....'
    print('                      ')
    print(stepName)
    start = time.time()

    fileName = "Q3"
    graphviz_QueryLocationQ3 = outDir + "/" + fileName + ".txt"
    with open(graphviz_QueryLocationQ3, 'w') as file:
        file.write(f'''''')

    for item in Activity_OCT_MappingRelation:
        with driver.session() as session:
            session.execute_write(cl3f.ActivityProperty_OCPS, item[0], item[1], item[2], item[3], graphviz_QueryLocationQ3)


    if selenium==True:
        print("\n Neo4J Query to SVG:")
        runingQuery = f'''
        match  p=( c:ActivityPropery ) -[:MAPPED_TO]-> ( s: Concept ) return p limit 25;
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



