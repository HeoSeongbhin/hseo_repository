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
    location = soup.find(class_="title")
    위치 = location.text.split(" ")
    weather = soup.find(class_="temperature_text")
    날씨 = weather.text.split(" ")
    info1 = soup.find(class_="temperature_info")
    정보 = info1.text.split(" ")
    
    print("위치:",위치[0],위치[1])
    print(날씨[1],날씨[2])
    if len(날씨)==8:
        print("날씨:",날씨[3],날씨[4],"\n"+"체감온도:",날씨[6])
    elif len(날씨)==7:
        print("날씨:",날씨[3],"\n"+"체감온도:",날씨[5])
    print("현지시간:",정보[3],정보[4])
    if(len(정보)==17):
        print("자외선:",정보[6])
        print("강수량:",정보[10],"\n"+"습도:",정보[12])
        print("풍속:",정보[13],정보[14])
    elif(len(정보)==15):
        print("강수량:",정보[8],"\n"+"습도:",정보[10])
        print("풍속:",정보[11],정보[12])

def Korean_weather():
    location = soup.find(class_="title_area _area_panel") 
    # 특정 클래스를 가진 요소들의 텍스트를 추출
    위치 = location.text.split(" ")
    #  //추출 텍스트를 공백기준으로 나눠 리스트 저장(각각의 변수에 저장)
    weather = soup.find(class_="weather_graphic") 
    날씨 = weather.text.split(" ") 
    atmosphere = soup.find(class_="today_chart_list") 
    대기질 = atmosphere.text.split(" ") 
    info = soup.find(class_="temperature_info") 
    상세정보 = info.text.split(" ")
    
    print("위치:",위치[1],위치[2])
    print("날씨:",날씨[2],"\n"+날씨[5],날씨[6])
    print("대기질:",대기질[3],대기질[4],"/",대기질[9],대기질[10]
    ,"/",대기질[15],대기질[16])
    print("일출:",대기질[22]) 
    print("일교차:",상세정보[1],상세정보[2],상세정보[3],상세정보[4]) 
    print("체감온도:",상세정보[10],"/","습도:",상세정보[14])
    print("풍속:",상세정보[17],상세정보[18])

test = soup.find(class_="provider _provider")
test2 = test.text.split(" ")
if test2[0]=="아큐웨더":
    global_weather()
elif test2[0]=="기상청":
    Korean_weather()
elif test2[0]=="웨더뉴스":
    global_weather()
    
