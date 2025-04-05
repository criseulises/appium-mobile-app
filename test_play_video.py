from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.google.android.youtube",
    "appActivity": "com.google.android.apps.youtube.app.WatchWhileActivity",
    "automationName": "UiAutomator2",
    "noReset": True
}

options = UiAutomator2Options()
options.load_capabilities(desired_caps)

driver = webdriver.Remote("http://localhost:4723", options=options)
wait = WebDriverWait(driver, 20)

wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Search")))
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search").click()

search_input = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.youtube:id/search_edit_text")))
search_input.send_keys("Appium tutorial")
driver.press_keycode(66)

wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.youtube:id/thumbnail")))

videos = driver.find_elements(AppiumBy.ID, "com.google.android.youtube:id/thumbnail")
if videos:
    videos[0].click()
    print("🎬 Video tocado correctamente.")
    time.sleep(10)
else:
    print("❌ No se encontraron videos para reproducir.")

driver.quit()
