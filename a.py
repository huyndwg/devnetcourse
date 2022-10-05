n = int(input('Nhap so: '))
#so = 1
sum = 0

# print('Cac so <= {}:'.format(n),end=' ')
# while so <= n:
#     if so%5 == 0:
#         print(so, end =' ')
#     so = so + 1

# while so <= n:
#     sum = sum + so
#     so = so + 1
# print('Tong: {}'.format(sum))

# while so < n:
#     if so%2 == 0:
#         sum = sum + so
#     so = so + 1
# print(sum)

# while so < n:
#     if n%so == 0 and so%2 == 0:
#         sum = sum + so
#     so = so + 1
# print(sum) 

so = n-1
# maxchan = 0
# while so < n:
#     if so%2 == 0:
#         maxchan = so
#         break
#     so = so - 1
# print(maxchan)

maxle = 1
while so < n:
    if n%so == 0 and so%2 ==1:
        maxle = so
        break
    so = so - 1
print(maxle)