from django.shortcuts import render,redirect

from myapp.forms import NextButton1
from myapp.webSocketFunctions import ProgressBar


import logging
logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")

def queryLister(request):
    import os
    import ast

    confDirectory = "./myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)

    pyDirectory = "./myapp/utils"
    script_directory = os.path.realpath(pyDirectory)

    svgDirectory = "./myapp/Data/0_svgLocation"
    downS = os.path.realpath(svgDirectory)
    svgPath = downS + "/" + '15_Final'

    dataDirectory = './media/uploads/0_Data'
    dataPath = os.path.realpath(dataDirectory)

    downloadDir = "./media/download/dfgTool"
    downD = os.path.realpath(downloadDir)
    outDir = downD + "/" + '15_Final'





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
        logger.info(f"This is the preview view POST part")

        scripts = [
            'A30_Run_Software.py'
        ]

        ProgressBar.run_scripts_asynchronously(script_directory, scripts)


        return redirect('DFG1')


    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info(f"This is the C20 view else part")

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
        savingTxt13 = outDir + "/" + "Q13.txt"
        savingTxt14 = outDir + "/" + "Q14.txt"
        savingTxt15 = outDir + "/" + "Q15.txt"
        savingTxt16 = outDir + "/" + "Q16.txt"
        savingTxt17 = outDir + "/" + "Q17.txt"
        savingTxt18 = outDir + "/" + "Q18.txt"
        savingTxt19 = outDir + "/" + "Q19.txt"
        savingTxt20 = outDir + "/" + "Q20.txt"
        savingTxt21 = outDir + "/" + "Q21.txt"
        savingTxt22 = outDir + "/" + "Q22.txt"


        savingSvg3 = svgPath + "/" + "Q3_svg_location.txt"
        savingSvg4 = svgPath + "/" + "Q4_svg_location.txt"
        savingSvg5 = svgPath + "/" + "Q5_svg_location.txt"
        savingSvg6 = svgPath + "/" + "Q6_svg_location.txt"
        savingSvg7 = svgPath + "/" + "Q7_svg_location.txt"
        savingSvg8 = svgPath + "/" + "Q8_svg_location.txt"
        savingSvg9 = svgPath + "/" + "Q9_svg_location.txt"
        savingSvg10 = svgPath + "/" + "Q10_svg_location.txt"
        savingSvg11 = svgPath + "/" + "Q11_svg_location.txt"
        savingSvg12 = svgPath + "/" + "Q12_svg_location.txt"
        savingSvg13 = svgPath + "/" + "Q13_svg_location.txt"
        savingSvg14 = svgPath + "/" + "Q14_svg_location.txt"
        savingSvg15 = svgPath + "/" + "Q15_svg_location.txt"
        savingSvg16 = svgPath + "/" + "Q16_svg_location.txt"
        savingSvg17 = svgPath + "/" + "Q17_svg_location.txt"
        savingSvg18 = svgPath + "/" + "Q18_svg_location.txt"
        savingSvg19 = svgPath + "/" + "Q19_svg_location.txt"
        savingSvg20 = svgPath + "/" + "Q20_svg_location.txt"
        savingSvg21 = svgPath + "/" + "Q21_svg_location.txt"
        savingSvg22 = svgPath + "/" + "Q22_svg_location.txt"

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

        with open(savingTxt13, 'r') as file:
            query13 = file.read()
            logger.info(f"\nquery13 : {query13}")

        with open(savingTxt14, 'r') as file:
            query14 = file.read()
            logger.info(f"\nquery14 : {query14}")

        with open(savingTxt15, 'r') as file:
            query15 = file.read()
            logger.info(f"\nquery15 : {query15}")

        with open(savingTxt16, 'r') as file:
            query16 = file.read()
            logger.info(f"\nquery16 : {query16}")

        with open(savingTxt17, 'r') as file:
            query17 = file.read()
            logger.info(f"\nquery17 : {query17}")

        with open(savingTxt18, 'r') as file:
            query18 = file.read()
            logger.info(f"\nquery18 : {query18}")


        with open(savingTxt19, 'r') as file:
            query19 = file.read()
            logger.info(f"\nquery19 : {query19}")

        with open(savingTxt20, 'r') as file:
            query20 = file.read()
            logger.info(f"\nquery20 : {query20}")

        with open(savingTxt21, 'r') as file:
            query21 = file.read()
            logger.info(f"\nquery21 : {query21}")

        with open(savingTxt22, 'r') as file:
            query22 = file.read()
            logger.info(f"\nquery22 : {query22}")

        ###############################################3

        with open(savingSvg3, 'r') as file:
            svg3 = file.read()
            logger.info(f"\nsvg3 : {svg3}")

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

        with open(savingSvg13, 'r') as file:
            svg13 = file.read()
            logger.info(f"\nsvg13 : {svg13}")

        with open(savingSvg14, 'r') as file:
            svg14 = file.read()
            logger.info(f"\nsvg14 : {svg14}")

        with open(savingSvg15, 'r') as file:
            svg15 = file.read()
            logger.info(f"\nsvg15 : {svg15}")

        with open(savingSvg16, 'r') as file:
            svg16 = file.read()
            logger.info(f"\nsvg16 : {svg16}")

        with open(savingSvg17, 'r') as file:
            svg17 = file.read()
            logger.info(f"\nsvg17 : {svg17}")

        with open(savingSvg18, 'r') as file:
            svg18 = file.read()
            logger.info(f"\nsvg18 : {svg18}")

        with open(savingSvg19, 'r') as file:
            svg19 = file.read()
            logger.info(f"\nsvg19 : {svg19}")

        with open(savingSvg20, 'r') as file:
            svg20 = file.read()
            logger.info(f"\nsvg20 : {svg20}")

        with open(savingSvg21, 'r') as file:
            svg21 = file.read()
            logger.info(f"\nsvg21 : {svg21}")

        with open(savingSvg22, 'r') as file:
            svg22 = file.read()
            logger.info(f"\nsvg22 : {svg22}")


        return render(request, 'D36_BuildingQuery.html', {
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
            'query13': query13,
            'query14': query14,
            'query15': query15,
            'query16': query16,
            'query17': query17,
            'query18': query18,
            'query19': query19,
            'query20': query20,
            'query21': query21,
            'query22': query22,

            'svg3': svg3,
            'svg4': svg4,
            'svg5': svg5,
            'svg6': svg6,
            'svg7': svg7,
            'svg8': svg8,
            'svg9': svg9,
            'svg10': svg10,
            'svg11': svg11,
            'svg12': svg12,
            'svg13': svg13,
            'svg14': svg14,
            'svg15': svg15,
            'svg16': svg16,
            'svg17': svg17,
            'svg18': svg18,
            'svg19': svg19,
            'svg20': svg20,
            'svg21': svg21,
            'svg22': svg22,


                                            }
                  )


