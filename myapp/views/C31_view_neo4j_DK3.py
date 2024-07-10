from django.shortcuts import render, redirect
from django.http import JsonResponse
from myapp.forms import NextButton1
import subprocess
import pandas as pd
from django.http import HttpResponse
import json
import logging
from myapp.webSocketFunctions import ProgressBar

def DK3Neo4jFunc(request):
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
    svgPath = downS + "/" + '10_DK3'

    dataDirectory  = './media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)


    downloadDir = "./media/download/dfgTool"
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '10_DK3'



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

        ProgressBar.run_scripts_asynchronously(script_directory, runingScripts[11])


        return redirect(listData[11])

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



        return render(request, 'C31_neo4j_DK3.html', {
            'nextButton': nextButton,
            'query1': query1,
            'query2': query2,

            'svg2': svg2,



        }
                      )


