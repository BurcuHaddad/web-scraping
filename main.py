import requests
import bs4

result = requests.get("https://example.com")
#print(type(result))
#print(result.text)
soup = bs4.BeautifulSoup(result.text, "lxml")
print("------------------------")
#print(soup)
print(soup.select("title")[0].getText())
print(soup.select("p")[0].getText())