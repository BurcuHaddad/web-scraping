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

res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")
soup2 = bs4.BeautifulSoup(res.text, "lxml")
#print(soup2.select(".vector-toc-text")[1].text)

deep = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup3 =   bs4.BeautifulSoup(deep.text, "lxml")
computer = soup3.select(".mw-file-element")[1]
print(computer["src"])
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg")
print(image_link.content)
f = open("my_comp_image.jpg", "wb")
f.write(image_link.content)
f.close()