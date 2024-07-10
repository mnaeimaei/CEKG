from neo4j import GraphDatabase
import platform
from graphviz import Digraph
import os

import A5_EntryCol_Step3_Step as cla

import A1_Scenario_Step2 as Ne0
import A6_Scenario_Final_Step as Ne02



import B02_Colors as cl7_color



import W64_funcCfgs_DFG5_featureValue_Domain_Relative_50 as funcConf
import W65_funcs_DFG5_featureValue_Domain_Relative_50 as cl9

import B02_txt_read as txtF
import B02_base as cl2
import webbrowser


print("************************** From cla: ****************************************************************************")


driver=cla.driver



print("************************** From cl1: ****************************************************************************")
entityList = Ne02.entityList
print("entityList=", entityList)

EnNum=len(Ne02.entityList)
print("EnNum=", EnNum)


entityListIDproperty=Ne02.entityListIDproperty
print("entityListIDproperty=",entityListIDproperty)


conditionProperty=Ne02.conditionProperty
print("conditionProperty=",conditionProperty)

conditionPropertyValue=Ne02.conditionPropertyValue
print("conditionPropertyValue=",conditionPropertyValue)


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
print(len(ID_Colors))

NodeColors=cl7_color.NodeColors
print("NodeColors=",NodeColors)




print("************************** conf conf ****************************************************************************")



confDirectory = "../Data/0_Conf"
confPath = os.path.realpath(confDirectory)
print(confPath)

generalFileName = (Ne0.DFG) + "_general"
print("generalFileName=", generalFileName)

txtFileExistance = txtF.txtExistance(generalFileName)
print("txtFileExistance=", txtFileExistance)



if txtFileExistance == True:
    Type5_Rel_1_DF_Show = txtF.stringTxt(generalFileName, "Type5_Rel_1_DF_Show")

    print("Type5_Rel_1_DF_Show=", Type5_Rel_1_DF_Show)

    Entity1=Type5_Rel_1_DF_Show.replace("\"","")
    print("Entity1=", Entity1)

    Type5_Rel_2_DF_Show = txtF.stringTxt(generalFileName, "Type5_Rel_2_DF_Show")
    print("Type5_Rel_2_DF_Show=", Type5_Rel_2_DF_Show)

    Entity2=Type5_Rel_2_DF_Show.replace("\"","")
    print("Entity2=", Entity2)


    Type5_Count = txtF.TypeCount(generalFileName, "Type5_Count")
    print("Type5_Count=", Type5_Count)


    case_selector_activation1 = txtF.TrueFalseTxt(generalFileName, "Type5_Rel_1_DF_Show_selection")
    print("case_selector_activation1=", case_selector_activation1)


    Type5_approach = txtF.TypeCount(generalFileName, "Type5_approach")
    print("Type5_approach=", Type5_approach)

    if Type5_approach == 0:
        print("approach is 0")
        Type5_Rel_1_DF_Show_selection_ID_instances = []
        print("Type5_Rel_1_DF_Show_selection_ID_instances=", Type5_Rel_1_DF_Show_selection_ID_instances)

        case_selector1, case_selector3, case_selector_list1 = funcConf.case_Selector1(Type5_Rel_1_DF_Show_selection_ID_instances)
        print("case_selector1=", case_selector1)
        print("case_selector3=", case_selector3)
        print("case_selector_list1=", case_selector_list1)


    if Type5_approach == 1:
        print("approach is 1")
        Type5_Rel_1_DF_Show_selection_ID_instances = txtF.listIntTxt(generalFileName,"Type5_Rel_1_DF_Show_selection_ID_instances")
        print("Type5_Rel_1_DF_Show_selection_ID_instances=", Type5_Rel_1_DF_Show_selection_ID_instances)


        case_selector1, case_selector3, case_selector_list1 = funcConf.case_Selector1(Type5_Rel_1_DF_Show_selection_ID_instances)
        print("case_selector1=", case_selector1)
        print("case_selector3=", case_selector3)
        print("case_selector_list1=", case_selector_list1)

    if Type5_approach == 2:
        print("approach is 2")
        Type5_Rel_1_DF_Show_selection_ID_instances = txtF.listIntTxt(generalFileName,"Type5_Rel_1_DF_Show_selection_ID_instances")
        print("Type5_Rel_1_DF_Show_selection_ID_instances=", Type5_Rel_1_DF_Show_selection_ID_instances)

        case_selector1, case_selector3, case_selector_list1 = funcConf.case_Selector1(Type5_Rel_1_DF_Show_selection_ID_instances)
        print("case_selector1=", case_selector1)
        print("case_selector3=", case_selector3)
        print("case_selector_list1=", case_selector_list1)


    case_selector_activation2 = txtF.TrueFalseTxt(generalFileName, "Type5_Rel_2_DF_Show_selection")
    print("case_selector_activation2=", case_selector_activation2)


    Type5_Rel_2_DF_Show_selection_ID_instances = txtF.listIntTxt(generalFileName, "Type5_Rel_2_DF_Show_selection_ID_instances")
    print("Type5_Rel_2_DF_Show_selection_ID_instances=", Type5_Rel_2_DF_Show_selection_ID_instances)

    case_selector2, case_selector4, case_selector_list2 = funcConf.case_Selector2(Type5_Rel_2_DF_Show_selection_ID_instances)
    print("case_selector2=", case_selector2)
    print("case_selector4=", case_selector4)
    print("case_selector_list2=", case_selector_list2)


    Type5_Domain_selection = txtF.TrueFalseTxt(generalFileName, "Type5_Domain_selection")
    print("Type5_Domain_selection=", Type5_Domain_selection)

    Type5_Domain_ID = txtF.listIntTxt(generalFileName, "Type5_Domain_ID")
    print("Type5_Domain_ID=", Type5_Domain_ID)







