#sets # syntax
# st = set()

# st = {'item1', 'item2', 'item3', 'item4'}
# print(len(st))

# st = {'item1', 'item2', 'item3', 'item4'}
# print("Does set st contains item5?" 'item5' in st)

# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.add('lime')

# Add multiple items using update() 
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.update(['apple', 'grape'])
# print(fruits)

# syntax remove()
# st = {'item1', 'item2', 'item3', 'item4'}
# st.remove('item2')

 # removes a random item from the set
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.pop() 
# print(fruits)
# clear
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# fruits.clear()
# print(fruits) 
# delete set

# fruits = {'banana', 'orange', 'mango', 'lemon'}
# del fruits


# Converting List to Set


# fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
# fruits = set(fruits)

# print(fruits)

# Joining Sets
 
# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'} 
# print(fruits.union(vegetables))

# Update This method inserts a set into a given set

# fruits = {'banana', 'orange', 'mango', 'lemon'}
# vegetables = {'tomato', 'potato', 'cabbage','onion', 'car
# fruits.update(vegetables)


# Finding Intersection Items

# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item3', 'item2'}
# st1.intersection(st2) # {'item3', 'item2'}
# print(st1)

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.intersection(even_numbers) 
# print(whole_numbers)

# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.intersection(dragon)  
# print(python) 

# Checking Subset and Super Set
# issubset: Returns True if all elements of one set are in the other.
# issuperset: Returns True if a set contains all elements of the other.

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.issubset(even_numbers)
# whole_numbers.issuperset(even_numbers) 

# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.issubset(dragon)     


# Checking the Difference Between Two Sets

# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_numbers = {0, 2, 4, 6, 8, 10}
# whole_numbers.difference(even_numbers)

# python = {'p', 'y', 't', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.difference(dragon)   
# dragon.difference(python) 
# print(python)
# print(dragon)   

# Finding Symmetric Difference Between Two Sets
# syntax
# st1 = {'item1', 'item2', 'item3', 'item4'}
# st2 = {'item2', 'item3'}
# # it means (A\B)∪(B\A)
# st2.symmetric_difference(st1) # {'item1', 'item4'}


# whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# some_numbers = {1, 2, 3, 4, 5}
# whole_numbers.symmetric_difference(some_numbers) 
# print(whole_numbers)
# python = {'p', 'y', 't', 'h', 'o','n'}
# dragon = {'d', 'r', 'a', 'g', 'o','n'}
# python.symmetric_difference(dragon) 
# print(python)

# Use isdisjoint() to check whether two sets share any elements.
# If no elements are shared, isdisjoint() returns True.
# If at least one element is shared, isdisjoint() returns False.

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers)
print(even_numbers)
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon) 
print(python)