def exportNeo4jSVG(runingQuery, driverUserName, driverPassword):

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    # Setup WebDriver
    service = Service('/usr/bin/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.get('http://localhost:7474/browser/')  # Adjust this URL to your Neo4j Browser's URL
    driver.implicitly_wait(10)


    # Login (if required)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="username"]'))
    )
    username_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="username"]')
    username_input.send_keys(driverUserName)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="password"]'))
    )
    password_input = driver.find_element(By.CSS_SELECTOR, '[data-testid="password"]')
    password_input.send_keys(driverPassword)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="connect"]'))
    )
    login_button = driver.find_element(By.CSS_SELECTOR, '[data-testid="connect"]')
    login_button.click()


    ############################################################################################
    #click on query box
    time.sleep(5)
    view_line_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.view-line'))
    )
    view_line_element.click()

    ############################################################################################
    #Type the query
    input_area = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.inputarea'))
    )

    input_area.clear()
    input_area.send_keys(runingQuery)

    ############################################################################################
    #run the query
    run_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="editor-Run"]'))
    )
    run_button.click()

    ############################################################################################
    #save th SVG
    time.sleep(1)


    element_to_click = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.sc-dkQkyq > .sc-eJwWfJ:nth-child(2) .SVGInline-svg'))
    )
    element_to_click.click()

    export_svg_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Export SVG"))
    )

    export_svg_link.click()


    time.sleep(5)
    # More steps may be necessary to handle the export dialog

    # Close browser
    driver.quit()


def moveSVG(outdirMic,filename):
    import os
    import shutil

    source_dir = os.path.expanduser('~/Downloads')
    print(source_dir)
    # Directories

    svg_files = [file for file in os.listdir(source_dir) if file.endswith('.svg')]

    # Initialize variables to find the latest file
    latest_file = None
    latest_mtime = 0

    # Find the SVG file with the latest modification time
    for file in svg_files:
        file_path = os.path.join(source_dir, file)
        mtime = os.stat(file_path).st_mtime
        if mtime > latest_mtime:
            latest_mtime = mtime
            latest_file = file_path

    # Move the latest file to the destination directory, if any
    if latest_file:
        print(latest_file)
        new_file_name = filename+".svg"
        new_file_path = os.path.join(outdirMic, new_file_name)
        if os.path.exists(new_file_path):
            os.remove(new_file_path)  # Remove the existing file if it exists
        shutil.move(latest_file, new_file_path)
        print(f"Moved and renamed '{os.path.basename(new_file_name)}' to '{new_file_path}'.")
    else:
        print("No SVG files found to move.")


def moveDefaultSVG(outdirMic,filename):
    import os
    import shutil

    confDirectory = "../Data/0_MultiMedia"
    source_dir = os.path.realpath(confDirectory)


    # Directories
    svg_file="Blank.svg"
    latest_file = os.path.join(source_dir, svg_file)
    #print(latest_file)

    new_file_name = filename + ".svg"
    new_file_path = os.path.join(outdirMic, new_file_name)
    #print(new_file_path)

    if os.path.exists(new_file_path):
        os.remove(new_file_path)  # Remove the existing file if it exists
    shutil.copy(latest_file, new_file_path)
    print(f"Copied and renamed '{os.path.basename(new_file_name)}' to '{new_file_path}'.")


def truncate_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Check if the file has more than 1000 lines
        if len(lines) > 1000:
            lines = lines[:1000] + ["...\n"]

        with open(file_path, 'w') as file:
            file.writelines(lines)

        print("File truncated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")