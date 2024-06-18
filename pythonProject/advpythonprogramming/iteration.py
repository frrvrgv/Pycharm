#iteration with iter() to initalize the list and next method to iterate among the objects
list=[2,45,67,7]
#iteration with iter() to initialize the list
my_iter=iter(list)
print(next(my_iter))
print(next(my_iter))
print(my_iter.__next__())
print(my_iter.__next__())

#iteration among strings
iterable_value=("Helloworld")
iterable_obj=iter(iterable_value)
for object in iterable_obj:
    print(object)

#iteration amoung integers
list=[7,8,9,5]
for object in list:
    print(object)