import random

def iniciar_laberinto():
    # Indicar todas las celdas como vacio
    for i in range(0, alto):
        columna = []
        for j in range(0, ancho):
            columna.append(vacio)
        laberinto.append(columna)

def limite_del_laberinto():
    # Lo que hace es que crea un margen de un cuadro para que no se genere el inicio en los margenes
    inicio_alto = random.randint(0, alto)
    inicio_ancho = random.randint(0, ancho)
    if (inicio_alto == 0):
        inicio_alto += 1
    if (inicio_alto == alto-1):
        inicio_alto -= 1
    if (inicio_ancho == 0):
        inicio_ancho += 1
    if (inicio_ancho == ancho-1):
        inicio_ancho -= 1
    #laberinto[inicio_alto][inicio_ancho] = camino
    return inicio_alto, inicio_ancho

def mapeo_de_pared():
    # al encontrar el punto de inicio, se define los 4 puntos cardinales del punto de inicio
    paredes = []
    paredes.append([inicio_alto - 1, inicio_ancho])
    paredes.append([inicio_alto, inicio_ancho - 1])
    paredes.append([inicio_alto, inicio_ancho + 1])
    paredes.append([inicio_alto + 1, inicio_ancho])

    # Se usa los puntos cardinales obtenidos y se coloca "w" (pared) 
    laberinto[paredes[0][0]][paredes[0][1]] = pared
    laberinto[paredes[1][0]][paredes[1][1]] = pared
    laberinto[paredes[2][0]][paredes[2][1]] = pared
    laberinto[paredes[3][0]][paredes[3][1]] = pared
    return paredes, laberinto

def mapeo_de_caminos(pared_aleatoria):
    s_caminos = 0
    if (laberinto[pared_aleatoria[0]-1][pared_aleatoria[1]] == camino):
        s_caminos += 1
    if (laberinto[pared_aleatoria[0]+1][pared_aleatoria[1]] == camino):
        s_caminos += 1
    if (laberinto[pared_aleatoria[0]][pared_aleatoria[1]-1] == camino):
        s_caminos +=1
    if (laberinto[pared_aleatoria[0]][pared_aleatoria[1]+1] == camino):
        s_caminos += 1
    return s_caminos

def aux(direccion):
    match direccion:
        case "arriba": list_aux = [0, 0, -1, 0]
        case "abajo": list_aux = [0, alto-1, 1, 0]
        case "derecha": list_aux = [1, ancho-1, 0, 1]
        case "izquierda": list_aux = [1, 0, 0, -1]
        case _: print("ERROR")
    return list_aux

def reemplazando_con_paredes(direccion):
    list_aux_2 = aux(direccion)
    if (pared_aleatoria[list_aux_2[0]] != list_aux_2[1]):
        if (laberinto[pared_aleatoria[0]+list_aux_2[2]][pared_aleatoria[1]+list_aux_2[3]] != camino):
            laberinto[pared_aleatoria[0]+list_aux_2[2]][pared_aleatoria[1]+list_aux_2[3]] = pared
        if ([pared_aleatoria[0]+list_aux_2[2], pared_aleatoria[1]+list_aux_2[3]] not in paredes):
            paredes.append([pared_aleatoria[0]+list_aux_2[2], pared_aleatoria[1]+list_aux_2[3]])
    return laberinto, paredes

