#Lists: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
#syntax
# empty_list = list()
# print(len(empty_list))

# #u can use square brakets[]
# my_list = [1, 2, 3, 4, 5]
# fruits = ['mongo', 'orange', 'Apple','carrot']
# animal_products = ['Milk', 'meat', 'butter']
# print(len(my_list))
# print('fruits are :', fruits)
# print(len(animal_products))

#Lists can have items of different data types
# lst = ['ashuu', 22, True, {'country': 'somalia', 'city':'mogadisho'} ]
# print(lst)

# Accessing List Items Using Positive Indexing

# fruits = ['banan', 'kariz', 'moz', 'lemon']
# first_fruit = fruits[0]
# print(first_fruit)
# second_fruit = fruits[1]
# print(second_fruit)
# last_fruit = fruits[3]
# print(last_fruit)
# last_index = len(fruits) -1
# last_fruit = fruits[last_index]
# print(last_fruit)

#Accessing List Items Using Negative Indexing
# fruits = ['banan', 'kariz', 'moz', 'lemon']
# first_fruit = fruits[-3]
# last_fruit = fruits[-1]
# second_last = fruits[-2]
# print(first_fruit) #kariz
# print(last_fruit) #lemon
# print(second_last) #moz

#Unpacking List Items
# lst = ['item1', 'item2','item3', 'item4', 'item5']
# first_item, sencond_item, third_item, *rest = lst

# print(first_item) 
# print(sencond_item)
# print(third_item)

# print(rest) 


# first, second, third, *rest, tenth = [1,2,3,4,5,6,7,8,9,10]
# print(first)
# print(second)
# print(third)
# print(rest)
# print(tenth)

#slicing items from a list
# lst = ['item1', 'item2','item3', 'item4', 'item5']
# All_lists = lst[0:4]
# All_lists[0:]
# item2_and_item3 = lst[1:3]
# item2_item3_item4 = lst[1:]
# item3_item4 = lst[::2]
# print(lst)
# print(All_lists)
# print(item2_and_item3)
# print(item2_item3_item4)
# print(item3_item4)

 #Negative Indexing      
# fruits = ['banana', 'orange', 'mango', 'lemon']
# all_fruits = fruits[-4:]
# orange_and_mango = fruits[-3:-1] 
# orange_mango_lemon = fruits[-3:] 
# reverse_fruits = fruits[::-1] 
# print(all_fruits)
# print(orange_and_mango)
# print(orange_mango_lemon)
# print(reverse_fruits) 
 
 #Modifying Lists
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits[0] = 'avagado'
# fruits[1] = 'apple'
# print(fruits)
# last_index = len(fruits) -1
# fruits[last_index] = 'lime'
# print(fruits)

#Checking Items in a List
# fruits = ['banana', 'orange', 'mango', 'lemon']
# does_exist = 'banan' in fruits
# print(does_exist)
# does_exist = 'lime' in fruits
# print(does_exist)

#Adding Items to a List
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.append('apple')
# print(fruits)        
# fruits.append('lime')  
# print(fruits)

#Inserting Items into a List

#syntax 
# lst = ['item1', 'item2']
# lst.insert(index, item)

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.insert(2, 'apple') 
# print(fruits)

# Removing Items from a List

# fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
# fruits.remove('banana')
# print(fruits)  
# fruits.remove('lemon')
# print(fruits) 

#Removing Items Using Pop
 
# syntax
# lst = ['item1', 'item2']
# lst.pop()       # last item
# lst.pop(index)

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.pop()
# print(fruits)       

# fruits.pop(0)
# print(fruits)       

#Removing Items Using Del

# syntax
# lst = ['item1', 'item2']
# del lst[index] # only a single item
# del lst        # to delete the list completely


# fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
# del fruits[0]
# print(fruits)      
# del fruits[1]
# print(fruits)       
# del fruits[1:3]    
# print(fruits)      
# del fruits
# print(fruits)      

# Clearing List Items
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.clear()
# print(fruits)    

# Copying a List

# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits_copy = fruits.copy()
# print(fruits)
# print(fruits_copy)      

#Joining Lists
 #Plus Operator (+)
# numbers = [1,2,3,4,5]
# negative_numbers = [-5,-6,-7,-8,-9]
# integers = numbers + negative_numbers
# print(integers)

#using extend()
## syntax
# list1 = ['item1', 'item2']
# list2 = ['item3', 'item4', 'item5']
# list1.extend(list2)

# num1 = [0, 1, 2, 3]
# num2= [4, 5, 6]
# num1.extend(num2)
# print('Numbers:', num1) 
# negative_numbers = [-5,-4,-3,-2,-1]
# positive_numbers = [1, 2, 3,4,5]
# zero = [0]

# negative_numbers.extend(positive_numbers)
# print('Negative Numbers:', negative_numbers)  

#Counting Items in a List

# fruits = ['banana', 'orange', 'mango', 'lemon', 'orange']
# print(fruits.count('orange'))  
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.count(24))  

#Finding Index of an Item

# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(fruits.index('orange'))   # 1
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# print(ages.index(24))                

#Reversing a List
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits.reverse()
# print(fruits) 
# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# ages.reverse()
# print(ages) 

#Sorting List Items
## syntax
# lst = ['item1', 'item2']
# lst.sort()                # ascending
# lst.sort(reverse=True)    # descending


# ages = [22, 19, 24, 25, 26, 24, 25, 24]
# ages.sort()
# print(ages) 

# ages.sort(reverse=True)
# print(ages) 

#sorted():

# fruits = ['banana', 'orange', 'mango', 'lemon']
# print(sorted(fruits)) 
# fruits = ['banana', 'orange', 'mango', 'lemon']
# fruits = sorted(fruits,reverse=True)
# print(fruits)   