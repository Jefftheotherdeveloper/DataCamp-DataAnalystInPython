#DataCamp: "Data Analyst in Python" Course
#Topic: Customization

#There are many options for data visualization: different plot types, customizations like the
#color, shapes, labels, axes which mainly depends on the data and what you are trying to tell
#with the data.

import matplotlib.pyplot as plt
year =       [1950, 1970, 1990, 2010, 2030, 2050, 2070, 2090, 2110]
population = [2.519, 3.692, 5.163, 6.972, 7.762, 8.528, 8.907, 9.653, 10.498]

plt.plot(year, population)

#You can give the data visualization a title by using the ".title()" function. To label our
#axis, we need to call the for ".xlabel()" and ".ylabel()" functions and write what text you
#would like the axis to represent.
plt.title('World Population Projections')
plt.xlabel('Year')
plt.ylabel('Population')

#You can control the x and y ticks by specifying two arguments, by using the ".yticks()" or "xticks()"
#it creates a list which allows you to represent data from an existing starting point or to even
# make it more clear, it would be the same length.
plt.yticks([0,2,4,6,8,10],
           ['0','2B', '4B', '6B', '8B', '10B'])

#You can even add a grid to your chart by using the ".grid()" function and setting the parameters
#to "True"
plt.grid(True)
plt.show()
#--------------------------------------------------------------------------------------------
#Exercise

#You can assign premade variables to represent your x-axis and y-axis too
year = [1950, 1970, 1990, 2010, 2030, 2050, 2070, 2090, 2110]
population = [2.519, 3.692, 5.163, 6.972, 7.762, 8.528, 8.907, 9.653, 10.498]
plt.scatter(year, population)
xlab = 'Increasing Years'
ylab = "World's Population"
title = 'World Development in Population'
plt.xlabel(xlab)
plt.ylabel(ylab)
plt.title(title)
plt.grid(True)
plt.show()


#--------------------------------------------------------------------------------------------