def reverse_string(func):
    def inner():
        x=func()
        return x[::-1]
    return inner
@reverse_string
def text():
    return "sowmitha here"
print(text())