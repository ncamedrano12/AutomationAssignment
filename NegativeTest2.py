from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

url = 'https://parking.e2log.com'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 5)
now = datetime.now()
passFile = open('PassFile3.txt','w')

# Need todays date for negative test
dt = now.strftime("%Y-%m-%d")
print(dt)


# Goes to new reservations page
reserveButton = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > ng-component > div > ng-component > div.container.d-none.d-sm-block.pt-12 > div > button')
reserveButton.click()

# Adds vehicle License Plate
vehicleAdd = driver.find_element(By.CSS_SELECTOR, '.fa-plus')
vehicleAdd.click()

vehicleInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="license-plate"]')))
vehicleInput.send_keys('KYL 6727')

vehicleCheck = driver.find_element(By.XPATH, '//button[2]')
vehicleCheck.click()

# Add Check-in Date incorrectly
cIn = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > ng-component > div > ng-component > div > div > div:nth-child(3) > div.flex-grow-1.ng-star-inserted > date-time-show > div > div > span > button')
cIn.click()

# Will do time first
cInTime = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="time-picker"]/div/input')))
cInTime.click()
cInTime.send_keys('00:00:00')

# This will cause Date to go to today's date
cInCalendar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="date-picker"]/div/div/input')))
cInCalendar.send_keys(dt)

#  Tries to check
cInCheck = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/div/div[2]/date-time-edit/form/div[1]/div[3]/button[2]')
cInCheck.click()

alert_obj = driver.switch_to.alert
passFile.write('Is the following error: "' + alert_obj.text + '" the correct error to be displayed?\n')
if alert_obj.text == "Error: Cannot read properties of undefined (reading 'getFullYear')":
    print('TRUE')
    passFile.write('   -TRUE\n')
else:
    print('FALSE')
    passFile.write('   -FALSE\n')
time.sleep(1)
alert_obj.accept()


time.sleep(2)
passFile.close()
driver.close()