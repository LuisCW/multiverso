from django.shortcuts import render
from .grafo import Node


def niveles(request):
    if request.method == "POST":
        if "boton_izquierda" in request.POST:
            mundo = siguienteMundo(1)
        elif "boton_derecha" in request.POST:
            mundo = siguienteMundo(2)

        return render(request, mundo)

    else:
        # Creacion del grafo
        root = Node("nivel1.html")

        # Asignacion de los nodos
        for i in range(2, 37):
            root.addNode("nivel" + str(i) + ".html")

        global nodo
        nodo = root

        return render(request, "nivel1.html")


def siguienteMundo(mundo):
    global nodo

    if mundo == 1:
        nodo = nodo.left
        print("Este es el mundo: ", nodo.data)
        return nodo.data
    elif mundo == 2:
        nodo = nodo.right
        print("Este es el mundo: ", nodo.data)
        return nodo.data
