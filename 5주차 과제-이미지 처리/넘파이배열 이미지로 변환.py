from PIL import Image
import numpy as np

# 넘파이 배열 생성 (예시: 파란색 이미지)
width, height = 200, 200
blue_pixels = np.zeros((height, width, 3), dtype=np.uint8)
blue_pixels[:, :, 2] = 255  # 파란 색 채널 설정

# 넘파이 배열을 이미지로 변환
image = Image.fromarray(blue_pixels)

# 이미지 저장
image.save('numpy_to_image.jpg')
