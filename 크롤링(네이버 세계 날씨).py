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

def global_weather():
    temperature = soup.find(class_="title_area")
    위치 = temperature.text.split(" ")
    if len(위치)==20:
        print("위치:",위치[1])
    elif len(위치)!=20:
        print("위치:",위치[1],위치[2])

    temperature = soup.find(class_="weather_graphic")
    날씨 = temperature.text.split(" ")
    print("날씨:",날씨[2],날씨[3])

    temperature = soup.find(class_="temperature_text")
    현재 = temperature.text.split(" ")

    if len(현재)==8:
        print(현재[1],현재[2],"\n"+현재[5]+":",현재[6])
    elif len(현재)==7:
        print(현재[1],현재[2],"\n"+현재[4]+":",현재[5])

    temperature = soup.find(class_="temperature_info")
    상세 = temperature.text.split(" ")

    if len(상세)==15:
        print(상세[2]+":",상세[3],상세[4],"\n"+상세[7]+":",상세[8])
        print(상세[9]+":",상세[10],"\n"+"풍향:",상세[11],상세[12])
    elif len(상세)==17:
        print(상세[2]+":",상세[3],상세[4],"\n"+상세[5]+":",상세[6])
        print(상세[9]+":",상세[10],"\n"+상세[11]+":",상세[12],"\n"+"풍향:",상세[13],상세[14])

def Korean_weather():
    temperature = soup.find(class_="title_area _area_panel")
    위치 = temperature.text.split(" ")
    print("위치:",위치[1],위치[2])

    temperature = soup.find(class_="weather_graphic")
    날씨 = temperature.text.split(" ")
    
    if len(날씨)==9:
        print("날씨:",날씨[2],"\n"+날씨[5],날씨[6])
    elif len(날씨)==10:
        print("날씨:",날씨[2],날씨[3],"\n"+날씨[6],날씨[7])
    
    temperature = soup.find(class_="today_chart_list")
    대기질 = temperature.text.split(" ")
    print("대기질:",대기질[3],대기질[4],"/",대기질[9],대기질[10],"/",대기질[15],대기질[16],"\n"+대기질[21]+":",대기질[22])

    temperature = soup.find(class_="temperature_info")
    상세정보 = temperature.text.split(" ")
    print("일교차:",상세정보[1],상세정보[2],상세정보[3],상세정보[4],"\n"+상세정보[9]+':',상세정보[10],"/",상세정보[13]+':',상세정보[14],"\n"+상세정보[17],상세정보[18])

test = soup.find(class_="provider _provider")
test2 = test.text.split(" ")
if test2[0]=="아큐웨더":
    global_weather()
elif test2[0]=="기상청":
    Korean_weather()
elif test2[0]=="웨더뉴스":
    global_weather()
    
