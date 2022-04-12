import time

from appium import webdriver

desired_caps = dict()
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'R4CBB19B25602280'
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# time.sleep(5)

driver.start_activity('com.ss.android.ugc.aweme','.splash.SplashActivity')
print(driver.current_package)
print(driver.current_activity)

print('准备进入后台')
driver.background_app(5)
print("返回前台")

time.sleep(5)

driver.quit()