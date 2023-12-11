from PIL import Image, ImageFilter

# 이미지 열기
image = Image.open('C:\\Users\\user\\Desktop\\cookie_cat.jpg')

# 1.이미지 크기 변경
width, height = image.size
new_width = width // 2
new_height = height // 2
resized_image = image.resize((new_width, new_height))

# 2.이미지 자르기
box = (60, 350, 1050, 950)
cropped_image = image.crop(box)

# 3.이미지 회전
angle = 90
rotated_image = image.rotate(angle)

# 4.이미지 상하 대칭 적용
flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)

# 5.이미지 상하 및 좌우 대칭 적용
flipped_image = flipped_image.transpose(Image.FLIP_LEFT_RIGHT)

# 6.이미지 필터 적용 (예: 블러)
filtered_image = image.filter(ImageFilter.GaussianBlur)

# 7.이미지 합치기
    # 병합할 이미지 파일 설정
image_paths = ['filtered_cookie_cat.jpg', 'flipped_top_bottom_left_right_cookie_cat.jpg', 'rotated_cookie_cat.jpg', 'resized_cookie_cat.jpg', 'cropped_cookie_cat.jpg']
    # 이미지 열기
images = [Image.open(path) for path in image_paths]
   # 이미지 크기 얻기
widths, heights = zip(*(image.size for image in images))
    # 총 이미지 너비와 높이 계산
total_width = sum(widths)
max_height = max(heights)
    # 새로운 이미지 생성
merged_image = Image.new('RGB', (total_width, max_height))
    # 이미지 병합
x_offset = 0
for image in images:
    merged_image.paste(image, (x_offset, 0))
    x_offset += image.width

# 크기 변경 이미지 저장
resized_image.save('resized_cookie_cat.jpg')

# 자른 이미지 저장
cropped_image.save('cropped_cookie_cat.jpg')

# 회전 이미지 저장
rotated_image.save('rotated_cookie_cat.jpg')

# 대칭 이미지 저장
flipped_image.save('flipped_top_bottom_left_right_cookie_cat.jpg')

# 필터 적용 이미지 저장
filtered_image.save('filtered_cookie_cat.jpg')

# 병합된 이미지 저장
merged_image.save('merged_image.jpg')


# 이미지 닫기
image.close()           #기본 이미지
resized_image.close()   #크기 변경 이미지
cropped_image.close()   #자른 이미지
rotated_image.close()   #회전 이미지
flipped_image.close()   #대칭 이미지
filtered_image.close()  #필터 적용 이미지
for image in images:
    image.close()   
merged_image.close()    #병합된 이미지
