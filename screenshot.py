import time
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

desired_cap = {
 

  """CAP FOR EMULATOR"""  
  "appium:deviceName": "Infinix HOT 10i",
  "platformName": "Android",
  "appium:app": "C:\\Users\\Saba.DESKTOP-GK3J0JB\\Downloads\\Ielts-Practice-1-14-Apr-2022-debug.apk"

}

"""MAKING CONNECTION WITH TESTING DEVICE"""
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)

"""LOCATING ELEMENTS ANF PERFORMING ACTIONS"""
##FLUENT WAIT###
wait = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[ElementClickInterceptedException])

continue_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button')))
continue_button.click()
tip_button = wait.until(EC.element_to_be_clickable((By.ID,'com.IELTS.IELTSpreparation.IELTShighBands.IELTStips:id/btn_tips')))
tip_button.click()

ti= time.strftime("%Y_%m_%d_%H%M%S")
activityName = driver.current_activity
filename = activityName+ti
time.sleep(3)
driver.save_screenshot("D:\APPIUM\screenshots\.png")

