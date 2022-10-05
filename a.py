sotien=int(input('Nhap so tien: '))
tongsoto=0

to500 = sotien//500
sotien = sotien%500
tongsoto = tongsoto + to500
print('So to 500: ',to500)

print('Tong cong co {} to'.format(tongsoto))