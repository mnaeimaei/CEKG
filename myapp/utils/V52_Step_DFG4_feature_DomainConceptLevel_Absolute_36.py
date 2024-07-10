from neo4j import GraphDatabase
import platform
from graphviz import Digraph
import os

import A5_EntryCol_Step3_Step as cla

import A1_Scenario_Step2 as Ne0
import A6_Scenario_Final_Step as Ne02


import B02_Colors as cl7_color



import V50_funcCfgs_DFG4_feature_DomainConceptLevel_Absolute_36 as funcConf
import V51_funcs_DFG4_feature_DomainConceptLevel_Absolute_36 as cl9

import B02_txt_read as txtF
import B02_base as cl2
import webbrowser


print("************************** From cla: ****************************************************************************")

driver=cla.driver

print("************************** From cl1: ****************************************************************************")




entityList=Ne02.entityList
print("entityList=",entityList)

EnNum=len(Ne02.entityList)
print("EnNum=", EnNum)

conditionProperty=Ne02.conditionProperty
print("conditionProperty=",conditionProperty)

conditionPropertyValue=Ne02.conditionPropertyValue
print("conditionPropertyValue=",conditionPropertyValue)


entityListIDproperty=Ne02.entityListIDproperty
print("entityListIDproperty=",entityListIDproperty)


DomainNode=Ne02.DomainNode
print("DomainNode=",DomainNode)

domainColTitle=Ne02.domainColTitle[0]
print("domainColTitle=",domainColTitle)



print("************************** From cl0 for Activity: *****************************************************")

Activity = Ne0.Activity
ActivityNode=Ne02.ActivityNode
colTitle=Ne02.colTitle

print("activityScenario=",Activity)
print("ActivityNode=",ActivityNode)
print("colTitle=", colTitle)


print("************************** From cl7 ****************************************************************************")


c_white=cl7_color.c_white
c_black=cl7_color.c_black



ID_Colors=cl7_color.ID_Colors
print("ID_Colors=",ID_Colors)

NodeColors=cl7_color.NodeColors
print("NodeColors=",NodeColors)



print("************************** From Func: ****************************************************************************")





entityIDlists=funcConf.Finading_Entities_ID(driver,entityList,entityListIDproperty,conditionProperty,conditionPropertyValue)
print("entityIDlists=",entityIDlists)

EntityOrgValue=funcConf.convert_to_list_of_lists(entityList)
print("EntityOrgValue=",EntityOrgValue)

refEntityIDlists2=funcConf.Finading_Reified_Entities_ID2(driver,entityList)
print("refEntityIDlists2=",refEntityIDlists2)

combining_IDs_List=funcConf.combining_IDs_List_func(EnNum, entityIDlists, refEntityIDlists2)
print("combining_IDs_List=",combining_IDs_List)

combining_IDs_List_color=funcConf.color_combine(combining_IDs_List)
print("combining_IDs_List_color=",combining_IDs_List_color)

final_DFG_List_Abs_color=funcConf.final_DFG_List_Absolute_2(EnNum, EntityOrgValue, combining_IDs_List, combining_IDs_List_color)
print("final_DFG_List_Abs_color=",final_DFG_List_Abs_color)


DomainValue=funcConf.Finading_DomainValue(driver,DomainNode,domainColTitle)
print("DomainValue=",DomainValue)


DomainColors=funcConf.Domain_colors_creater(DomainValue, NodeColors)
print("DomainColors=", DomainColors)


print("************************** From Config: ****************************************************************************")




confDirectory = "../Data/0_Conf"
confPath = os.path.realpath(confDirectory)
print(confPath)

generalFileName = (Ne0.DFG) + "_general"
print("generalFileName=", generalFileName)

txtFileExistance = txtF.txtExistance(generalFileName)
print("txtFileExistance=", txtFileExistance)

