from django.shortcuts import render,redirect
from django.http import JsonResponse


from myapp.forms import Dk7ActivityValueIdForm
from myapp.forms import Dk7DisordersForm

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

def DK7(request):
    import os
    import ast

    confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "../mydjangoapp/myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    dataDirectory  = '../mydjangoapp/media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

    if request.method == 'POST':
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the DK7 view POST part")

        dk7_activity_value_id_form = Dk7ActivityValueIdForm(request.POST)
        dk7_disorders_form = Dk7DisordersForm(request.POST)

        logger.debug(f"dk7_activity_value_id_form.is_valid() = {dk7_activity_value_id_form.is_valid()}")
        logger.debug(f"dk7_disorders_form.is_valid() = {dk7_disorders_form.is_valid()}")


        options_text_path = confPath + "/19_dk7Mapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/19_dk7Default.txt"

        def update_variable_in_file(file_path, variable_to_update, new_value):
            with open(file_path, 'r') as file:
                lines = file.readlines()

            # Update the specific line
            updated = False
            for i, line in enumerate(lines):
                if line.strip().startswith(variable_to_update):
                    lines[i] = f"{variable_to_update}={new_value}\n"
                    updated = True
                    break
            if updated:
                with open(file_path, 'w') as file:
                    file.writelines(lines)

        if dk7_activity_value_id_form.is_valid():
            DK7_Activity_Value_ID = dk7_activity_value_id_form.cleaned_data.get('dynamic_choice_B19_1')
            DK7_Activity_Value_ID = options_text_map[DK7_Activity_Value_ID]
            update_variable_in_file(savingPath, "DK7_Activity_Value_ID", DK7_Activity_Value_ID)

        if dk7_disorders_form.is_valid():
            DK7_Disorders = dk7_disorders_form.cleaned_data.get('dynamic_choice_B19_2')
            DK7_Disorders = options_text_map[DK7_Disorders]
            update_variable_in_file(savingPath, "DK7_Disorders", DK7_Disorders)

        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)


        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[16])


    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")


        dk7_activity_value_id_form = Dk7ActivityValueIdForm()
        dk7_disorders_form = Dk7DisordersForm()

        nextButton = NextButton1()

        openingPath = confPath + "/19_dk7DefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b19 = json.dumps(listData2)

        openingPath2 = confPath + "/19_dk7Number.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b19 = json.dumps(listData4)

        csvPath = dataPath + "/P_DK7.csv"
        df_DK7 = pd.read_csv(csvPath)
        logger.info(df_DK7)
        html_DK7 = df_DK7.to_html(classes='dataframe', index=False)



        return render(request, 'B19_csv_DK7.html', {
            'html_DK7': html_DK7,
            'dk7_activity_value_id_form': dk7_activity_value_id_form,
            'dk7_disorders_form': dk7_disorders_form,
            'options_to_show_default_b19': options_to_show_default_b19,
            'button_lists_b19': button_lists_b19,
            'nextButton': nextButton

                                            }
                  )


