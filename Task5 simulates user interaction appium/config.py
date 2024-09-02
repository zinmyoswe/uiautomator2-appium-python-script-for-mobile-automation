# config.py

# Replace these with your actual values
APP_PACKAGE = 'com.example.app'
APP_ACTIVITY = 'com.example.app.MainActivity'
DEVICE_NAME = 'Android Emulator'  # or 'Samsung Galaxy A30S' for real device
PLATFORM_NAME = 'Android'
PLATFORM_VERSION = '10'  # Replace with your device's version

CAPABILITIES = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'platformVersion': PLATFORM_VERSION,
    'appPackage': APP_PACKAGE,
    'appActivity': APP_ACTIVITY,
    'automationName': 'UiAutomator2'
}
