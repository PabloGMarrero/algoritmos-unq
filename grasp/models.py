from random import randint
import os

class Graph:
    def __init__(self, size):
        self.size = size
        self.edge_cost = None

    def generate(self):
        graph_path = f"resources/graphs/test_graph_{self.size}.txt"

        if not os.path.exists(graph_path):
            self.write_graph(f"resources/graphs/test_graph_{self.size}.txt", self.size)

        num_rows, matrix, tasks = self.read_graph(graph_path)

        return num_rows, matrix, tasks

    def init_with(self, size, edge_cost):
        self.size = size
        self.edge_cost = edge_cost
    
    def write_graph(self, filename, nodes):
        matrix = [[str(0) for x in range(nodes)] for y in range(nodes)]
        for i in range(0, nodes):
            for j in range (i+1, nodes):
                max_value = 1000 if self.edge_cost is None else self.edge_cost 
                value = str(randint(1, max_value)) 
                matrix[i][j] = value
                matrix[j][i] = value

        matrix = map(lambda row: ' '.join(row), matrix)

        tasks = [str(randint(1, 100)) for y in range(nodes)]
        tasks = ' '.join(tasks)

        graph_file = open(filename,"w")
        graph_file.write(str(nodes) + "\n")
        for row in matrix:
            graph_file.write(row + "\n")
        graph_file.write(tasks)
        graph_file.close()

    def read_graph(self, filename):
        with open(filename) as f:
            matrix = []         #Lista que contiene cada fila
            num_rows = int(f.readline())
            for row_index in range(num_rows):
                line = f.readline()
                row = [int(x) for x in line.split()] # Split en whitespace y castear cada elemento a int
                matrix.append(row)
            tasks = f.readline()
            tasks = [int(x) for x in tasks.split()]
        #print(matrix)
        #print(tasks)
        return num_rows, matrix, tasks

    def generate_random_matrix(self):
        
        outside_size = self.size # How many nested lists to include
        inside_size = self.size  # How many numbers will be in an inside list
        outside_list = [] # The final list
        max_number = self.edge_cost

        for i in range(0, outside_size, 1):
            _list = [] # Create new "inside" (nested) list
            for j in range(0, inside_size, 1): # Populate the nested list with random numbers
                if (i == j):
                    _list.append(0)
                else:
                    _list.append(randint(1, max_number))
            outside_list.append(_list) # Add the inside (nested) list to the outside (final) list
    
        return outside_list

    