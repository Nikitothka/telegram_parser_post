import requests
from bs4 import BeautifulSoup as bs
from database import db
import asyncio
from dotenv import load_dotenv


async def main():

    name_categor = 'tech business crypto economics design entertainment marketing news'.split()
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
    }
    url = 'https://tgstat.ru/ratings/channels/'
    url_add = '/public?sort=members'
    cnt_categor = 0
    for i in name_categor:
        cnt_categor += 1
        # print(i)
        url = 'https://tgstat.ru/ratings/channels/'
        url += i + url_add
        r = requests.get(url, headers=headers)
        if (r.status_code) == '200' or '201':
            # print(url)
            s = bs(r.text, 'lxml')

            s = (s.find_all(class_='card-body py-2 position-relative'))
            for j in s:
                for a in j.find_all('a', href=True):
                    channel_name = (str(a['href']).replace('https://tgstat.ru/channel/@', '')).replace('/stat', '')
                    # print(channel_name, cnt_categor)
                    await db.add_channel(channel_name=str(channel_name), category_id=int(cnt_categor))

        else:
            print(r.status_code, 'не записалось')
if __name__=="__main__":
    asyncio.run(main())

