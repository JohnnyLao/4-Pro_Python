import bs4
import requests


def start(URL, words):
    response = requests.get(URL)
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    for article in articles:
        preview = article.get_text().split()
        for word in words:
            if word in preview:
                href = article.find('h2').find('a').attrs.get('href')
                title = article.find("h2").find("a").find("span").text
                date = article.find('time').attrs.get('title')
                result = f'{date} --> {title} {URL}{href}'
                print(result)


if __name__ == '__main__':
    URL = 'https://habr.com/ru/'
    KEYWORDS = {'дизайн', 'фото', 'web', 'python','Как','как' }
    start(URL, KEYWORDS)