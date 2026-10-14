#DataCamp: "Data Analyst in Python" Course
#Topic: 2D NumPy Arrays

import numpy as np
np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
type(np_height)
type(np_weight)
#When you ask for the type of the arrays, Python tells you the type or element from what package
#your using.

#We can create multli-dimensional arrays. For learning purposes, we will mainly stick with
#2D dimensional arrays which can be created from list of lists. 2D numpy arrays as an improved
#list of lists.
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                 [65.4, 59.2, 63.6, 88.4, 68.7]])
#When you print out the array, each sublist in that array corresponds to a row in the two-dimensional
#numpy array
print(np_2d)

#You can use ".shape" which is a so-called "attribute" after your array's name to see how many rows
#and columns your multidimensional has The order when it prints shows the number of rows and then
#the number of columns afterward.
print(np_2d.shape) #Output: (2,5) <-- Rows, Columns
#The syntax for accessing an attribute looks the same as if you were calling a method, but they
#are not the same. Methods have a circle bracket while attributes do not.

#Remember that 2D arrays can only contain one single data type. So if you try to change a
#string to a float then all the array elements will be coerced to end up with a homogeneous
#array.
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                 [65.4, 59.2, 63.6, 88.4, 68.7]], dtype = '<U32')

#Here is an example of how to advance subsetting. You want the third element from the first row,
#To select the row, you need the index "0" in square brackets. To get the third element you
#will need to extend the same call with another pair of square brackets with the index your
#element is at "2". You could do the something with a single bracket by dividing it with a
#comma. If you want multiple elements from both rows. You need to put a colon before the comma.
#Then put in the indices 1 to 3 after the comma. You could get all the elements of a row too by
#just selecting the row, a comma, and a empty colon inside the brackets.
#                   0     1     2     3     4
np_2d = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],   # 0
                 [65.4, 59.2, 63.6, 88.4, 68.7]])   # 1
print(np_2d[0][2])
print(np_2d[0, 3])
print(np_2d[: , 1:3])
print(np_2d[1, :])

#2D numpy arrays enable you to do element-wise calculations the same way you can do it with 1D
#arrays

#Your array's name followed with "+ updated" refers to modifying, reassigning, or mutating
#elements, slices, or the structure of that 2D array in code.

#--------------------------------------------------------------------------------------------
#Exercise

#MLB data, create a 2D numpy array.
baseball = ([180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2])
np_baseball = np.array(baseball)
print(type(np_baseball))
print(np_baseball.shape)

#--------------------------------------------------------------------------------------------