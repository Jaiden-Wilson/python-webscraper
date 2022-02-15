from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
path= r"C:\Users\16479\Downloads\chromedriver_win32\chromedriver.exe"
s=Service(r'C:\Users\16479\.wdm\drivers\chromedriver\win32\97.0.4692.71\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
driver = webdriver.Chrome(service=s,options=options)
url = 'https://www.domcop.com/top-10-million-websites#'
driver.get(url)
driver.find_element(By.NAME,'top-domains-table_length').find_elements(By.TAG_NAME,'option')[3].click();


sites=[]
shopifySites=[]


for h in range(250): 
    
    WebDriverWait(driver,100).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,'text-left')))

    for i in range(49):
        sites.append(driver.find_elements(By.CLASS_NAME,'odd')[i].find_element(By.CLASS_NAME,'text-left').text)
        sites.append(driver.find_elements(By.CLASS_NAME,'even')[i].find_element(By.CLASS_NAME,'text-left').text)
    
    driver.find_element(By.CLASS_NAME, "next").find_element(By.TAG_NAME,"a").click()

for i in range(len(sites)):
    print(sites[i])
#Check if elements in sites[] are shopify stores   
for i in range(len(sites)): 
    WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.TAG_NAME,"body")))
    try:
        driver.get('https://www.'+sites[i]+'/admin') 
        if(driver.find_element(By.TAG_NAME,"title").text == "Request Denied."):
            print('Inaccessible URL')
        
    except:
        print('Inaccessible URL')
    if(len(driver.find_elements(By.LINK_TEXT,'Log in to another store'))>0):
            shopifySites.append(sites[i])
print(shopifySites) 
     

