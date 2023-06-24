'''n = int(input("Nhập N = "))
# Điều kiện dạng khuyết
if (n % 2 == 0):
    print("N là số chẵn.")

# Điều kiện dạng đủ
if (n % 2 == 1):
    print("N là số lẻ.")
else:
    print("N là số chẵn.")'''

import random

qua = random.randint(1,4)
if (qua == 1):
    print("Bỏ vào giỏ A.")
elif (qua == 2):
    print("Bỏ vào giỏ B.")
elif (qua == 2):
    print("Bỏ vào giỏ C.")
else:
    print("Bỏ vào giỏ D.")