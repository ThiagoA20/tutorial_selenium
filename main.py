from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from decouple import config
import time

"""
# In case of ChromeDriverManager isn't working, use this method instead, go to your browser, search for the version in the info section and then download the driver with the same version inside of the folder of your browser.
driver_path = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\chromedriver.exe'
driver = webdriver.Chrome(options=options, service=Service(driver_path))
"""

def initialConfigurations(start_maximised=True, headless=False):
    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) # exclude selenium logs
    options.binary_location = config('BINARY_LOCATION')
    if headless:
        options.add_argument("--headless") # start browser in background mode
    DRIVER = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    if start_maximised:
        DRIVER.maximize_window()
    return DRIVER

if __name__ == '__main__':
    DRIVER = initialConfigurations()
    DRIVER.get("https://www.google.com")
    time.sleep(1)
    
    # Get an input element by name and send keys
    search = DRIVER.find_element(by=By.NAME, value='q')
    search.send_keys('Test')
    time.sleep(1)
    
    # Press enter key in the selected element
    search.send_keys(Keys.RETURN)
    time.sleep(1)
    
    # print the text of elements with the same class
    titles = DRIVER.find_elements(by=By.CLASS_NAME, value='LC20lb')
    for element in titles:
        print(element.text)
    
    DRIVER.get("https://pubmed.ncbi.nlm.nih.gov/")
    search = WebDriverWait(DRIVER, 10).until(EC.presence_of_element_located((By.NAME, 'term')))
    search.clear()
    search.send_keys('CRISPR-Cas9')
    search.send_keys(Keys.RETURN)
    time.sleep(1)

    first_paper = DRIVER.find_element(by=By.XPATH, value="//*[@id='search-results']/section/div[1]/div/article[1]/div[2]/div[1]/a")
    first_paper.click()
    time.sleep(1)
    # DRIVER.execute_script("arguments[0].click();", element)
    # DRIVER.close() # close the actual tab
    DRIVER.quit() # close the browser