from neo4j import GraphDatabase
import platform
from graphviz import Digraph
import os


import A1_Scenario_Step2 as Ne0
import A6_Scenario_Final_Step as Ne02



import B02_Colors as cl7_color

import A5_EntryCol_Step3_Step as cla


import T50_funcCfgs_DFG2_featureValue_DomainConceptLevel_16 as funcConf
import T51_funcs_DFG2_featureValue_DomainConceptLevel_16 as cl9

import B02_txt_read as txtF
import B02_base as cl2
import webbrowser

print(
    "************************** From cla: ****************************************************************************")

driver = cla.driver

print("************************** From cl1: *****************************************************")

entityList = Ne02.entityList
print("entityList=", entityList)

EnNum = len(Ne02.entityList)
print("EnNum=", EnNum)

entityListIDproperty = Ne02.entityListIDproperty
print("entityListIDproperty=", entityListIDproperty)

conditionProperty = Ne02.conditionProperty
print("conditionProperty=", conditionProperty)

conditionPropertyValue = Ne02.conditionPropertyValue
print("conditionPropertyValue=", conditionPropertyValue)

DomainNode = Ne02.DomainNode
print("DomainNode=", DomainNode)

domainColTitle = Ne02.domainColTitle[0]
print("domainColTitle=", domainColTitle)

print("************************** From cl0 for Activity: *****************************************************")

Activity = Ne0.Activity
ActivityNode = Ne02.ActivityNode
colTitle = Ne02.colTitle

print("activityScenario=", Activity)
print("ActivityNode=", ActivityNode)
print("colTitle=", colTitle)

print(
    "************************** From cl7 ****************************************************************************")

c_white = cl7_color.c_white
c_black = cl7_color.c_black
SubEntities_Color = cl7_color.SubEntities_Color

EntitiesColors = cl7_color.EntitiesColors
print("EntitiesColors=", EntitiesColors)

NodeColors = cl7_color.NodeColors
print("NodeColors=", NodeColors)

print(
    "************************** From Func: ****************************************************************************")

EntityOrgValue = funcConf.convert_to_list_of_lists(entityList)
print("EntityOrgValue=", EntityOrgValue)

EntityOriginValueTemp = funcConf.EntityOriginValue_Temp(EntityOrgValue, EnNum)
print("Entities Origin Value Temp (EntityOriginValueTemp) =", EntityOriginValueTemp)

dicNumEntOrgAbr = funcConf.NumberEntityOriginAbr(EntityOriginValueTemp, EnNum)
# print(dicNumEntTypeAbr)
locals().update(dicNumEntOrgAbr)
print("Number of Entity Org Abr (dicNumEntOrgAbr)=", dicNumEntOrgAbr)

EntOrgAbrNum = list(dicNumEntOrgAbr.values())[0]  # accessing to entity Type abbr number
print("EntOrgAbrNum=", EntOrgAbrNum)

entityIDlists = funcConf.Finading_Entities_ID(driver, entityList, entityListIDproperty, conditionProperty,
                                              conditionPropertyValue)
print("entityIDlists=", entityIDlists)

refEntityIDlists = funcConf.Finading_Reified_Entities_ID(driver, entityList)
print("refEntityIDlists=", refEntityIDlists)

DomainValue = funcConf.Finading_DomainValue(driver, DomainNode, domainColTitle)
print("DomainValue=", DomainValue)

DomainColors = funcConf.Domain_colors_creater(DomainValue, NodeColors)
print("DomainColors=", DomainColors)

print("*********************************Conf General**************************************************")

confDirectory = "../Data/0_Conf"
confPath = os.path.realpath(confDirectory)
print(confPath)

generalFileName = (Ne0.DFG) + "_general"
print("generalFileName=", generalFileName)

txtFileExistance = txtF.txtExistance(generalFileName)
print("txtFileExistance=", txtFileExistance)