if txtFileExistance == True:

    ListEnDFSHow = txtF.ShowTxt(generalFileName, EnNum, "Type4_Entity", "_DF_Show")
    print("Entity_DF_Show (ListEnDFSHow)=", ListEnDFSHow)

    case_selector_activation = txtF.TrueFalseTxt(generalFileName, "Type4_selection")
    print("case_selector_activation=", case_selector_activation)

    Type4_selection_ID_instances = txtF.listIntTxt(generalFileName, "Type4_selection_ID_instances")
    print("Type4_selection_ID_instances=", Type4_selection_ID_instances)

    Type4_Count = txtF.TypeCount(generalFileName, "Type4_Count")
    print("Type4_Count=", Type4_Count)


    Type4_approach = txtF.TypeCount(generalFileName, "Type4_approach")
    print("Type4_approach=", Type4_approach)

    Type4_Domain_selection = txtF.TrueFalseTxt(generalFileName, "Type4_Domain_selection")
    print("Type4_Domain_selection=", Type4_Domain_selection)

    Type4_Domain_ID = txtF.listIntTxt(generalFileName, "Type4_Domain_ID")
    print("Type4_Domain_ID=", Type4_Domain_ID)

    if Type4_approach == 0:
        case_selector = "Not Exist"
        print("case_selector=", case_selector)

        case_selector_list = "Not Exist"
        print("case_selector_list=", case_selector_list)

    if Type4_approach == 1:
        case_selector, case_selector_list = funcConf.case_Selector(Type4_selection_ID_instances)
        print("case_selector=", case_selector)
        print("case_selector_list=", case_selector_list)

    if Type4_approach == 2:
        case_selector, case_selector_list = funcConf.case_Selector(Type4_selection_ID_instances)
        print("case_selector=", case_selector)
        print("case_selector_list=", case_selector_list)




else:
    import random

    n = len(range(EnNum))
    ListEnDFSHow = [0] * n
    random_index = random.randint(0, n - 1)
    ListEnDFSHow[random_index] = 1
    print("Entity_DF_Show (ListEnDFSHow)=", ListEnDFSHow)

    case_selector_activation = False
    print("case_selector_activation=", case_selector_activation)

    Type4_selection_ID_instances = "Not Exist"
    print("Type4_selection_ID_instances=", Type4_selection_ID_instances)

    Type4_Count = 1
    print("Type4_Count=", Type4_Count)

    case_selector = "Not Exist"
    print("case_selector=", case_selector)

    case_selector_list = "Not Exist"
    print("case_selector_list=", case_selector_list)


    Type4_Domain_selection = False
    print("Type4_Domain_selection=", Type4_Domain_selection)

    Type4_Domain_ID = "Not Exist"
    print("Type4_Domain_ID=", Type4_Domain_ID)


print("********************************* Output files *************************************************")


print("Output_Graph_File_Name=",Ne0.Output_Graph_File_Name)
input='Scenario_' + str(Ne0.DFG_Selection)
print("input=",input)
inputName = input
filename= inputName+ "_" + str(1)
print("filename=",filename)

downloadDir = "../../media/download/dfgTool"
downD = os.path.realpath(downloadDir)
outputDirectory= str(Ne0.DFG) +'_Files'
outdir = downD  + "/" +  outputDirectory

if not os.path.exists(outdir):
    os.mkdir(outdir)



i = 1
while os.path.exists(outdir + '/' + inputName + "_%s" % i):
    #print("i=",i)
    i += 1
    filename = inputName + "_" + str(i)
    #print("filename=",filename)

outdirMic = outdir + '/' + filename
print("outdirMic=",outdirMic)
if not os.path.isdir(outdirMic):
    os.mkdir(outdirMic)


graphviz_QueryLocation = outdirMic + "/" + filename + "_graphviz.txt"
with open(graphviz_QueryLocation, 'w') as file:
    file.write(f'''''')
print("\n A txt file for saving Queries was created")

print("*********************************Conditional***********************************************************")

dot = Digraph(comment='Query Result')
dot.attr("graph", rankdir="LR", margin="0")



print("*********************************DF_based_on_Entities***********************************************************")
print("final_DFG_List_Abs_color=",final_DFG_List_Abs_color)
cl9.DFC_based_on_Origins(final_DFG_List_Abs_color, ID_Colors, ListEnDFSHow, Type4_Count, case_selector, case_selector_activation, c_white, c_black, dot, driver, DomainColors,domainColTitle,Activity, colTitle, Type4_Domain_selection, Type4_Domain_ID,graphviz_QueryLocation)


print("*********************************Adding_Entities**********************************************")
print("final_DFG_List_Abs_color=",final_DFG_List_Abs_color)
cl9.DFC_Adding_Entities(final_DFG_List_Abs_color, ID_Colors, ListEnDFSHow, Type4_Count, case_selector, case_selector_activation, case_selector_list, c_white, c_black, dot, driver, Type4_Domain_selection, Type4_Domain_ID, domainColTitle,graphviz_QueryLocation)



print("*********************************Adding_Domains_Colors_Hint**********************************************")
print("final_DFG_List_Abs_color=",final_DFG_List_Abs_color)
cl9.Adding_Domains_Colors_Hint(final_DFG_List_Abs_color, ListEnDFSHow, Type4_Count, case_selector, case_selector_activation, DomainColors, c_white, c_black, dot, driver, domainColTitle, Type4_Domain_selection, Type4_Domain_ID,graphviz_QueryLocation)





