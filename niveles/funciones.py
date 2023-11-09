def cambiarNodo(nodo, nodo_actual, graph):
    if (nodo_actual >= 17 and nodo_actual <= 35) and nodo_actual != 31:
        nodo_actual = 36
    elif nodo_actual == 36:
        nodo_actual = 1
    else:
        if nodo == 1 and len(graph.get_neighbors(nodo_actual)) > 1:
            nodo_actual = graph.get_neighbors(nodo_actual)[0]
        elif nodo == 2 and len(graph.get_neighbors(nodo_actual)) > 1:
            nodo_actual = graph.get_neighbors(nodo_actual)[1]
        elif len(graph.get_neighbors(nodo_actual)) == 1:
            nodo_actual = graph.get_neighbors(nodo_actual)[0]
        else:
            nodo_actual = None

    return nodo_actual
