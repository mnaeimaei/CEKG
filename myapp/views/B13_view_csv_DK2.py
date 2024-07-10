from django.shortcuts import render,redirect
from django.http import JsonResponse

from myapp.forms import NextButton1


import subprocess
import os
import pandas as pd
import ast




from django.http import HttpResponse
import json
import logging
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")

def DK2(request):
    confDirectory = "../ckegWeb/myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "../ckegWeb/myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    dataDirectory  = '../ckegWeb/media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

    if request.method == 'POST':
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view POST part")

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[10])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")

        openingPath = confPath + "/13_dk2DefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b13 = json.dumps(listData2)

        openingPath2 = confPath + "/13_dk2Number.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b13 = json.dumps(listData4)

        csvPath = dataPath + "/K_DK2.csv"
        df_DK2 = pd.read_csv(csvPath)
        logger.info(df_DK2)
        html_DK2 = df_DK2.to_html(classes='dataframe', index=False)



        return render(request, 'B13_csv_DK2.html', {
            'html_DK2': html_DK2,
            'options_to_show_default_b13': options_to_show_default_b13,
            'button_lists_b13': button_lists_b13,

                                            }
                  )


