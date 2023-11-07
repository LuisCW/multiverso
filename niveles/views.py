from django.shortcuts import render
from .grafo import Graph


def niveles(request):
    if request.method == "POST":
        if "boton_izquierda" in request.POST:
            mundo = str(cambiarNodo(1))
        elif "boton_derecha" in request.POST:
            mundo = str(cambiarNodo(2))

        return render(request, "nivel" + mundo + ".html")

    else:
        # Creacion del grafo
        global graph
        graph = Graph()

        # Asignacion de los nodos
        for i in range(1, 37):
            graph.add_node(i)

        # Asignacion de los arcos
        graph.add_edge(1, 2)
        graph.add_edge(1, 3)
        graph.add_edge(2, 4)
        graph.add_edge(2, 5)
        graph.add_edge(3, 6)
        graph.add_edge(3, 7)
        graph.add_edge(4, 8)
        graph.add_edge(4, 9)
        graph.add_edge(5, 10)
        graph.add_edge(5, 11)
        graph.add_edge(6, 12)
        graph.add_edge(6, 13)
        graph.add_edge(7, 14)
        graph.add_edge(7, 15)
        graph.add_edge(8, 16)
        graph.add_edge(8, 17)
        graph.add_edge(9, 18)
        graph.add_edge(9, 19)
        graph.add_edge(10, 20)
        graph.add_edge(10, 21)
        graph.add_edge(11, 22)
        graph.add_edge(11, 23)
        graph.add_edge(12, 24)
        graph.add_edge(12, 25)
        graph.add_edge(13, 26)
        graph.add_edge(13, 27)
        graph.add_edge(14, 28)
        graph.add_edge(14, 29)
        graph.add_edge(15, 30)
        graph.add_edge(15, 31)
        graph.add_edge(16, 32)
        graph.add_edge(16, 33)
        graph.add_edge(31, 34)
        graph.add_edge(31, 35)
        graph.add_edge(17, 36)
        graph.add_edge(18, 36)
        graph.add_edge(19, 36)
        graph.add_edge(20, 36)
        graph.add_edge(21, 36)
        graph.add_edge(22, 36)
        graph.add_edge(23, 36)
        graph.add_edge(24, 36)
        graph.add_edge(25, 36)
        graph.add_edge(26, 36)
        graph.add_edge(27, 36)
        graph.add_edge(28, 36)
        graph.add_edge(29, 36)
        graph.add_edge(30, 36)
        graph.add_edge(32, 36)
        graph.add_edge(33, 36)
        graph.add_edge(34, 36)
        graph.add_edge(35, 36)

        global nodo_actual

        nodo_actual = 1

        return render(request, "nivel1.html")


def cambiarNodo(nodo):
    global nodo_actual, graph
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
