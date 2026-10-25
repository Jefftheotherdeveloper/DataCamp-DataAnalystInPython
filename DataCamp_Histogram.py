#DataCamp: "Data Analyst in Python" Course
#Topic: Histogram

#The histogram is a type of visualization that's very useful to explore data. That helps give
#an idea about the distribution of your variables. We can use histograms through matplotlib
#by calling ".hist()". There are many arguments hist can do but the first two are the most
#important: "x" should be a list of values you want to build and "bins" which tells python how
#many bins the data should be divided into.

import matplotlib.pyplot as plt
help(plt.hist)
values = [0, 0.6, 1.4, 2.2, 2.5, 2.6, 3.2, 3.9, 4.2, 6]
plt.hist(values, bins=3)
#If you don't specify the bins argument, it will be 10 by default
plt.show()

#Examples of other types of methods we can call
plt.clf()   # --> Stands for "Clear Figure" which removes all plots, subplots, axes, labels,
            #     labels, and title from the current active figure
plt.close() # --> Stands for "Close Window" which destroy and terminates he entire figure window
            #     and frees up memory space.
#--------------------------------------------------------------------------------------------
#Exercise

#Create a histogram of student's age in their freshman year of college using the data below
#and put into 10 bins
student_ages = [18,18,19,18,20,19,19,18,17,17,17,19,19,18,18,19,20,17,18,19]
plt.hist(student_ages, bins=10)
plt.show()

#--------------------------------------------------------------------------------------------