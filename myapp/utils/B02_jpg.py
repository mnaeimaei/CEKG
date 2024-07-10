from PIL import Image
import fitz
import os

def jpgCreator(FileName, outdirMic,PDF_Output_Location,n, resolution ):


    originalJpegFile= FileName + '.jpg'
    print(originalJpegFile)
    savingPath=outdirMic+"/"


    zoom_x = 2.0  # horizontal zoom
    zoom_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zoom_y)  # zoom factor 2 in each dimension

    doc = fitz.open(PDF_Output_Location)  # open document
    for page in doc:  # iterate through the pages
        pix = page.get_pixmap(matrix=mat, dpi=resolution)  # render page to an image
        pix.save(savingPath + originalJpegFile)  # store image as a PNG


    img = Image.open(savingPath+originalJpegFile)

    width = img.width
    height = img.height

    z = round(width / n)
    # print(z)

    list1 = []
    for i in range(n):
        k1 = z * i
        list1.append(k1)
    list1.append(width)
    #print(list1)

    list2 = []
    for i in range(len(list1)):
        list3 = []
        if i + 1 < len(list1):
            list3.append(list1[i])
            list3.append(0)
            list3.append(list1[i + 1])
            list3.append(height)
            list2.append(list3)
    #print(list2)

    for i in range(len(list2)):
        x1 = list2[i][0]
        y1 = list2[i][1]
        x2 = list2[i][2]
        y2 = list2[i][3]
        box = (x1, y1, x2, y2)
        img2 = img.crop(box)
        nameSplitJPG = f'{FileName}_{i + 1}.jpg'
        print(nameSplitJPG)
        img2.save(savingPath+nameSplitJPG, dpi=(resolution, resolution))









