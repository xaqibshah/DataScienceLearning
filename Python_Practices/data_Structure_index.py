#define a list

food = ["Dahi Ballay", "Biryani", "Dall", "Samosay", "Shami","Palak Paneer"]
# print(food)

# print(food[0]) #first item in list
# print(food[-1])  # select from last in list

food[0] = "Chiken Puloe" 
# print(food)   


#2 tupple

coordinates = (4.21, 9.26)
# print(coordinates)
# print(coordinates[0])


#3 sets
#sets are used to store multiple items in a single variable
#sets are unordered, so you cannot be sure in which order the items will appear
#sets are unchangeable, meaning that we cannot change the items after the set has been created
#sets cannot contain duplicate values
#sets are written with curly brackets
#sets are written with curly brackets
food_set = {'Dahi Bhallay', "Biryani", "Daal", "Samosay", "Shami", "Palak Paneer"}
# print(food_set)
#add an element into the set
food_set.add("Pakora")
# print(food_set)

# 4 Dictionary

#dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
car = {
    'brand': 'Ford',
    'Model': "Mustang",
    'year': 1964
}
print(car['brand'])
car['year'] = 1970
print(car)


#add a new item to the original dictionary, and see that the keys list gets updated as well:
car['color'] = 'white'
print(car)





