from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from datetime import datetime

url = 'https://parking.e2log.com'
driver = webdriver.Chrome('C:/Users/ncame/OneDrive/Documents/drivers/chromedriver.exe')
driver.get(url)
wait = WebDriverWait(driver, 5)
now = datetime.now()

# First Test Case to reserve spot

# Goes to reservation page
reserveButton = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > ng-component > div > ng-component > div.container.d-none.d-sm-block.pt-12 > div > button')
reserveButton.click()

# Adds vehicle License Plate
vehicleAdd = driver.find_element(By.CSS_SELECTOR, '.fa-plus')
vehicleAdd.click()

vehicleInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="license-plate"]')))
vehicleInput.send_keys('KYL 6727')

vehicleCheck = driver.find_element(By.XPATH, '//button[2]')
vehicleCheck.click()

# Add Check-in Date
cIn = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > ng-component > div > ng-component > div > div > div:nth-child(3) > div.flex-grow-1.ng-star-inserted > date-time-show > div > div > span > button')
cIn.click()

cInCalendar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="date-picker"]/div/div/input')))
cInCalendar.click()

# In order for test to work in future, clicks arrow to next month, ensuring future date
cInCalendarArrow = driver.find_element(By.XPATH, '//*[@id="cdk-overlay-0"]/div/div/date-range-popup/div/div/inner-popup/div/div/date-header/div/button[3]')
cInCalendarArrow.click()
cInDate = driver.find_element(By.XPATH, '//*[@id="cdk-overlay-0"]/div/div/date-range-popup/div/div/inner-popup/div/div/div/date-table/table/tbody/tr[1]/td[4]/div')
cInDate.click()

# Add Check-in time
cInTime = driver.find_element(By.XPATH, '//*[@id="time-picker"]/div/input')
cInTime.click()
cInTime.send_keys('23:59:59')

# Confirm Check In
cInCheck = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/div/div[2]/date-time-edit/form/div[1]/div[3]/button[2]')
cInCheck.click()


# Check Out Area
cOut = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > ng-component > div > ng-component > div > div > div:nth-child(4) > div.flex-grow-1.ng-star-inserted > date-time-show > div > div > span > button')
cOut.click()

cOutCalendar = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="date-picker"]/div/div/input')))
cOutCalendar.click()

# In order for test to work in future, clicks arrow to next month, ensuring future date
time.sleep(1)
cOutCalendarArrow = driver.find_element(By.CLASS_NAME, 'ant-picker-header-next-btn')
cOutCalendarArrow.click()

cOutDate = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/date-range-popup/div/div/inner-popup/div/div/div/date-table/table/tbody/tr[2]/td[4]/div')
cOutDate.click()

# Add Check Out-time
cOutTime = driver.find_element(By.XPATH, '//*[@id="time-picker"]/div/input')
cOutTime.click()
cOutTime.send_keys('23:59:59')

# Confirm Check In
cOutCheck = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/div/div[3]/date-time-edit/form/div[1]/div[3]/button[2]')
cOutCheck.click()






time.sleep(5)
driver.close()