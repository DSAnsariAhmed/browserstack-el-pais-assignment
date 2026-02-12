from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import threading
import time

# Replace with your credentials
# USERNAME = "YOUR_USERNAME"
# ACCESS_KEY = "YOUR_ACCESS_KEY"

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"

# Target URL
TEST_URL = "https://elpais.com/opinion/"

# 5 Browser Configurations
browsers = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "11",
            "buildName": "ElPais Selenium Assignment",
            "sessionName": "Chrome - Windows Test"
        }
    },
    {
        "browserName": "Firefox",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "10",
            "buildName": "ElPais Selenium Assignment",
            "sessionName": "Firefox - Windows Test"
        }
    },
    {
        "browserName": "Edge",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "Windows",
            "osVersion": "11",
            "buildName": "ElPais Selenium Assignment",
            "sessionName": "Edge - Windows Test"
        }
    },
    {
        "browserName": "Safari",
        "browserVersion": "latest",
        "bstack:options": {
            "os": "OS X",
            "osVersion": "Sonoma",
            "buildName": "ElPais Selenium Assignment",
            "sessionName": "Safari - Mac Test"
        }
    },
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "bstack:options": {
            "deviceName": "iPhone 14",
            "realMobile": "true",
            "osVersion": "16",
            "buildName": "ElPais Selenium Assignment",
            "sessionName": "iPhone 14 - Mobile Test"
        }
    }
]

def run_test(cap):
    options = Options()

    for key, value in cap.items():
        options.set_capability(key, value)

    driver = webdriver.Remote(
        command_executor=BROWSERSTACK_URL,
        options=options
    )

    driver.get(TEST_URL)
    time.sleep(6)

    driver.quit()

# Run in Parallel Threads
threads = []

for cap in browsers:
    t = threading.Thread(target=run_test, args=(cap,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All 5 BrowserStack sessions executed successfully.")

