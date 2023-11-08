from PIL import Image
import io

# 이미지 열기
image = Image.open('merged_image.jpg')

# 이미지를 바이트 버퍼에 저장
buffer = io.BytesIO()
image.save(buffer,format="JPEG")

# 바이트 버퍼를 바이트 배열로 변환
image_bytes = buffer.getvalue()

# 변환 이미지 저장
with open('image_bytes.jpg', 'wb') as file:
    file.write(image_bytes)
    
# 이미지 닫기 (꼭 닫는 것이 좋음)
image.close()


