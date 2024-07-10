from django.shortcuts import render,redirect
from django.http import JsonResponse
from myapp.forms import NextButton1
import subprocess
import pandas as pd
from django.http import HttpResponse
import json
import logging
from myapp.webSocketFunctions import ProgressBar


def eventLogNeo4jFunc(request):
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
    svgPath =  downS + "/" + '01_EventLog'

    downloadDir = "../mydjangoapp/media/download/dfgTool"
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '01_EventLog'

    openingPath = confPath + "/3_pageSequencePart2.txt"
    with open(openingPath, 'r') as file:
        data = file.read()
        listData = ast.literal_eval(data)

    openingPath = confPath + "/3_pageSequencePart3.txt"
    with open(openingPath, 'r') as file:
        data = file.read()
        runingScripts = ast.literal_eval(data)

    if request.method == 'POST':
        logger.info(f"************************************************************************************************************************************************************************************************************")


        ProgressBar.run_scripts_asynchronously(script_directory, runingScripts[1])

        return redirect(listData[1])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")

        nextButton = NextButton1()

        savingTxt1 = outDir + "/" + "Q1.txt"
        savingTxt2 = outDir + "/" + "Q2.txt"
        savingTxt3 = outDir + "/" + "Q3.txt"
        savingTxt4 = outDir + "/" + "Q4.txt"
        savingTxt5 = outDir + "/" + "Q5.txt"
        savingTxt6 = outDir + "/" + "Q6.txt"
        savingTxt7 = outDir + "/" + "Q7.txt"
        savingTxt8 = outDir + "/" + "Q8.txt"
        savingTxt9 = outDir + "/" + "Q9.txt"
        savingTxt10 = outDir + "/" + "Q10.txt"
        savingTxt11 = outDir + "/" + "Q11.txt"
        savingTxt12 = outDir + "/" + "Q12.txt"


        savingSvg4 = svgPath + "/" + "Q4_svg_location.txt"
        savingSvg5 = svgPath + "/" + "Q5_svg_location.txt"
        savingSvg6 = svgPath + "/" + "Q6_svg_location.txt"
        savingSvg7 = svgPath + "/" + "Q7_svg_location.txt"
        savingSvg8 = svgPath + "/" + "Q8_svg_location.txt"
        savingSvg9 = svgPath + "/" + "Q9_svg_location.txt"
        savingSvg10 = svgPath + "/" + "Q10_svg_location.txt"
        savingSvg11 = svgPath + "/" + "Q11_svg_location.txt"
        savingSvg12 = svgPath + "/" + "Q12_svg_location.txt"





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

        with open(savingTxt5, 'r') as file:
            query5 = file.read()
            logger.info(f"\nquery5 : {query5}")

        with open(savingTxt6, 'r') as file:
            query6 = file.read()
            logger.info(f"\nquery6 : {query6}")

        with open(savingTxt7, 'r') as file:
            query7 = file.read()
            logger.info(f"\nquery7 : {query7}")

        with open(savingTxt8, 'r') as file:
            query8 = file.read()
            logger.info(f"\nquery8 : {query8}")

        with open(savingTxt9, 'r') as file:
            query9 = file.read()
            logger.info(f"\nquery9 : {query9}")

        with open(savingTxt10, 'r') as file:
            query10 = file.read()
            logger.info(f"\nquery10 : {query10}")

        with open(savingTxt11, 'r') as file:
            query11 = file.read()
            logger.info(f"\nquery11 : {query11}")

        with open(savingTxt12, 'r') as file:
            query12 = file.read()
            logger.info(f"\nquery12 : {query12}")

        ###############################################3



        with open(savingSvg4, 'r') as file:
            svg4 = file.read()
            logger.info(f"\nsvg4 : {svg4}")

        with open(savingSvg5, 'r') as file:
            svg5 = file.read()
            logger.info(f"\nsvg5 : {svg5}")

        with open(savingSvg6, 'r') as file:
            svg6 = file.read()
            logger.info(f"\nsvg6 : {svg6}")

        with open(savingSvg7, 'r') as file:
            svg7 = file.read()
            logger.info(f"\nsvg7 : {svg7}")

        with open(savingSvg8, 'r') as file:
            svg8 = file.read()
            logger.info(f"\nsvg8 : {svg8}")

        with open(savingSvg9, 'r') as file:
            svg9 = file.read()
            logger.info(f"\nsvg9 : {svg9}")

        with open(savingSvg10, 'r') as file:
            svg10 = file.read()
            logger.info(f"\nsvg10 : {svg10}")

        with open(savingSvg11, 'r') as file:
            svg11 = file.read()
            logger.info(f"\nsvg11 : {svg11}")

        with open(savingSvg12, 'r') as file:
            svg12 = file.read()
            logger.info(f"\nsvg12 : {svg12}")



        return render(request, 'C21_neo4j_EventLog.html', {
            'nextButton': nextButton,
            'query1': query1,
            'query2': query2,
            'query3': query3,
            'query4': query4,
            'query5': query5,
            'query6': query6,
            'query7': query7,
            'query8': query8,
            'query9': query9,
            'query10': query10,
            'query11': query11,
            'query12': query12,


            'svg4': svg4,
            'svg5': svg5,
            'svg6': svg6,
            'svg7': svg7,
            'svg8': svg8,
            'svg9': svg9,
            'svg10': svg10,
            'svg11': svg11,
            'svg12': svg12,


                                            }
                  )


