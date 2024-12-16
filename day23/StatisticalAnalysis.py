#Statistical Analysis

#Importing NumPy
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from scipy import stats

#check the version of the numpy pacage
# print('numpy:', np.__version__)
# # Checking the available methods
# print(dir(np))

# Creating numpy array using int

# python_list = [1,2,3,4,5]
# print('type:', type(python_list))
# print(python_list)

# two_dimensional_list = [[0,1,2], [3,4,5],[6,7,8]]
# print(two_dimensional_list)

# numpy_array_from_list = np.array(python_list)
# print(type(numpy_array_from_list))
# print(numpy_array_from_list)


# Creating float numpy arrays
# Creating a float numpy array from list with a float data type parameter

# python_list = [1,2,3,4,5]
# numpy_array_from_list2 = np.array(python_list)
# print(numpy_array_from_list2)


# Creating boolean numpy arrays
# Creating a boolean a numpy array from list

# numpy_bool_array = np.array([0, 1, -1, 0,0], dtype=bool)
# print(numpy_bool_array)

# Creating multidimensional array using numpy
# A numpy array may have one or multiple rows and columns

# two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
# numpy_two_dimensional_list = np.array(two_dimensional_list)
# print(type(numpy_two_dimensional_list))
# print(numpy_two_dimensional_list)


#Converting numpy array to list

# np_to_list = numpy_array_from_list.tolist()
# print(type (np_to_list))
# print('one dimensional array:', np_to_list)
# print('two dimensional array: ', numpy_two_dimensional_list.tolist())


#Creating numpy array from tuple

# python_tuple = (1,2,3,4,5)
# print('python tuple:', python_tuple)

# numpy_array_from_tuple = np.array(python_tuple)
# print(type (numpy_array_from_tuple)) 
# print('numpy_array_from_tuple: ', numpy_array_from_tuple)

#Shape of numpy array

# nums = np.array([1,2,3,4,5])
# print(nums)
# print(numpy_two_dimensional_list)
# print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
# three_by_four_array = np.array([[0, 1, 2, 3],
#         [4,5,6,7],
#         [8,9,10, 11]])
# print(three_by_four_array.shape)

#Data type of numpy array
#Type of data types: str, int, float, complex, bool, list, None

# int_lists = [-3, -2, -1, 0, 1, 2,3]
# int_array = np.array(int_lists)
# float_array = np.array(int_lists, dtype=float)

# print(int_array)
# print(int_array.dtype)
# print(float_array)
# print(float_array.dtype)

# Size of a numpy array
# In numpy to know the number of items in a numpy array list we use size


# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# two_dimensional_list = np.array([[0, 1, 2],
#                               [3, 4, 5],
#                               [6, 7, 8]])

# print('The size:', numpy_array_from_list.size) #5
# print('The size:', two_dimensional_list.size)  #9

#Mathematical Operation using numpy

# Mathematical Operation
# Addition
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_plus_original = numpy_array_from_list  + 10
# print(ten_plus_original)

# Subtraction
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_minus_original = numpy_array_from_list  - 10
# print(ten_minus_original)

# # Multiplication
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list * 10
# print(ten_times_original)

# Division
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list / 10
# print(ten_times_original)

# Modulus; Finding the remainder
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list % 3
# print(ten_times_original)

# # Floor division: the division result without the remainder
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list // 10
# print(ten_times_original)

# # Exponential is finding some number the power of another:
# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list  ** 2
# print(ten_times_original)

# Checking data types

#Int,  Float numbers
# numpy_int_arr = np.array([1,2,3,4])
# numpy_float_arr = np.array([1.1, 2.0,3.2])
# numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

# print(numpy_int_arr.dtype)
# print(numpy_float_arr.dtype)
# print(numpy_bool_arr.dtype)



# Converting types
# We can convert the data types of numpy array

# Int to Float
# numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
# print(numpy_int_arr)

# # Float to Int
# # numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
# # print(numpy_int_arr)
# #     array([1, 2, 3, 4])
# # #Int ot boolean
# # numpy_float_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')
# # print(numpy_float_arr)
# # #
# # numpy_float_list.astype('int').astype('str')
# #     print(array(['1', '2', '3'], dtype='<U21'))

#Multi-dimensional Arrays

# 2 Dimension Array
# two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
# print(type (two_dimension_array))
# print(two_dimension_array)
# print('Shape: ', two_dimension_array.shape)
# print('Size:', two_dimension_array.size)
# print('Data type:', two_dimension_array.dtype)

# #Getting items from a numpy array


# # 2 Dimension Array
# two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
# first_row = two_dimension_array[0]
# second_row = two_dimension_array[1]
# third_row = two_dimension_array[2]
# print('First row:', first_row)
# print('Second row:', second_row)
# print('Third row: ', third_row)



# first_column= two_dimension_array[:,0]
# second_column = two_dimension_array[:,1]
# third_column = two_dimension_array[:,2]
# print('First column:', first_column)
# print('Second column:', second_column)
# print('Third column: ', third_column)
# print(two_dimension_array)


#Slicing Numpy array

# two_dimensional_array = np.array([[1,2,3], [4,5,6],[7,8,9]])
# first_two_rows_and_columns = two_dimensional_array[0:2, 0:2]
# print('First two rows and columns:', first_two_rows_and_columns)