def comprobacion_de_pared_cercano(direccion, laberinto, paredes):
    #list_aux = []
    list_aux = aux(direccion)
    list_direccion =[]
    match direccion:
        case "arriba": list_direccion = ["arriba", "derecha", "izquierda"]
        case "abajo": list_direccion = ["abajo", "derecha", "izquierda"]
        case "derecha": list_direccion = ["arriba", "abajo", "derecha"]
        case "izquierda": list_direccion = ["arriba", "abajo", "izquierda"]
        case _: print("ERROR")
    #Imprimir_laberinto(laberinto)
    #print ("------------------------------")
    # Compruebe si es una pared izquierda
    if (pared_aleatoria[list_aux[0]] != list_aux[1] and laberinto[pared_aleatoria[0]+list_aux[2]][pared_aleatoria[1]+list_aux[3]] == vacio and laberinto[pared_aleatoria[0]-list_aux[2]][pared_aleatoria[1]-list_aux[3]] == camino):
        # Encuentre el número de celdas circundantes
        c=1
        s_caminos = mapeo_de_caminos(pared_aleatoria)
        if (s_caminos < 2):
            # Se reemplaza la pared con una "c" (camino)
            laberinto[pared_aleatoria[0]][pared_aleatoria[1]] = camino
            # Se definen las paredes el 3 puntos cardinales
            # Celda superior
            laberinto, paredes = reemplazando_con_paredes(list_direccion[0])
            # Celda inferior
            laberinto, paredes = reemplazando_con_paredes(list_direccion[1])
            # Celda más a la izquierda
            laberinto, paredes = reemplazando_con_paredes(list_direccion[2])
        # Eliminar la pared de la lista para que ya no se use en la siguiente iteracion
        for pared in paredes:
            if (pared[0] == pared_aleatoria[0] and pared[1] == pared_aleatoria[1]):
                paredes.remove(pared)
    else:
        c=0
    return c, laberinto, paredes

def Imprimir_laberinto(laberinto):
    for i in range(0, alto):
        for j in range(0, ancho):
            if (laberinto[i][j] == vacio):
                print(str(laberinto[i][j]), end=" ")
            elif (laberinto[i][j] == camino):
                print(str(laberinto[i][j]), end=" ")
            else:
                print(str(laberinto[i][j]), end=" ")
        print('\n')

alto = 7
ancho = 8
vacio = "v"
camino = "c"
pared = "#"

laberinto = []
paredes = []

iniciar_laberinto()
inicio_alto, inicio_ancho = limite_del_laberinto()
laberinto[inicio_alto][inicio_ancho] = camino
paredes, laberinto = mapeo_de_pared()
CONTADOR = 0
while (paredes):
    CONTADOR = CONTADOR+1
    #if CONTADOR ==10:
    #    break
    # Se elige una de los puntos cardinales al azar  
    pared_aleatoria = paredes[int(random.random()*len(paredes))-1]
    # Compruebe si es una pared izquierda
    aux1, aux2, aux3 = comprobacion_de_pared_cercano("izquierda", laberinto, paredes)
    if aux1:
        laberinto = aux2
        paredes = aux3
        continue

    aux1,aux2,aux3 = comprobacion_de_pared_cercano("arriba", laberinto, paredes)
    if aux1:
        laberinto = aux2
        paredes = aux3
        continue

    aux1,aux2,aux3 = comprobacion_de_pared_cercano("abajo", laberinto, paredes)
    if aux1:
        laberinto = aux2
        paredes = aux3
        continue

    aux1,aux2,aux3 = comprobacion_de_pared_cercano("derecha", laberinto, paredes)
    if aux1:
        laberinto = aux2
        paredes = aux3
        continue

    for pared_ in paredes:
        if (pared_[0] == pared_aleatoria[0] and pared_[1] == pared_aleatoria[1]):
            paredes.remove(pared_)

# Se reemplaza los puestos vacios con una pares
for i in range(0, alto):
    for j in range(0, ancho):
        if (laberinto[i][j] == vacio):
            laberinto[i][j] = pared

# Establecer entrada y salida
for i in range(0, ancho):
    if (laberinto[1][i] == camino):
        laberinto[0][i] = camino
        break

for i in range(ancho-1, 0, -1):
    if (laberinto[alto-2][i] == camino):
        laberinto[alto-1][i] = camino
        break

print("Cantidad de Repeticiones para realizar el laberinto es ",CONTADOR)
#Imprimir_laberinto(laberinto)

for lab in laberinto:
    print(lab)