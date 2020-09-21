import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

def add_data():
    f = open("exaple.txt", "r")
    lines = f.readlines()[1:]
    for line in lines:
        data = line.split(';')
        code = data[1]
        value = data[2]
        limit = data[3]
        start = data[4]
        end = data[5]
        print(data[0])
        try:
            add_code(code, value, limit, start, end)
        except selenium.common.exceptions.NoSuchElementException:
            print("Code already exists!")
            driver.get("https://admin.konfeo.com/events/33705/discounts")
        sleep(3)
        
    f.close()

def connect():
    email = input("Inpot login: ")
    haslo = input("Input password: ")

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://admin.konfeo.com/pl/users/sign_in")

    passData = [email, haslo]

    driver.implicitly_wait(1)

    email = driver.find_element_by_id("user_email")
    email.send_keys(passData[0])
    passwd = driver.find_element_by_id("user_password")
    passwd.send_keys(passData[1])

    login = driver.find_element_by_name("commit")
    login.click()

    driver.implicitly_wait(1)

    driver.get("https://admin.konfeo.com/events/33705/discounts")
    return driver

def add_code(code, value, limit, start, end):
    addCodeButton = driver.find_element_by_link_text("Dodaj kod")
    addCodeButton.click()

    driver.implicitly_wait(1)
    
    codeName = driver.find_element_by_id("form_code")
    codeName.send_keys(code)
    codeValue = driver.find_element_by_id("form_value")
    codeValue.send_keys(value)
    codeLimit = driver.find_element_by_id("form_amount")
    codeLimit.send_keys(limit)
    codeDateStart = driver.find_element_by_id("form_valid_from")
    codeDateStart.send_keys(Keys.CONTROL+"a")
    codeDateStart.send_keys(start, "00:00")
    codeDateEnd = driver.find_element_by_id("form_valid_until")
    codeDateEnd.send_keys(Keys.CONTROL+"a")
    codeDateEnd.send_keys(end, "23:59")
    commit = driver.find_element_by_name("commit")
    commit.click()

driver = connect()
add_data()