def greet(func):
    def mfunc(*args, **kwargs):
        print("Good Morning")
        func(*args, **kwargs)
        print("Thanks for using this funcction")
    return mfunc


@greet
def hello():
    print("Hello world")


@greet
def add(a, b):
    print(a+b)


hello()
add(1, 2)
