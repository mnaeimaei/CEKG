from django.shortcuts import render,redirect
from django.http import JsonResponse


from myapp.forms import ApIdForm
from myapp.forms import ApActivityNameForm
from myapp.forms import ApActivitySynonymForm
from myapp.forms import ApLabelForm
from myapp.forms import ApValueForm

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

def activityProperties(request):
    import os
    import ast
    confDirectory = "./myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)


    dataDirectory  = './media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

    if request.method == 'POST':
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view POST part")


        ap_id_form = ApIdForm(request.POST)
        ap_activity_name_form = ApActivityNameForm(request.POST)
        ap_activity_synonym_form = ApActivitySynonymForm(request.POST)
        ap_label_form = ApLabelForm(request.POST)
        ap_value_form = ApValueForm(request.POST)

        logger.debug(f"ap_id_form.is_valid() = {ap_id_form.is_valid()}")
        logger.debug(f"ap_activity_name_form.is_valid() = {ap_activity_name_form.is_valid()}")
        logger.debug(f"ap_activity_synonym_form.is_valid() = {ap_activity_synonym_form.is_valid()}")
        logger.debug(f"ap_label_form.is_valid() = {ap_label_form.is_valid()}")
        logger.debug(f"ap_value_form.is_valid() = {ap_value_form.is_valid()}")

        options_text_path = confPath + "/7_acPropertiesMapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/7_acPropertiesDefault.txt"

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

        if ap_id_form.is_valid():
            AcP_acID = ap_id_form.cleaned_data.get('dynamic_choice_B7_1')
            AcP_acID = options_text_map[AcP_acID]
            update_variable_in_file(savingPath, "AcP_acID", AcP_acID)

        if ap_activity_name_form.is_valid():
            AcP_activityName = ap_activity_name_form.cleaned_data.get('dynamic_choice_B7_2')
            AcP_activityName = options_text_map[AcP_activityName]
            update_variable_in_file(savingPath, "AcP_activityName", AcP_activityName)

        if ap_activity_synonym_form.is_valid():
            AcP_activitySynonym = ap_activity_synonym_form.cleaned_data.get('dynamic_choice_B7_3')
            AcP_activitySynonym = options_text_map[AcP_activitySynonym]
            update_variable_in_file(savingPath, "AcP_activitySynonym", AcP_activitySynonym)

        if ap_label_form.is_valid():
            AcP_label = ap_label_form.cleaned_data.get('dynamic_choice_B7_4')
            AcP_label = options_text_map[AcP_label]
            update_variable_in_file(savingPath, "AcP_label", AcP_label)

        if ap_value_form.is_valid():
            AcP_Value = ap_value_form.cleaned_data.get('dynamic_choice_B7_5')
            AcP_Value = options_text_map[AcP_Value]
            update_variable_in_file(savingPath, "AcP_Value", AcP_Value)

        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[4])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")


        ap_id_form = ApIdForm()
        ap_activity_name_form = ApActivityNameForm()
        ap_activity_synonym_form = ApActivitySynonymForm()
        ap_label_form = ApLabelForm()
        ap_value_form = ApValueForm()

        nextButton = NextButton1()

        openingPath = confPath + "/7_acPropertiesDefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b7 = json.dumps(listData2)

        openingPath2 = confPath + "/7_acPropertiesNumber.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b7 = json.dumps(listData4)

        csvPath = dataPath + "/E_Activity_Properties.csv"
        df_Activity_Properties = pd.read_csv(csvPath)
        logger.info(df_Activity_Properties)
        html_Activity_Properties = df_Activity_Properties.to_html(classes='dataframe', index=False)



        return render(request, 'B7_csv_activityProperties.html', {
            'html_Activity_Properties': html_Activity_Properties,
            'ap_id_form': ap_id_form,
            'ap_activity_name_form': ap_activity_name_form,
            'ap_activity_synonym_form': ap_activity_synonym_form,
            'ap_label_form': ap_label_form,
            'ap_value_form': ap_value_form,
            'options_to_show_default_b7': options_to_show_default_b7,
            'button_lists_b7': button_lists_b7,
            'nextButton': nextButton
                                            }
                  )


