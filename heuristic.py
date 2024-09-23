# Heuristic 1: Straight line distance to Craiova calculated using the Straight Line Distance to Bucharest given in the book
def get_heuristic1(cityName):
    # Define a dictionary with heuristic values for each city
    heuristic_values = {
    'Arad' : 521,
    'Bucharest' : 160,
    'Craiova' : 0,
    'Drobeta' : 115,
    'Eforie' : 316,
    'Fagaras' : 333,
    'Giurgiu' : 232,
    'Hirsova' : 306,
    'Iasi' : 381,
    'Lugoj' : 339,
    'Mehadia' : 396,
    'Neamt' : 389,
    'Oradea' : 535,
    'Pitesti' : 133,
    'Rimnicu_Vilcea' : 141,
    'Sibiu' : 408,
    'Timisoara' : 484,
    'Urziceni' : 235,
    'Vaslui' : 354,
    'Zerind' : 529
}
    
    return heuristic_values.get(cityName, float('inf'))  # Return heuristic or infinity if city not in list

# Heuristic 2: Straight line distance to Craiova calculated using path cost estimate given on the Romania map and intermediate cities
def get_heuristic2(cityName):
    # Define a dictionary with heuristic values for each city
    heuristic_values = {
    'Arad' : 341,
    'Bucharest' : 224,
    'Craiova' : 0,
    'Drobeta' : 115,
    'Eforie' : 468,
    'Fagaras' : 300,
    'Giurgiu' : 304,
    'Hirsova' : 392,
    'Iasi' : 518,
    'Lugoj' : 245,
    'Mehadia' : 180,
    'Neamt' : 595,
    'Oradea' : 352,
    'Pitesti' : 133,
    'Rimnicu_Vilcea' : 141,
    'Sibiu' : 211,
    'Timisoara' : 346,
    'Urziceni' : 304,
    'Vaslui' : 436,
    'Zerind' : 406
}
    
    return heuristic_values.get(cityName, float('inf'))  # Return heuristic or infinity if city not in list