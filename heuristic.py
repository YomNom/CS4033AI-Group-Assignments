# Straight line distance to Bucharest

def get_heuristic(cityName):
    # Define a dictionary with heuristic values for each city
    heuristic_values = {
    'Arad' : 366,
    'Bucharest' : 0,
    'Craiova' : 160,
    'Drobeta' : 242,
    'Eforie' : 161,
    'Fagaras' : 176,
    'Giurgiu' : 77,
    'Hirsova' : 151,
    'Iasi' : 226,
    'Lugoj' : 244,
    'Mehadia' : 241,
    'Neamt' : 234,
    'Oradea' : 380,
    'Pitesti' : 100,
    'Rimnicu Vilcea' : 193,
    'Sibiu' : 253,
    'Timisoara' : 329,
    'Urziceni' : 80,
    'Vaslui' : 199,
    'Zerind' : 374
}
    
    return heuristic_values.get(cityName, float('inf'))  # Return heuristic or infinity if city not in list