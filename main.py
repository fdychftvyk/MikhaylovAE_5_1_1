class Graph:
    def __init__(self):
        self._edges = []  # Список рёбер
        self._arcs = []  # Список дуг
        self._neighbors = {}  # Словарь смежности
        self._arc_bundles = {}  # Словарь пучков дуг

    def add_vertex(self, vertex):
        """Добавляет вершину в граф."""
        if not self.has_vertex(vertex):
            self._neighbors[vertex] = []
            self._arc_bundles[vertex] = []
            print(f"Вершина {vertex} добавлена в граф.")

    def add_edge(self, u, v, weight=0):
        """Добавляет ребро от вершины u к вершине v с весом weight."""
        if not self.has_vertex(u):
            self._neighbors[u] = []
        if not self.has_vertex(v):
            self._neighbors[v] = []

        edge = (u, v, weight)
        self._edges.append(edge)
        self._arcs.append((u, v))
        self._neighbors[u].append(v)
        self._arc_bundles.setdefault(u, []).append((v, weight))
        print(f"Ребро {u} -> {v} весом '{weight}' добавлено в граф.")

    def remove_edge(self, u, v, weight=None):
        """Удаляет ребро от вершины u к вершине v с заданным весом."""
        for edge in self._edges:
            if edge == (u, v, weight):
                self._edges.remove(edge)
                self._arcs.remove((u, v))
                self._neighbors[u].remove(v)
                self._arc_bundles[u].remove((v, weight))
                print(f"Ребро {u} -> {v} весом '{weight}' удалено из графа.")
                return
        print(f"Ребро {u} -> {v} весом '{weight}' не найдено для удаления.")

    def has_vertex(self, vertex):
        """Проверяет наличие вершины vertex в графе."""
        return vertex in self._neighbors

    def get_neighbors(self, vertex):
        """Возвращает список смежных вершин для данной вершины."""
        return self._neighbors.get(vertex, [])

    def get_arc_bundle(self, vertex):
        """Возвращает пучок дуг для данной вершины."""
        return self._arc_bundles.get(vertex, [])

    def remove_vertex(self, vertex):
        """Удаляет вершину и все её рёбра."""
        if vertex in self._neighbors:
            del self._neighbors[vertex]
            for neighbors in self._neighbors.values():
                if vertex in neighbors:
                    neighbors.remove(vertex)

            del self._arc_bundles[vertex]
            self._edges = [edge for edge in self._edges if edge[0] != vertex and edge[1] != vertex]
            self._arcs = [arc for arc in self._arcs if arc[0] != vertex and arc[1] != vertex]

            for bundles in self._arc_bundles.values():
                bundles[:] = [(v, w) for v, w in bundles if v != vertex]

            print(f"Вершина {vertex} и все её рёбра удалены из графа.")
        else:
            print(f"Вершина {vertex} не найдена для удаления.")

    def find_vertex(self, vertex):
        """Ищет вершину в графе и выводит результат."""
        if self.has_vertex(vertex):
            print(f"\nВершина {vertex} найдена в графе.")
        else:
            print(f"\nВершина {vertex} не найдена в графе.")

    def find_edge(self, u, v, weight=None):
        """Ищет ребро с заданным весом и выводит результат."""
        if (u, v, weight) in self._edges:
            print(f"Ребро {u} -> {v} весом '{weight}' найдено в графе.")
        else:
            print(f"Ребро {u} -> {v} весом '{weight}' не найдено в графе.")

    def print_graph(self):
        """Функция для красивого вывода графа."""
        print("Список рёбер:")
        for edge in self._edges:
            u, v, weight = edge
            print(f"  {u} -> {v} [вес: {weight}]")

        print("\nСписок дуг:")
        for arc in self._arcs:
            u, v = arc
            print(f"  {u} -> {v}")

        print("\nСловарь смежности:")
        for vertex, neighbors in self._neighbors.items():
            print(f"  {vertex}: {', '.join(map(str, neighbors))}")

        print("\nСловарь пучков дуг:")
        for vertex, bundles in self._arc_bundles.items():
            bundles_str = ', '.join([f"{v} [вес: {w}]" for v, w in bundles])
            print(f"  {vertex}: {bundles_str}")

# Создаем экземпляр графа
graph = Graph()

# Добавляем рёбра согласно изображению
graph.add_edge(1, 2, 'a')
graph.add_edge(2, 3, 'b')
graph.add_edge(2, 5, 'c')
graph.add_edge(5, 6, 'd')
graph.add_edge(3, 5, 'e')
graph.add_edge(6, 7, 'f')
graph.add_edge(7, 1, 'g')
graph.add_edge(4, 4, 's')

graph.print_graph()

print('=' * 30)
# Добавляем вершину 8
graph.add_vertex(8)

# Добавляем ребро 3 -> 4 весом 't'
graph.add_edge(3, 4, 't')

# Удаляем вершину 7
graph.remove_vertex(7)

# Ищем вершину 6
graph.find_vertex(6)

# Ищем ребро 5 -> 2 весом 'e'
graph.find_edge(2, 5, 'c')

print('=' * 30)

# Используем функцию для вывода графа
graph.print_graph()

print('=' * 30)
graph.add_edge( 8,1,'k')

graph.print_graph()