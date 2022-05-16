import base64
import os
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

desired_cap = {
  """CAP FOR REAL DEVICE"""

  #"appium:deviceName": "Infinix HOT 10i",
  #"platformName": "Android",
  #"automationName": "UIAutomator2",
  #"appPakage":"com.IELTS.IELTSpreparation.IELTShighBands.IELTStips",
  #"appWaitActivity":"com.ielts.ieltspreparation.ui.splash.SplashScreenActivity",
  #"appium:app": "C:\\Users\\Saba.DESKTOP-GK3J0JB\\Downloads\\Ielts-Practice-1-06-Apr-2022-debug.apk"


  """CAP FOR EMULATOR"""  
  "appium:deviceName": "Infinix HOT 10i",
  "platformName": "Android",
  "appium:app": "D:\\APIS\\ieltsApp.apk"

}

"""MAKING CONNECTION WITH TESTING DEVICE"""
driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.start_recording_screen()

"""LOCATING ELEMENTS AND PERFORMING ACTIONS"""
##FLUENT WAIT###
wait = WebDriverWait(driver, 30, poll_frequency=1, ignored_exceptions=[ElementClickInterceptedException])

continue_button = wait.until(EC.element_to_be_clickable((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.Button')))
continue_button.click()
tip_button = wait.until(EC.element_to_be_clickable((By.ID,'com.IELTS.IELTSpreparation.IELTShighBands.IELTStips:id/btn_tips')))
tip_button.click()


"""SCROLLING SCREEN 4 TIMES"""
for i in range(5):
  actions = ActionChains(driver)
  actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
  actions.w3c_actions.pointer_action.move_to_location(327, 1404)
  actions.w3c_actions.pointer_action.pointer_down()
  actions.w3c_actions.pointer_action.move_to_location(361, 320)
  actions.w3c_actions.pointer_action.release()
  actions.perform()
  time.sleep(4)

vedio_rawadata = driver.stop_recording_screen()
vedio_name = driver.current_activity + time.strftime("%y_%m_%d_%H%M%S")

"""CREATE FILEPATH"""
filePath = os.path.join("D:\APPIUM\screenshots", vedio_name+".mp4")

with open(filePath,"wb") as vd:
  vd.write(base64.b64decode(vedio_rawadata))