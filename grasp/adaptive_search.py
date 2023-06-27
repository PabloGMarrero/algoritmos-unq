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
       

    def search(self, greedy_solution, better_distance, matrix, result_iterations, limit):
        best_solution = greedy_solution
        best_cost = better_distance
        isBest = True

        while isBest and limit > 0:
            neighbor_cycle, neighbor_cost = self.neighbor_search(best_solution, best_cost, matrix)

            if neighbor_cost < best_cost:
                if limit % 5 == 0:
                    limit = -1
                best_solution = neighbor_cycle
                best_cost = neighbor_cost
            else:
                isBest = False
            
            result_iterations.append(best_cost)

        return (best_solution, best_cost)

    
