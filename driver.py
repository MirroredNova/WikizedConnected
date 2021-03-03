from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page import Page

import config
import graph



def setup_driver():
    chromedriver = 'C:\\Users\\aneth\\Desktop\\PycharmWorkspace\\webdrivers\\chromedriver.exe'
    options = Options()
    return webdriver.Chrome(executable_path=chromedriver, options=options)


def get_links(driver, page):
    driver.get(page)
    raw_links = driver.find_elements_by_xpath("//a[contains(@href, '/wiki/')]")
    links = []
    for link in raw_links:
        href = link.get_attribute("href")
        if 'en.wikipedia.org' not in href:
            continue
        if any(ext in href for ext in config.blacklist_link_words):
            continue
        if href not in links:
            links.append(href)

    for link in links:
        print(link)


def create_page():
    page = Page()


def main():
    driver = setup_driver()
    get_links(driver, config.base_url)
    driver.close()


main()
