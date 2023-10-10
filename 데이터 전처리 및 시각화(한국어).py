from soynlp.normalizer import repeat_normalize
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from wordcloud import WordCloud
import re
from urllib.parse import quote
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request

def fetch_titles(query):
    # 기사 헤드라인 정보 요소들
    change = quote(query, encoding="utf-8")
    url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={change}"

    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    html_class = soup.find_all(class_="news_tit")
    
    return [tit.text.strip() for tit in html_class]

def normalize_and_tokenize(titles):
    # 정규화
    normalized_titles = [repeat_normalize(title, num_repeats=1) for title in titles]
    
    # 토큰화
    okt = Okt()
    tokens = [okt.morphs(title) for title in normalized_titles]
    
    return tokens

def remove_stopwords(tokens):
    #파일 불러오기(한국어 불용어 리스트 txt파일)
    stop_words_file_path = "C:\\Users\\user\\Downloads\\stopword (1).txt"  
    with open(stop_words_file_path, "r", encoding="utf-8") as file:
        stop_words = set(file.read().split('\n'))

    # 불용어 제외
    filtered_tokens = [[word for word in token if word not in stop_words] for token in tokens]
    
    return filtered_tokens

def main():
    #검색결과 전처리전 헤드라인들 출력 후 다른 함수들 호출 후 전처리 결과 출력
    query = input("검색어를 입력하세요: ")
    
    titles = fetch_titles(query)
    print("검색 결과:")
    for idx, title in enumerate(titles):
        print(f"{idx + 1}. {title}")

    tokens = normalize_and_tokenize(titles)
    filtered_tokens = remove_stopwords(tokens)

    print("\n불용어 제외한 토큰:")
    text_for_wordcloud = ' '.join([' '.join(token) for token in filtered_tokens])
    print(text_for_wordcloud)
    
    # 워드 클라우드     
    from PIL import Image
    import numpy as np
    im = Image.open('C:\\Users\\user\\Desktop\\heart.png')
    mask_arr = np.array(im)
    wordcloud = WordCloud(
        font_path="C:/Windows/Fonts/Malgun.ttf",
        background_color="white",
        colormap='autumn',
        width=700,
        height=800,
        random_state = 43,
        mask = mask_arr,
        prefer_horizontal = True
    ).generate(text_for_wordcloud) 

    # 이미지
    plt.figure(figsize=(5,5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

#데이터 전처리 후 시각화 실행
if __name__ == "__main__":
    main()