# FILE: greedySearch.py
# Purpose: Implements algorithm Greedy Search i.e. Best Search
# 	The queue is maintained in nondecreasing order of the straight line distance formula, h(n),
#	of the children of the current city to the goal city
import romaniaMap

import heuristic

sld = heuristic.get_heuristic('Lugoj')

print(sld)