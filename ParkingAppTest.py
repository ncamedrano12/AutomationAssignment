from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# import requests
# from bs4 import BeautifulSoup


url = 'https://parking.e2log.com'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 5)


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

# Submit
selectParkingButton = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/div/div[4]/button[2]')
selectParkingButton.click()

# Select Spot
selectSpot = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/div[2]/div[1]/spot-list/div/div[1]/div/div/button')))
selectSpot.click()

# Review
reviewRes = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/button[2]/span')))
reviewRes.click()

# Validations

value1 = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/reservation-detail/div[1]/div[1]/h5')
value2 = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/reservation-detail/div[1]/div[2]/div[1]/h5')
value3 = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/reservation-detail/div[1]/div[2]/div[2]/h4')
value4 = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/reservation-detail/div[1]/div[3]/h5[1]')
value5 = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/reservation-detail/div[1]/div[3]/h5[2]')
value6 = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/reservation-detail/div[1]/div[4]/div[1]/h3')
value7 = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/reservation-detail/div[1]/div[4]/div[2]/h3')


print(value1.text)
print(value2.text)
print(value3.text)
print(value4.text)
print(value5.text)
print(value6.text)
print(value7.text)

time.sleep(5)
driver.close()