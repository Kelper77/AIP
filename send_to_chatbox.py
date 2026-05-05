"""Standalone script to send a message to a web chatbox using Selenium."""

import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHAT_INPUT_SELECTORS = [
    "textarea",
    "input[type='text']",
    "[contenteditable='true']",
]


def send_to_chatbox(url: str, message: str) -> bool:
    """Open *url* in headless Chrome, locate a chat input, type *message*, and press Enter.

    Parameters
    ----------
    url : str
        The page URL containing the chatbox.
    message : str
        The text to type into the input element.

    Returns
    -------
    bool
        ``True`` if the message was sent successfully, ``False`` otherwise.
    """
    driver = None
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)
        driver.get(url)

        wait_seconds = random.uniform(4, 12)
        time.sleep(wait_seconds)

        input_element = None
        for selector in CHAT_INPUT_SELECTORS:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            if elements:
                input_element = elements[0]
                break

        if input_element is None:
            print("No chat input element found.")
            return False

        input_element.click()
        input_element.send_keys(message)
        time.sleep(1)
        input_element.send_keys(Keys.ENTER)
        time.sleep(2)

        print(f"Message sent to {url}")
        return True

    except Exception as exc:
        print(f"Error: {exc}")
        return False

    finally:
        if driver is not None:
            driver.quit()


if __name__ == "__main__":
    send_to_chatbox("https://example.com", "Hello from send_to_chatbox!")
