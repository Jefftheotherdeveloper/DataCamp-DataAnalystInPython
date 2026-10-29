#DataCamp: "Data Analyst in Python" Course
#Topic: Pandas Part 2

#There are a few ways to index and select data from DataFrames
import pandas as pd
dict = {
    'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
    'capital': ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
    'area': [8.516, 17.10, 3.286, 9.597, 1.221],
    'population': [200.4, 143.5, 1252, 1357, 52.98]}
brics = pd.DataFrame(dict)
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']

#Let's say that you want to only select a specific column from your DataFrame then all you need
#to do is write your DataFrame's name followed with your column's label inside square brackets
print(brics['country'])
#You will normally ger the whole column's data and indexes even with the "dtype" set as "object"
#but if you call the type function you will see it's a Pandas Series
print(type(brics['country']))
#A series can be thought as a 1-dimensional array that cen be labeled just like DataFrame and
#if you paste a bunch of Series then you can create a DataFrame

#If you want to select a column and keep the data in a DataFrame then you will need double
#square brackets. You can extend this call to select as many columns as you want by separating
#them with a comma. You can even check if the type is a DataFrame instead of Series using the
#type function again.
print(brics[['country', 'capital']])
#If you want to select rows then you will need to specify a slice. "_ : _"
print(brics[1:4])

#Square brackets works, but it is limited functionality, and ideally you want something similar
#to 2D NumPy arrays "my_array(rows, columns)". You will need to use Panda's "loc" (label-based)
#"iloc" (integer position-based) functions. loc is a technique to select parts of your data
#based on labels, iloc is position based

#For "loc", you put the labels of the row of interest in square brackets after loc
print(brics.loc[['RU']])
print(brics.loc[['RU', 'IN', 'CH'], ['country', 'capital']])
#The difference is that you can extend your selection with a common and a specification of the
#columns of interest since this is much more versatile: you can select rows and columns at the
#same time.

#If you want to subset Pandas DataFrame based on their position or index, you will need the
#"iloc" function. To get the rows, you will need a list
print(brics.iloc[[1]])
print(brics.iloc[[1,2,3]])
print(brics.iloc[[1,2,3], [0,1]])