import os
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

def get_brave_driver():
    # 1. Define options for Chrome (which Brave uses)
    options = Options()
    
    # 2. Point to your Brave executable (Update this path if you installed it elsewhere)
    # Common path for Windows:
    options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    
    # 3. Initialize the driver using Chrome
    # Selenium Manager (in newer versions) will automatically download the matching ChromeDriver
    driver = webdriver.Chrome(options=options)
    
    return driver

def scrape_quotes_selenium():

    data = []
    driver = get_brave_driver()
    driver.get("https://quotes.toscrape.com/js/")

    wait = WebDriverWait(driver, 10)

    while True:

        # --Current page scraping--
        quotes_elements = driver.find_elements(By.CSS_SELECTOR, ".quote")

        for q in quotes_elements:
            text = q.find_element(By.CSS_SELECTOR, ".text").text
            author = q.find_element(By.CSS_SELECTOR, ".author").text
            tags = [t.text for t in q.find_elements(By.CSS_SELECTOR, ".tags")]

            data.append({
                "text": text,
                "author": author,
                "tags": tags
            })

        # --Pagination logic (next button)--
        try:
            load_more_btn = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.pager .next a'))
            )

            load_more_btn.click()

            time.sleep(0.5)

        except TimeoutException:
            print("Alle sider loaded (eller knap ikke fundet).")
            break

    driver.quit()

    print(f"Total quotes found and saved: {len(data)}")

    # --Gemmer til fil-- 
    os.makedirs("outputs", exist_ok=True)
    with open("outputs/quotes_selenium.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    scrape_quotes_selenium()