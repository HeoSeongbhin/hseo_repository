import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# WAV 파일 경로 설정
file_path = "그대가 분다.wav"

# WAV 파일 읽기
sample_rate, audio_data = wavfile.read(file_path)

# 첫 번째 채널 데이터 추출
audio_data_channel_1 = audio_data[:, 0]

# 프리에 변환 수행 (첫 번째 채널)
fft_result = np.fft.fft(audio_data_channel_1)
magnitude = np.abs(fft_result)

# 시간 배열 생성 (초 단위)
time = np.arange(0, len(audio_data_channel_1)) / sample_rate

# 스펙트로그램 생성 (첫 번째 채널)
plt.figure(figsize=(12, 6))
plt.specgram(audio_data_channel_1, Fs=sample_rate, NFFT=1024, noverlap=512, cmap="viridis")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.title("Spectrogram of Audio (Channel 1)")

# 그래프 표시
plt.show()


