# FILE: Assignment 1 SEARCH
# FALL 2024 CS 4033 Artificial Intelligence 
# Purpose: The driver file for implementing informed & uninformed search of a part of Romania
#	(1) Breadth Search
#	(2) Depth First
#	(3) Best First (greedy algorithm)
#	(4) A* Algorithm

from romaniaMap import findCity, readInMap

import breadthSearch
import depthFirst
import greedySearch
import aAlgorithm

path = []

# Nodes of cities are allocated into an array from an external file
romania = readInMap('romaniaMap.txt')

print("\nList of cities to travel from and to: ")
for i in romania:
    print(i.cityName)

start_city = input("\nTraveling from: ")

if findCity(start_city, romania) == "False":
    print("Uh-Oh! A city was typed in wrong! BYE!")
else:  # Correct input for start_city
    while True:
        goal_city = input("Destination (or type 'exit' to quit): ")
        if goal_city.lower() == 'exit':
            break

        if findCity(goal_city, romania) == "False":
            print("Uh-Oh! A city was typed in wrong! Please try again.")
            continue

        implementSearch = int(input("Which search algorithm should be implemented?\n"
                                     "(1) Breadth Search\n"
                                     "(2) Depth First\n"
                                     "(3) Greedy Search (fixed goal city: Craiova)\n"
                                     "(4) A* Algorithm (fixed goal city: Craiova)\n"
                                     "(Enter value from 1 to 4): "))

        match(implementSearch):
            case 1:  # Breadth Search
                path = breadthSearch.bfs(romania, start_city, goal_city)
            case 2:  # Depth First
                path = depthFirst.dfs(romania, start_city, goal_city)
            case 3:  # Best First Search
                goal_city = "Craiova"  # Fixed goal city for Greedy Search
                heuristic_choice = int(input("Which heuristic to use?\n(1) Heuristic 1\n(2) Heuristic 2\n(Enter value from 1 to 2): "))
                if heuristic_choice in [1, 2]:
                    path = greedySearch.best_first_search(romania, start_city, goal_city, heuristic_choice)
                else:
                    print("Invalid heuristic choice.")
            case 4:  # A* Algorithm
                goal_city = "Craiova"  # Fixed goal city for A* Algorithm
                heuristic_choice = int(input("Which heuristic to use?\n(1) Heuristic 1\n(2) Heuristic 2\n(Enter value from 1 to 2): "))
                if heuristic_choice in [1, 2]:
                    path = aAlgorithm.a_star(romania, start_city, goal_city, heuristic_choice)
                else:
                    print("Invalid heuristic choice.")
            case default: 
                print("No search implementation chosen")

        if path:
            print("Path from ", start_city, " to ", goal_city, ": ", path, "\n")
        else:
            print("No path found or cities are unreachable.")

    print("Thank you for using the program!")