import requests
from bs4 import BeautifulSoup
from datetime import datetime
from pprint import pprint
import time
import json
import os
from dotenv import load_dotenv

load_dotenv()


def get_first_news():
    headers = {
        'user-agent': os.getenv('USER_AGENT')
    }
    url = os.getenv('URL')
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    article_cards = soup.find_all('a', class_='article-card')


def main():
    get_first_news()


if __name__ == '__main__':
    main()
