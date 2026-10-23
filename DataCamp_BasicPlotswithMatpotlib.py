#DataCamp: "Data Analyst in Python" Course
#Topic: Basic plots with Matpotlib

#Data visualization is very important in data analysis

import matplotlib.pyplot as plt
year = [1950, 1970, 1990, 2010]
population = [2.519, 3.692, 5.263, 6.972]

#To plot this data as a line chart, we call our subpackage pyplot name and use ".plot()" following
#our two list names as arguments. To need to use the ".show()" function to display the plot. If you
#want to map your horizontal axis and vertical axis then you need to separate it with a common.
#         horizontal | vertical
plt.plot(year, population)
plt.show()

#You can even use the ".scatter" function to create a scatter plot
plt.scatter(year, population)
plt.show()

#--------------------------------------------------------------------------------------------
#Exercise

#Print the last item from year and population. Plot the x-axis and y-axis onto a line chart
#and lastly then display it
year = [1950, 1970, 1990, 2010, 2030, 2050, 2070, 2100]
population = [2.519, 3.692, 5.263, 6.972, 7.634, 8.567, 9.456, 10.849]
plt.plot(year, population)
plt.show()
#--------------------------------------------------------------------------------------------