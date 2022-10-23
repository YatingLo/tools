"""
grep web novel
https://czbooks.net/n/c542oi
"""

import sys
import os
import re

import requests
from bs4 import BeautifulSoup

def get_infos(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None

    html_doc = r.text
    soup = BeautifulSoup(html_doc, "html.parser")
    title = soup.find("span",class_="title").text
    title = re.sub(r"[《》]","",title)
    urls = []

    table = soup.find(id="chapter-list")
    for h in table.find_all("li"):
        # looking for anchor tag inside the <li>tag
        a = h.find('a')
        try:

            # looking for href inside anchor tag
            if 'href' in a.attrs:
                # storing the value of href in a separate variable
                url = a.get('href')

                # appending the url to the output list
                urls.append(url)
        except:
            pass

    return title, urls

def get_content(chapter_url):
    r = requests.get('http:' + chapter_url)

    if r.status_code != 200:
        return None

    html_doc = r.text
    soup = BeautifulSoup(html_doc, "html.parser")
    title = soup.find('div', class_='name').text
    content = f"\n\n{title}\n" + soup.find('div', class_='content').text

    print(f"...{title} done")

    return content

if __name__ == '__main__':
    URL = sys.argv[1]

    title, chapters = get_infos(URL)

    print(f"{title}共{len(chapters)}章")

    file_name = f"{title}.txt"

    if os.path.exists(file_name):
        os.remove(file_name)

    with open(file_name, "a+") as file_object:
        file_object.write(title)

        for url in chapters:
            content = get_content(url)
            file_object.write(content)
