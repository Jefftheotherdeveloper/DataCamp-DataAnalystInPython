#DataCamp: "Data Analyst in Python" Course
#Topic: Dictionaries Part 1

population = [30.55, 2.77, 39.21]
countries = ['afghanistan', 'albania', 'algeria']

#We can use the index function to look for specific things in a list but this can be very insufficient
#with a large amoutn of data
ind_alb = countries.index('albania')

#You can convert your data into a dictionary, inside the curly brackets are our key value pairs
world = {'afghanistan':30.55, 'albania':2.77, 'algeria':39.21}
print(world['albania'])
#Doing this will allow you to pass the key in the square brackets and gets you the corresponding
#value which is much easier than finding the index of a list

#--------------------------------------------------------------------------------------------
#Exercise
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris' 'berlin', 'oslo']
europe = {'spain':'madrid' ,'france':'paris' , 'germeny':'berlin' , 'norway':'oslo'}
print(europe.keys())
print(europe)
#-------------------------------------------------------------'-------------------------------