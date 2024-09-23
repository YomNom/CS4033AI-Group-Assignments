# FILE: depthFirst.py
# Purpose: Implement depth first search algorithm
from collections import deque
from romaniaMap import findCity 

# By KB
# Depth First Search Algorithm
# INPUT: map(list of cityNodes)
#        startCity, endCity - cityNodes
# OUTPUT: Deque representing path to the goal city
def dfs(map, startCity, goalCity):
    startIndex = findCity(startCity, map)
    goalIndex = findCity(goalCity, map)

    # Step 1: Initialize the frontier (stack) with the starting city
    frontier = [[startIndex]]  # Store paths instead of just indices
    explored = set()  # Use a set for explored cities

    # Step 2: Start the DFS loop
    while frontier:
        path = frontier.pop()  # Get the last path from the stack (LIFO)
        current = path[-1]  # The last city in the current path

        # Check if we have reached the goal
        if current == goalIndex:
            return " -> ".join(map[i].cityName for i in path)  # Join city names

        # Mark the current city as explored
        if current not in explored:
            explored.add(current)

            # Step 3: Explore the neighbors (routes from the current city)
            for arc in map[current].route:
                if arc.index not in explored:
                    new_path = list(path)  # Create a new path
                    new_path.append(arc.index)  # Add the neighbor to the path
                    frontier.append(new_path)  # Add the new path to the stack

    return "Goal city not reachable from the start city."

# Example usage with romaniaMap.txt
# romania_map = map.readInMap('romaniaMap.txt')
# start_city = 'Arad'
# goal_city = 'Bucharest'
# print("Depth First Search Path:", dfs(romania_map, start_city, goal_city))