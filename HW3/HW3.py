import bs4
import requests

URL = "https://habr.com/"

response = requests.get(URL)
# print(response)
text = response.text
# print(text)


soup = bs4.BeautifulSoup(text, features="html.parser")

ip_ad = soup.find(id="d_clip_button").find("span")
print(ip_ad.text)