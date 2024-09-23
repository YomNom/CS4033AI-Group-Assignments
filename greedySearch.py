# bestFirstSearch.py
from romaniaMap import findCity
from heuristic import get_heuristic  # Import the heuristic function

# Best-First Search algorithm
def best_first_search(map, startCity, goalCity):
    startIndex = findCity(startCity, map)
    if startIndex == "False":
        return f"Start city {startCity} not found."

    goalIndex = findCity(goalCity, map)
    if goalIndex == "False":
        return f"Goal city {goalCity} not found."

    # Step 1: Initialize the frontier (priority queue) with the starting city
    frontier = [(get_heuristic(map[startIndex].cityName), [startIndex])]  # Store paths instead of indices
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
                frontier.append((get_heuristic(map[arc.index].cityName), new_path))

    return "Goal city not reachable from the start city."
