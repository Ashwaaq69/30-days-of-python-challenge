#exercise level 1
#1 create an empty tuple

# tp = ()
# print(tp)

# 2: Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

# siters = ('Laila', 'lula', 'saida', 'yahya', 'ciisa')

#3 Join brothers and sisters tuples and assign it to siblings

# siters = ('laila', 'lula', 'saida')
# brothers = ('yahya', 'ciisa')
# siblings = siters + brothers

# # print(siblings)


#4How many siblings do you have?

# print(len(siblings))

#5 Modify the siblings tuple and add the name of your father and mother and assign it to family_members

# family_members = siblings + ('father:ibraahiim', 'mother :Qadija')
# print(family_members)

#exercise level 2

#1 Unpack siblings and parents from family_members
# family_members = ("Father", "Mother", "Brother", "Sister", "Younger Brother")

# # Unpacking parents and siblings
# father, mother, *siblings = family_members

# print("Father:", father)
# print("Mother:", mother)
# print("Siblings:", siblings)


#2 Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ('mango', 'apple', 'lemon')
vegtable = ('salad', 'bawbaw', 'tomato')

animal_products = ('cat', 'dog', 'bird')

food_stuff_tp = fruits + vegtable + animal_products
print(food_stuff_tp)

#3 Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list (food_stuff_tp)
print(food_stuff_lt)

#4 Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

# food_stuff_tp_slice = food_stuff_tp[len(food_stuff_tp)//2:]
# print(food_stuff_tp_slice)

#5 Slice out the first three items and the last three items from food_staff_lt list

# first_three = food_stuff_lt[:3]
# last_three = food_stuff_lt[-3:]
# print("First three items:", first_three)
# print("Last three items:", last_three)

#6 Delete the food_staff_tp tuple completely

# del food_stuff_tp

#7 Check if an item exists in tuple:

# nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# 'Norway' in nordic_countries

# 'iceland' in nordic_countries
# print(nordic_countries)

# end
