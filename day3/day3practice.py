#strings
# letter = 'M'
# print(len(letter))
# print(letter.lower())  # Output: M
# greeting = 'hello suufi iam ashuu mohaz'
# print(greeting)
# print(len(greeting))


#multi line string use 3 single concatination

# multiLine_string = '''iam ashuu mohaz iam student and enjoy studying.i started learnig python with my friend.
# we are very good friends.'''
# print(multiLine_string)

#string concatination 

# first_name = 'ashuu'
# last_name = 'mohaz'
# full_name = first_name + ' ' + last_name
# print(full_name)

#Escape Sequences in Strings

'''\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (")'''

# print('i hope everone is enjoying the python challenge. \n are you?')
# print('Days\tTopics\tExercises')
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3/t5\t23')
# print('Day 4\t1\t35')

# print('This is a backlash symbol(//)')
# print('in every programing language is starts with \"Hello, world!\"')


# String formatting

'''%s - String (or any object with a string representation, like numbers)
%d - Integers
%f - Floating point numbers
"%.number of digitsf" - Floating point numbers with fixed precision'''

#strings only
# first_name = 'Ashwag'
# last_name = 'Mohaz'
# language = 'python'
# formated_string = 'i am %s %s. Miki %s '%(first_name, last_name, language)
# print(formated_string)

#string and numbers

# radius = 10
# pi = 3.14
# area = pi * radius **2
# formated_string = 'The area of circle with radius %.2f is %.2f '%(radius, area)

# print(formated_string)

# python_libries = ['Django', 'Flask', 'numpy', 'Matplot', 'pandas']
# formated_string = 'the following are python libries:%s' %(python_libries)
# print(formated_string)

#New Style String Formatting (str.format)

#python version 3.

# subject1 = 'react'
# subject2 = 'node.js'
# subject3 = 'python'

# formated_string = 'the subjects are: {}, {}, {}'.format(subject1, subject2, subject3)

# print(formated_string)

# a = 4
# b = 3
# print(' {} + {} = {}'.format(a, b, a+ b))
# print('{} - {} = {}'.format(a, b, a-b))
# print('{} * {} = {}'.format(a, b, a*b))
# print('{} / {} = {:.2f}'.format(a, b, a/b))  # division by zero error
# print('{} % {} = {}'.format(a, b, a%b))
# print('{} // {} = {}'.format(a, b, a//b)) 
# print('{} ** {} = {}'.format(a, b, a**b))  

# Python Strings as Sequences of Characters

# language = 'python'
# a,b,c,d,e,f = language
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)

# Accessing Characters in Strings by Index

# language = 'react'
# first_leter = language[0]
# print(first_leter)
# second_letter = language[1]
# print(second_letter)
# last_index = len(language)-1
# last_leter = language[last_index]
# print(last_leter)

#FROM right end
# language = 'Python'
# last_letter = language[-3]
# print(last_letter) # n
# second_last = language[-4]
# print(second_last) # o

#slicing python string
# language = 'javascript'
# print(language[0:3]) # jav 
# print(language[0:5])  # javas
# print(language[1:7]) #avascr

#Reversing a String
greeting = 'hello, dear world!'
# print(greeting[::-1]) # !dlrow raed ,olleh
# print(greeting[0:10][::-1]) # aed ,olleh

# String Methods

# challenge = 'hello world'
# print(challenge.capitalize())

 
# count()

# challenge = 'thirty days of python'
# print(challenge.count('y')) # 3
# print(challenge.count('y', 7, 14)) 

# endswith() =  Checks if a string ends with a specified ending
# challenge = 'thirty days of python'
# print(challenge.endswith('on')) # True
# print(challenge.endswith('python')) # True

#expandtabs()

# names = 'Ashuu\tibrahiim\tmohaz'
# print(names.expandtabs())
# print(names.expandtabs(10))

#find()
# challenge = 'thirty days of python'
# print(challenge.find('o'))

#rfind()

# challenge = 'thirty days of python'
# print(challenge.rfind('m'))
# print(challenge.rfind('th'))

# first_name = 'Ashwag'
# last_name = 'ibraahiim'
# age = 22
# job = 'student'
# country = 'somalia'
# sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
# print(sentence) 

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
# print(result) 

#isalnum(): Checks alphanumeric character
# challenge = 'thirtydays'
# print(challenge.isalnum)

#isalpha(): C
# challenge = 'thirty days of python'
# print(challenge.isalpha()) 
# challenge = 'ThirtyDaysPython'
# print(challenge.isalpha()) 
# num = '123'
# print(num.isalpha())  


#isdecimal():

# challenge = 'thirty days of python'
# print(challenge.isdecimal()) 
# challenge = '123'
# print(challenge.isdecimal())  
# challenge = '\u00B2'
# print(challenge.isdigit())   
# challenge = '12 3'
# print(challenge.isdecimal())  
  
#isdigit
# challenge = 'Thirty'
# print(challenge.isdigit())
# challenge = '30'
# print(challenge.isdigit())   
# challenge = '\u00B2'
# print(challenge.isdigit())   

#isnumeric(): 

# num = '10'
# print(num.isnumeric()) 
# num = '\u00BD'
# print(num.isnumeric()) 
# num = '10.5'
# print(num.isnumeric()) 

#isidentifier()
# challenge = 'thirty_days_of_python'

# print(challenge.isidentifier())
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier())

#islower
# challenge = 'thirty days of python'
# print(challenge.islower()) 
# challenge = 'Thirty days of python'
# print(challenge.islower()) 


#isupper

# challenge = 'thirty days of python'
# print(challenge.isupper()) 
# challenge = 'THIRTY DAYS OF PYTHON'
# print(challenge.isupper()) 


#join()

# technologies = ['html', 'css', 'js', 'react', 'next.js']
# print('-'.join(technologies))

#strip() removes 

# challenge = 'iam too tired man'
# print(challenge.strip('in')) 

#replace()

challenge = 'thirty days of python'
print(challenge.replace('thirty', 'forty'))

#split():

challenge = 'thirty days of python'
print(challenge.split()) 
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) 

#title()

challenge = 'thirty days of python'
print(challenge.title())

#swapcase()

challenge = 'thirty days of python'
print(challenge.swapcase())

#startswith()

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) 

challenge = '30 days of python'
print(challenge.startswith('thirty')) 
