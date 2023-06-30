import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import sys

class Graphic():
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        
    def do_graphic(self, searches, save=False):

        plt.figure(1)
        plt.title(f"Resultados GRASP para {self.nodes} nodos")
        plt.xlabel("# iteraciones")
        plt.ylabel("scoring")

        min_value = sys.maxsize
        xpoints = np.array(range(0, len(searches)))
        gr_searches = []
        for search in searches:
            val = search[1]
            if val < min_value:
                min_value = val
            gr_searches.append(min_value)

        ypoints = np.array(gr_searches)
        plt.plot(xpoints, ypoints, label = "With AS")


        x2 = np.array(range(0, len(searches)))
        as_searches = []
        min_value = sys.maxsize
        for search in searches:
            val = search[0]
            if val < min_value:
                min_value = val
            as_searches.append(min_value)

        y2 = np.array(as_searches)

        # plotting the line 2 points 
        plt.plot(x2, y2, label = "Without AS")

        plt.legend()
        plt.show()

        if save:
            plt.savefig("path_bl")
    