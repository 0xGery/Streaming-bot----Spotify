from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random
import pytz
import time

# 0xGery
def set_random_timezone(driver):
    supported_timezones = pytz.all_timezones
    random_timezone = random.choice(supported_timezones)
    driver.execute_cdp_cmd("Emulation.setTimezoneOverride", {"timezoneId": random_timezone})

def set_fake_geolocation(driver, latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "accuracy": 100
    }
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", params)

def main():
    chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    driver_path = 'chromedriver.exe'

    with open('accounts.txt', 'r') as file:
        accounts = file.readlines()

    use_proxy = input("Do you want to use proxies? (y/n):")

    if use_proxy.lower() == 'y':
        print("Proxy functionality will be added after receiving 50 stars. Proceeding without a proxy.")
        time.sleep(3)

    spotify_song = input("Enter the Spotify song URL (e.g., https://open.spotify.com/track/5hFkGfx038V0LhqI0Uff2J?si=bf290dcc9a994c36):")

    drivers = []
    delay = random.uniform(2, 6)
    delay2 = random.uniform(5, 14)

    for account in accounts:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-notifications')
        driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

        username, password = account.strip().split(':')

        try:
            driver.get("https://www.spotify.com/us/login/")
            username_input = driver.find_element(By.CSS_SELECTOR, "input#login-username")
            password_input = driver.find_element(By.CSS_SELECTOR, "input#login-password")
            username_input.send_keys(username)
            password_input.send_keys(password)
            driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button']").click()
            time.sleep(delay)
            driver.get(spotify_song)
            driver.maximize_window()
            time.sleep(10)
            playmusic_xpath = "(//button[@data-testid='play-button']//span)[3]"
            playmusic = driver.find_element(By.XPATH, playmusic_xpath)
            playmusic.click()
            time.sleep(1)
            print("Username: {} - Listening process has started.".format(username))
        except Exception as e:
            print("An error occurred in the bot system:", str(e))

        set_random_timezone(driver)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        set_fake_geolocation(driver, latitude, longitude)

        drivers.append(driver)
        time.sleep(5)

    print("Streaming operations completed. Close the program to stop all activities.")
    while True:
        pass

if __name__ == "__main__":
    main()