####################################Output######################################################################
################################################################################################################
################################################################################################################
################################################################################################################
################################################################################################################

print("")
print("")
print("********************************* Creating Output*******************************************************")

print("input=",input)
print("filename=",filename)
print("outdirMic=",outdirMic)





print("\n Converting to DOT File:")
DOT_Output_Location = f'{outdirMic}/{filename}.dot'
file = open(DOT_Output_Location, "w")
file.write(dot.source)
file.close()
print("\n Dot File was created")

'''
#Showing Dot File
DOT_Output = f'xdot "{outdirMic}/{filename}.dot"'
print(DOT_Output)
os.system(DOT_Output)
'''

print("\n Converting to PDF File:")
PDF_Output_Location = f'{outdirMic}/{filename}.pdf'
PDF_Output = f'dot -Tpdf "{DOT_Output_Location}" -o "{PDF_Output_Location}"'
os.system(PDF_Output)
print("\n PDF File was created")

'''
#Showing Dot File
if platform.system() == 'Linux':
    chrome_path_in_Linux='/usr/bin/google-chrome-stable  %s'
    webbrowser.get(chrome_path_in_Linux).open_new_tab(PDF_Output_Location)
'''


############################################################################################
############################################################################################
############################################################################################
############################################################################################

'''
print("\n Converting to JPG Files:")
import B02_jpg as function
n=8
resolutionDPI=300
function.jpgCreator(filename, outdirMic,PDF_Output_Location, n, resolutionDPI)
print("\n JPG Files were created")
'''

print("\n Converting to Split PFDF File:")
x=[4,8,10,20]
import B02_pdf as bPDF
bPDF.splitPDFCreator(outdirMic, filename, x)
print("\n Splitting PDFs were done")




############################################################################################

print("\n Neo4J Query to SVG:")
import B02_svg as svgFunction
selenium = cla.selenium
driverUserName=cla.driverUserName
driverPassword=cla.driverPassword

runingQuery = f'''
MATCH (n:Activity) RETURN n LIMIT 25
'''
if selenium==True:

    svgFunction.exportNeo4jSVG(runingQuery, driverUserName, driverPassword)
    svgFunction.moveSVG(outdirMic,filename)
    print("\n SVG File was created")

############################################################################################

print("\n Neo4J Query to txt:")

neo4j_txtQuery = outdirMic + "/" + filename + "_neo4j.txt"
with open(neo4j_txtQuery, 'a') as file:
    file.write(f'''//Neo4J Query for creating graph''')
    file.write(f'''\n{runingQuery}\n\n''')
print("\n Neo4J Query to txt was finished")

############################################################################################

print("\n Saving the location of production:")
confDirectory  = "../Data/0_DataConf"
confPath = os.path.realpath(confDirectory)

savingTxt1 = confPath + "/" + "X1_dfgGraphvizPdfLocation.txt"
with open(savingTxt1, 'w') as file:
    file.write(f'''{outdirMic}/{filename}.pdf''')

savingTxt2 = confPath + "/" + "X2_dfgGraphvizDotLocation.txt"
with open(savingTxt2, 'w') as file:
    file.write(f'''{outdirMic}/{filename}.dot''')

savingTxt3 = confPath + "/" + "X3_dfgGraphvizQueryLocation.txt"
with open(savingTxt3, 'w') as file:
    file.write(f'''{graphviz_QueryLocation}''')

savingTxt4 = confPath + "/" + "X4_dfgNeo4jSVgLocation.txt"
with open(savingTxt4, 'w') as file:
    file.write(f'''{outdirMic}/{filename}.svg''')

savingTxt5 = confPath + "/" + "X5_dfgNeo4jQueryLocation.txt"
with open(savingTxt5, 'w') as file:
    file.write(f'''{neo4j_txtQuery}''')

savingTxt6 = confPath + "/" + "X6_dfgNeo4jQueries.txt"
with open(savingTxt6, 'w') as destination_file:
    with open(graphviz_QueryLocation, 'r') as source_file:
        content = source_file.read()
        destination_file.write(content)

savingTxt7 = confPath + "/" + "X7_dfgGraphvizQueries.txt"
with open(savingTxt7, 'w') as destination_file:
    with open(neo4j_txtQuery, 'r') as source_file:
        content = source_file.read()
        destination_file.write(content)


print("\n Output location saving were done")