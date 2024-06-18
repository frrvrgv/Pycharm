#filter
#even & odd
n=[10,20,30,40,50,60,70,80,90,7,9,99,5,33]
even=list(filter(lambda n : n%2==0, n))
odd=list(filter(lambda n : n%2!=0, n))
print(even)
print(odd)

#divisible by 4
n=[10,20,30,40,50,60,70,80,90,12,4,32,5,44]
div=list(filter(lambda n : n%4==0, n))
print(div)

#age>18
n=[10,20,30,40,50,60,70,80,90,7,9,99,5,33]
age=list(filter(lambda n : n>18, n))
print(age)

#maps
#power of 2
l=[10,20,30,40,50]
powerOfTwo=list(map(lambda x : x**2,l))
print(powerOfTwo)

#div by 10
l=[18,20,30,40,80,36,90,198]
div=list(map(lambda x : x/10,l))
print(div)