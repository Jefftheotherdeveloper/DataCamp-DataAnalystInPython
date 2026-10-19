#DataCamp: "Data Analyst in Python" Course
#Topic: NumPy - BasicStatistics

import numpy as np
#We will deal with thousands, millions or even billion data.
#         Height | Weight
np_city = ([1.64, 71.78],
           [1.37, 63.35],
           [1.6, 55.09],
           [2.04, 74.85],
           [2.04, 68.72],
           [2.01, 73.57])
np_city = np.array(np_city)
#You can use numpy's mean and median function to find the averages
np.mean(np_city[:,0])
np.median(np_city[:,0])
#Examples of other functions we can use:
np.std(np_city[:,0]) #Standard deviation
np.corrcoef(np_city[:,0], np_city[:,1]) #If two data are correlated
np.sort(np_city[:,0]) #sort the data in order
np.sum(np_city[:,0]) #Add the data together

#You can numpy randomly generate data to simulate using the "random.normal" function and
#also use "column_stack" to paste your variables together in columns
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 0.20, 5000), 2)
np_city = np.column_stack((height, weight))


#--------------------------------------------------------------------------------------------
#Exercise

#Create a baseball array with player's height and weight and then print out the mean and median
#height
baseball = ([180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2])
np_baseball = np.array(baseball)
np_height_in = np_baseball[:,0]
print(np.mean(np_height_in))
print(np.median(np_height_in))

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

med = np.median(np_baseball[:,0])
print("Median: " + str(med))

stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

corr = np.corrcoef(np_baseball[:,0], np_baseball[:,0])
print("Correlation: " + str(corr))

#--------------------------------------------------------------------------------------------