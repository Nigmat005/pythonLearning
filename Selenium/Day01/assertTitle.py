#from selenium import webdriver as driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


try:
    driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver")
    driver=webdriver.Chrome("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))
    url="https://opensource-demo.orangehrmlive.com/"
# url="https://www.Google.com"
    driver.get(url)
except Exception:
    print("No such browser")