if txtFileExistance == True:

    ListEnDFSHow = txtF.ShowTxt(generalFileName, EnNum, "Type2_Entity", "_DF_Show")
    print("Entity_DF_Show (ListEnDFSHow)=", ListEnDFSHow)

    case_selector_activation = txtF.TrueFalseTxt(generalFileName, "Type2_selection")
    print("case_selector_activation=", case_selector_activation)

    Type2_approach = txtF.TypeApproach(generalFileName, "Type2_approach")
    print("Type2_approach=", Type2_approach)

    Type2_selection_ID = txtF.listIntTxt(generalFileName, "Type2_selection_ID")
    print("Type2_selection_ID=", Type2_selection_ID)

    Type2_selection_ID_instances = txtF.listIntTxt(generalFileName, "Type2_selection_ID_instances")
    print("Type2_selection_ID_instances=", Type2_selection_ID_instances)

    ListEnOrgRelDFShow = txtF.ShowTxt(generalFileName, EnNum, "Type2_Entity", "OrgRel_DF_Show")
    print("Entity_Org_Rel_DF_Show (ListEnOrgRelDFShow)=", ListEnOrgRelDFShow)

    Type2_feature_Name = txtF.listIntTxt(generalFileName, "Type2_feature_Name")
    print("Type2_feature_Name=", Type2_feature_Name)

    Type2_feature_label = txtF.listIntTxt(generalFileName, "Type2_feature_label")
    print("Type2_feature_label=", Type2_feature_label)

    Type2_feature_Value = txtF.listIntTxt(generalFileName, "Type2_feature_Value")
    print("Type2_feature_Value=", Type2_feature_Value)

    Type2_Domain_selection = txtF.TrueFalseTxt(generalFileName, "Type2_Domain_selection")
    print("Type2_Domain_selection=", Type2_Domain_selection)

    Type2_Domain_ID = txtF.listIntTxt(generalFileName, "Type2_Domain_ID")
    print("Type2_Domain_ID=", Type2_Domain_ID)

    if Type2_approach == 0:
        case_selector1 = "Not Exist"
        print("case_selector1=", case_selector1)

        case_selector2 = "Not Exist"
        print("case_selector2=", case_selector2)

    if Type2_approach == 1:
        case_selector1 = funcConf.case_Selector1(Type2_selection_ID, Type2_selection_ID_instances)
        case_selector2 = funcConf.case_Selector2(Type2_selection_ID, Type2_selection_ID_instances)
        print("case_selector1=", case_selector1)
        print("case_selector2=", case_selector2)

    if Type2_approach == 2:
        # Type2_selection_ID_new,Type2_selection_ID_instances_new  = funcConf.case_Selector_pre1(Type2_selection_ID,Type2_feature_Name, Type2_feature_label,Type2_feature_Value,driver )
        # print("Type2_selection_ID_new=", Type2_selection_ID_new)
        # print("Type2_selection_ID_instances_new=", Type2_selection_ID_instances_new)

        # result
        # Type2_selection_ID_new==['Patient', 'Admission', 'Concept']
        # Type2_selection_ID_instances_new=[['1'], ['1'], ['1']]

        Type2_selection_ID_instances_new = funcConf.case_Selector_pre2(Type2_selection_ID, Type2_feature_Name,
                                                                       Type2_feature_label, Type2_feature_Value, driver)
        print("Type2_selection_ID_instances_new=", Type2_selection_ID_instances_new)

        case_selector = funcConf.case_Selector(Type2_selection_ID, Type2_selection_ID_instances_new)
        print("case_selector=", case_selector)




else:

    ListEnDFSHow = []
    # Loop through each number up to n
    for i in range(EnNum):
        # Append 1 if the current index is even (including 0), otherwise append 0
        ListEnDFSHow.append(1)

    print("Entity_DF_Show (ListEnDFSHow)=", ListEnDFSHow)

    case_selector_activation = False
    print("case_selector_activation=", case_selector_activation)

    ListEnOrgRelDFShow = []
    # Loop through each number up to n
    for i in range(EnNum):
        # Append 1 if the current index is even (including 0), otherwise append 0
        ListEnOrgRelDFShow.append(1)

    print("Entity_Org_Rel_DF_Show (ListEnOrgRelDFShow)=", ListEnOrgRelDFShow)

    case_selector1 = "Not Exist"
    print("case_selector1=", case_selector1)

    case_selector2 = "Not Exist"
    print("case_selector2=", case_selector2)

    Type2_Domain_selection = False
    print("Type2_Domain_selection=", Type2_Domain_selection)

    Type2_Domain_ID = "Not Exist"
    print("Type2_Domain_ID=", Type2_Domain_ID)


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

print(
    "*********************************DF_based_on_Entities***********************************************************")

cl9.DF_based_on_Entities(entityList, entityIDlists, EntOrgAbrNum, EntitiesColors, ListEnDFSHow, case_selector1,
                         case_selector2, case_selector_activation, c_white, c_black, dot, driver, DomainColors,
                         domainColTitle, Activity, colTitle, Type2_Domain_selection, Type2_Domain_ID,graphviz_QueryLocation)

print("*********************************DF_based_on_ID************************************************")

cl9.DF_based_on_ID(entityList, refEntityIDlists, ListEnOrgRelDFShow, case_selector1, case_selector2,
                   case_selector_activation, c_white, c_black, SubEntities_Color, dot, driver, Type2_Domain_selection,
                   Type2_Domain_ID, domainColTitle,graphviz_QueryLocation)

print("*********************************Adding_Entities_ID ForFirstEvent**********************************************")

cl9.Adding_Entities_ID_ForFirstEvent(entityList, entityIDlists, EntitiesColors, ListEnDFSHow, case_selector1,
                                     case_selector_activation, c_white, c_black, dot, driver, Type2_Domain_selection,
                                     Type2_Domain_ID, domainColTitle,graphviz_QueryLocation)

print("*********************************Adding_Entities**********************************************")

cl9.Adding_Entities(entityList, entityIDlists, EntitiesColors, ListEnDFSHow, c_white, c_black, dot, driver,
                    case_selector2, case_selector_activation, Type2_Domain_selection, Type2_Domain_ID, domainColTitle,graphviz_QueryLocation)

print(
    "*********************************Adding_Domains_Colors_Hint***********************************************************")
print("DomainColors=", DomainColors)
cl9.Adding_Domains_Colors_Hint(entityList, entityIDlists, ListEnDFSHow, case_selector1, case_selector_activation,
                               DomainColors, c_white, c_black, dot, driver, domainColTitle, Type2_Domain_selection,
                               Type2_Domain_ID,graphviz_QueryLocation)



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