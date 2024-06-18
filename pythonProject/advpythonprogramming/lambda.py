def add(a, b):
    result=a+b
    return result
print(add(6,7))

#using lambda
#eg 1
add=lambda a,b: a+b
print(add(6,7))

#eg 2
add=lambda x : x*100
print(add(50))

#eg 3
product=lambda x,y,z:x*y*z
print(product(x=5,y=6,z=9))

#pass arguments in the lambda functions
addition=lambda *args:sum(args)
print(addition(20,4,6,7,7,7,7))

#conditional ifs
(lambda x : (x%2 and "even" or "odd"))(150)

#filters

#reduce

#maps

#filter the string
sub_string=lambda string : string in "Welcome to python programming"
print(sub_string)

#filter in list
num=[10,20,30,40,50,60,70]
greater=list(filter(lambda num : num>30, num))
print(greater)

#maps
list1=[10,40,60,80,100,120,200,300]
double=list(map(lambda x : x*2,list1))
print(double)

#maps example
list(map(lambda var : var*2 , range(0,10)))
#[2,4,6,8,10,12,14,16,18,20]

#map executes all the conditions of a function on the items in the iterable objects
#filter
list(filter(lambda var : var%2 == 0,range(0,10)))
#[0 2 4 6 8]

#reduce
from functools import reduce
list2 = [2,3,4,5,6,7,8,9,]
sum = reduce((lambda x, y : x+y), list2)
print(sum)