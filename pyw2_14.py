ttl=int(input('Nhap so tien: '))
type=[500,200,100,50,20,10,5,2,1]
sum = 0
print('So tien {} se duoc doi thanh:'.format(ttl))
for i in type:
    print('Loai {} gom {} to'.format(i,ttl//i))
    sum = sum + ttl//i
    ttl = ttl%i
print('TONG CONG CO {} TO'.format(sum))