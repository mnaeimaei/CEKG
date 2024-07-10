

def readFileSource(confPath):
    import os
    value1=""

    inputTex_FilePath= confPath + "/2_downloadingFileSource.txt"
    if os.path.exists(inputTex_FilePath):
        with open(inputTex_FilePath, 'r') as file:
            for line in file:
                variable_name, value1 = line.split('=')
                value1 = value1.strip()


    return value1




def readFileLocation(confPath,fileSource):
    import os
    value2=""
    value3=""


    if fileSource == "1":

        inputTex_FilePath= confPath + "/2_downloadingGoogleCloud1.txt"
        if os.path.exists(inputTex_FilePath):
            with open(inputTex_FilePath, 'r') as file:
                for line in file:
                    variable_name, value2 = line.split('=')
                    value2 = value2.strip()

        inputTex_FilePath= confPath + "/2_downloadingGoogleCloud2.txt"
        if os.path.exists(inputTex_FilePath):
            with open(inputTex_FilePath, 'r') as file:
                for line in file:
                    variable_name, value3 = line.split('=')
                    value3 = value3.strip()




    if fileSource == "2":

        inputTex_FilePath = confPath + "/2_downloadingLocal1.txt"
        if os.path.exists(inputTex_FilePath):
            with open(inputTex_FilePath, 'r') as file:
                for line in file:
                    variable_name, value2 = line.split('=')
                    value2 = value2.strip()

        inputTex_FilePath = confPath + "/2_downloadingLocal2.txt"
        if os.path.exists(inputTex_FilePath):
            with open(inputTex_FilePath, 'r') as file:
                for line in file:
                    variable_name, value3 = line.split('=')
                    value3 = value3.strip()
    return value2, value3






def copyFile(savingPath, fileSource,EventLogName,Location):
    if fileSource == "1":

        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        import requests
        from googleapiclient.discovery import build
        import io
        from googleapiclient.http import MediaIoBaseDownload
        print("1")
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(Location, scope)
        print("2")
        gc = gspread.authorize(credentials)
        print("3")
        workbook = gc.open(EventLogName)
        print("4")
        SHEET_ID=workbook.id
        drive_service = build('drive', 'v3', credentials=credentials)

        file_id = SHEET_ID
        mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        request = drive_service.files().export_media(fileId=file_id, mimeType=mime_type)

        # Download the file
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("Download %d%%." % int(status.progress() * 100))

        with io.open(savingPath, 'wb') as f:
            fh.seek(0)
            f.write(fh.read())

        print("Download completed.")

    if fileSource == "2":
        import shutil
        source_path = Location+EventLogName+'.xlsx'

        # Copy the file from source to destination
        shutil.copyfile(source_path, savingPath)




def copyFile2(savingPath, fileSource,EventLogName,Location):
    if fileSource == "1":
        print("SSDSDD")
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials
        import requests
        from googleapiclient.discovery import build
        import io
        from googleapiclient.http import MediaIoBaseDownload

        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(Location, scope)

        gc = gspread.authorize(credentials)

        workbook = gc.open(EventLogName)

        import os
        import csv
        directory = '../../media/uploads/0_Data'


        for worksheet in workbook.worksheets():
            sheet_name = worksheet.title
            data = worksheet.get_all_values()

            # Define CSV file path
            myCSV = os.path.realpath(directory + sheet_name + '.csv')


            # Save data to CSV
            with open(myCSV, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerows(data)


    if fileSource == "2":
        import shutil
        source_path = Location+EventLogName+'.xlsx'

        # Copy the file from source to destination
        shutil.copyfile(source_path, savingPath)
