# FILE: map.py
# Purpose: Holds map class and functions

class CityNode: 
	def __init__(self, cityName):
		self.cityName = cityName
		self.used = False
		self.route = [] 

class Arc(): 
	def __init__(self, i, distance): 
		self.index = i
		self.distance = distance

# By JY
# Looks for a city in the map List
# INPUT: cityToFind - a string of the city name
#		 map - an array to look for the city in
# OUTPUT: index of where the city was in the List
#		  False if no city was found
def findCity(cityToFind, map): 
	for i in range(len(map)): 
		if map[i].cityName == cityToFind:
			return i
	return "False"

# By JY
# Prints out an array of the class CityNode
def printMap(map): 
	for i in map:
		print(i.cityName)
		for x in i.route:
			print(x.index, x.distance)

# By JY
# Reads in a text file containing information about the routes
# Note: Text file should be in the same folder as this file(map.py)
# INPUT: fileInput - string containing name of file to read data from
# OUTPUT: Data read into a linked list representing the map
##########################################################################
#### TEXT FILE format: 
#####	Name of city from
#####	Name of city to
#####   Distance between two cities
#####   ...
def readInMap(fileInput): 
	map = []

	f = open(fileInput, 'r')
	for line in f: 
		# Splits line from file and removes line breaks
		Road = line.split(' ')
		Road[2] = Road[2].strip()

		# Adding city to map if its not there
		cityFrom = findCity(Road[0], map)
		if cityFrom == "False": # Not on map
			map.append(CityNode(Road[0]))
			cityFrom = findCity(Road[0], map)

		cityTo = findCity(Road[1], map)
		if cityTo == "False": 
			map.append(CityNode(Road[1]))
			cityTo = findCity(Road[1], map)

		cityArc = Arc(cityTo, Road[2])
		map[cityFrom].route.append(cityArc)
		cityArc = Arc(cityFrom, Road[2])
		map[cityTo].route.append(cityArc)
	f.close()
	return map
