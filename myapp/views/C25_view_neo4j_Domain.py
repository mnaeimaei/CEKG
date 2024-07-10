from django.shortcuts import render, redirect
from django.http import JsonResponse
from myapp.forms import NextButton1
import subprocess
import pandas as pd
from django.http import HttpResponse
import json
import logging
from myapp.webSocketFunctions import ProgressBar

def DomainNeo4jFunc(request):
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

    downloadDir = "../mydjangoapp/media/download/dfgTool"
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '04_Domain'

    svgDirectory = "../mydjangoapp/myapp/Data/0_svgLocation"
    downS = os.path.realpath(svgDirectory)
    svgPath =  downS + "/" + '04_Domain'

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

        ProgressBar.run_scripts_asynchronously(script_directory, runingScripts[5])

        return redirect(listData[5])

    else:
        logger.info(
            f"************************************************************************************************************************************************************************************************************")

        nextButton = NextButton1()

        savingTxt1 = outDir + "/" + "Q1.txt"
        savingTxt2 = outDir + "/" + "Q2.txt"
        savingTxt3 = outDir + "/" + "Q3.txt"
        savingTxt4 = outDir + "/" + "Q4.txt"

        savingSvg4 = svgPath + "/" + "Q4_svg_location.txt"



        with open(savingTxt1, 'r') as file:
            query1 = file.read()
            logger.info(f"\nquery1 : {query1}")

        with open(savingTxt2, 'r') as file:
            query2 = file.read()
            logger.info(f"\nquery2 : {query2}")

        with open(savingTxt3, 'r') as file:
            query3 = file.read()
            logger.info(f"\nquery3 : {query3}")

        with open(savingTxt4, 'r') as file:
            query4 = file.read()
            logger.info(f"\nquery4 : {query4}")

        ###############################################3


        with open(savingSvg4, 'r') as file:
            svg4 = file.read()
            logger.info(f"\nsvg4 : {svg4}")




        return render(request, 'C25_neo4j_Domain.html', {
            'nextButton': nextButton,
            'query1': query1,
            'query2': query2,
            'query3': query3,
            'query4': query4,

            'svg4': svg4,



        }
                      )


