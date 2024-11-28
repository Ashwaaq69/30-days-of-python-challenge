# 1:Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

# age = input("Enter your age :")
# age = int(age)
# if age >= 18:
#     print("you can drive")
# else:
#     years_to_wait = 18 - age
#     print(f"You need to wait {years_to_wait} more years to be old enough to drive.")

# 2:Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# Get user inputs
# my_age = int(input("Enter my age: "))
# your_age = int(input("Enter your age: "))

# # Compare ages
# if my_age > your_age:
#     difference = my_age - your_age
#     if difference == 1:
#         print("I am 1 year older than you.")
#     else:
#         print(f"I am {difference} years older than you.")
# elif my_age < your_age:
#     difference = your_age - my_age
#     if difference == 1:
#         print("You are 1 year older than me.")
#     else:
#         print(f"You are {difference} years older than me.")
# else:
#     print("We are the same age!")


# 3:Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
number_one = input("enter number one (a) :")
number_two = input("enter number two (b) :")
if number_one > number_two:
    print("a is greater than b ")
elif number_one < number_two:
    print(" a is smaller than b ")
else:
    print(" a is equal to b ")
    
   


    