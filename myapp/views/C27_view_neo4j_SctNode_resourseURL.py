from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, FileResponse
from django.http import HttpResponse

import os
import logging

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")
downloadDir = "../../media/download/dfgTool"
downD = os.path.realpath(downloadDir)
outDir = downD + "/" + '06_OCT_Node'


svgLocDir = "./myapp/Data/0_svgLocation"
svgLoc = os.path.realpath(svgLocDir)
svgDir = svgLoc + "/" + '06_OCT_Node'
print(svgDir)

def seve_neo4jQuery_funcQ1_sctNode(request):
    neo4jQuery_url = outDir + "/" + "Q1.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ2_sctNode(request):
    neo4jQuery_url = outDir + "/" + "Q2.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ3_sctNode(request):
    neo4jQuery_url = outDir + "/" + "Q3.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


def seve_neo4jQuery_funcQ4_sctNode(request):
    neo4jQuery_url = outDir + "/" + "Q4.txt"
    logger.info(f"\nneo4j query URL : {neo4jQuery_url}")

    if not os.path.exists(neo4jQuery_url):
        logger.error(f"File not found at {neo4jQuery_url}")
        return HttpResponseNotFound("The requested neo4j query txt file was not found.")
    try:
        return FileResponse(open(neo4jQuery_url, 'rb'), content_type='text/plain')
    except Exception as e:
        logger.error(f"Failed to read the file at {neo4jQuery_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")


################################################################################



def seve_neo4jQuery_svgQ4_sctNode(request):
    savingTxt = svgDir + "/" + "Q4_svg_location.txt"

    with open(savingTxt, 'r') as file:
        svg_url = file.read()
        logger.info(f"\nSVG URL : {svg_url}")

    if not os.path.exists(svg_url):
        logger.error(f"File not found at {svg_url}")
        return HttpResponseNotFound("The requested SVG was not found.")
    try:
        return FileResponse(open(svg_url, 'rb'), content_type='image/svg+xml')
    except Exception as e:
        logger.error(f"Failed to read the file at {svg_url}: {e}")
        return HttpResponseNotFound("Error accessing the PDF file.")

