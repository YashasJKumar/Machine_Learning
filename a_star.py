def heurestic(n):
    h = {
        'A': 10,
        'B': 8,
        'C': 5,
        'D': 7,
        'E': 3,
        'F': 6,
        'G': 5,
        'H': 3,
        'I': 1,
        'J': 0
    }
    return h[n]


def get_neighbours(v):
    if v in graph:
        return graph[v]
    return None


graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('C', 3), ('D', 2)],
    'C': [('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 8)],
    'E': [('I', 5), ('J', 5)],
    'F': [('G', 1), ('H', 7)],
    'G': [('I', 3)],
    'H': [('I', 2)],
    'I': [('E', 5), ('J', 3)],

}


def a_star_algorithm(start, stop):
    open_set = set(start)
    closed_set = set()
    g = {}
    parents = {start: start}
    g[start] = 0
    while len(open_set) > 0:
        n = None
        for v in open_set:
            if n is None or g[v] + heurestic(v) < g[n] + heurestic(n):
                n = v

        if n is stop:
            pass
        else:
            for m, weight in get_neighbours(n):
                if m not in closed_set and m not in open_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    if g[m] + heurestic(m) < g[n]:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        if n is None:
            print("Path Not Found!")
            return None

        if n == stop:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start)
            path.reverse()
            print("Path Found: {}".format(path))
            return path

        open_set.remove(n)
        closed_set.add(n)
    print("Path Not Found!")
    return None


a_star_algorithm('A', 'J')
