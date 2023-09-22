from soynlp.normalizer import *
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import re

# 정규화
korea_text = repeat_normalize(
    "Python은 놀라운 프로그래밍 Python언어입니다. 데이터 Python분석, 웹 개발, 인공지능 등 Python다양한 분야에서 사용됩니다. Python은 간결하고 읽기 쉬운 코드를 작성하는 데 도움이 됩니다.",
    num_repeats=1,
)

# 토큰화
from konlpy.tag import Okt,Kkma, Komoran
tokenizer = Okt()
token=tokenizer.morphs(korea_text)
print(token)

# 불용어처리
stop_words=['은','놀라운','입니다','등','다양한','에서','됩니다','은','하고','읽기','쉬운','를','하는','데','이','됩니다','.',',',',','.','.']

result=[]
for word in token:
    if word not in stop_words:
        result.append(word)

print(result)
list=' '.join(result)

# 워드 클라우드     
from PIL import Image
import numpy as np
im = Image.open('heart.png')
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
).generate(list) 

# 이미지
plt.figure(figsize=(5,5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()