diem=int(input('Nhap diem: '))
if diem < 0 or diem > 100:
    print('Chi nhan gia tri tu 0 den 100')
elif diem >=90:
    print('Xep loai A')
elif diem >=80:
    print('Xep loai B')
elif diem >=70:
    print('Xep loai C')
elif diem >=65:
    print('Xep loai D')
else:
    print('Xep loai E')


