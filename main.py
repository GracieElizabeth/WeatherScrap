from selenium import webdriver
import time

def get_driver():
    # Set options to make browsing easier
    chrome_settings = webdriver.ChromeOptions()
    chrome_settings.add_argument("disable-infobars") # Disable the info bar if website has it
    chrome_settings.add_argument("start-maximized") # Start browser as maximized
    chrome_settings.add_argument("disable-dev-shm-usage") # Disabled devshm for Linux
    chrome_settings.add_argument("no-sandbox") # Disable sandboxing mode
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
    time.sleep(2)
    item = driver.find_element(by="xpath", value="/html/body/div[1]/main/div[2]/main/div[1]/div/section/div/div/div[2]/div[1]/div[1]")  # Finds item

    return get_temperature(item.text)


print(main())
