from models import Graph
from strategies import Greedy
from strategies import RandomGreedy
from adaptive_search import AdaptiveSearch
from grasp import Grasp
from graphic import Graphic
import sys

"""g = Graph(500, edge_cost=500)
num_rows, matrix, tasks = g.read_graph("resources/graphs/test_graph_1000.txt")
#matrix = g.write_graph("resources/graphs/test_graph_50.txt", 50)

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
graphic.do_grasp_graphic(searches, save=True, path_to_save=f'output/graphics/grasp_{num_rows}.png')
graphic.do_bl_graphic(local_searches, save=True, path_to_save=f'output/graphics/bl_{num_rows}.png')
"""
import os

if __name__ == "__main__":
    nodes = int(sys.argv[1])
    
    print(nodes)
    g = Graph(nodes)
    
    graph_path = f"resources/graphs/test_graph_{nodes}.txt"

    if not os.path.exists(graph_path):
        g.write_graph(f"resources/graphs/test_graph_{nodes}.txt", nodes)

    num_rows, matrix, tasks = g.read_graph(graph_path)

    random_greedy = RandomGreedy(matrix)
    adaptive_search = AdaptiveSearch()


    #limit_adaptive_search=5.0
    #max_search_procedure=50
    limit_adaptive_search = float(sys.argv[2])
    max_search_procedure = int(sys.argv[3])
    solution=None
    searches = []
    local_searches = []
    grasp_1 = Grasp(random_greedy, adaptive_search, max_search_procedure, limit_adaptive_search, matrix, searches)
    grasp_result = grasp_1.do_grasp(local_searches)

    graphic = Graphic(len(matrix))
    graphic.do_grasp_graphic(searches, save=True, path_to_save=f'output/graphics/grasp_rows_{num_rows}_as_{limit_adaptive_search}_max-iterations{max_search_procedure}.png')
    graphic.do_bl_graphic(local_searches, save=True, path_to_save=f'output/graphics/bl_{num_rows}_as_{limit_adaptive_search}_max-iterations{max_search_procedure}.png')

    