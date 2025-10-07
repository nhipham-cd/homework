# #for i in range (start =0 , stop, step=1)
# range(stop): lap tu 0 den stop-1
# range (start, stop): lap tu start den stop-1, buoc=step=1
# range(start,stop,step): lap tu start den stop-1, buoc=step

# for i in range (91): i=0,1,2,...,90
# for i in range (2,10): i= 2, 3,4,5,...,9
# for i in range (2,100,2): i=2,4,6,...,98

# for_in range (10): so lan lap #10 lan lap, an i


#W4A1
#dùng for hoặc while để tính tổng các số nguyên từ 1 đến n (n<=1000)
n = int(input())
S=0 #bien luu tru
for i in range (1, n+1):
  print (i, end=' ')
  S+=i #S=S+i
print ("\n", S)


#W4A2
#Viết chương trình nhập vào một số tới khi được một số nguyên dương thì thôi.
#Kiểm tra số này có phải là số nguyên tố hay không?
import math
n = 0
for _ in range (1000):
  try:
    n = int(input('nhap vao mot so nguyen duong? '))
    if n > 0:
      break  # break= ngắt, nhánh này đạt đến thì for dừng tại đây
    else:
      print("ban phai nhap so nguyen duong de TIEP TUC") # Đã sửa lại thông báo cho rõ nghĩa hơn
  except ValueError:
    print("ban nhap du lieu sai, hay nhap lai")

print("so nguyen duong nhap duoc la:", n)
#continue: nhánh này đạt đến thì bỏ qua tất những gì phía sau continue

#so nguyen to: 2,3,5,7,... chia het cho 1 va chinh no
flag = True
# Kiểm tra các trường hợp đặc biệt của số nguyên tố
if n < 2:
    flag = False
elif n == 2:
    flag = True
else:
    # Chỉ kiểm tra các ước số từ 2 đến căn bậc hai của n
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i == 0):
            flag = False
            break

if flag:
    print(n, "la so nguyen to")
else:
    print(n, "khong phai la so nguyen to")

#28: 1 2 4 7 14 28
#n=a*b a<b <=b  -> a*a<=n
#a<= sqrt(n)


#W4A3
#Viết chương trình tính giai thừa của một số nguyên n cho trước (n!=1×2×…×n)
#với 0 < n < 100
try:
  n=int(input())
  giaithua=1
  for i in range (1,n+1):
    giaithua = giaithua * i
  print (giaithua)
except ValueError:
  print("ban nhap sai du lieu")


#W4A4
#Viết chương trình nhập vào một số nguyên n và in ra màn hình số chữ số (trừ dấu)
#của số đó. Không dùng kiểu dữ liệu string
n = 0
try:
  n = int(input())
  n = abs(n)
  count = 0
  if n==0:
    count = 1
  for _ in range (10000):
    if n > 0:
      count += 1
      n//= 10 #chia lay nguyen
    else:
      break
  print (count)
except ValueError:
  print('ban nhap sai du lieu')


#W4A5
#Hãy viết một chương trình nhận vào một số nguyên dương n và một dãy gồm n số
#nguyên. Nếu n số nguyên đó có số 42 thì in ra màn hình dòng chữ "I′ve found the
#meaning of life!", ngược lại in ra dòng chữ "It′s a joke!"
try:
  n = int(input())
  flag = False
  for _ in range (n):
    a = int(input())
    if a==42:
      print ("I've found the meaning of life!")
      flag = True
      break
  if flag==False:
    print ('It s a joke!')
except ValueError:
  print('Du lieu khong hop le')


#W4A11
#Viết chương trình đếm số lượng ước số chẵn của số nguyên dương n với n < 10**6
n = int(input(""))
dem = 1 if n%2==0 else 0
for i in range (2,n//2+1,2):
  if n%i == 0:
    print (i, end=" ")
    dem += 1
print (dem)


#w4A12
#Một người có tài khoản tiết kiệm ở ngân hàng và gửi vào X đồng với lãi suất là
#0.7% mỗi tháng. Viết chương trình tính số tiền sau N tháng người ấy rút được (cả
#gốc và lãi, bỏ qua phần lẻ thập phân)
x = int(input("Nhap so tien gui: "))
n = int(input("So thang muon gui: "))
for _ in range (n):
  x = x*1.007
print (round(x))


#W4A13
try:
  a = int(input())
  b = int(input())
  tong_uoc_a = 0
  for i in range (1,a//2+1):
    if a%i == 0:
      tong_uoc_a += i
  tong_uoc_b = 0
  for i in range (1,b//2+1):
    if b%i == 0:
      tong_uoc_b += i
  if tong_uoc_a == b and tong_uoc_b == a:
    print("True")
  else:
    print("False")
except ValueError:
  print("Du lieu khong hop le")


#W4A13
try:
  a = int(input())
  b = int(input())
  tong_uoc_a = 0
  for i in range (1,a//2+1):
    if a%i == 0:
      tong_uoc_a += i
  tong_uoc_b = 0
  for i in range (1,b//2+1):
    if b%i == 0:
      tong_uoc_b += i
  print(tong_uoc_a == b and tong_uoc_b == a)

except ValueError:
  print("Du lieu khong hop le")


#W4A14