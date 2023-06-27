from typing import List
import random
import sys 

class Strategy():

    def __init__(self, matrix):
        self.matrix = matrix
        self.matrix_length = len(matrix)
        self.visited = [False] * self.matrix_length
        self.circuit = [None] * self.matrix_length

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

    def get_circuit(self) -> List[int]:

        start_vertex = random.randint(0, 9)
        current_vertex = start_vertex
        self.visited[current_vertex] = True
        self.circuit[0] = current_vertex
        better_distance = 0

        for i in range(0, self.matrix_length, 1):
            near_vertex = -1
            min_distance = sys.maxsize

            random_vertex = self.get_random_vertex(self.visited, self.matrix)
            
            for j in random_vertex:
                if(not self.visited[j] and self.matrix[current_vertex][j] < min_distance):
                    near_vertex = j
                    if not min_distance == sys.maxsize:
                        better_distance = better_distance - min_distance
                    min_distance = self.matrix[current_vertex][j]
                    if not min_distance == sys.maxsize:
                        better_distance = better_distance + min_distance
        
            if near_vertex == -1:
                near_vertex = start_vertex

            current_vertex = near_vertex
            self.visited[current_vertex] = True
            self.circuit[i] = current_vertex

            

        return self.circuit, better_distance
    
    def get_random_vertex(self, visited, matrix):
        vertex = range(0, len(matrix))
        non_visited_elements = []

        max_size = 5

        for i in vertex:
            if not visited[i]:
                non_visited_elements.append(i)

        if len(non_visited_elements) < max_size:
            return non_visited_elements
    
        return random.sample(non_visited_elements, max_size)


