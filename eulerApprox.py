
def yPrime(x,y):
    return 2 * x * y
x = 1
y = 1
h = .1
inc = 5



def f(n):
    return "{:.4f}".format(n)
print('   x  |   y  |   y\'  ')
for i in range(inc):
    print(f'{f(x)}|{f(y)}|{f(yPrime(x,y))}')
    x+= h;y+= h*yPrime(x,y)

