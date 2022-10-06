
# n = int(input('Nhap so: '))
# #so = 1
# sum = 0

# # print('Cac so <= {}:'.format(n),end=' ')
# # while so <= n:
# #     if so%5 == 0:
# #         print(so, end =' ')
# #     so = so + 1

# # while so <= n:
# #     sum = sum + so
# #     so = so + 1
# # print('Tong: {}'.format(sum))

# # while so < n:
# #     if so%2 == 0:
# #         sum = sum + so
# #     so = so + 1
# # print(sum)

# # while so < n:
# #     if n%so == 0 and so%2 == 0:
# #         sum = sum + so
# #     so = so + 1
# # print(sum) 

# so = n-1

# # while so < n:
# #     if so%2 == 0:
# #         print(so)
# #         break
# #     so = so - 1

# # while True:
# #     if n%so == 0 and so%2 != 0:
# #         print(so)
# #         break
# #     so = so - 1


# # so = n//2
# # while not(n%so==0 and so%2!=0):
# #     so=so-1


n=int(input('Nhap n: '))
S=int(input('Nhap S: '))
so=1
tong=0
while so<=n:
    tong=tong+so
    so=so+1
if tong-S==0:
    print('Bo ve du')
else:
    print('So thu tu con bi mat: {}'.format(tong-S))
