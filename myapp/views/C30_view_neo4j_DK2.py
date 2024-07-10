from django.shortcuts import render, redirect
from django.http import JsonResponse
from myapp.forms import NextButton1
import subprocess
import pandas as pd
from django.http import HttpResponse
import json
import logging
from myapp.webSocketFunctions import ProgressBar

def DK2Neo4jFunc(request):
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger = logging.getLogger("myapp")

    import os
    import ast

    confDirectory = "./myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    svgDirectory = "./myapp/Data/0_svgLocation"
    downS = os.path.realpath(svgDirectory)
    svgPath = downS + "/" + '09_DK2'

    dataDirectory  = './media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)


    downloadDir = "./media/download/dfgTool"
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '09_DK2'

    openingPath = confPath + "/3_pageSequencePart2.txt"
    with open(openingPath, 'r') as file:
        data = file.read()
        listData = ast.literal_eval(data)

    openingPath = confPath + "/3_pageSequencePart3.txt"
    with open(openingPath, 'r') as file:
        data = file.read()
        runingScripts = ast.literal_eval(data)

    if request.method == 'POST':
        logger.info(
            f"************************************************************************************************************************************************************************************************************")

        ProgressBar.run_scripts_asynchronously(script_directory, runingScripts[10])


        return redirect(listData[10])

    else:
        logger.info(
            f"************************************************************************************************************************************************************************************************************")

        nextButton = NextButton1()



        return render(request, 'C30_neo4j_DK2.html', {
            'nextButton': nextButton

        }
                      )


