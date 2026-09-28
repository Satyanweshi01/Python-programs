#generator function
def genfun():
    print("hello")
    yield 
    print("world")
    yield
h = genfun()
h.__next__()
h.__next__()