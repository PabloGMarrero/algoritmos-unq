from typing import List
import random
import sys 

class Strategy():

    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_length = len(matrix)
        self.visited = [False] * self.matrix_length
        #self.circuit = [None] * self.matrix_length
        self.circuit = []

    def get_circuit(self, matrix) -> List[int]:
        pass

class Greedy(Strategy):

    def __init__(self, matrix):
        super().__init__(matrix)

    def get_circuit(self) -> List[int]:
        start_vertex = 0 
        current_vertex = start_vertex
        self.visited[current_vertex] = True
        self.circuit[0] = current_vertex

        for i in range(0, self.matrix_length, 1):
            near_vertex = -1
            min_distance = sys.maxsize
            
            for j in range(0, self.matrix_length, 1):
                if(not self.visited[j] and self.matrix[current_vertex][j] <min_distance):
                    near_vertex = j
                    min_distance = self.matrix[current_vertex][j]
        
            if near_vertex == -1:
                near_vertex = start_vertex

            current_vertex = near_vertex
            self.visited[current_vertex] = True
            self.circuit[i] = current_vertex

        return self.circuit

class RandomGreedy(Strategy):

    def __init__(self, matrix):
        super().__init__(matrix)

    def reset(self):
        self.visited = [False] * self.matrix_length
        #self.circuit = [None] * self.matrix_length
        self.circuit = []

    #O(n^2 * log n) donde n son la cantidad de nodos
    def get_circuit(self) -> List[int]:

        start_vertex = random.randint(0, self.matrix_length-1) #O(1)
        index = 0 #O(1)
        current_vertex = start_vertex #O(1)
        self.visited[current_vertex] = True  #O(1)
        self.circuit.append(current_vertex) #O(1)
        better_distance = 0 #O(1)
        
         #O(n * n log n) = #O(n^2 * log n)
        while len(self.circuit) < self.matrix_length:
            near_vertex = -1
            min_distance = sys.maxsize

            random_vertexes = self.get_better_vertexes(self.visited, self.matrix, current_vertex) #O(n log n)

            random_destiny_vertex = random.choice(random_vertexes) #O(1)
            near_vertex = random_destiny_vertex[0] #O(1)

            min_distance = random_destiny_vertex[1] #O(1)
            if not min_distance == sys.maxsize: #O(1)
                better_distance = better_distance + min_distance #O(1)

            current_vertex = near_vertex #O(1)
            self.visited[current_vertex] = True #O(1)
            self.circuit.append(current_vertex) #O(1)
            index = index + 1 #O(1)

        self.circuit.append(start_vertex) #O(1)
        return self.circuit, better_distance #O(1)
    
    #O(n log n) donde n es la cantidad de nodos
    def get_better_vertexes(self, visited, matrix, current):
        non_visited_elements = []
        
        neighbors = matrix[current] #O(1)
        for i in range(0, len(neighbors)): #O(n) donde n son la cantidad de vecinos
            if not visited[i] and neighbors[i] !=0:
                non_visited_elements.append((i, neighbors[i]))

        non_visited_elements.sort(key=lambda tup:(tup[1], tup[0])) #O(n log n) donde n es la cantidad de non_visited_elements
        slice_value = int(len(non_visited_elements)*0.15)
        #slice_value = 5

        if len(non_visited_elements) < slice_value: #O(1)
            return non_visited_elements #O(1)
        
        if slice_value == 0: #O(1)
            return non_visited_elements #O(1)

        return non_visited_elements[0:slice_value] #O(1)


