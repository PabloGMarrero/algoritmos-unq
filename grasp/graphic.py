import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import sys
import datetime

class Graphic():
    def __init__(self, nodes) -> None:
        self.nodes = nodes
        
    def do_grasp_graphic(self, searches, start_vertex, save=False, path_to_save=None):

        plt.figure(1)
        plt.title(f"Resultados GRASP para {self.nodes} nodos comenzando por {start_vertex}")
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
        if not save:
            plt.show()

        if save:
            date = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            plt.savefig(path_to_save+"-"+date+".png")
    
    def do_bl_graphic(self, searches, save=False, path_to_save=None):

        plt.figure(2)
        plt.title(f"Resultados BL para {self.nodes} nodos")
        plt.xlabel("# iteraciones")
        plt.ylabel("test")

        """min_value = sys.maxsize
        bl_searches = []
        iterations = 0
        for search in searches:
            local_bl_searches = []
            for i in range(0, len(search)):
                val = search[i]
                if val < min_value:
                    min_value = val
                local_bl_searches.append(min_value)
                iterations = iterations + 1
            bl_searches.append(local_bl_searches)

        xpoints = np.array(range(0, iterations))
        ypoints = np.array(bl_searches)

        plt.plot(xpoints, ypoints, label = "With AS")
        plt.legend()"""

        #legend = []
        for search in searches:
            scoring = []
            min_value = sys.maxsize
            for i in range(0, len(search)):
                val = search[i]
                if val < min_value:
                    min_value = val
                scoring.append(min_value)
            #legend.append("BL"+str(len(search)))
            plt.plot(list(range(0, len(search))), scoring)

        plt.xlim(0, max([len(res) for res in searches]) + 1)
        plt.ylim(0, max([sol for res in searches for sol in res]) + 300)
        plt.legend()

        
        if not save:
            plt.show()

        if save:
            date = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            plt.savefig(path_to_save+"-"+date+".png")