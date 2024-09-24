# Author : Khushbu Borwal
# Purpose: Implement Best First Search Algorithm
from romaniaMap import findCity
from heuristic import get_heuristic1, get_heuristic2  # Import the heuristic function

# Implementation of Best-First Search algorithm
def best_first_search(map, startCity, goalCity, heuristic_choice):
    startIndex = findCity(startCity, map)
    if startIndex == "False":
        return f"Start city {startCity} not found."

    goalIndex = findCity(goalCity, map)
    if goalIndex == "False":
        return f"Goal city {goalCity} not found."

    # Step 1: Initialize the frontier (priority queue) with the starting city
    initial_value = get_heuristic_choice(map[startIndex].cityName, heuristic_choice)
    frontier = [(initial_value, [startIndex])]  # Store paths instead of indices
    explored = set()

    while frontier:
        # Get the path with the lowest heuristic value
        frontier.sort(key=lambda x: x[0])
        current_heuristic, path = frontier.pop(0) # frontier.pop(0) = (5, [0,3]), 5 as the current_heuristic ans [0, 3] as the path
        current = path[-1]

        # Check if we reached the goal
        if current == goalIndex:
            return " -> ".join(map[i].cityName for i in path)  # Join city names

        explored.add(current)

        # Explore neighbors
        for arc in map[current].route:
            if arc.index not in explored:
                new_path = list(path)  # Copy the current path
                new_path.append(arc.index)  # Add neighbor to the new path
                frontier.append((get_heuristic_choice(map[arc.index].cityName, heuristic_choice), new_path))

    return "Goal city not reachable from the start city."

def get_heuristic_choice(cityName, heuristic_choice):
    if heuristic_choice == 1:
        return get_heuristic1(cityName)
    elif heuristic_choice == 2:
        return get_heuristic2(cityName)
    else:
        return float('inf')  # Default to infinity if invalid choice
