# Exception Handling

# try:
#     print(10 + '5')
# except:
#     print("An error occurred") # error b/c we can not add into to str
    
# try:
#     name = input('Enter your name: ')
#     year_born = input('Enter year you were born:')
#     age = 2024 - year_born
#     print(f'Your name is {name}, and your age is {age}')
# except:
#     print('An error occurred. Please ensure you entered valid inputs.')     # An error occurred. Please ensure you entered valid inputs.



# try:
#     name = input('Enter your name: ')
#     year_born = input('Enter year you were born:')
#     age = 2024 - year_born
#     print(f'Your name is {name}, and your age is {age}')
# except TypeError:
#     print('type error occured')
# except ValueError:
#     print('value error occured')
# except ZeroDivisionError:
#     print('zero division error occured')
# Enter your name: ashuu
# Enter year you were born:1920
# type error occured

        
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2024 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block')
# finally:
#     print('I alway run.')

# It is also shorten the above code as follows:
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - int(year_born)
#     print(f'You are {name}. And your age is {age}.')
# except Exception as e:
#     print(e)


# Packing and Unpacking Arguments in Python
# We use two operators:

# * for tuples
# ** for dictionaries

# Unpacking Lists


# def sum_of_five_nums(a,b,c,d,e):
#     return a+b+c+d+e
# lst = [1,2,3,4,5]
# print(sum_of_five_nums(lst))


# When we run the this code, it raises an error, because this function takes numbers (not a list) as arguments. Let us unpack/destructure the list.

# def sum_of_five_nums(a, b, c, d, e):
#     return a + b + c + d + e

# lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(*lst)) 


# We can also use unpacking in the range built-in function that expects a start and an end.

# numbers = range(2,7)
# print(list(numbers))
# args = [2,7]
# numbers = range(*args)
# print(numbers)

# A list or a tuple can also be unpacked like this:

# countries = ['somalia', 'dubai', 'saudi', 'yemen', 'falastin']
# som,dub,sau, *rest = countries
# print(som,dub,sau, rest)
# numbers = [1,2,3,4,5,6,7]
# one, *middle, last = numbers
# print(one,middle,last)  

# Unpacking Dictionaries

# def unpacking_person_info(name, country, city, age):
#     return f'{name} lives in {country}, {city}. she is {age} year old.'
# dct = {'name':'ashuu', 'country':'somali', 'city':'mogadisho', 'age':22}
# print(unpacking_person_info(**dct))

# Packing

# Packing Lists


# def sum_all(*args):
#     s = 0
#     for i in args:
#         s += i
#     return s
# print(sum_all(1, 2, 3))             
# print(sum_all(1, 2, 3, 4, 5, 6, 7))


# Packing Dictionaries

# def packing_person_info(**kwargs):
   
#     for key in kwargs:
#         print(f"{key} = {kwargs[key]}")
#     return kwargs

# print(packing_person_info(name="ashuu",
#     country="somalia", city="mogadisho", age=22))

# Spreading in Python

# lst_one = [1,2,3]
# lst_two = [4,5,6,7]
# lst = [0, *lst_one, *lst_two]
# print(lst)


# Enumerate

# If we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list.

# for index, item in enumerate([20,30,40]):
#     print(index, item)

# countries = ['somalia', 'Dubai', 'yemen', 'Finland', 'falastin']
# for index, i in enumerate(countries):
#     print('hi')
#     if i == 'Dubai':
#         print(f'The country {i} has been found at index {index}')

# Zip


# fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
# vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
# fruits_and_veges = []
# for f, v in zip(fruits, vegetables):
#     fruits_and_veges.append({'fruit':f, 'veg':v})

# print(fruits_and_veges)