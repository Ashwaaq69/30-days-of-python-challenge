#Dictionaries
#A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.

#syntax empty_dict = {}

person =  {
    "firt_name" : "Miki",
    "last_name" : "mohaz",
    "age" : 30,
    "country" : "Dubai",
    "skills" : ["Python", "JavaScript", "HTML", "CSS"],
    "hobbies" : ["Reading", "Cooking", "Hiking"],
    "address" : {
    "street" : "123 Main St",
    "city" : "Dubai", 
}
}

# print(len (person))

#Accessing Dictionary Items
# print(person["firt_name"])
# print(person['age'])
# print(person['hobbies'][1])

#Accessing an item by key name raises an error if the key does not exist use get method

# print(person.get('hobbies'))
# print(person.get('height'))

#Adding Items to a Dictionary

# person['height'] = 1.75
# print(person)

#Modifying Items in a Dictionary
# person['age'] = 31
# person['hobbies'] = ['sleeping', 'swiming']
# print(person)

#Checking Keys in a Dictionary
# print('firt_name' in person)
# print('age' in person)

# Removing Key and Value Pairs from a Dictionary
# pop(key): removes the item with the specified key name:
# popitem(): removes the last item
# del: removes an item with specified key name

# person.pop('hobbies')
# person.popitem()
# del person['adress']['city'] #error
# print(person)

#Changing Dictionary to a List of Items
#The items() method changes dictionary to a list of tuples.

# syntax
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct.items())
#Clearing a Dictionary
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# print(dct.clear())

#Deleting a Dictionary
# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# del dct

#Copy a Dictionary

# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# dct_copy = dct.copy()
# print(dct_copy)

#Getting Dictionary Keys as a List

# dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
# keys = dct.keys()
# print(keys)

#Getting Dictionary Values as a List

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)