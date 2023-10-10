from PIL import Image



# 고양이 이미지 불러와서 img라는 변수에 입력
img = Image.open('cat.jpg')

# 이미지 보여주기
img.show()

# 이미지 파일명
print(img.filename)

# 이미지 형식
print(img.format)

# 이미지 크기
print(img.size)


# 이미지 너비
print(img.width)

# 이미지 높이
print(img.height)

# 이미지의 색상 모드
print(img.mode)

# 이미지 사이즈 변경
img_resized = img.resize((400,300))

# 변경한 이미지 출력
img_resized.show()

# 이미지 자르기
img_cropped = img.crop((70,50,300,300))

# 잘라낸 이미지 출력
img_cropped.show()

# 이미지 180도 회전
img_rotated = img.rotate(180)

# 회전한 이미지 출력
img_rotated.show()

# 상하대칭
img_flipped_TB = img.transpose(Image.FLIP_TOP_BOTTOM)
img_flipped_TB.show()

# 좌우대칭
img_flipped_LR = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipped_LR.show()


# 상하반전한 이미지 저장
#img_flipped_TB.save('cat_flip.jpg')

# RGB로 표현된 컬러 이미지를 흑백으로 변경
img_gray = img.convert("L")

# 흑백으로 변환된 이미지 출력
img_gray.show()

from PIL import ImageFilter

img_edge = img.filter(ImageFilter.EDGE_ENHANCE)

img_edge.show()