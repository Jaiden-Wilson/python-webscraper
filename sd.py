from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import json


s=Service(r'C:\Users\16479\.wdm\drivers\chromedriver\win32\97.0.4692.71\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox") 
options.add_argument("--disable-dev-shm-usage") 
options.add_experimental_option('excludeSwitches', ['enable-logging']) 

driver = webdriver.Chrome(service=s,options=options)
driver.set_page_load_timeout(5) 
driver.command_executor.set_timeout(100)
url = 'https://webinopoly.com/blogs/news/top-100-most-successful-shopify-stores'
url2='https://www.siteworthtraffic.com/'
driver.get(url)
shopifyData=[]
for i in range(100):
    shopifyData.append([]) 
for j in range(80,100): 
    shopifyData[j].append(driver.find_elements(By.TAG_NAME,"td")[j*5].text)
    shopifyData[j].append(driver.find_elements(By.TAG_NAME,"td")[(j*5)+1].text)
    driver.get(url2)
    
    driver.find_element(By.ID,"hf-domain").send_keys(shopifyData[j][1])
    time.sleep(1)
    driver.find_element(By.NAME,"go").click()
    
    WebDriverWait(driver,100).until(EC.visibility_of_all_elements_located((By.TAG_NAME,"table")))
   
    shopifyData[j].append(driver.find_elements(By.TAG_NAME,"table")[1].find_elements(By.TAG_NAME,"tr")[1].find_elements(By.TAG_NAME,"td")[1].text)
    shopifyData[j].append(driver.find_elements(By.TAG_NAME,"table")[1].find_elements(By.TAG_NAME,"tr")[2].find_elements(By.TAG_NAME,"td")[1].text)
    driver.get(url)
    shopifyData[j].append(driver.find_elements(By.TAG_NAME,"td")[(j*5)+4].text)
for i in range(80):
    shopifyData.remove(shopifyData[0])     
print(shopifyData) 

json_data= json.dumps({"shopifyData":shopifyData})
print(json_data)
with open(r"C:\Users\16479\shopify-rankings\src\database5.json","w") as outfile:
    json.dump({"shopifyData":shopifyData},outfile)