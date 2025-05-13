import pytest
import os
import platform
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def browser():
    """
    Simplified browser setup that doesn't rely on webdriver-manager
    """
    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    # Uncomment this if you need headless mode
    # chrome_options.add_argument("--headless")

    # Try the simplest approach first - let Selenium find ChromeDriver
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except Exception as e:
        print(f"Simple Chrome setup failed: {e}")

        # If that doesn't work, try specifying a Chrome driver path
        # You may need to download ChromeDriver manually and specify the path here
        driver_path = "./chromedriver"  # Update this path as needed

        # Check if the driver exists at the specified path
        if os.path.exists(driver_path):
            service = Service(executable_path=driver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)
        else:
            raise Exception(f"ChromeDriver not found at {driver_path}. Please download it manually.")

    # Maximize window and set implicit wait
    driver.maximize_window()
    driver.implicitly_wait(10)

    # Yield driver to the test
    yield driver

    # Quit the driver after the test
    driver.quit()