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

# Buscar el ícono de búsqueda y hacer clic
wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Search")))
driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search").click()

# Ingresar texto de búsqueda
search_input = wait.until(EC.presence_of_element_located((AppiumBy.ID, "com.google.android.youtube:id/search_edit_text")))
search_input.send_keys("Appium tutorial")
driver.press_keycode(66)  # Enter

# Esperar resultados
time.sleep(5)

# Hacer swipe (scroll)
for _ in range(2):
    driver.execute_script("mobile: swipeGesture", {
        "left": 100,
        "top": 1000,
        "width": 800,
        "height": 800,
        "direction": "up",
        "percent": 0.75
    })
    time.sleep(1.5)

driver.quit()