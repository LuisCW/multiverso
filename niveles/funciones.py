def cambiarNodo(nodo, nodo_actual, graph):
    if (nodo_actual >= 17 and nodo_actual <= 35) and nodo_actual != 31:
        nodo_actual = 36
    elif nodo_actual == 36:
        nodo_actual = 0
    else:
        if nodo == 1:
            nodo_actual = graph.get_neighbors(nodo_actual)[0]
        elif nodo == 2:
            nodo_actual = graph.get_neighbors(nodo_actual)[1]

    return nodo_actual
