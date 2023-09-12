from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
 
# 검색
text = input(">>")
change = quote(text, encoding="utf-8")
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query="
url += change
html = urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

temperature = soup.find(class_="title_area _area_panel")
위치 = temperature.text.split(" ")
print("위치:",위치[1],위치[2])

temperature = soup.find(class_="weather_graphic")
날씨 = temperature.text.split(" ")
print("날씨:",날씨[2],"\n"+날씨[5],날씨[6])

temperature = soup.find(class_="today_chart_list")
대기질 = temperature.text.split(" ")
print("대기질:",대기질[3],대기질[4],"/",대기질[9],대기질[10],"/",대기질[15],대기질[16],"\n"+대기질[21]+":",대기질[22])

temperature = soup.find(class_="temperature_info")
상세정보 = temperature.text.split(" ")
print("일교차:",상세정보[1],상세정보[2],상세정보[3],상세정보[4],"\n"+상세정보[9]+':',상세정보[10],"/",상세정보[13]+':',상세정보[14],"\n"+상세정보[17],상세정보[18])