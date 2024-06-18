# stop iterator
iterable_value = "helloworld"
iterable_obj = iter(iterable_value)
while True:
    try:
        item = next(iterable_obj)
        print(item)
    except StopIteration:
        break

