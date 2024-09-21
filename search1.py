# Group 17 - All members contributed in equal measure
#	Member Names: Afreen Alam, Joey Yong, Khushbu Borwal
# Honor Statement: 
# Bibliography: 
#

# FILE: Assignment 1 SEARCH
# FALL 2024 CS 4033 Artificial Intelligence 
# Purpose: The driver file for implementing informed & uninformed search of a part of Romania
#	(1) Breadth Search
#	(2) Depth First
#	(3) Best First(greedy algorithm)
#	(4) A* Algorithm
from romaniaMap import findCity, readInMap

import breadthSearch
import depthFirst
path = []

# Nodes of cities are allocated into an array from an external file
romania = readInMap('romaniaMap.txt')

print("\nList of cities to travel from and to: ")
for i in romania:
	print(i.cityName)

start_city = input("\nTraveling from: ")
goal_city = input("Destination: ")

if findCity(start_city, romania) == "False" or findCity(goal_city, romania) == "False":
	print("Uh-Oh! A city was typed in wrong! BYE!")
else: # Correct input for start_city and goal_city
	implementSearch = int(input("Which search algorithm should be implemented?\n(1) Breadth Search\n(2) Depth First\n(3) Greedy Search\n(4) A* Algorithm\n(Enter value from 1 to 4): "))

	match(implementSearch):
		case 1: # Breadth Search
			path = breadthSearch.bfs(romania, start_city, goal_city)
		case 2: # Depth First
			path = depthFirst.dfs(romania, start_city, goal_city)
		case 3: # Greedy/Best Search
			path = "Greedy"
		case 4: # A* Algorithm
			path = "A* Algorithm"
		case default: 
			print("No search implementation chosen")

	if path: print("Path from ", start_city, " to ", goal_city, ": ", path, "\n")
	else: print("No path found or cities are unreachable.")

	