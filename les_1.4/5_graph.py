class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        return_nubmers = []
        available_numbers = [i for i in range(Graph.LIMIT_Y[0], Graph.LIMIT_Y[1]+1)]
        for i in self.data:
            if i in available_numbers:
                return_nubmers.append(str(i))
        
        return " ".join(return_nubmers)
    

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
print(graph_1.draw())
