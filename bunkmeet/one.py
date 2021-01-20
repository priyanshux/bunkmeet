from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time


def chrome_options():
    global options
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--use-fake-ui-for-media-stream")


def bunk(email, password):
    global teams
    chrome_options()
    PATH = '/usr/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.get("https://teams.microsoft.com/_#/school//?ctx=teamsGrid")
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)
    email_element = WebDriverWait(driver, 50, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.ID, "i0116"))
    )
    email_element.send_keys(email)
    email_element.send_keys(Keys.RETURN)
    time.sleep(3)

    password_element = WebDriverWait(driver, 50, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.ID, "i0118"))
    )
    password_element.send_keys(password)
    time.sleep(3)

    element = WebDriverWait(driver, 100, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    element.click()
    time.sleep(3)

    actions = ActionChains(driver)
    actions.send_keys(Keys.RETURN)
    actions.perform()
    time.sleep(7)

    try:
        t4sne = WebDriverWait(driver, 50, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "team-name-text"))
        )
        teams = []
        for i in t4sne:
            teams.append(i.text)
        driver.quit()
        return teams
    except TimeoutException:
        message = 'Invalid credentials'
        return message
