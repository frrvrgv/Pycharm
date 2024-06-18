def make_pretty(func):
    def inner():
        print("I am decorated")
        func()
    return inner
def ordinary():
    print("I am ordinary")
dec_fun_value=make_pretty(ordinary)
dec_fun_value()