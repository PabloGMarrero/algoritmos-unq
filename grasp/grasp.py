class Grasp():
    def __init__(self, random_greedy, adaptive_search, max_search_procedure,limit_adaptive_search, matrix, searches ) -> None:
        self.random_greedy = random_greedy
        self.adaptive_search =adaptive_search
        self.max_search_procedure = max_search_procedure
        self.limit_adaptive_search = limit_adaptive_search
        self.matrix = matrix
        self.searches = searches

    def do_grasp(self, local_searches):
        amount_times = 0
        #better_solution = []
        #better_cost = 0

        better_solution, better_cost = self.random_greedy.get_circuit()
        #print("GR best, GR cost", better_solution, better_cost)
        as_best_solution, as_best_cost = self.adaptive_search.search(better_solution, better_cost, self.matrix, self.limit_adaptive_search, local_searches)
        #print("AS best, as cost", as_best_solution, as_best_cost)
        
        if as_best_cost < better_cost:
            better_solution = as_best_solution
            better_cost = as_best_cost

        self.searches.append((better_cost, as_best_cost))
        limit = self.limit_adaptive_search
        #print("-----------WHILE------------")
        while(self.max_search_procedure > amount_times and limit > 1):
            amount_times = amount_times + 1

            self.random_greedy.reset()
            greedy_circuit, greedy_circuit_cost = self.random_greedy.get_circuit()
            as_best_solution, as_best_cost = self.adaptive_search.search(greedy_circuit, greedy_circuit_cost, self.matrix, self.limit_adaptive_search, local_searches)
        
            #print("GR best, GR cost", greedy_circuit, greedy_circuit_cost)
            #print("AS best, as cost", as_best_solution, as_best_cost)

            if greedy_circuit_cost < as_best_cost :
                as_best_cost = greedy_circuit_cost
                as_best_solution = greedy_circuit_cost

            if as_best_cost < better_cost:
                better_choice = (better_cost-as_best_cost)/better_cost*100
                #if limit > abs(better_choice):
                    #limit = -1
                better_solution = as_best_solution
                better_cost = as_best_cost
                
            
            self.searches.append((greedy_circuit_cost, as_best_cost))
        
        return better_solution, better_cost