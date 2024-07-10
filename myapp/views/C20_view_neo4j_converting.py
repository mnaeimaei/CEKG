from django.shortcuts import render,redirect
from django.http import JsonResponse
from myapp.forms import NextButton1
import subprocess
import pandas as pd
from django.http import HttpResponse
import json
import logging
from myapp.webSocketFunctions import ProgressBar


def convertingNeo4jFunc(request):
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

    multiDirectory = "../mydjangoapp/myapp/Data/0_MultiMedia"
    multiD = os.path.realpath(multiDirectory)



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


        ProgressBar.run_scripts_asynchronously(script_directory, runingScripts[0])


        return redirect(listData[0])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")

        nextButton = NextButton1()


        jpegCKEG = multiD + "/" + "CEKG.txt"

        with open(jpegCKEG, 'r') as file:
            ckeg = file.read()
            logger.info(f"\nckeg : {ckeg}")

        return render(request, 'C20_neo4j_Converting.html', {
            'nextButton': nextButton,
            'ckeg': ckeg

                                            }
                  )


