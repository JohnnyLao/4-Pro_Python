import bs4
import requests

URL = 'https://habr.com/ru/'
KEYWORDS = {'дизайн', 'фото', 'web', 'python', ''}

response = requests.get(URL)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

articles = soup.find_all('article')
for article in articles:
    l1 = article.find(class_="tm-article-snippet")
    for l2 in l1:
        l3 = l2.find(class_='tm-article-body tm-article-snippet__lead')
        print(l3)
        for l4 in l3:
            ptext = l3.find(class_="article-formatted-body article-formatted-body article-formatted-body_version-2")
            res = set(l4.get_text().strip().split())
            for word in KEYWORDS:
                if word in ptext:
                    href = article.find('h2').find('a').attrs.get('href')
                    title = article.find("h2").find("a").find("span").text
                    date = article.find('time').attrs.get('title')
                    result = f'{date} - {title} --> {URL}{href}'
                    print(result)
