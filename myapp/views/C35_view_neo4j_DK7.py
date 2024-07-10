from django.shortcuts import render, redirect
from django.http import JsonResponse
from myapp.forms import NextButton1
import subprocess
import pandas as pd
from django.http import HttpResponse
import json
import logging
from myapp.webSocketFunctions import ProgressBar

def DK7Neo4jFunc(request):
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logger = logging.getLogger("myapp")

    import os
    import ast

    confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "../mydjangoapp/myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    dataDirectory  = '../mydjangoapp/media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

    svgDirectory = "../mydjangoapp/myapp/Data/0_svgLocation"
    downS = os.path.realpath(svgDirectory)
    svgPath =  downS + "/" + '14_DK7'


    downloadDir = "../mydjangoapp/media/download/dfgTool"
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '14_DK7'

    openingPath = confPath + "/3_pageSequencePart2.txt"
    with open(openingPath, 'r') as file:
        data = file.read()
        listData = ast.literal_eval(data)

    openingPath = confPath + "/3_pageSequencePart3.txt"
    with open(openingPath, 'r') as file:
        data = file.read()
        runingScripts = ast.literal_eval(data)
        logger.info(runingScripts)

    if request.method == 'POST':
        logger.info(
            f"******* neo4j DK7 *************************************************************************************************************************************************************************************************")

        #Runing Q
        ProgressBar.run_scripts_asynchronously(script_directory, runingScripts[15])


        return redirect(listData[15])

    else:
        logger.info(
            f"************************************************************************************************************************************************************************************************************")

        nextButton = NextButton1()

        savingTxt1 = outDir + "/" + "Q1.txt"
        savingTxt2 = outDir + "/" + "Q2.txt"

        savingSvg2 = svgPath + "/" + "Q2_svg_location.txt"


        with open(savingTxt1, 'r') as file:
            query1 = file.read()
            logger.info(f"\nquery1 : {query1}")

        with open(savingTxt2, 'r') as file:
            query2 = file.read()
            logger.info(f"\nquery2 : {query2}")

        ###############################################3


        with open(savingSvg2, 'r') as file:
            svg2 = file.read()
            logger.info(f"\nsvg2 : {svg2}")



        return render(request, 'C35_neo4j_DK7.html', {
            'nextButton': nextButton,
            'query1': query1,
            'query2': query2,

            'svg2': svg2,



        }
                      )


