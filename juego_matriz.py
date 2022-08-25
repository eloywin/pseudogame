from os import system

# Everything coded by Eloy 8)

lista3d = [[], [], [], [], [], [], [], [], []]

# variables player / movimiento
player = "𓀠"
eje_x = 0
eje_y = 16
entrada = None


def mapa():
    global lista3d
    # creacion de la matriz
    for i in lista3d:
        if isinstance(i, list):
            for x in range(35):
                i.append(".")
    # spawneo de el player
    lista3d[eje_x][eje_y] = player
    # graficacion
    for x in lista3d:
        for y in x:
            print(y, end="")
        print("")


def limpiarmapa():
    global lista3d
    for i in lista3d:
        if isinstance(i, list):
            if len(i) > 0:
                # borro todo el contenido de la lista
                for x in reversed(range(len(i))):
                    i.pop(x)


def movimiento():
    global eje_x
    global eje_y
    while True:
        print("[+]Controles : ⬆(w)  ⬅(a)  ⬇(s)  ⮕(d)")
        entrada = input("[+]Esperando movimiento : ")
        if entrada.lower() == "s":
            lista3d[eje_x][eje_y] = "."
            eje_x += 1
            lista3d[eje_x][eje_y] = player
        elif entrada.lower() == "w":
            lista3d[eje_x][eje_y] = "."
            eje_x -= 1
            lista3d[eje_x][eje_y] = player
        elif entrada.lower() == "a":
            lista3d[eje_x][eje_y] = "."
            eje_y -= 1
            lista3d[eje_x][eje_y] = player
        elif entrada.lower() == "d":
            lista3d[eje_x][eje_y] = "."
            eje_y += 1
            lista3d[eje_x][eje_y] = player
        system("cls")
        limpiarmapa()
        mapa()


system("cls")
mapa()
movimiento()
