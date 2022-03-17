import requests
from selenium import webdriver
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
    browser = webdriver.Chrome()
    browser.get(os.getenv('URL'))

    xpath = '/html/body/div[1]/div[1]/div[1]/dl/dd/div[7]/div[1]/div/button'
    browser.find_element_by_xpath(xpath).click()


def main():
    # use_bs()
    use_selenium()


if __name__ == '__main__':
    main()
