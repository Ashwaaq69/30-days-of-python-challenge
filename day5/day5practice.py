#Tuples : A tuple is a collection of different data types which is ordered and unchangeable (immutable). 

#create empty_tuple

# empty_tuple = ()
# print(empty_tuple)
# tp1 = ('item1', 'item2', 'item3')
# fruits = ('cinab', 'burtugal', 'mango', 'farowla')
# print(tp1)
# print(fruits)

#Tuple length use len() method
# tp1 = ('item1', 'item2', 'item3')
# print(len(tp1))

# accessing tuple items

# tp1 = ('item1', 'item2', 'item3')
# first_tp = tp1[0]
# second_tp = tp1[1]
# last_index = len(tp1) - 1
# last_tp = tp1[last_index]
# print(first_tp)
# print(second_tp)
# print(last_index)
# print(last_tp)


## Syntax
# tpl = ('item1', 'item2', 'item3','item4')
# first_item = tpl[-4]
# second_item = tpl[-3]


# fruits = ('banana', 'orange', 'mango', 'lemon')
# first_fruit = fruits[-4]
# second_fruit = fruits[-3]
# last_fruit = fruits[-1]

# print(first_fruit)
# print(second_fruit)
# print(last_fruit)


#slicing tuple

#Slicing tuples

# items = ('item1', 'item2', 'item3', 'item4')
# all_items = items[0:4]
# all_items = items[0:]
# item2_item3 = items [1:3]
# item2_tothe_rest = items[1:]
# print(all_items)
# print(item2_item3)
# print(item2_tothe_rest)


#Range of Negative Indexes

# Syntax
# tpl = ('item1', 'item2', 'item3','item4')
# all_items = tpl[-4:]         # all items
# middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)


# fruits = ('banana', 'orange', 'mango', 'lemon')
# all_fruits = fruits[-4:]    
# orange_mango = fruits[-3:-1]  
# orange_to_the_rest = fruits[-3:]

# print(all_fruits)
# print(orange_mango)
# print(orange_to_the_rest)


#Changing Tuples to Lists

# Syntax
# tpl = ('item1', 'item2', 'item3','item4')
# lst = list(tpl)


# items = ('item1', 'item2', 'item3', 'item4')
# items = list(items)
# items[0] = 'new item5'
# print(items)


# items = tuple (items)
# print(items)


#Checking an Item in a Tuple using in() 

# Syntax
# tpl = ('item1', 'item2', 'item3','item4')
# 'item2' in tpl # True

# fruits = ('banana', 'orange', 'mango', 'lemon')
# print('orange' in fruits) 
# print('apple' in fruits) 
# fruits[0] = 'apple' # TypeError: 


#Joining Tuples

# fruits = ('banana', 'orange', 'mango', 'lemon')
# vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
# fruits_and_vegetables = fruits + vegetables
# print(fruits)

# print(vegetables)
# print(fruits_and_vegetables)  # ('banana', 'orange', 'mango',


#Deleting Tuples

# fruits = ('banana', 'orange', 'mango', 'lemon')
# del fruits
