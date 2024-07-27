def yPrime(x,y):
    return x
x = 0
y = 1
h = .1
inc = 40




def f(n):
    return "{:.4f}".format(n)
print('   x  |   y  |   y\'  ')
for i in range(inc+1):
    print(f'{f(x)}|{f(y)}|{f(yPrime(x,y))}')
    y_S=y + h*yPrime(x,y)
    y+= h * ((yPrime(x,y) + yPrime(x+h,y_S)))
    x+= h

