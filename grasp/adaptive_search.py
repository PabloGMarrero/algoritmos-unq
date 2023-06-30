class AdaptiveSearch():
    
    def neighbor_search(self, solution, cost, matrix):
        iterations = len(matrix)
        best_local_change = 0
        best_i = -1
        best_j = -1

        for i in range(iterations-2):
            for j in range(i+2, iterations-1):
                # current cost
                cost_x = matrix[solution[i]][solution[i+1]] + matrix[solution[j]][solution[j+1]]
                # neighbor cost
                cost_y = matrix[solution[i]][solution[j]] + matrix[solution[i+1]][solution[j+1]]

                delta = cost_y - cost_x

                if delta < best_local_change:
                    best_local_change = delta
                    best_i = i
                    best_j = j

        if best_local_change < 0:
            solution[best_i+1:best_j+1:] = solution[best_i+1:best_j+1][::-1]
            cost = cost + best_local_change

        return solution, cost
    
    def get_costo_circuito(self, matrix, solution):
        costo = 0

        for i in range(0, len(solution)):
            costo = costo + matrix[solution[i-1]][solution[i]]
        
        return costo

    def neighbor_search_swapping(self, solution, cost, matrix):
        #i = 0
        isBetter = False
        size_solution = len(solution)
        best_cost = 0
        best_solution = solution

        """while not isBetter and i < size_solution:
            list_swap = []
            list_swap.extend(solution[0:i+1])
            if ( i+3 == size_solution):
                list_swap.extend(solution[i:i+3])
                i = i+3
            else:
                list_swap.append(solution[i+2]) #swapeo posicion dos adelante y lo pongo antes
                list_swap.append(solution[i+1]) #swapeo posicion siguiente y lo pongo después
                list_swap.extend(solution[i+3:size_solution]) ## meto el resto

            best_cost = self.get_costo_circuito(matrix, list_swap)

            ## explorar toda la solución 
            if best_cost < cost:
                best_solution = list_swap
                isBetter = True
        
            i= i+1"""
        for i in range(0, size_solution):
            list_swap = []
            list_swap.extend(solution[0:i+1])
            if ( i+3 == size_solution):
                list_swap.extend(solution[i:i+3])
                i = i+3
            else:
                list_swap.append(solution[i+2]) #swapeo posicion dos adelante y lo pongo antes
                list_swap.append(solution[i+1]) #swapeo posicion siguiente y lo pongo después
                list_swap.extend(solution[i+3:size_solution]) ## meto el resto

            best_cost = self.get_costo_circuito(matrix, list_swap)

            if best_cost < cost:
                best_solution = list_swap           

        return best_solution, best_cost
       

    def search(self, greedy_solution, better_distance, matrix, limit):
        best_solution = greedy_solution
        best_cost = better_distance
        isBest = True

        while isBest and limit > 0:
            # ver de pasarle limite par que corte y no explore todos si la mejora es baja
            neighbor_cycle, neighbor_cost = self.neighbor_search_swapping(best_solution, best_cost, matrix)
            
            if neighbor_cost < best_cost:
                better_choice = (best_cost-neighbor_cost)/best_cost*100
                if limit > abs(better_choice):
                    limit = -1
                best_solution = neighbor_cycle
                best_cost = neighbor_cost
            else:
                isBest = False

        return (best_solution, best_cost)

    
