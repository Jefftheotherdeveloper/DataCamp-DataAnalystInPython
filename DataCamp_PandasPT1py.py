#DataCamp: "Data Analyst in Python" Course
#Topic: Pandas Part 1

#If you try to add another key value pair to the same key, the last pair you specified in the
#curly brackets will be kept in the resulting dictionary
population = [30.55, 2.77, 39.21]
countries = ['afghanistan', 'albania', 'algeria']
world = {'afghanistan':30.55, 'albania':2.77, 'algeria':39.21, 'albania':2.81}
print(world)

#Keys should be "immutable" objects so once they are created, they can't be changed. But the
#list is mutable because you can change its contents after it's created. If you could like to
#add/update another key value to the list then you need to call your list's name in square and
#then assign the update. You can even find if it's true by writing the name as '___' in '___'
#your list's name
world['germany'] = 0.000028
print(world)
print('germany' in world)

#You can remove/delete a key value by using the "del()" function and pointing to the key inside
#the square brackets from the list
del(world['germany'])

#List and dictionaries are pretty similar: You can select, update, and remove elements with
#square brackets. Lists is a sequence of values that are indexed by a range of numbers while the
#dictionary is indexed by unique keys that can be any immutable type. You should use a list when
#you have a collection of values and the order matters for selecting entire subsets and use
#a dictionary when you need a sort of look up table, where looking for data should be fast
#--------------------------------------------------------------------------------------------
#Exercise
countries2 = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris' 'berlin', 'oslo']
europe = {'spain':'madrid', 'france':'paris', 'germeny':'berlin', 'norway':'oslo'}
europe['italy'] = 'rome'
europe['poland'] = 'warsaw'
print('italy' in europe)
print(europe)

#You can put a dictionary inside of dictionaries. They contain key values pairs that the values
#are also dictionaries. Below is an example:
europe2 = { 'spain': {'capital':'madrid', 'population':46.77},
            'france': {'capital':'paris', 'population':66.03},
            'germany': {'capital':'berlin', 'population':80.62},
            'norway': {'capital':'oslo', 'population':5.084}}
#You can chain square brackets to select elements. Example to get the population from Spain:
print(europe2['spain']['population'])
#Create a sub-dictionary called "new_data" and then add it under "italy" to the list
new_data = {'capital':'rome', 'population':59.83}
europe2['italy'] = new_data
print(europe2)
#--------------------------------------------------------------------------------------------