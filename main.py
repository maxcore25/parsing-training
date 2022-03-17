import time
from selenium.webdriver.common.keys import Keys
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv

load_dotenv()


def use_bs():
    headers = {
        'user-agent': os.getenv('USER_AGENT')
    }
    url = os.getenv('URL')
    r = requests.get(url, headers=headers)
    # soup = BeautifulSoup(r.text, 'lxml')
    # article_cards = soup.find_all('a', class_='article-card')


def use_selenium():
    # driver = webdriver.Chrome(ChromeDriverManager().install())
    browser = webdriver.Chrome()
    browser.get(os.getenv('URL'))

    xpath = '/html/body/div[13]/div[2]/div/div/div/div/a[1]'
    browser.find_element(by=By.XPATH, value=xpath).click()
    time.sleep(3)


def main():
    # use_bs()
    use_selenium()


if __name__ == '__main__':
    main()
