from django.shortcuts import render


def inicio(request):
    # Definir la estructura del multiverso como un grafo
    grafo_multiverso = {
        1: [2],  # Nivel 1 está conectado al Nivel 2
        2: [3, 4],  # Nivel 2 está conectado a los Niveles 3 y 4
        3: [5],  # Nivel 3 está conectado al Nivel 5
        4: [5, 6],  # Nivel 4 está conectado a los Niveles 5 y 6
        # Agrega más conexiones según sea necesario
    }

    # Obtener el nivel actual del usuario (por ejemplo, nivel 3)
    nivel_actual = (
        3  # Puedes cambiar esto según tus necesidades o obtenerlo de la base de datos
    )

    # Obtener los niveles desbloqueados hasta el nivel actual
    niveles_desbloqueados = set()
    cola = [1]  # Comienza desde el primer nivel
    while cola:
        nivel = cola.pop(0)
        if nivel <= nivel_actual:
            niveles_desbloqueados.add(nivel)
            cola.extend(grafo_multiverso.get(nivel, []))

    context = {
        "niveles": range(1, 31),
    }

    return render(request, "index.html", context)


def nivel1(request):
    return render(request, "nivel1.html")
