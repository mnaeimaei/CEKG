from django.shortcuts import render,redirect
from django.http import JsonResponse



from myapp.forms import SctnConceptId
from myapp.forms import SctnConceptCode
from myapp.forms import SctnTermA
from myapp.forms import SctnTermB
from myapp.forms import SctnSemanticTags
from myapp.forms import SctnConceptType
from myapp.forms import SctnLevels

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

def SctNode(request):
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


        sctn_concept_id = SctnConceptId(request.POST)
        sctn_concept_code = SctnConceptCode(request.POST)
        sctn_term_a = SctnTermA(request.POST)
        sctn_term_b = SctnTermB(request.POST)
        sctn_semantic_tags = SctnSemanticTags(request.POST)
        sctn_concept_type = SctnConceptType(request.POST)
        sctn_levels = SctnLevels(request.POST)


        logger.debug(f"sctn_concept_id.is_valid() = {sctn_concept_id.is_valid()}")
        logger.debug(f"sctn_concept_code.is_valid() = {sctn_concept_code.is_valid()}")
        logger.debug(f"sctn_term_a.is_valid() = {sctn_term_a.is_valid()}")
        logger.debug(f"sctn_term_b.is_valid() = {sctn_term_b.is_valid()}")
        logger.debug(f"sctn_semantic_tags.is_valid() = {sctn_semantic_tags.is_valid()}")
        logger.debug(f"sctn_concept_type.is_valid() = {sctn_concept_type.is_valid()}")
        logger.debug(f"sctn_levels.is_valid() = {sctn_levels.is_valid()}")

        options_text_path = confPath + "/10_octNodeMapping.txt"
        with open(options_text_path, 'r') as file:
            data = file.read()
            options_text_map = ast.literal_eval(data)
            logger.debug(f"options_text_map = {options_text_map}")

        savingPath = confPath + "/10_octNodeDefault.txt"

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

        if sctn_concept_id.is_valid():
            conceptId = sctn_concept_id.cleaned_data.get('dynamic_choice_B10_1')
            conceptId = options_text_map[conceptId]
            update_variable_in_file(savingPath, "conceptId", conceptId)

        if sctn_concept_code.is_valid():
            conceptCode = sctn_concept_code.cleaned_data.get('dynamic_choice_B10_2')
            conceptCode = options_text_map[conceptCode]
            update_variable_in_file(savingPath, "conceptCode", conceptCode)

        if sctn_term_a.is_valid():
            termA = sctn_term_a.cleaned_data.get('dynamic_choice_B10_3')
            termA = options_text_map[termA]
            update_variable_in_file(savingPath, "termA", termA)

        if sctn_term_b.is_valid():
            termB = sctn_term_b.cleaned_data.get('dynamic_choice_B10_4')
            termB = options_text_map[termB]
            update_variable_in_file(savingPath, "termB", termB)

        if sctn_semantic_tags.is_valid():
            Semanti_tags = sctn_semantic_tags.cleaned_data.get('dynamic_choice_B10_5')
            Semanti_tags = options_text_map[Semanti_tags]
            update_variable_in_file(savingPath, "Semanti_tags", Semanti_tags)

        if sctn_concept_type.is_valid():
            ConceptType = sctn_concept_type.cleaned_data.get('dynamic_choice_B10_6')
            ConceptType = options_text_map[ConceptType]
            update_variable_in_file(savingPath, "ConceptType", ConceptType)

        if sctn_levels.is_valid():
            level = sctn_levels.cleaned_data.get('dynamic_choice_B10_7')
            level = options_text_map[level]
            update_variable_in_file(savingPath, "level", level)

        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)
        #subprocess.run(['python', 'XXXXXXXXXX.py'], cwd=script_directory)

        openingPath = confPath + "/3_pageSequence.txt"
        import ast
        with open(openingPath, 'r') as file:
            data = file.read()
            listData = ast.literal_eval(data)

        return redirect(listData[7])

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the preview view else part")


        sctn_concept_id = SctnConceptId()
        sctn_concept_code = SctnConceptCode()
        sctn_term_a = SctnTermA()
        sctn_term_b = SctnTermB()
        sctn_semantic_tags = SctnSemanticTags()
        sctn_concept_type = SctnConceptType()
        sctn_levels = SctnLevels()

        nextButton = NextButton1()

        openingPath = confPath + "/10_octNodeDefaultValue.txt"
        import ast
        with open(openingPath, 'r') as file:
            data2 = file.read()
            listData2 = ast.literal_eval(data2)
            options_to_show_default_b10 = json.dumps(listData2)

        openingPath2 = confPath + "/10_octNodeNumber.txt"
        import ast
        with open(openingPath2, 'r') as file:
            default4 = file.read()
            listData4 = ast.literal_eval(default4)
            button_lists_b10 = json.dumps(listData4)

        csvPath = dataPath + "/I_OCT_Node.csv"
        df_OCT_Node = pd.read_csv(csvPath)
        logger.info(df_OCT_Node)
        html_OCT_Node = df_OCT_Node.to_html(classes='dataframe', index=False)



        return render(request, 'B10_csv_SctNode.html', {
            'html_OCT_Node': html_OCT_Node,
            'sctn_concept_id': sctn_concept_id,
            'sctn_concept_code': sctn_concept_code,
            'sctn_term_a': sctn_term_a,
            'sctn_term_b': sctn_term_b,
            'sctn_semantic_tags': sctn_semantic_tags,
            'sctn_concept_type': sctn_concept_type,
            'sctn_levels': sctn_levels,
            'options_to_show_default_b10': options_to_show_default_b10,
            'button_lists_b10': button_lists_b10,
            'nextButton': nextButton

                                            }
                  )


