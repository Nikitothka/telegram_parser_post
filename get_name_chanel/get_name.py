import requests
from bs4 import BeautifulSoup as bs
from database import db
import asyncio
from dotenv import load_dotenv
import os

async def main():
    load_dotenv()
    name_categor = 'tech business crypto economics design entertainment marketing news'.split()
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
    }
    url_add = '/public?sort=members'
    cnt_categor = 0
    for i in name_categor:
        cnt_categor += 1
        url = os.getenv("URL_PARSER")
        url += i + url_add
        r = requests.get(url, headers=headers)
        print(r.url)
        if r.status_code == '200' or '201':
            s = bs(r.text, 'lxml')

            s = (s.find_all(class_='card-body py-2 position-relative'))
            for j in s:
                for a in j.find_all('a', href=True):
                    username = (str(a['href']).replace(str(os.getenv("URL_PARSER_LEFT")), '')).replace('/stat', '')
                    await db.add_username_for_channel(username=str(username), category_id=int(cnt_categor))
        else:
            print(r.status_code, 'не записалось')
if __name__=="__main__":
    asyncio.run(main())
    # print('не та прога')

