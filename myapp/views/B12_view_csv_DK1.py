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

def DK1(request):
    confDirectory = "./myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    dataDirectory  = './media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

    if request.method == 'POST':
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view POST part")



        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[9])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")



        openingPath = confPath + "/12_dk1DefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b12 = json.dumps(listData2)

        openingPath2 = confPath + "/12_dk1Number.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b12 = json.dumps(listData4)


        csvPath = dataPath + "/J_DK1.csv"
        df_DK1 = pd.read_csv(csvPath)
        logger.info(df_DK1)
        html_DK1 = df_DK1.to_html(classes='dataframe', index=False)



        return render(request, 'B12_csv_DK1.html', {
            'html_DK1': html_DK1,
            'options_to_show_default_b12': options_to_show_default_b12,
            'button_lists_b12': button_lists_b12,

                                            }
                  )


