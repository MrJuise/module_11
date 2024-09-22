import requests
from PIL import Image



page = requests.get("https://google.com")


print(f'код ответа: {page.status_code}\n')
print(f'страница в HTML:\n {page.content}\n')
print(f'раскодированные данные страницы в текст: \n{page.text}\n')
# -------------------------------------------------------------------------------

img = Image.open('img_1.png')
print(img.__dict__)
print(img.format)
print(img.size)
print(img.mode)
img = img.rotate(45)
img = img.resize((800, 600))
img.save("D:/Python/pythonProject/new_img.png")
img.show()
