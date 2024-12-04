from selenium import webdriver
import time
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_driver():
    # Set options to make browsing easier
    chrome_settings = webdriver.ChromeOptions()
    chrome_settings.add_argument("disable-infobars") # Disable the info bar if website has it
    chrome_settings.add_argument("start-maximized") # Start browser as maximized
    chrome_settings.add_argument("disable-dev-shm-usage") # Disabled devshm for Linux
    chrome_settings.add_argument("no-sandbox") # Disable sandboxing mode
    chrome_settings.add_argument("headless")  # Run in headless mode
    # Enable script to access browser
    chrome_settings.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_settings.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=chrome_settings)# Initialize driver with above options
    driver.get("https://weather.com/weather/today/l/212af395835a74620e1150988047c8eaa4fa6740b600aff9bb63b98b2dae6fc1")
    return driver

def get_temperature(text):
    # Extract temp from string
    temperature = text.split()[0]
    return temperature

def main():
    driver = get_driver()  # Creates browser instance
    try:
        # Wait until the element is present
        item = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]"))
        )
        temperature = get_temperature(item.text)
    except Exception as e:
        print(f"Error occurred: {e}")
        temperature = "error"

    return temperature

start_time = datetime.now()
end_time = start_time + timedelta(minutes=1)

while datetime.now() < end_time:
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{current_time}.txt"

    with open(file_name, "w") as file:
        file.write(main())

    time.sleep(3)

print("Function has stopped running after 1 minute.")