else:

    print("No File")

    Entity1, Entity2 = funcConf.entityFinder(driver)
    print("Entity1=", Entity1)
    print("Entity2=", Entity2)

    Type5_Count = 1
    print("Type5_Count=", Type5_Count)


    case_selector_activation1 = False
    print("case_selector_activation1=", case_selector_activation1)


    Type5_Rel_1_DF_Show_selection_ID_instances = []
    print("Type5_Rel_1_DF_Show_selection_ID_instances=", Type5_Rel_1_DF_Show_selection_ID_instances)


    case_selector_activation2 = False
    print("case_selector_activation2=", case_selector_activation2)


    Type5_Rel_2_DF_Show_selection_ID_instances = []
    print("Type5_Rel_2_DF_Show_selection_ID_instances=", Type5_Rel_2_DF_Show_selection_ID_instances)

    case_selector1, case_selector3, case_selector_list1 = funcConf.case_Selector1(
        Type5_Rel_1_DF_Show_selection_ID_instances)
    print("case_selector1=", case_selector1)
    print("case_selector3=", case_selector3)
    print("case_selector_list1=", case_selector_list1)



    case_selector2, case_selector4, case_selector_list2 = funcConf.case_Selector2(Type5_Rel_2_DF_Show_selection_ID_instances)
    print("case_selector2=", case_selector2)
    print("case_selector4=", case_selector4)
    print("case_selector_list2=", case_selector_list2)



    Type5_Domain_selection = False
    print("Type5_Domain_selection=", Type5_Domain_selection)

    Type5_Domain_ID = "Not Exist"
    print("Type5_Domain_ID=", Type5_Domain_ID)





print("********************************* From REL ***********************************************************")



DomainValue=funcConf.Finading_DomainValue(driver,DomainNode,domainColTitle)
print("DomainValue=",DomainValue)

DomainColors=funcConf.Domain_colors_creater(DomainValue, NodeColors)
print("DomainColors=", DomainColors)

entityIDlists = funcConf.Finading_Entities_ID_2(driver, Entity1)
print("entityIDlists=", entityIDlists)

rel_all = funcConf.relationship_rel(Entity1, Entity2, entityIDlists)
print("rel_all=", rel_all)

rel_list = funcConf.final_DFG_List_func_3(rel_all)
print("rel_list=", rel_list)






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
print("rel_list=",rel_list)
cl9.DFC_based_on_Origins(rel_list, ID_Colors, Type5_Count, c_white, c_black, dot, driver,DomainColors,domainColTitle,Activity, colTitle,case_selector_activation1,case_selector_list1,case_selector1,case_selector_activation2,case_selector_list2,case_selector2, case_selector3, case_selector4,Type5_Domain_selection, Type5_Domain_ID,graphviz_QueryLocation)




print("*********************************Adding_Entities**********************************************")
print("rel_list=",rel_list)
cl9.DFC_Adding_Entities(rel_list, Type5_Count, ID_Colors, c_white, c_black,dot, driver,case_selector_activation1,case_selector_list1,case_selector1,case_selector_activation2,case_selector_list2,case_selector2,domainColTitle,Type5_Domain_selection, Type5_Domain_ID,graphviz_QueryLocation)



print("*********************************Adding_Domains_Colors_Hint***********************************************************")
print("rel_list=",rel_list)
cl9.Adding_Domains_Colors_Hint(rel_list, Type5_Count, DomainColors, c_white, c_black, dot, driver,domainColTitle,case_selector_activation1,case_selector_list1,case_selector1,case_selector_activation2,case_selector_list2,case_selector2,Type5_Domain_selection, Type5_Domain_ID,graphviz_QueryLocation)



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