from appium import webdriver
import time

desired_cap = {
  "platformName": "Android",
  "deviceName": "OPPO",
  "appPackage": "com.browser2345",
  "appActivity": ".BrowserActivity"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)

a = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout[5]")
a.click()
time.sleep(2)
b = driver.find_element_by_accessibility_id("登录领5元红包")
b.click()


