from scipy.io import wavfile
import numpy as np

# 원본 WAV 파일 로드
input_path = "그대가 분다.wav"
output_path = "path_output.wav"

# 원본 샘플링 속도와 변경할 샘플링 속도 설정
original_sample_rate = 22050
new_sample_rate = 11025

# WAV 파일 읽기
sample_rate, data = wavfile.read(input_path)

# 샘플링 속도 변경
data = data.astype(float)
data = data[::int(original_sample_rate / new_sample_rate)]

# WAV 파일로 저장
wavfile.write(output_path, new_sample_rate, data.astype(np.int16))

print("샘플링 속도가 변경된 WAV 파일이 생성되었습니다.")



