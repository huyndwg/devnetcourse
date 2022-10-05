a,b,c=map(int,input('Nhap a, b, c: ').split(','))
if c-b == b-a:
    print('AP sequence. Next number: {}'.format(c+c-b))
elif c/b == b/a:
    print('GP sequence. Next number: {}'.format(c*c/b))
else:
    print('Not AP and GP sequence')

