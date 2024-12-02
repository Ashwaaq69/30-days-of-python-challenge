# 1:Filter only negative and zero in the list using list comprehension

# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# negative_nums = [i for i in numbers if i <=0]
# print(negative_nums)

# 2:Flatten the following list of lists of lists to a one dimensional list :

# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# flattened_list = [number for row in list_of_lists for col in row for number in col]

# print(flattened_list)


# 3 Using list comprehension create the following list of tuples:

# num = [(n, 1, n**1, n**2, n**3, n**4, n**4) for n in range(11)]
#  print(num)

# 4 Flatten the following list to a new list:

# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# flattened_countries = [[country.upper(), country[:3].upper(), capital.upper()] for row in countries for country, capital in row]
# print(flattened_countries)
# 5

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_dict = [{'country': country.upper(), 'city': city.upper()} for row in countries for country, city in row]
print(countries_dict)


# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_names = [f"{first} {last}" for row in names for first, last in row]
print(concatenated_names)

# 7
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else 'Undefined (vertical line)'

y_intercept = lambda x, y, m: y - m * x

# Slope
print(slope(1, 2, 3, 6))  # Output: 2.0

# Y-Intercept
print(y_intercept(1, 2, 2))  # Output: 0




