from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# Capabilities básicas
desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "com.google.android.youtube",
    "appActivity": "com.google.android.apps.youtube.app.WatchWhileActivity",
    "automationName": "UiAutomator2",
    "noReset": True
}

# Crear opciones compatibles con versiones actuales
options = UiAutomator2Options()
options.load_capabilities(desired_caps)

# Conectar al servidor de Appium
driver = webdriver.Remote("http://localhost:4723", options=options)

print("✅ YouTube se abrió correctamente")

time.sleep(5)
driver.quit()