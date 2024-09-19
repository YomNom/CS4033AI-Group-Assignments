# FILE: map.py
# Purpose: Holds map class and functions

class CityNode: 
	def _init_(cityName):
		self.cityName = cityName
		self.used = false
		self.route = [ToCity] 

class ToCity(CityNode): 
	def _init_(i, distance): 
		self.index = i
		self.distance = distance

# Reads in a text file containing information about the routes
# Pre-Cond: Text file should be in the same folder as this file(map.py)
# INPUT: fileInput - name of file to read data from
# OUTPUT: Data read into a linked list representing the map
##########################################################################
#### TEXT FILE format: 
#####	Name of city from
#####	Name of city to
#####   Distance between two cities
#####   ...
def readInMap(fileInput): 


