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
from romaniaMap import findCity, readInMap
# Import the breadth_search function
import breadthSearch
import depthFirst

romania = readInMap('romaniaMap.txt')

print("List of cities: ")
for i in romania:
	print(i.cityName)

start_city = input("Starting city: ")
goal_city = input("Destination: ")

if findCity(start_city, romania) == "False" or findCity(goal_city, romania) == "False":
	print("A city is not in the list")
else: 
	# path = breadthSearch.bfs(romania, start_city, goal_city)
	# # Print the result of the BFS function
	# if path: print("Breadth First Search Path:", path)
	# else:
	# 	print("No path found or cities are unreachable.")
	path = depthFirst.dfs(romania, start_city, goal_city)
	# Print the result of the BFS function
	if path: print("Depth First Search Path:", path)
	else:
		print("No path found or cities are unreachable.")