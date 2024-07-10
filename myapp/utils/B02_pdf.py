from PIL import Image
import fitz
import os
import os
from PyPDF2 import PdfFileReader, PdfReader, PdfFileWriter, PdfWriter
from reportlab.pdfgen import canvas

def splitPDFCreator(outdirMic, FileName, x):

    for n in x:
        pdfLocationRealPathWithPDF = outdirMic + "/" + FileName + ".pdf"
        # originalJpegFile= FileName + '.jpg'
        # print(originalJpegFile)
        savingPath = outdirMic + "/"
        savingPathOutputFile = savingPath + FileName +  '_crop_' + str(n) + "_.pdf"

        # print("outdir=",outdir)
        # print("pdfLocation=",pdfLocation)
        # print("pdfLocationRealPath=",pdfLocationRealPath)
        # print("pdfLocationRealPathWithPDF=",pdfLocationRealPathWithPDF)
        # print("savingPath=",savingPath)

        with open(pdfLocationRealPathWithPDF, 'rb') as input_file:
            pdf = PdfReader(input_file)

            # Create a new PDF writer
            output_pdf = PdfWriter()

            # Get the first page from the input PDF
            page = pdf.pages[0]

            width = page.mediabox.width
            height = page.mediabox.height

            z = round(width / n)
            # print(z)

            list1 = []
            for i in range(n):
                k1 = z * i
                list1.append(k1)
            list1.append(width)
            # print(list1)

            list2 = []
            for i in range(len(list1)):
                list3 = []
                if i + 1 < len(list1):
                    list3.append(list1[i])
                    list3.append(0)
                    list3.append(list1[i + 1])
                    list3.append(height)
                    list2.append(list3)
            # print(list2)

            for i in range(len(list2)):
                x1 = list2[i][0]
                y1 = list2[i][1]
                x2 = list2[i][2]
                y2 = list2[i][3]
                box = (x1, y1, x2, y2)
                page.cropbox.lower_left = (x1, y1)
                page.cropbox.upper_right = (x2, y2)

                # Add the modified page to the output PDF
                output_pdf.add_page(page)

                # Write the output PDF to a file
                with open(savingPathOutputFile, 'wb') as output_file:
                    output_pdf.write(output_file)












