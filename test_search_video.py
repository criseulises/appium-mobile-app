from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

# Configuración del dispositivo y la app de YouTube
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

# Iniciar sesión con Appium
driver = webdriver.Remote("http://localhost:4723", options=options)

print("✅ YouTube abierto")

# Esperar que cargue la pantalla principal
time.sleep(5)

# Tocar el ícono de búsqueda (por su content-desc)
search_icon = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search")
search_icon.click()
print("🔍 Se tocó el botón de búsqueda")

time.sleep(2)

# Escribir el texto de búsqueda
search_input = driver.find_element(AppiumBy.ID, "com.google.android.youtube:id/search_edit_text")
search_input.send_keys("Appium tutorial")
print("⌨️ Se escribió la búsqueda")

time.sleep(2)

# Presionar ENTER en el teclado virtual
driver.press_keycode(66)  # 66 = KEYCODE_ENTER
print("✅ Búsqueda enviada")

time.sleep(5)

driver.quit()