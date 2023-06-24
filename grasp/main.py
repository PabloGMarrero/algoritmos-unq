from models import Graph
from strategies import Greedy
from strategies import RandomGreedy

g = Graph(10)
matrix = g.generate_matrix()
print(matrix)

greedy = Greedy(matrix=matrix)
random_greedy = RandomGreedy(matrix=matrix)

#circuit_greedy = greedy.get_circuit()
#print(circuit_greedy)

circuit_random_greedy = random_greedy.get_circuit()
print(circuit_random_greedy)