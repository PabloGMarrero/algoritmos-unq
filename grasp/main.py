from models import Graph
from strategies import Greedy
from strategies import RandomGreedy
from adaptive_search import AdaptiveSearch

g = Graph(10)
matrix = g.generate_matrix()
print(matrix)

greedy = Greedy(matrix=matrix)
random_greedy = RandomGreedy(matrix=matrix)

#circuit_greedy = greedy.get_circuit()
#print(circuit_greedy)

circuit_random_greedy, better_distance = random_greedy.get_circuit()
print("Circuit", circuit_random_greedy)
print("Better distance", better_distance)

adaptive_search = AdaptiveSearch()
adaptive_solution = adaptive_search.search(circuit_random_greedy, better_distance, matrix, result_iterations=[], limit=5)
print(adaptive_solution)