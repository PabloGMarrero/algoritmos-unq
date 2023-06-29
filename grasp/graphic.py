import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

class Graphic():
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        
    def do_graphic(self, searches, save=False):

        plt.figure(1)
        plt.title(f"Resultados para {self.nodes} nodos")
        plt.xlabel("# iteraciones")
        plt.ylabel("puntaje")

        #for i in range(0, len(searches)):
            #puntajes = [sol for sol in search]
        #    plt.plot(i, searches[i])

        #plt.xlim(0, max(searches) + 1)
        #plt.ylim(0, max(searches) + 300)
        xpoints = np.array(range(0, len(searches)))
        gr_searches = []
        for search in searches:
            gr_searches.append(search[1])

        ypoints = np.array(gr_searches)

        plt.plot(xpoints, ypoints, label = "With AS")

        x2 = np.array(range(0, len(searches)))
        as_searches = []
        for search in searches:
            as_searches.append(search[0])

        y2 = np.array(as_searches)

        # plotting the line 2 points 
        plt.plot(x2, y2, label = "Without AS")

        plt.legend()
        plt.show()

        if save:
            plt.savefig("path_bl")
    