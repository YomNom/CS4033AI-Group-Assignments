# Author : Khushbu Borwal
# Purpose: Implement Breadth Search algorithm

from collections import deque
from romaniaMap import findCity

# Implementation of Breadth Search algorithm
def bfs(map, startCity, goalCity):
    startIndex = findCity(startCity, map)
    if startIndex == "False":
        return f"Start city {startCity} not found."

    goalIndex = findCity(goalCity, map)
    if goalIndex == "False":
        return f"Goal city {goalCity} not found."

    # Step 1: Initialize the frontier (queue) with the starting city
    frontier = deque([[startIndex]])  # Store paths instead of just indices
    explored = set()  # Use a set for explored cities

    # Step 2: Start the BFS loop
    while frontier:
        path = frontier.popleft()  # Get the first path from the queue
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
                    frontier.append(new_path)  # Add the new path to the queue

    return "Goal city not reachable from the start city."
