#1.Write a  Python program that creates a generator function that yields cubes of numbers from 1 to n
def Cube(n):
    for value in range(1,n):
        yield value**3
for value in Cube(10):
    print(value)