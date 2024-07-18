from os import name
import requests
from bs4 import BeautifulSoup
import time

site = "https://unn.ua/politics"


def get_news():
    while True:
        try:
            response = requests.get(site)
            response.raise_for_status()  # Check if the request was successful
            site_view = response.text

            soup = BeautifulSoup(site_view, 'lxml')
            block = soup.find('div', class_="home-page_newsWrapper__TgxkK")
            if block:
                print("ok")
            else:
                print("The specified class was not found on the page.")
            block1 = block.find('div', class_="news-by-category-block_content__r9Xfu")
            blocks = block1.find('a', class_="news-by-category-block_linkItem__Rfn9O")
            lines_main = []
            with open("datenews.txt", "r", encoding="utf-8") as file:
                lines_main = file.readlines()
            temp_lines = []
            href = blocks['href']
            name_stats = blocks.find('span', class_="red-lightning_headerWrap__hqKfp").text
            site_href = "https://unn.ua" + href
            temp_lines.append(name_stats + '\n')
            temp_lines.append(site_href + '\n')
            if lines_main != temp_lines:
                with open("datenews.txt", "w", encoding="utf-8") as file:
                    file.writelines(temp_lines)
                print(name_stats)
                print(site_href)

            time.sleep(60)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while trying to fetch the page: {e}")
            break
