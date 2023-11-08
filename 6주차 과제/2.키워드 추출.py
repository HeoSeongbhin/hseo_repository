from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer #


def load_stopwords(file_path):
    #
    with open(file_path, 'r', encoding='utf-8') as file:
        stopwords = [line.strip() for line in file]
    return stopwords

def extract_korean_keywords(text, stopwords_file, top_n=5):
    # 형태소 분석
    okt = Okt()
    words = okt.morphs(text)

    # 불용어 불러오기
    stop_words = load_stopwords(stopwords_file)

    # 불용어 제거
    words = [word for word in words if word not in stop_words]

    # TF-IDF 벡터화
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([" ".join(words)])

    # TF-IDF 점수를 기반으로 상위 N개의 키워드 선택
    feature_names = vectorizer.get_feature_names_out()
    sorted_items = sorted(enumerate(tfidf_matrix.toarray()[0]), key=lambda x: x[1], reverse=True)
    keywords = [feature_names[idx] for idx, score in sorted_items[:top_n]]

    return keywords

# 텍스트 파일 열기
with open('사회 기사.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 불용어 파일 경로 설정
stopwords_file = '키워드 추출 불용어.txt'

# 상위 7개의 한국어 키워드 추출(top_n=N에서 N개를 바꿀 수 있다.)
top_keywords = extract_korean_keywords(text, stopwords_file, top_n=7)
print(top_keywords)

