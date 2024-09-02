import uiautomator2 as u2
import time

# Step 1: Connect to the Android device
device = u2.connect()  # Connect to the first available device via USB or WiFi

# Step 2: Launch the Chrome app
print("Launching Chrome...")
device.app_start('com.android.chrome')

# Step 3: Wait for the app to load
print("Waiting for Chrome to load...")
time.sleep(5)

# Step 4: Navigate through the initial screens (if any)
# Accept terms and conditions or click through prompts
if device(text="Accept & continue").exists:
    print("Accepting terms and conditions...")
    device(text="Accept & continue").click()
    time.sleep(2)

if device(text="Next").exists:
    print("Navigating through setup screens...")
    device(text="Next").click()
    time.sleep(2)

if device(text="No thanks").exists:
    print("Skipping additional settings...")
    device(text="No thanks").click()
    time.sleep(2)

# Step 5: Extract text from a specific screen element
# Example: Extract the text from the search/address bar
print("Extracting text from the Chrome URL bar...")
try:
    text_data = device(resourceId="com.android.chrome:id/url_bar").get_text()
    print(f"Extracted Text: {text_data}")
except Exception as e:
    print(f"Failed to extract text: {e}")

# Step 6: Close the app
print("Closing Chrome...")
device.app_stop('com.android.chrome')
print("Chrome closed successfully.")

