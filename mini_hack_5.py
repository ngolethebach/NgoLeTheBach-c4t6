#n = int(input("What's number:"))
#if n < 13:
    #print("so nay k lon hon 13")
#else:
    #print("so nay lon hon 13")
#n = int(input("Number:"))
#if n%2 == 0:
    #print("n la so chan")
#else:
    #print("n la so le")

n = int(input("Thang ban chon: "))
if 0 < n < 8:
    if n == 2:
        print("so ngay trong thang la: 28 hoac 29")
    elif n%2 == 0:
        print("so ngay trong thang la: 30")
    elif n == 2:
        print("so ngay trong thang la: 28 hoac 29")
    else:
        print("so ngay trong thang la: 31")
elif 8 <= n <13:
    if n%2 == 0:
        print("co 31 ngay")
    else:
        print("co 30 ngay")
else:
    print("nhap lai di")
