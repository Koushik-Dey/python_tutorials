# def double(x):
#     return x *2

def double(x): return x*2


def cube(x): return x*x*x


def avg(x, y): return (x + y)/2


def apply(fx, value):
    return 6 + fx(value)


print(double(5))
print(avg(3, 4))
print(apply(cube, 5))
