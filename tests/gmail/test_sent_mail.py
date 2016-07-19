from appium import webdriver 
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
import re

success = True
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4'
desired_caps['deviceName'] = 'testGmail'
desired_caps['appPackage'] = 'com.google.android.gm'
desired_caps['appActivity'] = 'com.google.android.gm.ComposeActivityGmail'

wd = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

def test_sent_gmail():
    try:
        # vars
        xpath_to_field="//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.TextView[1]"
	xpath_frequent_recipient="//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.EditText[1]"
	xpath_subject_field="//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.EditText[1]"
	xpath_email_body="//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.EditText[1]"
        xpath_sent_mail="//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.LinearLayout[7]"
        xpath_desc="//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.support.v4.widget.DrawerLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.View[1]/android.widget.FrameLayout[1]/android.widget.ListView[1]/android.widget.FrameLayout[1]/android.view.View[1]/android.view.View[1]"

        string_recipient_email="foxfantasticfox@gmail.com"
        string_subject="Verify sending email"
        string_email_body="Hello, this is a test from the testing script."

        # sending mail 
	wd.find_element_by_xpath(xpath_to_field).send_keys(string_recipient_email)
	wd.find_element_by_xpath(xpath_frequent_recipient).click()
	wd.find_element_by_xpath(xpath_subject_field).send_keys(string_subject)
	wd.find_element_by_xpath(xpath_email_body).send_keys(string_email_body)
	wd.find_element_by_id("Send").click()

        # check current time
        click_time=datetime.datetime.now()

        # find text for verification
       	wd.find_element_by_id("Apps").click()
	wd.find_element_by_id("Gmail").click()
        wd.find_element_by_id("Navigate up").click()
	wd.find_element_by_xpath(xpath_sent_mail).click()
        time.sleep(1)
        summary=wd.find_element_by_xpath(xpath_desc).get_attribute("name")

        # check current time
        current_time=datetime.datetime.now()

        # verification
        assert string_subject in summary
        assert string_email_body in summary
        # TBD: add check for time of sent mail, should be quite close to current_time

    finally:
	wd.quit()
	if not success:
		raise Exception("Test failed.")

