import itertools
for i in itertools.count(5,5):
    if i==35:
        break
    else:
        print(i,end=" ")
infinite_iterator=itertools.count(1)
print(infinite_iterator)
for i in range(5):
    print(next(infinite_iterator))