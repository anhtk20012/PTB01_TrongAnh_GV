#print("Em tên là:", "Ánh", sep="-", end=" ")
#print("Tuổi: 25")

'''
a = 4
b = "Trọng Ánh"
c = True

print(type(a))
print(type(b))
print(type(c))
'''

'''
Ten = input("Tên bạn là gì: ")
Ten_dem = input("Phần tên đệm: ")
Ho = input("Họ của bạn là gì: ")
print("Họ tên đầy đủ của bạn là:",Ho, Ten_dem, Ten)
'''

'''
n = int(float(input("Nhập n là số nguyên: ")))
# 2.7
print("HiHiHi"*3)
'''

#print("Lã " + "Ánh" - "Ánh")

dola = 1500
vnd = 35205000
kq1 = vnd/dola
print("Số tiền VND của 1$ là: " + str(kq1) + "VND")

tqd = float(input("Số đô la cần quy đổi: "))
kq2 = tqd * kq1
print("Số tiền VND của "+ str(tqd) +" đô la: " + str(kq2))

mot_t = 1340233
tien_t = 367329673
kq3_1 = tien_t//mot_t
print("Số tháng kiếm được hơn 367.329.673 VND là: " + str(kq3_1 + 1) + " tháng.")
kq3_2 = ((kq3_1 + 1) * mot_t)/kq1
print("Số đô la của tháng hơn đó là: " + str(kq3_2) + "$")