# Group 17 - All members contributed in equal measure
#	Member Names: Afreen Alam, Joey Yong, Khushbu Borwal
# Honor Statement: 
# Bibliography: 
#	Reading text file - https://www.pythontutorial.net/python-basics/python-read-text-file/ 

# FILE: Assignment 1 SEARCH
# FALL 2024 CS 4033 Artificial Intelligence 
# Purpose: The driver file for implementing informed & uninformed search of a part of Romania
#	(1) Breadth Search
#	(2) Depth First
#	(3) Best First(greedy algorithm)
#	(4) A* Algorithm
import map
import depthFirst

romania = map.readInMap('romaniaMap.txt')

print("List of cities: ")
for i in romania:
	print(i.cityName)

start = input("Starting city: ")
end = input("Destination: ")

if findCity(start, romania) == "False" or findCity(end, romania) == "False":
	print("A city is not in the list")
else: 
	path = depthFirstSearch()
	printMap(path)