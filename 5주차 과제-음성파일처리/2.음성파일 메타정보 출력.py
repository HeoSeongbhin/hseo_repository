from mutagen.mp3 import MP3

# 오디오 파일 로드
audio = MP3("그대가 분다.mp3")

# 샘플링 속도 (샘플/초)
sample_rate = audio.info.sample_rate
print(f"샘플링 속도: {sample_rate} 샘플/초")

# 오디오 길이 (초)
duration_in_sec = audio.info.length
print(f"오디오 길이: {duration_in_sec} 초")

# 채널 수 (모노 또는 스테레오)
channels = audio.info.channels
if channels == 1:
    print("채널: 모노")
elif channels == 2:
    print("채널: 스테레오")
else:
    print(f"채널: {channels}")
