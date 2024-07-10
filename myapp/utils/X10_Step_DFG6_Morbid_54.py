from neo4j import GraphDatabase
import platform
from graphviz import Digraph
import os

import A5_EntryCol_Step3_Step as cla


import A1_Scenario_Step2 as Ne0
import A6_Scenario_Final_Step as Ne02



import B02_Colors as cl7_color



import X08_funcCfgs_DFG6_Morbid_54 as funcConf
import X09_funcs_DFG6_Morbid_54 as cl9

import B02_txt_read as txtF
import B02_base as cl2
import webbrowser


print("************************** Test: ****************************************************************************")

'''
Test:


match  p2=(a1:Admission)-[r1:INCLUDED]->(m1:Multimorbidity) -[r2:INCLUDED]-> (d ) -[r3:DF_E]-> (:Admission )
match  p1= (s)-[r6:INCLUDED]- (:Admission)-[r4:INCLUDED]->(m2:Multimorbidity) -[r5:INCLUDED]-> (d2 )
where  (LABELS(d) = ["untreatedMorbids"] or LABELS(d) = ["newMorbids"] or  LABELS(d) = ["treatedMorbids"])
and   (LABELS(d2) = ["untreatedMorbids"] or LABELS(d2) = ["newMorbids"] or  LABELS(d2) = ["treatedMorbids"])
and s.ID="1" and r3.sourceID="1"
RETURN p2,p1



'''
print("************************** From cla: ****************************************************************************")

driver=cla.driver

print("************************** From cl1: ****************************************************************************")


node1=funcConf.node1Finder(driver)
print("node1=",node1)



print("************************** From cl7 ****************************************************************************")

c_white=cl7_color.c_white
c_black=cl7_color.c_black

EntitiesColors=cl7_color.EntitiesColors
print("EntitiesColors=",EntitiesColors)

ID_Colors=cl7_color.ID_Colors
print("ID_Colors=",ID_Colors)
print(len(ID_Colors))

patientColor='#e31a1c'

AdmissionColor='#1f78b4'
multiMorbidityColor="#91bfdb"

TreatedColor='#70ad47'
NewDisordersColor='#a034a8'
NotTreatedColor='#f59d56'


print("************************** From conf: ****************************************************************************")

confDirectory = "../Data/0_Conf"
confPath = os.path.realpath(confDirectory)
print(confPath)

generalFileName = (Ne0.DFG) + "_general"
print("generalFileName=", generalFileName)

txtFileExistance = txtF.txtExistance(generalFileName)
print("txtFileExistance=", txtFileExistance)


if txtFileExistance == True:
    print("txtFileExistance")

    dfgType = txtF.TypeCount(generalFileName, "Type_approach")
    print("dfgType=", dfgType)


    mainEntity_selection = txtF.TrueFalseTxt(generalFileName, "mainEntity_selection")
    print("mainEntity_selection=", mainEntity_selection)


    mainEntity_selection_ID_instances = txtF.listIntTxt(generalFileName, "mainEntity_selection_ID_instances")
    print("mainEntity_selection_ID_instances=", mainEntity_selection_ID_instances)

else:

    print("No File")

    dfgType = 1
    print("dfgType=", dfgType)


    mainEntity_selection = False
    print("mainEntity_selection=", mainEntity_selection)


    mainEntity_selection_ID_instances = []
    print("mainEntity_selection_ID_instances=", mainEntity_selection_ID_instances)


case_selector=funcConf.case_Selector(mainEntity_selection_ID_instances)
print("case_selector=", case_selector)

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

cl9.DFC_based_on_Origins1(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,AdmissionColor,multiMorbidityColor,graphviz_QueryLocation)

cl9.DFC_based_on_Origins2(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,multiMorbidityColor,TreatedColor,graphviz_QueryLocation)

cl9.DFC_based_on_Origins3(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,multiMorbidityColor,NotTreatedColor,graphviz_QueryLocation)

cl9.DFC_based_on_Origins4(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,multiMorbidityColor,NewDisordersColor,graphviz_QueryLocation)

cl9.DFC_based_on_Origins5(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,TreatedColor,AdmissionColor,graphviz_QueryLocation)

cl9.DFC_based_on_Origins6(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,NotTreatedColor,AdmissionColor,graphviz_QueryLocation)

cl9.DFC_based_on_Origins7(case_selector, mainEntity_selection, c_white, c_black, dot, driver,node1,dfgType,NewDisordersColor,AdmissionColor,graphviz_QueryLocation)



print("*********************************Adding Entity ***********************************************************")

cl9.Adding_Entities_ID_ForFirstEvent(ID_Colors, case_selector, mainEntity_selection, c_white, c_black, dot, driver,EntitiesColors,node1,dfgType,patientColor,graphviz_QueryLocation)



print("*********************************Adding Entity Hint ***********************************************************")

cl9.Adding_Entities_Hint(c_white, c_black, dot, patientColor ,AdmissionColor,multiMorbidityColor, TreatedColor ,NewDisordersColor,NotTreatedColor,graphviz_QueryLocation)





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