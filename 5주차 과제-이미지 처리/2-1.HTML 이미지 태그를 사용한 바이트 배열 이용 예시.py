from PIL import Image
import io
import base64

# 이미지 열기
image = Image.open('merged_image.jpg')

# 이미지를 바이트 버퍼에 저장
buffer = io.BytesIO()
image.save(buffer, format="JPEG")

# 바이트 버퍼를 바이트 배열로 변환
image_bytes = buffer.getvalue()

# 이미지 닫기
image.close()

# 바이트 배열을 HTML 파일에 포함하여 저장
with open('image_display.html', 'w') as html_file:
    html_file.write('<html><body>')
    html_file.write('<img src="data:image/jpeg;base64,' + base64.b64encode(image_bytes).decode() + '">')
    html_file.write('</body></html>')

#이제 file:///C:/Users/user/image_display.html 를 웹페이지에 입력하여 
# 접속하면 내가 이미지 처리에서 최종적으로 병합한 이미지가 나오게 된다.

