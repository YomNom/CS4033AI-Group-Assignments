# FILE: depthFirst.py
# Implementation of uninformed search Depth-First Search
#		First child of current node is put in front of queue
import map

# INPUT: 
# OUTPUT: Path[] from initial city to goal city
#		  Number of nodes visited
def depthFirstSearch(initial, goal, map): 
	path = [] # expanding node
	current = initial

	if current == goal:
		return path.append(current)
	else:
		path.append(current)
		current.used = True

		for x in current.route:
			if map[x.index].used == False: # Unvisited node found
				return path.append(depthFirstSearch(map[x.index], goal, map))
		
		# No unvisited nodes
		return path

def allVisited(map): 
	for i in map: 
		if i.used == False:
			return False

	# No nodes found unused
	return True