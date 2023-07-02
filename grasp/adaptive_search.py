class AdaptiveSearch():
    
    ## O(n)
    def get_costo_circuito(self, matrix, solution):
        costo = 0

        for i in range(0, len(solution)):
            costo = costo + matrix[solution[i-1]][solution[i]]
        
        return costo

    ## O(n^2)
    def neighbor_search_swapping(self, solution, cost, matrix, neighbor_searches):
        i = 0
        #isBetter = False
        size_solution = len(solution)
        best_cost = cost
        best_solution = solution

        #while not isBetter and i < size_solution:
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

            swap_cost = self.get_costo_circuito(matrix, list_swap)

            ## explorar toda la solución 
            if swap_cost < best_cost:
                best_solution = list_swap
                best_cost = swap_cost
                #isBetter = True
        
            neighbor_searches.append(swap_cost)

            i= i+1

        return best_solution, best_cost
       

    def search(self, greedy_solution, better_distance, matrix, limit, local_searches):
        best_solution = greedy_solution
        best_cost = better_distance
        isBest = True
        iterations = 0
        neighbor_searches = []

        while isBest and limit > 0:
            # ver de pasarle limite par que corte y no explore todos si la mejora es baja
            neighbor_cycle, neighbor_cost = self.neighbor_search_swapping(best_solution, best_cost, matrix, neighbor_searches)
            
            if neighbor_cost < best_cost:
                better_choice = (best_cost-neighbor_cost)/best_cost*100
                #if not abs(better_choice) < limit:
                mejora_minima_apreciable = best_cost * 0.01
                if better_choice < mejora_minima_apreciable:
                    isBest = False
                
                best_solution = neighbor_cycle
                best_cost = neighbor_cost
            
            if neighbor_cost == best_cost:
                iterations = iterations + 1
                if iterations > 10:
                    isBest = False

            local_searches.append(neighbor_searches)

        return (best_solution, best_cost)

    
