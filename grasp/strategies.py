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

    def reset(self):
        self.visited = [False] * self.matrix_length
        self.circuit = [None] * self.matrix_length

    def get_circuit(self) -> List[int]:

        start_vertex = random.randint(0, self.matrix_length-1)
        current_vertex = start_vertex
        self.visited[current_vertex] = True
        self.circuit[0] = current_vertex
        better_distance = 0

        for i in range(1, self.matrix_length):
            near_vertex = -1
            min_distance = sys.maxsize

            random_vertexes = self.get_better_vertexes(self.visited, self.matrix, current_vertex)
            
            if len(random_vertexes) !=0:
                random_vertex = random.choice(random_vertexes)
                near_vertex = random_vertex[0]
            
                #if not min_distance == sys.maxsize:
                #    better_distance = better_distance - min_distance
                min_distance = random_vertex[1]
                if not min_distance == sys.maxsize:
                    better_distance = better_distance + min_distance

                    #if near_vertex == -1:
                    #    near_vertex = start_vertex

                current_vertex = near_vertex
                self.visited[current_vertex] = True
                self.circuit[i] = current_vertex
    

        return self.circuit, better_distance
    
    def get_better_vertexes(self, visited, matrix, current):
        non_visited_elements = []
        
        neighbors = matrix[current]
        for i in range(0, len(neighbors)):
            if not visited[i] and neighbors[i] !=0:
                non_visited_elements.append((i, neighbors[i]))

        non_visited_elements.sort(key=lambda tup:(tup[1], tup[0]))
        slice_value = 5

        if len(non_visited_elements) < slice_value:
            return non_visited_elements

        return non_visited_elements[0:slice_value]


