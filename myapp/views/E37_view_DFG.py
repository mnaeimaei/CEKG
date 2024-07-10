from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, FileResponse
from myapp.forms import BroweserButton
import os
import logging

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")

def DFG(request):
    import os
    import ast

    confDirectory = "./myapp/Data/0_DataConf"
    confPath = os.path.realpath(confDirectory)



    if request.method == 'POST':
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info("This is the preview view POST part")
        return redirect('browse')

    else:
        logger.info(f"************************************************************************************************************************************************************************************************************")
        logger.info("This is the preview view else part")
        browseButton = BroweserButton()

        import os
        savingTxt1 = confPath + "/" + "X1_dfgGraphvizPdfLocation.txt"
        savingTxt2 = confPath + "/" + "X2_dfgGraphvizDotLocation.txt"
        savingTxt3 = confPath + "/" + "X3_dfgGraphvizQueryLocation.txt"
        savingTxt4 = confPath + "/" + "X4_dfgNeo4jSVgLocation.txt"
        savingTxt5 = confPath + "/" + "X5_dfgNeo4jQueryLocation.txt"
        savingTxt6 = confPath + "/" + "X6_dfgNeo4jQueries.txt"
        savingTxt7 = confPath + "/" + "X7_dfgGraphvizQueries.txt"

        with open(savingTxt1, 'r') as file:
            pdf_url = file.read()
            logger.info(f"\nPDF URL : {pdf_url}")

        with open(savingTxt2, 'r') as file:
            dot_url = file.read()
            logger.info(f"\nDOT URL : {dot_url}")

        with open(savingTxt3, 'r') as file:
            graphvizQuery_url = file.read()
            logger.info(f"\ngraphviz query URL : {graphvizQuery_url}")

        with open(savingTxt4, 'r') as file:
            svg_url = file.read()
            logger.info(f"\nSVG URL : {svg_url}")

        with open(savingTxt5, 'r') as file:
            neo4jQuery_url = file.read()
            logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

        with open(savingTxt6, 'r') as file:
            graphvizQuery = file.read()
            logger.info(f"\ngraphviz query  : {graphvizQuery}")

        with open(savingTxt7, 'r') as file:
            neo4jQuery = file.read()
            logger.info(f"\nneo4j query  : {neo4jQuery}")

        return render(request, 'E37_DFG.html', {
            'browseButton': browseButton,
            'pdf_url': pdf_url,
            'dot_url': dot_url,
            'graphvizQuery_url': graphvizQuery_url,
            'svg_url': svg_url,
            'neo4jQuery_url': neo4jQuery_url,
            'graphvizQuery': graphvizQuery,
            'neo4jQuery': neo4jQuery
        })

