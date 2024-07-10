from django.shortcuts import render,redirect
from django.http import JsonResponse


from myapp.forms import OenOriginForm
from myapp.forms import OenIDForm
from myapp.forms import OenNameForm
from myapp.forms import OenValueForm
from myapp.forms import OenCategoryForm

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

def otherEntities(request):
    import ast
    import os
    confDirectory = "../mydjangoapp/myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "../mydjangoapp/myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    dataDirectory  = '../mydjangoapp/media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

    if request.method == 'POST':
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view POST part")

        oen_origin_form = OenOriginForm(request.POST)
        oen_id_form = OenIDForm(request.POST)
        oen_name_form = OenNameForm(request.POST)
        oen_value_form = OenValueForm(request.POST)
        oen_category_form = OenCategoryForm(request.POST)


        logger.debug(f"oen_origin_form.is_valid() = {oen_origin_form.is_valid()}")
        logger.debug(f"oen_id_form.is_valid() = {oen_id_form.is_valid()}")
        logger.debug(f"oen_name_form.is_valid() = {oen_name_form.is_valid()}")
        logger.debug(f"oen_value_form.is_valid() = {oen_value_form.is_valid()}")
        logger.debug(f"oen_category_form.is_valid() = {oen_category_form.is_valid()}")

        options_text_path = confPath + "/5_otherEntitiesMapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/5_otherEntitiesDefault.txt"

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


        if oen_origin_form.is_valid():
            EnP_Origin = oen_origin_form.cleaned_data.get('dynamic_choice_B5_1')
            EnP_Origin = options_text_map[EnP_Origin]
            update_variable_in_file(savingPath, "EnP_Origin", EnP_Origin)

        if oen_id_form.is_valid():
            EnP_ID = oen_id_form.cleaned_data.get('dynamic_choice_B5_2')
            EnP_ID = options_text_map[EnP_ID]
            update_variable_in_file(savingPath, "EnP_ID", EnP_ID)

        if oen_name_form.is_valid():
            EnP_Name = oen_name_form.cleaned_data.get('dynamic_choice_B5_3')
            EnP_Name = options_text_map[EnP_Name]
            update_variable_in_file(savingPath, "EnP_Name", EnP_Name)

        if oen_value_form.is_valid():
            EnP_Value = oen_value_form.cleaned_data.get('dynamic_choice_B5_4')
            EnP_Value = options_text_map[EnP_Value]
            update_variable_in_file(savingPath, "EnP_Value", EnP_Value)

        if oen_category_form.is_valid():
            EnP_Category = oen_category_form.cleaned_data.get('dynamic_choice_B5_5')
            EnP_Category = options_text_map[EnP_Category]
            update_variable_in_file(savingPath, "EnP_Category", EnP_Category)


        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)


        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[2])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")


        oen_origin_form = OenOriginForm()
        oen_id_form = OenIDForm()
        oen_name_form = OenNameForm()
        oen_value_form = OenValueForm()
        oen_category_form = OenCategoryForm()

        nextButton = NextButton1()

        openingPath = confPath + "/5_otherEntitiesDefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b5 = json.dumps(listData2)

        openingPath2 = confPath + "/5_otherEntitiesNumber.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b5 = json.dumps(listData4)



        csvPath = dataPath + "/D_OtherEntities.csv"
        df_OtherEntities = pd.read_csv(csvPath)
        logger.info(df_OtherEntities)
        html_OtherEntities = df_OtherEntities.to_html(classes='dataframe', index=False)



        return render(request, 'B5_csv_otherEntities.html', {
            'html_OtherEntities': html_OtherEntities,
            'oen_origin_form': oen_origin_form,
            'oen_id_form': oen_id_form,
            'oen_name_form': oen_name_form,
            'oen_value_form': oen_value_form,
            'oen_category_form': oen_category_form,
            'options_to_show_default_b5': options_to_show_default_b5,
            'button_lists_b5': button_lists_b5,
            'nextButton': nextButton

                                            }
                  )


