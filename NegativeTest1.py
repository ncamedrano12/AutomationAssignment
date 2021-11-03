from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'https://parking.e2log.com'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 5)
passFile = open('PassFile1.txt','w')

# Goes to new reservations page
reserveButton = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > ng-component > div > ng-component > div.container.d-none.d-sm-block.pt-12 > div > button')
reserveButton.click()

# Attempt to add vehicle License Plate that is empty
vehicleAdd = driver.find_element(By.CSS_SELECTOR, '.fa-plus')
vehicleAdd.click()

# Purposefully remove send_keys and click check
vehicleInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="license-plate"]')))
vehicleCheck = driver.find_element(By.XPATH, '//button[2]')
vehicleCheck.click()

neededLicense = driver.find_element(By.XPATH, '/html/body/app-root/div/ng-component/div/ng-component/div/div/div[1]/vehicle-edit/form/nz-form-item/nz-form-control/div[2]').text
print(neededLicense)
passFile.write('Is "' + neededLicense + '" the correct error message?\n' )
if neededLicense == "License plate needed":
    print('TRUE')
    passFile.write('   -TRUE\n')
else:
    print('FALSE')
    passFile.write('   -FALSE\n')

time.sleep(2)
passFile.close()
driver.close()