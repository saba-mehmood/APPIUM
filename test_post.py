from multiprocessing.connection import wait
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from time import sleep

from test_login import TestLogin

desired_cap = { 
    "appium:deviceName": "Infinix HOT 10i",
    "platformName": "Android",
    "appWaitActivity": "*",
    "browserName":"",
    "appium:app": "C:\\Users\\Saba.DESKTOP-GK3J0JB\\Downloads\\wordpress-19-5.apk"
}


class TestPost(TestLogin):

  """CONSTRUCTOR"""
  def __init__(self, driver):

    """INHERIT BASE CLASS"""
    super().__init__(driver)

  #def setup(self):
#
  #  """MAKING CONNECTION WITH TESTING DEVICE"""
  #  self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=desired_cap)

  
  def teardown(self):
   self.driver.quit()

  
  def test_post(self):
    """CALLING LOGIN FUNCTION"""  
    a=TestLogin()  
    a.test_login()

    post_btn = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/fab_button')))
    post_btn.click()

    blog_btn = wait.until(EC.element_to_be_clickable((By.NAME,'Blog post')))
    blog_btn.click()
    
    add_title1 = wait.until(EC.visibility_of_element_located((By.XPATH,'//android.widget.EditText[@content-desc="Post title. Empty"]'))).send_keys('First Post')
    add_title2 = wait.until(EC.visibility_of_element_located((By.XPATH,'//android.widget.ScrollView[@content-desc="block-list"]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText"]'))).send_keys('Description')
    
    publish_btn = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/menu_primary_action')))
    publish_btn.click()
    
    publish_now = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/publish_button')))
    publish_now.click()

    sleep(2)

