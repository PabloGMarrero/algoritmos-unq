class AdaptiveSearch():
    
    # O(n) donde n es el largo de la lista solution
    def get_costo_circuito(self, matrix, solution):
        costo = 0 #O(1)

        # O(n)
        for i in range(0, len(solution)):
            costo = costo + matrix[solution[i-1]][solution[i]] #O(1)
        
        return costo #O(1)

    ## O(n^2) donde n corresponde a la cantidad de nodos
    def neighbor_search_swapping(self, solution, cost, matrix, neighbor_searches):
        i = 0 #O(1)
        size_solution = len(solution) #O(1)
        best_cost = cost #O(1)
        best_solution = solution #O(1)

        #O(n * n) = O(n^2)
        while i < size_solution:    
            list_swap = []
            list_swap.extend(solution[0:i+1])
            if ( i+3 == size_solution):
                list_swap.extend(solution[i:i+3])
                i = i+3
            else:
                list_swap.append(solution[i+2]) #swapeo posicion dos adelante y lo pongo antes
                list_swap.append(solution[i+1]) #swapeo posicion siguiente y lo pongo después
                list_swap.extend(solution[i+3:size_solution]) ## meto el resto

            swap_cost = self.get_costo_circuito(matrix, list_swap) #O(n) donde n corresponde a la cantidad de nodos

            ## explorar toda la solución 
            if swap_cost < best_cost:
                best_solution = list_swap
                best_cost = swap_cost
                #isBetter = True
        
            neighbor_searches.append(swap_cost)

            i= i+1

        return best_solution, best_cost
       

    def search(self, greedy_solution, better_distance, matrix, limit, local_searches):
        best_solution = greedy_solution #O(1)
        best_cost = better_distance #O(1)
        isBest = True #O(1)
        iterations = 0 #O(1)
        neighbor_searches = [] #O(1)

        #O(n * n^2) = #O(n^3) donde n son la cantidad de nodos
        while isBest and limit > 0:
            neighbor_cycle, neighbor_cost = self.neighbor_search_swapping(best_solution, best_cost, matrix, neighbor_searches) #O(n^2)
            
            if neighbor_cost < best_cost:
                better_choice = (best_cost-neighbor_cost)/best_cost*100 #O(1)
                mejora_minima_apreciable = best_cost * 0.01 #O(1)
                if better_choice < mejora_minima_apreciable: #O(1)
                    isBest = False #O(1)
                
                best_solution = neighbor_cycle #O(1)
                best_cost = neighbor_cost #O(1)
            
            if neighbor_cost == best_cost: #O(1)
                iterations = iterations + 1 #O(1)
                if iterations > 10: #O(1)
                    isBest = False #O(1)

            local_searches.append(neighbor_searches) #O(1)

        return (best_solution, best_cost) #O(1)

    
