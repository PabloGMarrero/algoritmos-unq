class Grasp():
    def __init__(self, random_greedy, adaptive_search, max_search_procedure,limit_adaptive_search, matrix, searches ) -> None:
        self.random_greedy = random_greedy
        self.adaptive_search =adaptive_search
        self.max_search_procedure = max_search_procedure
        self.limit_adaptive_search = limit_adaptive_search
        self.matrix = matrix
        self.searches = searches

    #O(m) * O(n^3) donde m son la cantidad de veces y n son la cantidad de nodos.
    def do_grasp(self, local_searches):
        amount_times = 0 #O(1)

        better_solution, better_cost = self.random_greedy.get_circuit()#O(n^2 * log n) donde n son la cantidad de nodos
        as_best_solution, as_best_cost = self.adaptive_search.search(better_solution, better_cost, self.matrix, self.limit_adaptive_search, local_searches) #O(n^3)
        
        if as_best_cost < better_cost: #O(1)
            better_solution = as_best_solution #O(1)
            better_cost = as_best_cost #O(1)

        self.searches.append((better_cost, as_best_cost)) #O(1)
        #limit = self.limit_adaptive_search

        #O(m) * O(n^3) donde m son la cantidad de veces y n son la cantidad de nodos.
        while(self.max_search_procedure > amount_times):
            amount_times = amount_times + 1  #O(1)

            self.random_greedy.reset() #O(1)
            greedy_circuit, greedy_circuit_cost = self.random_greedy.get_circuit()#O(n^2 * log n) donde n son la cantidad de nodos
            as_best_solution, as_best_cost = self.adaptive_search.search(greedy_circuit, greedy_circuit_cost, self.matrix, self.limit_adaptive_search, local_searches) #O(n^3)


            if greedy_circuit_cost < as_best_cost: #O(1)
                as_best_cost = greedy_circuit_cost #O(1)
                as_best_solution = greedy_circuit_cost #O(1)

            if as_best_cost < better_cost: #O(1)
                better_choice = (better_cost-as_best_cost)/better_cost*100 #O(1)
                #if limit > abs(better_choice):
                    #limit = -1
                better_solution = as_best_solution #O(1)
                better_cost = as_best_cost #O(1)
                
            
            self.searches.append((greedy_circuit_cost, as_best_cost)) #O(1)
        
        return better_solution, better_cost #O(1)