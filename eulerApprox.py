def yPrime(x,y):
    return x**2+y**2
x = 0
y = 1
h = .05
inc = 10




def f(n):
    return "{:.4f}".format(n)
print('   x  |   y  |   y\'  ')
for i in range(inc+1):
    print(f'{f(x)}|{f(y)}|{f(yPrime(x,y))}')
    y+= h*yPrime(x,y)
    x+= h

