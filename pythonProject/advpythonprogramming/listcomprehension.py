#list comprehension
#normal lists
numbers=[12,13,14]
doubled=[x*2 for x in numbers]
print(doubled)

#using list comprehension
doubled_numbers=[num*2 for num in numbers]
print(doubled_numbers)

#Find all of the numbers from 1-1000 that are divisible by 7
divisible_by_seven = [num for num in range(1, 1001) if num % 7 == 0]
print(divisible_by_seven)

#find even and odd in the range of 0 to 20
even=[n for n in range(0,20) if n%2==0]
print(even)
odd=[n for n in range(0,20) if n%2!=0]
print(odd)

#matrix display
matrix=[[j for j in range(3)] for i in range(3)]
print(matrix)

#if else condition in list comprehension
even_odd_list=["Even" if i%2==0 else "odd" for i in numbers]
print(even_odd_list)

#if else nested conditions
num_list=[y for y in range(100) if y%2==0 if y%5==0]
print(num_list)

#print the range >50 using integers
new_list=[x for x in range(100) if x>50]
print(new_list)

#.Given a list of numbers, remove floats (numbers with decimals)
numbers=[1.11,5,6,90,76,4.66,89,2.9,7.9,9.9,777]
remove_floats=[num for num in numbers if not isinstance(num, float)]
print(remove_floats)

#Count the number of spaces in a string
# String
my_string = "Count the number of spaces in this string."
spaces = [char for char in my_string if char == ' ']
space_count = len(spaces)
print("Number of spaces:", space_count)

#Find common numbers in two lists of numbers
list1=[45,8,9,66,74,32,89,5]
list2=[5,66,90,45,78,83,33,1]
common_num=[num for num in list1 if num in list2]
print(common_num)

#Consonants in a string
my_string = "Count the number of consonants in this string."
vowels = "aeiouAEIOU"
consonants = [char for char in my_string if char.isalpha() and char not in vowels]
print("Consonants:", ''.join(consonants))