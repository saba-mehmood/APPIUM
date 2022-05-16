import re
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
from time import sleep

desired_cap = { 
    "appium:deviceName": "Infinix HOT 10i",
    "platformName": "Android",
    "appWaitActivity": "*",
    "browserName":"",
    "appium:app": "C:\\Users\\Saba.DESKTOP-GK3J0JB\\Downloads\\wordpress-19-5.apk"
}


class TestLogin():

  def setup(self):

    """MAKING CONNECTION WITH TESTING DEVICE"""
    self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=desired_cap)

  
  #def teardown(self):
  # self.driver.quit()


  def test_login(self):
    ##FLUENT WAIT###
    wait = WebDriverWait(self.driver, 30, poll_frequency=1, ignored_exceptions=[ElementClickInterceptedException,ElementNotVisibleException])  
    
    login_btn = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/continue_with_wpcom_button')))
    login_btn.click()
    
    sleep(2)

    email_field = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'android.widget.EditText'))).send_keys('testingdevice878@gmail.com')
    sleep(2)
    ##signup
    continue_btn = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/login_continue_button')))
    continue_btn.click()
   ##sleep(2)
   ##check_email_btn = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/login_open_email_client')))
   ##check_email_btn.click()
   ##sleep(5)
   ##mail = wait.until(EC.element_to_be_clickable((By.CLASS_NAME,'android.widget.TextView')))
   ##wp ='WordPress.com'
   ##wpp = re.sub(" \d+", " ", mail.text)
   ##print(wpp)
   ##assert wp == wpp
   ##wpp.click()
   ##sleep(2)
   ##signup_btn = wait.until(EC.element_to_be_clickable((By.XPATH,'//android.view.View[@content-desc="Sign up to WordPress.com"]')))
   ##signup_btn.click()
  
    password = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'android.widget.EditText'))).send_keys('testing12345')
    
    continue_btn = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/bottom_button')))
    continue_btn.click()
     
    title= wait.until(EC.visibility_of_element_located((By.ID,'org.wordpress.android:id/login_epilogue_header_title')))
    print(title.text)
    assert title.text == "testingdevice878"

    site_title = wait.until(EC.visibility_of_element_located((By.ID,'org.wordpress.android:id/text_title')))
    site_title.click()
    sleep(2)

    no_thanks_btn = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/quick_start_prompt_dialog_button_negative')))
    no_thanks_btn.click()
    sleep(2)

    post_btn = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/fab_button')))
    post_btn.click()

    blog_btn = wait.until(EC.visibility_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[3]/android.widget.TextView')))
    blog_btn.click()
    
    add_title1 = wait.until(EC.visibility_of_element_located((By.XPATH,'//android.widget.EditText[@content-desc="Post title. Empty"]'))).send_keys('First Post')
    add_title2 = wait.until(EC.visibility_of_element_located((By.XPATH,'//android.view.ViewGroup[@content-desc="Paragraph Block. Row 1. Empty"]/android.widget.EditText')))
    add_title2.click()
    add_title2.send_keys('Description')

    publish_btn = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/menu_primary_action')))
    publish_btn.click()
    
    publish_now = wait.until(EC.element_to_be_clickable((By.ID,'org.wordpress.android:id/publish_button')))
    publish_now.click()

    sleep(2)
    
    
