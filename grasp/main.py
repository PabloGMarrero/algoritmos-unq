from models import Graph
from strategies import Greedy
from strategies import RandomGreedy
from adaptive_search import AdaptiveSearch
from grasp import Grasp
from graphic import Graphic

g = Graph(100, edge_cost=500)
matrix = g.generate_matrix()
#print(matrix)

#greedy = Greedy(matrix=matrix)
#circuit_greedy = greedy.get_circuit()
#print(circuit_greedy)


random_greedy = RandomGreedy(matrix)
#circuit_random_greedy, better_distance = random_greedy.get_circuit()
#print("Circuit", circuit_random_greedy)
#print("Better distance", better_distance)

adaptive_search = AdaptiveSearch()
#adaptive_solution = adaptive_search.search(circuit_random_greedy, better_distance, matrix, limit=10.0)
#print("Adaptive solution: ", adaptive_solution)

limit_adaptive_search=5.0
max_search_procedure=50
solution=None
searches = []
local_searches = []
grasp_1 = Grasp(random_greedy, adaptive_search, max_search_procedure, limit_adaptive_search, matrix, searches)
grasp_result = grasp_1.do_grasp(local_searches)
#print(local_searches)
#print(grasp_result)
#print (searches)

graphic = Graphic(len(matrix))
graphic.do_grasp_graphic(searches)
graphic.do_bl_graphic(local_searches)

