import numpy as np
import scipy.io.wavfile as wav

# WAV 파일 경로 설정
input_file = "그대가 분다.wav"
output_file = "cut_output.wav"

# 시작 시간과 종료 시간 설정 (초 단위)
start_time = 78.5  # 시작 시간 (예: 5초)
end_time = 110.0  # 종료 시간 (예: 10초)

# WAV 파일 읽기
sample_rate, audio_data = wav.read(input_file)

# 시작 및 종료 샘플 인덱스 계산
start_sample = int(start_time * sample_rate)
end_sample = int(end_time * sample_rate)

# 오디오 데이터에서 잘라내기
cut_audio_data = audio_data[start_sample:end_sample]

# WAV 파일로 저장
wav.write(output_file, sample_rate, cut_audio_data)

print(f"오디오 파일이 {start_time}부터 {end_time}까지 잘라내어 {output_file}로 저장되었습니다.")
