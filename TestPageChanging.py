from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://parking.e2log.com'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 5)
passFile = open('PassFile2.txt','w')


# Second Test case to go between pages
# First to Log Out page
logOutPage = driver.find_element(By.XPATH, '/html/body/app-root/app-navbar/div/div[2]/div/h5[2]/a')
logOutPage.click()
# Quick page check
pageValue = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/p').text
passFile.write(pageValue + ' is found value?\n')
if pageValue == "not-found works!":
    passFile.write('  -TRUE\n')
else:
    passFile.write('  -FALSE\n')


# Back to home page
time.sleep(1)
homePage = driver.find_element(By.XPATH, '/html/body/app-root/app-navbar/div/div[2]/div/h2/a')
homePage.click()

# Check buttons are there
reserveSpotValue = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > ng-component > div > ng-component > div.container.d-none.d-sm-block.pt-12 > div > button').text
print(reserveSpotValue)
checkSpotValue = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > ng-component > div > ng-component > div.container.d-none.d-sm-block.pt-12 > div > a').text
print(checkSpotValue)
passFile.write(reserveSpotValue + " and " + checkSpotValue + " buttons are present?\n")
if reserveSpotValue == "Reserve a spot" and checkSpotValue == "Check in my spot and pay later":
    passFile.write('  -TRUE\n')
else:
    passFile.write('  -FALSE\n')

# Back to logout page again
logOutPage.click()
time.sleep(1)
reservationTab = driver.find_element(By.XPATH, '/html/body/app-root/app-navbar/div/div[2]/div/h5[1]/a')
reservationTab.click()

# Check if buttons are there again
reserveSpotValue = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > ng-component > div > ng-component > div.container.d-none.d-sm-block.pt-12 > div > button').text
print(reserveSpotValue)
checkSpotValue = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > ng-component > div > ng-component > div.container.d-none.d-sm-block.pt-12 > div > a').text
print(checkSpotValue)

passFile.write(reserveSpotValue + " and " + checkSpotValue + " buttons are present again?\n")
if reserveSpotValue == "Reserve a spot" and checkSpotValue == "Check in my spot and pay later":
    passFile.write('  -TRUE\n')
else:
    passFile.write('  -FALSE\n')


# Close file and driver
passFile.close()
time.sleep(3)
driver.close()