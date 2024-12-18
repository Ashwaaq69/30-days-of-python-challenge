import pandas as pd
import numpy as np


# nums = [1,2,3,4,5]
# s = pd.Series(nums)
# print(s)

#Creating Pandas Series with custom index

# nums = [1,2,3,4,5]
# s = pd.Series(nums, index=[1,2,3,4,4])
# print(s)


# fruits = ['orange', 'lemon', 'apple']
# fruits = pd.Series(fruits, index=[1,2,3])
# print(fruits)

#Creating Pandas Series from a Dictionary

# dct = {'name':'ashuu', 'country':'somali', 'city':'mogadisho'}
# s = pd.Series(dct)
# print(s)

#Creating a Constant Pandas Series
# s = pd.Series(20, index=[4,5,6])
# print(s)

#Creating a Pandas Series Using Linspace
# s = pd.Series(np.linspace(5,20,10)) # linspace(starting, end, items)
# print(s)

#DataFrames

# Pandas data frames can be created in different ways.

# Creating DataFrames from List of Lists

# data = [
#     ['ashuu', 'somalia', 'mog'],
#     ['miki', 'somali', 'mog'],
#     ['mohaz', 'somalia', 'mogadisho'],
# ]

# df = pd.DataFrame(data, columns=['names', 'country', 'city'])
# print(df)

#Creating DataFrame Using Dictionary


# data = { 
#     'names': ['ashuu','miki','mohaz'],
#     'country': ['somalia','dubai','swiz'],
#     'city': ['mog','qruj','den'],
# }
# df = pd.DataFrame(data)
# print(df)

#Creating DataFrames from a List of Dictionaries

# data = [
#     {'Name': 'ashuu', 'Country': 'somali', 'City': 'mog'},
#     {'Name': 'moha', 'Country': 'UK', 'City': 'London'},
#     {'Name': 'miki', 'Country': 'Sweden', 'City': 'Stockholm'}]
# df = pd.DataFrame(data)
# print(df)

#Reading CSV File Using Pandas

df=pd.read_excel('C:/Users/pc/Employee_Dataset_Pandas.xlsx')
# print(df)

# Data Exploration
# Let us read only the first 5 rows using head()

# print(df.head())

# Let us also explore the last recordings of the dataframe using the tail() methods.

# print(df.tail())

# print(df.shape) # as you can see 10000 rows and three columns

# print(df.columns)
# print(Salary.describe())

# print(df.describe())


#Modifying a DataFrame

#Creating a DataFrame
data = {'Name': ['ashuu','miki','mohaz'],
        'country':['somali', 'dubai', 'falastin'],
        'age':[20, 22, 19],
        'weight':[62, 60, 54],
        'height':[173, 170, 160]
        
        }
df = pd.DataFrame(data)
print(df)


#Adding a New Column

# weights = [74, 78, 69]
# df['Weight'] = weights
# print(df)

#Let's add a height column into the DataFrame aswell

# heights = [173, 175, 169]
# df['Height'] = heights
# print(df)

#Modifying column values

# df['height'] = df['height'] * 0.01
# print(df)

# Using functions makes our code clean, but you can calculate the bmi without one
def calculate_bmi ():
    weights = df['weight']
    heights = df['height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()

df['BMI'] = bmi
# print(df)

#Formating DataFrame columns
# df['BMI'] = round(df['BMI'], 1)
# print(df)

# birth_year = ['1769', '1985', '1990']
# current_year = pd.Series(2020, index=[0, 1,2])
# df['Birth Year'] = birth_year
# df['Current Year'] = current_year
# print(df)

#Checking data types of Column values
# print(df.Weight.dtype)
# df['Birth Year'] = df['Birth Year'].astype('int')
# print(df['Birth Year'].dtype) 
# df['Current Year'].dtype

# mean = (35 + 30)/ 2
# print('Mean: ',mean)	