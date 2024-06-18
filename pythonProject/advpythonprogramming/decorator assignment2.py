def divide (func):
    def inner(x,y):
        return x // y
    return inner
@divide
def num(x, y):
    return x//y
print(num)