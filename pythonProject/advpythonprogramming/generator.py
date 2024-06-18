def simple_gen():
    yield 1
    yield 2
    yield 3
for value in simple_gen():
    print(value)

#create the object of the generator
def simple_gen():
    yield 1
    yield 2
    yield 3
x=simple_gen()
print(next(x))
print(next(x))
print(next(x))