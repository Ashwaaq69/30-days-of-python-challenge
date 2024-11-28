#Loops
#  Python programming language also provides the following types of two loops:

# while loop
# for loop

#While Loop
# count = 0
# while count < 5:
#     print(count)
#     count+=1
   
   
# count = 0
# while count < 5:
#     print(count)
#     count+=1
# else:
#     print("Count value reached 5")


# Break and Continue - Part 1

# count = 0
# while count < 5:
#   print(count)
#   count += 1
#   if count == 3:
#       break

# count = 0
# while count < 5:
#     if count == 3:
#         count = count + 1
#         continue
#     print(count)
#     count = count + 1



# For Loop

# numbers = [0,1,2,3,4,5]
# for number in numbers:
#     print(number)


# language = 'Python'
# for letter in language:
#     print(letter)


# for i in range(len(language)):
#     print(language[i])


# numbers = (0, 1, 2, 3, 4, 5)
# for number in numbers:
#     print(number)


# person = {
#     'first_name':'Ashuu',
#     'last_name':'mohaz',
#     'age':22,
#     'country':'Dubai',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Adan ade street',
#         'zipcode':'255'
#     }
# }


# for key in person:
#     print(key)
#     for key, value in person.items():
#      print(key, value)


# it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
# for company in it_companies:
#     print(company)
    
    
# # Break and Continue - Part 2
    
# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#      break



# numbers = (0,1,2,3,4,5)
# for number in numbers:
#     print(number)
#     if number == 3:
#         continue
#     print('Next number should be ', number + 1) if number != 5 else print("loop's end")
# print('outside the loop')


# The Range Function

# lst = list(range(11))
# print(lst)
# st = set(range(1,11))
# print(st)

# lst = list(range(0,11,2))
# print(lst)
# st = set(range(0,11,2))
# print(st) 

# Nested For Loop


# person = {
#     'first_name':'Ashuu',
#     'last_name':'mohaz',
#     'age':22,
#     'country':'Dubai',
#     'is_marred':True,
#     'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address':{
#         'street':'Adan ade street',
#         'zipcode':'255'
#     }
# }


# for key in person:
#     if key == 'skills':
#         for skill in person['skills']:
#             print(skill)



# For Else

# for number in range(11):
#     print(number)   
# else:
#     print('The loop stops at', number)


# Pass

# for number in range(6):
#     pass