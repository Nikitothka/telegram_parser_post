import requests
from bs4 import BeautifulSoup as bs

if __name__=='__main__':
    name_categor = 'tech business crypto economics design entertainment marketing news'.split()
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15"
    }
    url = 'https://tgstat.ru/ratings/channels/'
    url_add = '/public?sort=members'

    for i in name_categor:
        url = 'https://tgstat.ru/ratings/channels/'
        url += i + url_add
        r = requests.get(url, headers=headers)
        if (r.status_code) == '200'or '201':
            print(url)
            s = bs(r.text, 'lxml')

            s = (s.find_all(class_='card-body py-2 position-relative'))
            for j in s:
                for a in j.find_all('a', href=True):
                    print((str(a['href']).replace('https://tgstat.ru/channel/', '')).replace('/stat', ''),i)
            break

        else:
            print(r.status_code,'не записалось')
