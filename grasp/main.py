from models import Graph
from strategies import Greedy
from strategies import RandomGreedy
from adaptive_search import AdaptiveSearch
from procedure import Procedure
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
procedure_1 = Procedure(random_greedy, adaptive_search, max_search_procedure, limit_adaptive_search, matrix, searches)
grasp_result = procedure_1.do_grasp()
#print(grasp_result)
#print (searches)

graphic = Graphic(len(matrix))
graphic.do_graphic(searches)