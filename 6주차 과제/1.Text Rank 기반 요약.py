import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.cluster.util import cosine_distance
import numpy as np

# nltk 라이브러리의 필요한 데이터를 다운로드
nltk.download('punkt')
nltk.download('stopwords')

# 문장 간의 유사도를 계산하는 함수
def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []  # 불용어 목록이 제공되지 않으면 빈 리스트로 초기화
    sent1 = [word.lower() for word in sent1]  # 모든 단어를 소문자로 변환
    sent2 = [word.lower() for word in sent2]
    all_words = list(set(sent1 + sent2))  # 두 문장에서 모든 고유한 단어를 모아서 리스트를 생성
    vector1 = [0] * len(all_words)  # 각 문장의 단어 벡터를 초기화
    vector2 = [0] * len(all_words)
    for w in sent1:
        if w not in stopwords:
            vector1[all_words.index(w)] += 1  # 단어의 출현 횟수를 증가
    for w in sent2:
        if w not in stopwords:
            vector2[all_words.index(w)] += 1
    return 1 - cosine_distance(vector1, vector2)  # 코사인 거리를 계산하여 두 문장의 유사도를 반환

# 문장 간의 유사도 행렬을 생성하는 함수
def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))  # 모든 요소를 0으로 초기화한 유사도 행렬을 생성
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j], stop_words)  # 문장 유사도를 계산하고 행렬에 저장
    return similarity_matrix  # 유사도 행렬을 반환

# 텍스트를 요약하는 함수(top_n=N, N:문장 개수)
def generate_summary(text, top_n=5):
    stop_words = set(stopwords.words('english'))  # 영어 불용어 목록을 불러오기(한글 출력도 가능)
    sentences = sent_tokenize(text)  # 입력 텍스트를 문장으로 분할
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)  # 문장 간의 유사도 행렬을 생성
    scores = np.array([sum(sentence_similarity_matrix[i]) for i in range(len(sentences))])  # 각 문장의 유사도 합을 계산
    ranked_sentences = [sentences[i] for i in scores.argsort()[-top_n:]]  # 상위 N개의 중요한 문장을 선택
    return ' '.join(ranked_sentences)  # 선택된 문장을 결합하여 요약을 생성하고 반환

# 텍스트 데이터 로드
# 텍스트 파일 열기
with open('사회 기사.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 요약 생성
summary = generate_summary(text)  # 텍스트를 요약
print(summary)  # 요약된 텍스트를 출력
