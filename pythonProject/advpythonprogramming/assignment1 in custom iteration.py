class PowerOfTwo:
    def __init__(self,num):
        self.num=num
    def next_(self):
        self.num**=2
        return self.num
p=PowerOfTwo(5)
print(p.next_())
print(p.next_())
print(p.next_())
print(p.next_())
print(p.next_())