from neo4j import GraphDatabase
import platform
from graphviz import Digraph
import os




import A1_Scenario_Step2 as Ne0
import A6_Scenario_Final_Step as Ne02

import B02_base as cl2
import B02_Colors as cl7_color

import A5_EntryCol_Step3_Step as cla

import Z02_funcs_DFG_10 as cl17

import webbrowser

print(
    "************************** From cla: ****************************************************************************")

driver = cla.driver

dot = Digraph(comment='Query Result')
dot.attr("graph")

with dot.subgraph(name='cluster1') as cluster1:
    cluster1.attr(label=' ')
    cluster1.node('a')
    cluster1.node('b')
    cluster1.node('c')

# Create subgraph cluster2
with dot.subgraph(name='cluster2') as cluster2:
    cluster2.attr(peripheries='0')
    cluster2.attr(label='c 2')
    cluster2.node('a')
    cluster2.node('e')
    cluster2.node('f')

# Render the graph
dot.edge("a", "f", style="dashed", arrowhead="none",
                     color="#000000")


cl17.DFC_based_on_Origins ( dot, driver)


print("")
print("")
print("*********************************Output*******************************************************")



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







#Creating Dot File
DOT_Output_Location = f'{outdirMic}/{filename}.dot'
file = open(DOT_Output_Location, "w")
file.write(dot.source)
file.close()

'''
#Showing Dot File
DOT_Output = f'xdot {outdirMic}/{filename}.dot'
os.system(DOT_Output)
'''


#Creating PDF File
PDF_Output_Location = f'{outdirMic}/{filename}.pdf'
PDF_Output = f'dot -Tpdf {DOT_Output_Location} -o {PDF_Output_Location}'
os.system(PDF_Output)

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

print("\n Converting to JPG Files:")
import B02_jpg as function
n=8
resolutionDPI=300
function.jpgCreator(filename, outdirMic,PDF_Output_Location, n, resolutionDPI)


print("\n Converting to Split PFDF File:")
x=[4,8,10,20]
import B02_pdf as bPDF
bPDF.splitPDFCreator(outdirMic, filename, x)

