
from django.http import HttpResponseNotFound, FileResponse


import os
import logging

logging.basicConfig(filename='myapp.log', level=logging.INFO)
logger = logging.getLogger("myapp")


downloadDir = "./media/download/dfgTool"
downD = os.path.realpath(downloadDir)
outDir = downD + "/" + '01_EventLog'
print(outDir)

svgLocDir = "./myapp/Data/0_svgLocation"
svgLoc = os.path.realpath(svgLocDir)
svgDir = svgLoc + "/" + '01_EventLog'
print(svgDir)


multiLocDir = "./myapp/Data/0_MultiMedia"
multiLoc = os.path.realpath(multiLocDir)
print(multiLoc)




def seve_jpegCKEG(request):
    savingTxt = multiLoc + "/" + "CEKG.txt"

    try:
        with open(savingTxt, 'r') as file:
            jpeg_url = file.read().strip()  # Read and strip any extra whitespace
        logger.info(f"JPEG URL: {jpeg_url}")

        if not os.path.exists(jpeg_url):
            logger.error(f"File not found at {jpeg_url}")
            return HttpResponseNotFound("The requested JPEG was not found.")

        return FileResponse(open(jpeg_url, 'rb'), content_type='image/jpeg')
    except Exception as e:
        logger.error(f"Failed to read the file at {jpeg_url}: {e}")
        return HttpResponseNotFound("Error accessing the JPEG file.")




