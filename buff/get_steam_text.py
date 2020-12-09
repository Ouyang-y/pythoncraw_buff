from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_steam_text(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    steam_text = driver.find_element_by_xpath("//pre").text
    driver.close()
    return steam_text
