# FILE: map.py
# Purpose: Holds map class and functions

class CityNode: 
	def _init_(cityName):
		self.cityName = cityName
		self.used = false
		self.route = [] 

class Arc(): 
	def _init_(i, distance): 
		self.index = i
		self.distance = distance

def findCityIndex(cityToFind, map[]): 


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
	with open(fileInput) as f: 
		for line in f: 

			# Splits line from file and removes line breaks
			Route = line.split(' ')
			Route[2] = Route[2].strip()

			print(Route) 

			GoTo = Arc(Route[1], Route[2])
			map.append(CityNode(Route[0]))