# How to reverse the rows and the whole array?
# two_dimension_array[::]
#     array([[1, 2, 3],
#            [4, 5, 6],
#            [7, 8, 9]])

#Reverse the row and column positions

# two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
# two_dimension_array[::-1,::-1]


# How to represent missing values ?
# print(two_dimension_array)
# two_dimension_array[1,1] = 55
# two_dimension_array[1,2] = 44
# print(two_dimension_array)


# Numpy Zeroes
# numpy_ones = np.ones((3,3),dtype=int,order='C')
# print(numpy_ones)

# Reshape
# numpy.reshape(), numpy.flatten()
# first_shape  = np.array([(1,2,3), (4,5,6)])
# print(first_shape)
# reshaped = first_shape.reshape(3,2)
# print(reshaped)

# flattened = reshaped.flatten()
# flattened

# print(flattened)


    ## Horitzontal Stack
# np_list_one = np.array([1,2,3])
# np_list_two = np.array([4,5,6])

# print(np_list_one + np_list_two)

# print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))

#    ## Vertical Stack
# print('Vertical Append:', np.vstack((np_list_one, np_list_two)))


#Generating Random Numbers
# random_float = np.random.random()
# print(random_float)

    # Generate a random float  number
# random_floats = np.random.random(5)
# print(random_floats)

# # Generating a random integers between 0 and 10

# random_int = np.random.randint(0, 11)
# print(random_int)

# # Generating a random integers between 0 and 10
# random_int = np.random.randint(2,10, size=(3,3))
# print(random_int)



# #Generationg random numbers


#     # np.random.normal(mu, sigma, size)
# normal_array = np.random.normal(79, 15, 80)
# print(normal_array)


#Numpy and Statistics

# plt.hist(normal_array, color="grey", bins=50)
# print(normal_array)

#Matrix in numpy

# four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
# # print(four_by_four_matrix)

# np.asarray(four_by_four_matrix)[2] = 2
# print(four_by_four_matrix)

#Numpy numpy.arange()

# creating list using range(starting, stop, step)
# lst = range(0, 11, 2)
# print(lst)
# for i in lst:
#     print(i)

#Creating sequence of numbers using linspace

# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
# np.linspace(1.0, 5.0, num=10)
# # not to include the last value in the interval
# np.linspace(1.0, 5.0, num=5, endpoint=False)
# # to check the size of an array
# x = np.array([1,2,3], dtype=np.complex128)
# print(x)

#NumPy Statistical Functions with Example


# Numpy Functions
# Min np.min()
# Max np.max()
# Mean np.mean()
# Median np.median()
# Varience
# Percentile
# Standard deviation np.std()
# two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
# np_normal_dis = np.random.normal(5, 0.5, 100)
# print('normal dis is: ', np_normal_dis)
# ## min, max, mean, median, sd
# print('min: ', two_dimension_array.min())
# print('max: ', two_dimension_array.max())
# print('mean: ',two_dimension_array.mean())
# # print('median: ', two_dimension_array.median())
# print('sd: ', two_dimension_array.std())


# print(two_dimension_array)
# print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
# print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
# print('=== Row ==')
# print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
# print('Row with maximum: ', np.amax(two_dimension_array,axis=1))


#How to generate random numbers?
# One random number between [0,1)
# one_random_num = np.random.random()
# one_random_in = np.random
# # print(one_random_num)


# # Random numbers between [0,1) of shape 2,3
# r = np.random.random(size=[2,3])
# print(r)
# print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))


# np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
# np_normal_dis
## min, max, mean, median, sd
# print('min: ', np.min(np_normal_dis))
# print('max: ', np.max(np_normal_dis))
# print('mean: ', np.mean(np_normal_dis))
# print('median: ', np.median(np_normal_dis))
# print('mode: ', stats.mode(np_normal_dis))
# print('sd: ', np.std(np_normal_dis))

# plt.hist(np_normal_dis, color="grey", bins=21)
# plt.show()

# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot

# Syntax

# numpy.dot(x, y, out=None)

### Linear algebra
### Dot product: product of two arrays
# f = np.array([1,2,3])
# g = np.array([4,5,3])
# ### 1*4+2*5 + 3*6
# np.dot(f, g)  # 23
# #NumPy Matrix Multiplication with np.matmul()

# ### Matmul: matruc product of two arrays
# h = [[1,2],[3,4]]
# i = [[5,6],[7,8]]
# ### 1*5+2*7 = 19
# np.matmul(h, i)
# np.linalg.det(i)
# Z = np.zeros((8,8))
# Z[1::2,::2] = 1
# Z[::2,1::2] = 1


# new_list = [ x + 2 for x in range(0, 11)]
# print(new_list)

# np_arr = np.array(range(0, 11))
# np_arr + 2
# print(np_arr)

# We use linear equation for quantities which have linear relationship. Let's see the example below:

# temp = np.array([1,2,3,4,5])
# pressure = temp * 2 + 5
# print(pressure)

# plt.plot(temp,pressure)
# plt.xlabel('Temperature in oC')
# plt.ylabel('Pressure in atm')
# plt.title('Temperature vs Pressure')
# plt.xticks(np.arange(0, 6, step=0.5))
# plt.show()



# mu = 28
# sigma = 15
# samples = 100000

# x = np.random.normal(mu, sigma, samples)
# ax = sns.distplot(x);
# ax.set(xlabel="x", ylabel='y')
# plt.show()