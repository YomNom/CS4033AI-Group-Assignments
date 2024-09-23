# Author : Khushbu Borwal
# Purpose: Implement A* algorithm
from collections import deque
import romaniaMap
from heuristic import get_heuristic1, get_heuristic2
from romaniaMap import findCity

# Implementation of A* algorithm
def a_star(map, startCity, goalCity, heuristic_choice):
    startIndex = findCity(startCity, map)
    if startIndex == 'False':
        return f"Start city {startCity} not found."

    goalIndex = findCity(goalCity, map)
    if goalIndex == "False":
        return f"Goal city {goalCity} not found."
    
    # Step 1: Initialize the frontier (priority queue) with the starting city
    # frontier contains tuples of (f(n), g(n), path)
    initial_heuristic = get_heuristic_choice(startCity, heuristic_choice)
    frontier = [(initial_heuristic, 0, [startIndex])] # f(n), g(n), and the path
    explored = set()  # Use a set for explored cities

    # Step 2: Start the loop
    while frontier:
        # Sort the frontier by the f(n) value (first element of the tuple)
        frontier.sort(key=lambda x: x[0])
        current_f, current_g, path = frontier.pop(0)
        current = path[-1] # The last city in the current path

        # Check if we have reach the goal
        if current == goalIndex:
            return " -> ".join(map[i].cityName for i in path)  # Join city names
        
        # Mark the current city as explored
        if current not in explored:
            explored.add(current)

            # Step 3: Explore the neighbors (routes from the current city)
            for arc in map[current].route:
                if arc.index not in explored:
                    new_g = current_g + int(arc.distance)  # Update the g(n) value
                    heuristic_value = get_heuristic_choice(map[arc.index].cityName, heuristic_choice)
                    f_value = new_g + heuristic_value  # f(n) = g(n) + h(n)
                    new_path = list(path)
                    new_path.append(arc.index)
                    frontier.append((f_value, new_g, new_path))  # Add the new path to the frontier
    
    return "Goal city not reachable from the start city."


def get_heuristic_choice(cityName, heuristic_choice):
    if heuristic_choice == 1:
        return get_heuristic1(cityName)
    elif heuristic_choice == 2:
        return get_heuristic2(cityName)
    else:
        return float('inf')  # Default to infinity if invalid choice
