from django.shortcuts import render, redirect


from myapp.forms import UserNameNeo
from myapp.forms import PassWordNeo
from myapp.forms import NextButton1


from myapp.webSocketFunctions import ProgressBar

import subprocess

from django.http import HttpResponse
import json
import logging

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")


def importing_view(request):
    import os
    import ast
    import os
    confDirectory = "./myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)


    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)
    if request.method == 'POST' :
        logger.debug(f"Hello23")
        logger.info("This is an info message")

        userNameNeo = UserNameNeo(request.POST)
        passWordNeo = PassWordNeo(request.POST)

        logger.debug(f"userNameNeo.is_valid() = {userNameNeo.is_valid()}")
        logger.debug(f"passWordNeo.is_valid() = {passWordNeo.is_valid()}")

        if userNameNeo.is_valid():
            logger.debug(f"userNameNeo.cleaned_data = {userNameNeo.cleaned_data}")
            userNameNeo_json = json.dumps(userNameNeo.cleaned_data)
            finalUserName = userNameNeo.cleaned_data.get('userNameNeoMode')



        if passWordNeo.is_valid():
            logger.debug(f"passWordNeo.cleaned_data = {passWordNeo.cleaned_data}")
            passWordNeo_json = json.dumps(passWordNeo.cleaned_data)
            finalPassWord = passWordNeo.cleaned_data.get('passWordNeoMode')

        savingFile4 = confPath + "/" + "2_downloadingLocal1.txt"
        with open(savingFile4, 'w') as file:
            file.write(f'''finalUsrWord={finalUserName}''' + "\n")

        savingFile5 = confPath + "/" + "2_downloadingLocal2.txt"
        with open(savingFile5, 'w') as file:
            file.write(f'''finalPassWord={finalPassWord}''' + "\n")

        scripts = [
            'A2_FileLocation_Step2_xlsx_Step.py',
            'A2_FileLocation_Step3_sheetName_Step.py'
        ]

        ProgressBar.run_scripts_asynchronously(script_directory, scripts)

        return redirect('excelPreview')

    else:

        userNameNeo = UserNameNeo()
        passWordNeo = PassWordNeo()
        nextButton=NextButton1()

        defaultUser, defaultPass = existanceFileName(confPath)
        logger.info(defaultUser)
        logger.info(defaultPass)

        return render(request, 'A02_downloading.html', {
            'userNameNeo': userNameNeo,
            'passWordNeo': passWordNeo,
            'defaultUser': defaultUser,
            'defaultPass': defaultPass,
            'nextButton': nextButton,

        }
                      )


def existanceFileName(confPath):
    value3 = ""
    value4 = ""

    import os

    inputTex_FilePath = confPath + "/2_downloadingLocal1.txt"
    if os.path.exists(inputTex_FilePath):
        with open(inputTex_FilePath, 'r') as file:
            for line in file:
                variable_name, value3 = line.split('=')
                value3 = value3.strip()

    inputTex_FilePath = confPath + "/2_downloadingLocal2.txt"
    if os.path.exists(inputTex_FilePath):
        with open(inputTex_FilePath, 'r') as file:
            for line in file:
                variable_name, value4 = line.split('=')
                value4 = value4.strip()

    return value3, value4