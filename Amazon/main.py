from selenium import webdriver
from homework5.loginPage import LoginPage
from homework5.searchPage import SearchPage
from homework5.productPage import ProductPage
import time

driverPath = "C:/Users/User/Desktop/chromedriver.exe"
driver = webdriver.Chrome(driverPath)
driver.maximize_window()
driver.get("https://www.amazon.com")

# driver.implicitly_wait(20)

# Login Page
login = LoginPage(driver)
login.openLoginPage()
login.enterMail("ahmettoktasdot@gmail.com")
login.clickEmailLogin()
login.enterPassword("159753")
login.clickPasswordLogin()

# Search Page
search = SearchPage(driver)
search.enterSearchText("samsung")
search.clickSearch()
search.clickSecondPage()
search.productClick()

# Product Page
product = ProductPage(driver)
product.addToListClick()
product.viewListClick()
product.deleteItemClick()

time.sleep(5)
driver.quit()
