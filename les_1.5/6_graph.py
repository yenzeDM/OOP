class Graph:
    def __init__(self, data):
        self.data = data.copy()
        self.is_show = True


    def set_data(self, data):
        self.data = data

    def show_table(self):
        if not self.is_show:
            return "Отображение данных закрыто"
        return " ".join(list(map(str, self.data)))
        
    def show_graph(self):
        if not self.is_show:
            return "Отображение данных закрыто"
        return f'Графическое отображение данных: {" ".join(list(map(str, self.data)))}'

    def show_bar(self):
        if not self.is_show:
            return "Отображение данных закрыто"
        return f'Столбчатая диаграмма: {" ".join(list(map(str, self.data)))}'

    def set_show(self, fl_show):
        self.is_show = fl_show


data_graph = list(map(int, input().split()))

gr = Graph(data_graph)
print(gr.show_bar())
gr.set_show(fl_show=False)
print(gr.show_table())


