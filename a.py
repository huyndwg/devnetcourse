sotien = int(input("Nhap so tien: ")) #1234

tongsoto = 0
to500 = sotien//500 #=2
sotien = sotien%500 #sotien = 234
tongsoto = tongsoto + to500 # tongso=2
if to500 > 0:
    print('so to 500: ',to500)

to200 = sotien//200 #=2
sotien = sotien%200 #sotien = 234
tongsoto = tongsoto + to200 # tongso=2
if to200 > 0:
    print("so to 200: ", to200)

to100= sotien//100 #=2
sotien = sotien%100 #sotien = 234
tongsoto = tongsoto + to100# tongso=2
if to100 > 0:
    print("so to 100: ", to100)

to50 = sotien//50 #=2
sotien = sotien%50 #sotien = 234
tongsoto = tongsoto + to50 # tongso=2
if to50 > 0:
    print("so to 50: ", to50)

to20 = sotien//20 #=2
sotien = sotien%20 #sotien = 234
tongsoto = tongsoto + to20 # tongso=2
if to20 > 0:
    print("so to 20: ", to20)

to10 = sotien//10 #=2
sotien = sotien%10 #sotien = 234
tongsoto = tongsoto + to10 # tongso=2
if to10 > 0:
    print("so to 10: ", to10)

to5 = sotien//5 #=2
sotien = sotien%5 #sotien = 234
tongsoto = tongsoto + to5 # tongso=2
if to5 > 0:
    print("so to 5: ", to5)

to2 = sotien//2 #=2
sotien = sotien%2 #sotien = 234
tongsoto = tongsoto + to2
if to2 > 0:
    print("so to 2: ", to2)


to1 = sotien//1
tongsoto = tongsoto + to1
if to1 > 0:
    print("so to 1: ", to1)

print(f'Tong cong co {tongsoto} to ')