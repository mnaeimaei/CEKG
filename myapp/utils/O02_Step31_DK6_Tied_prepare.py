from neo4j import GraphDatabase
import pandas as pd
import time, os, csv
import O01_funcs31_DK6_Tied_prepare as cl1n
import B02_base as cl2
import A5_EntryCol_Step3_Step as cl1
import A1_Scenario_Step2 as clN
import B02_txt_read as txtF

print("")
print("************************** From Event Log Entry (performance) ****************************************************************************")


Perf_file_path = cl1.Perf_file_path
print("Perf_file_path=", Perf_file_path)




print("************************** input from cl1: ****************************************************************************")

driver = cl1.driver


Neo4JImport=cl2.Neo4j_import_dir(driver)
print("Neo4JImport=",Neo4JImport)




print("************************** input from DK5_1 ****************************************************************************")

Domain_Input_FileName_1 = cl1.Domain_Input_FileName_1
Domain_Neo4JImport_FileName_1 = cl1.Domain_Neo4JImport_FileName_1

Domain1_Activity = cl1.Domain1_Activity
Domain1_Activity_Synonym = cl1.Domain1_Activity_Synonym
Domain1_Domain = cl1.Domain1_Domain


csv_DK5_1=cl2.ImportCSV(Domain_Input_FileName_1)
#print("csv_Activity_OCT=\n",csv_Activity_OCT)
#print("")


DK5_1_Rel=cl1n.CreateMappingRelation3(csv_DK5_1, Domain1_Activity,Domain1_Activity_Synonym,Domain1_Domain)
print("DK5_1_Rel=",DK5_1_Rel)
print("")


cl1n.Create_CSV_in_Neo4J_import(csv_DK5_1, Neo4JImport, Domain_Neo4JImport_FileName_1)

header_DK5_1, csvLog_DK5_1 = cl2.LoadLog(Neo4JImport+Domain_Neo4JImport_FileName_1)
print("header_DK5_1=",header_DK5_1)
print("")
print("csvLog_DK5_1=\n",csvLog_DK5_1)
print("")


print("************************** input from DK5_2 ****************************************************************************")

Domain_Input_FileName_2 = cl1.Domain_Input_FileName_2
Domain_Neo4JImport_FileName_2 = cl1.Domain_Neo4JImport_FileName_2

Domain2_Domain = cl1.Domain2_Domain
Domain2_OTC = cl1.Domain2_OTC
Domain2_SCTCode = cl1.Domain2_SCTCode


csv_DK5_2=cl2.ImportCSV(Domain_Input_FileName_2)
#print("csv_Activity_OCT=\n",csv_Activity_OCT)
#print("")


DK5_2_Rel=cl1n.CreateMappingRelation3(csv_DK5_2, Domain2_Domain,Domain2_OTC,Domain2_SCTCode)
print("DK5_2_Rel=",DK5_2_Rel)
print("")


cl1n.Create_CSV_in_Neo4J_import(csv_DK5_2, Neo4JImport, Domain_Neo4JImport_FileName_2)

header_DK5_2, csvLog_DK5_2 = cl2.LoadLog(Neo4JImport+Domain_Neo4JImport_FileName_2)
print("header_DK5_2=",header_DK5_2)
print("")
print("csvLog_DK5_2=\n",csvLog_DK5_2)
print("")

print("************************** input from  ****************************************************************************")
DFG=clN.DFG
print(DFG)

list0=['DFG1',	'DFG1_featureValue',	'DFG2',	'DFG2_featureValue',	'DFG3',	'DFG3_feature',	'DFG3_featureValue',	'DFG4',	'DFG4_feature',	'DFG4_featureValue',	'DFG5',	'DFG5_feature',	'DFG5_featureValue']
list1=['DFG1_Domain',	'DFG1_featureValue_Domain',	'DFG2_Domain',	'DFG2_featureValue_Domain',	'DFG3_Domain',	'DFG3_feature_Domain',	'DFG3_featureValue_Domain','DFG4_Domain',	'DFG4_feature_Domain',	'DFG4_featureValue_Domain',	'DFG5_Domain',	'DFG5_feature_Domain',	'DFG5_featureValue_Domain']
list2=['DFG1_DomainConcept',	'DFG1_featureValue_DomainConcept',	'DFG2_DomainConcept',	'DFG2_featureValue_DomainConcept',	'DFG3_DomainConcept',	'DFG3_feature_DomainConcept',	'DFG3_featureValue_DomainConcept',	'DFG4_DomainConcept',	'DFG4_feature_DomainConcept',	'DFG4_featureValue_DomainConcept',	'DFG5_DomainConcept',	'DFG5_feature_DomainConcept',	'DFG5_featureValue_DomainConcept']
list3=['DFG1_DomainConceptLevel',	'DFG1_featureValue_DomainConceptLevel',	'DFG2_DomainConceptLevel',	'DFG2_featureValue_DomainConceptLevel',	'DFG3_DomainConceptLevel',	'DFG3_feature_DomainConceptLevel',	'DFG3_featureValue_DomainConceptLevel',	'DFG4_DomainConceptLevel',	'DFG4_feature_DomainConceptLevel',	'DFG4_featureValue_DomainConceptLevel',	'DFG5_DomainConceptLevel',	'DFG5_feature_DomainConceptLevel',	'DFG5_featureValue_DomainConceptLevel']



if DFG in list0:
    print("************************** input for:  0:main_Entities ****************************************************************************")
    # Main Disorder
    print("This scenario doesn't use DK6")
    print("")

if DFG in list1:
    print("************************** input for:  1:Domain ****************************************************************************")
    # Main Disorder
    sc1_list =cl1n.sc1(driver, DK5_1_Rel)
    print("sc1_list=",sc1_list)
    print(len(sc1_list))
    print("")

if DFG in list2:
    print("************************** input for: 2:	DomainConcept ****************************************************************************")
    # ICD
    sc2_list =cl1n.sc2(driver, DK5_1_Rel, DK5_2_Rel)
    print("sc2_list=",sc2_list)
    print(len(sc2_list))
    print("")

if DFG in list3:
    print("************************** input for: 3:	DomainConceptLevel ****************************************************************************")
    # ICD UP
    txtFileExistance = txtF.txtExistance(DFG)
    print("txtFileExistance=", txtFileExistance)

    if txtFileExistance==True:
        distanceFrom_Domain = txtF.listIntTxt(DFG, "distanceFrom_Domain")
        Semanti_tags_Domain = txtF.stringTxt(DFG, "Semanti_tags_Domain")
        ConceptType_Domain = txtF.stringTxt(DFG, "ConceptType_Domain")
        TLC_Semanti_tags_Domain = txtF.stringTxt(DFG, "TLC_Semanti_tags_Domain")
    else:
        distanceFrom_Domain = 1
        Semanti_tags_Domain = "procedure"
        ConceptType_Domain = "Concept"
        TLC_Semanti_tags_Domain = "procedure"



    print("distanceFrom_Domain=", distanceFrom_Domain)
    print("Semanti_tags_Domain=", Semanti_tags_Domain)
    print("ConceptType_Domain=", ConceptType_Domain)
    print("TLC_Semanti_tags_Domain=", TLC_Semanti_tags_Domain)


    sc3_list =cl1n.sc3(driver, DK5_1_Rel, DK5_2_Rel,distanceFrom_Domain,Semanti_tags_Domain,ConceptType_Domain,TLC_Semanti_tags_Domain)
    print("sc3_list=",sc3_list)
    print(len(sc3_list))
    print("")

