from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driverPath = "C:/Users/User/Desktop/chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.maximize_window()
driver.get("https://inshoppingcart.inone.useinsider.com")

driver.implicitly_wait(20)
driver.find_element(By.ID, "email").send_keys("mustafa.corekci@useinsider.com")
driver.find_element(By.ID, "password").send_keys("")
driver.find_element(By.ID, "login-button").click()

# Exercise1
# driver.find_element(By.XPATH, "//label[@for = 'enableUtmSettings']").click()

# Exercise 3
# inputSMS = browser.find_element_by_xpath("//div[@id = 'smsMessageAttribute']")
# inputSMS.send_keys(" ")
# print(browser.find_element_by_xpath("//p[contains(text(), 'Message')]").text)

# Exercise 4
# inputSearchJourney = browser.find_element_by_xpath("//input[contains(@placeholder, 'Filter')]")
# inputSearchJourney.send_keys("test")

# Exercise 5
# radiobuttonTest = browser.find_element_by_xpath("//label[@for = 'test']")
# radiobuttonTest.click()

# Exercise 6
# browser.find_element_by_xpath("//img[@class = 'close']").click()
# buttonStatistic = browser.find_element_by_xpath("(//td[contains(@class, 'statistics')]//a//i)[1]")
# buttonStatistic.click()

# Exercise 7
# buttonDeleteVariation = browser.find_element_by_xpath("//button[@id = 'delete']").click()

# Exercise 8
# buttonDelete = browser.find_element_by_xpath("(//p[text() = 'Delete'])[1]")
# buttonChange = browser.find_element_by_xpath("(//p[text() = 'Change'])[1]")

# Exercise 9
# browser.find_element_by_xpath("//p[text() = 'SMS']").click()
# browser.implicitly_wait(20)
# browser.find_element_by_id("smsMessageAttribute").send_keys(" ")
# browser.find_element_by_name("submitButton").click()
# print(browser.find_element_by_xpath("//p[contains(text(), 'fields')]").text)

# Exercise 10
# createCamp = browser.find_element(By.XPATH,"//a[contains(@class, 'btnBlue')]")
