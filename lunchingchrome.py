#lunching the chrome

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

from selenium.webdriver.chrome.options import Options

# Configure Chrome options (headless for Jenkins)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


#driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))For seleniumV4
driver=webdriver.Chrome()

driver.get("http://www.udemy.com/")
driver.maximize_window()#maximize_window
time.sleep(2)
driver.refresh()

time.sleep(2)
driver.back()

time.sleep(2)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


print("Yes")
time.sleep(10)
driver.quit()
