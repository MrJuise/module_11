import requests

page = requests.get("https://google.com")
print(f'код ответа: {page.status_code}\n')
print(f'страница в HTML:\n {page.content}\n')
print(f'раскодированные данные страницы в текст: \n{page.text}\n')
# -------------------------------------------------------------------------------

from PIL import Image

img = Image.open('img_1.png')
print(img.__dict__)
print(img.format)
print(img.size)
print(img.mode)
img = img.rotate(45)
img = img.resize((800, 600))
img.save("D:/Python/pythonProject/new_img.png")
img.show()
#----------------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 10)
y = x ** 2
plt.figure()
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Name schedule')
plt.show()

