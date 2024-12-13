#Classes and Objects

#Creating a Class
# syntax class ClassName:
# code goes here

# class Person:
#     pass
# print(Person)

# Creating an Object
# We can create an object by calling the class.

# p = Person()
# print(p)


# Class Constructor

# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# p = person('ashuu', 22)
# print(p.name)
# print(p.age)



# class person:
#     def __init__(self, firstname, lastname, age, country):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
# p = person('ashuu', 'mohaz', 22, 'somali')
# print(p.firstname)
# print(p.lastname)
# print(p.age)
# print(p.country)



#Object Methods


# class person:
#     def __init__(self, firstname, lastname, age, country):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#     def person_info(self):
#             return f'Name: {self.firstname} {self.lastname}, Age: {self.age}, Country: {self.country}'
# p = person('ashuu', 'mohaz', 22, 'somali')
# print(p.person_info())


#Object Default Methods

# class person:
#     def __init__(self, firstname= 'ashuu', lastname = 'mohaz', age= 22, country= 'somali'):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#     def person_info(self):
#         return f'{self.firstname} {self.lastname},{self.age} yers old. lives in, {self.country}'
# p1 = person()
# print(p1.person_info())
# p2 = person('moha', 'apdi', 20, 'somali')
# print(p2.person_info())

#Method to Modify Class Default Values


# class person:
#     def __init__(self, firstname= 'ashuu', lastname = 'mohaz', age= 22, country= 'somali'):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#         self.skills = []
#     def person_info(self):
#         return f'{self.firstname} {self.lastname},{self.age} yers old. lives in, {self.country}'
#     def add_skill(self, skill):
#         self.skills.append(skill)
# p1 = person()
# print(p1.person_info())
# p1.add_skill('html')
# p1.add_skill('css')
# p1.add_skill('js')
# p2 = person('moha', 'apdi', 20, 'somali')
# print(p2.person_info())
# print(p1.skills)
# # print(p2.skills)

# # #Inheritance

# class student(person):
#     pass

# s1 = student('moha', 'apdi', 20, 'somali')
# s2 = student('ashuu', 'mohaz', 22, 'somali')

# print(s1.person_info())
# s1.add_skill('JavaScript')
# s1.add_skill('React')
# s1.add_skill('Python')
# print(s1.skills)

# print(s2.person_info())
# s2.add_skill('Organizing')
# s2.add_skill('Marketing')
# s2.add_skill('Digital Marketing')
# print(s2.skills)


# #Overriding parent method

# class Student(Person):
#     def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
#         self.gender = gender
#         super().__init__(firstname, lastname,age, country, city)
#     def person_info(self):
#         gender = 'He' if self.gender =='male' else 'She'
#         return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

# s1 = Student('ashwan', 'yasir', 22, 'somalia', 'mogadisho','male')
# s2 = Student('miki', 'moha', 22, 'somali', 'mog', 'female')
# print(s1.person_info())
# s1.add_skill('JavaScript')
# s1.add_skill('React')
# s1.add_skill('Python')
# print(s1.skills)

# print(s2.person_info())
# s2.add_skill('Organizing')
# s2.add_skill('Marketing')
# s2.add_skill('Digital Marketing')
# print(s2.skills)