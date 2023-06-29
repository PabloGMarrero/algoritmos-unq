from random import randint

class Graph:
    def __init__(self, size, edge_cost):
        self.size = size
        self.edge_cost = edge_cost
    
    def generate_matrix(self):
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

    