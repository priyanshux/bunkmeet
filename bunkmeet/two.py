import os
import sys
import time
import schedule
from datetime import timedelta
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import pause as pause


def covid(email, password, team, datetime, duration):
    global mute_mic, camera_off, webapp
    print("\n\n ____              _                        _   \n| __ ) _   _ _ __ | | ___ __ ___   ___  ___| |_ \n|  _ "
          "\| | | | '_ \| |/ / '_ ` _ \ / _ \/ _ \ __|\n| |_) | |_| | | | |   <| | | | | |  __/  __/ |_ \n|____/ \__,"
          "_|_| |_|_|\_\_| |_| |_|\___|\___|\__|\n")
    print("Hello, I am Celerito Gomez. Please don't get alarmed by this unexpected warning.")
    print("I work for Bunkmeet and we're both good. I shall attend {} for you.".format(team))
    print("Once I've joined, I'll keep checking if I'm still in the lecture every minute.")
    print("I shall rejoin the lecture in case your call has been dropped.\n")
    pause.until(datetime)
    XPATH = "/html/body/div[2]/div[2]/div[2]/div[1]/teams-grid/div/div[2]/div[1]/div/div/div[1]//div[" \
            "@data-tid='team-"
    teampath = XPATH + team + "']"

    options = webdriver.ChromeOptions()
    # options.binary_location = "/usr/bin/google-chrome-stable"
    # options.add_argument("--no-sandbox")
    # options.add_argument("--headless")
    # options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--use-fake-ui-for-media-stream")
    PATH = '/usr/bin/chromedriver'
    driver = webdriver.Chrome(executable_path=PATH, options=options)
    driver.get("https://teams.microsoft.com/_#/school//?ctx=teamsGrid")
    # driver.set_window_size(1280, 1440)
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException)
    email_element = WebDriverWait(driver, 25, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.ID, "i0116"))
    )
    email_element.send_keys(email)
    email_element.send_keys(Keys.RETURN)
    time.sleep(2)

    password_element = WebDriverWait(driver, 26, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.ID, "i0118"))
    )
    password_element.send_keys(password)
    time.sleep(3)

    element = WebDriverWait(driver, 27, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.ID, "idSIButton9"))
    )
    element.click()

    actions = ActionChains(driver)
    actions.send_keys(Keys.RETURN)
    actions.perform()

    try:
        select_team = WebDriverWait(driver, 81, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH, teampath))
        )
        select_team.click()
    except TimeoutException:
        print("Invalid credentials or team name.")
        sys.exit(1)

    # COMMENT OUT THE FOLLOWING IF YOU HAVE A STABLE INTERNET CONNECTION. THIS DELAYS THE PROGRAM BY 1 MINUTE
    # CODE FOR UNSTABLE NETWORK STARTS (SEARCHING FOR RETRY BUTTON)
    try:
        join_call = WebDriverWait(driver, 60, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-tid='tidConfirm']"))
        )
        join_call.click()
    except TimeoutException:
        pass
    # CODE FOR UNSTABLE NETWORK ENDS

    try:
        join_call = WebDriverWait(driver, 62, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH, "//button[@title='Join call with video']"))
        )
        join_call.click()
    except TimeoutException:
        print("Couldn't find an ongoing meeting. Please check your team name, date, time and internet connection.")
        sys.exit(1)
    except TypeError:
        pass
    except ElementNotInteractableException:
        join_call = WebDriverWait(driver, 31, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH, "//button[@title='Join call with video']"))
        )
        time.sleep(5)
        join_call.click()

    try:
        camera_off = WebDriverWait(driver, 60, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH, "//span[@title='Turn camera off']"))
        )
        camera_off.click()
    except TimeoutException:
        pass
    except ignored_exceptions as e:
        time.sleep(2)
        camera_off.click()

    try:
        mute_mic = WebDriverWait(driver, 33, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.XPATH, "//span[@title='Mute microphone']"))
        )
        mute_mic.click()
    except TimeoutException:
        pass
    except ignored_exceptions as e:
        time.sleep(2)
        mute_mic.click()

    try:
        webapp = WebDriverWait(driver, 34, ignored_exceptions=ignored_exceptions).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-col"))
        )
        webapp.click()
    except TimeoutException:
        pass
    except ignored_exceptions as e:
        time.sleep(2)
        webapp.click()

    time.sleep(5)

    def rejoin():
        try:
            rejoin_call = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
                EC.presence_of_element_located((By.XPATH, "//button[@title='Rejoin']"))
            )
            rejoin_call.click()
        except TimeoutException:
            pass
        try:
            rejoin_call = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
                EC.presence_of_element_located((By.XPATH, "//button[@title='Rejoin call']"))
            )
            rejoin_call.click()
        except TimeoutException:
            pass

    schedule.every(1).minutes.do(rejoin)
    minute = duration - timedelta(minutes=1)

    while datetime.now() < minute:
        schedule.run_pending()
        time.sleep(1)

    pause.until(duration)
    if datetime.now() > minute:
        driver.quit()
