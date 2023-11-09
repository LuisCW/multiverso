from django.shortcuts import render, redirect
from django.urls import reverse
from .grafo import Graph
from .funciones import cambiarNodo
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
from io import BytesIO
from django.http import HttpResponse

matplotlib.use("Agg")


def niveles(request):
    global nodo_actual, graph
    if request.method == "POST":
        if "boton_izquierda" in request.POST:
            mundo = str(cambiarNodo(1, nodo_actual, graph))
        elif "boton_derecha" in request.POST:
            mundo = str(cambiarNodo(2, nodo_actual, graph))

        if mundo == "None":
            return redirect("/404")

        nodo_actual = int(mundo)

        return render(request, "nivel" + mundo + ".html", {"nodo_actual": nodo_actual})

    else:
        nodo_actual = 1

        return render(request, "nivel1.html", {"nodo_actual": nodo_actual})


def inicio(request):
    global graph, nodo_actual, nodos_creados

    si = request.GET.get("first", None)

    if si == None:
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

        nodos_creados = {}

    nodo_actual = 0

    return render(request, "index.html", {"nodos_creados": nodos_creados.keys()})


def mostrar_grafo(request):
    grafo = nx.Graph()

    global graph

    grafo.add_nodes_from(graph.graph.keys())
    for key in graph.graph.keys():
        for value in graph.graph[key]:
            grafo.add_edge(key, value)

    node_colors = ["skyblue" for i in range(len(grafo.nodes))]
    if nodo_actual != 0:
        node_colors[nodo_actual - 1] = "red"

    pos = nx.spring_layout(grafo)
    nx.draw(grafo, pos, with_labels=True, node_color=node_colors, node_size=500)
    plt.axis("off")

    buffer = BytesIO()
    plt.savefig(buffer, format="png")
    plt.close()
    response = HttpResponse(content_type="image/png")
    response.write(buffer.getvalue())
    return response


def nuevo_nodo(request):
    global nodos_creados, graph

    if request.method == "POST":
        if len(nodos_creados) == 0:
            numero = 37
        else:
            numero = max(nodos_creados.keys()) + 1

        titulo = request.POST.get("titulo")
        descripcion = request.POST.get("descripcion")
        conexion_izquierda = request.POST.get("checklist_izquierdo")
        conexion_derecha = request.POST.get("checklist_derecho")

        nodo = [
            str(titulo),
            str(descripcion),
            int(conexion_izquierda),
            int(conexion_derecha),
        ]

        nodos_creados[numero] = nodo

        graph.add_node(numero)
        graph.add_edge(numero, nodo[2])
        graph.add_edge(numero, nodo[3])

        return redirect("/?first=1")
    else:
        return render(request, "nuevoNodo.html", {"mundos": graph.graph.keys()})


def eliminar_nodo(request):
    global graph, nodos_creados
    if request.method == "POST":
        nodo = int(request.POST.get("checklist"))

        graph.remove_node(nodo)
        if nodo in nodos_creados:
            del nodos_creados[nodo]

        return redirect("/?first=1")
    else:
        return render(request, "eliminarNodo.html", {"mundos": graph.graph.keys()})


def error404(request):
    return render(request, "404.html")
