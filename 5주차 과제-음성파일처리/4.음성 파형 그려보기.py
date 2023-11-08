import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

# WAV 파일 경로 설정
file_path = "그대가 분다.wav"

# WAV 파일 읽기
sample_rate, audio_data = wavfile.read(file_path)

# 시간 배열 생성 (초 단위)
time = np.arange(0, len(audio_data)) / sample_rate

# 파형 그리기
plt.figure(figsize=(12, 4))
plt.plot(time, audio_data, lw=0.5)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Waveform of Audio")
plt.grid()

# 그래프 표시
plt.show()
