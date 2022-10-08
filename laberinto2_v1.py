import random
def buscar_dato(dato_y, dato_x,LC):
    for total in List_total_caminos:
        aux_1=total
        for camino in aux_1:
            if(camino==[dato_y,dato_x]):
                return 1
    for total_camino in LC:
        if (total_camino == [dato_y,dato_x]):
            return 1
    return 0
#Nos dice los caminos sin explorar que hay
def mapeo_de_caminos(Posicion_Actual,LC):
    s_caminos = 0
    caminos_libres = []
    if (laberinto[Posicion_Actual[0]-1][Posicion_Actual[1]] == camino and buscar_dato(Posicion_Actual[0]-1 , Posicion_Actual[1],LC) == 0):
        s_caminos += 1
        #print("Camino Arriba", Posicion_Actual[0]-1," ",Posicion_Actual[1])
        caminos_libres.append([Posicion_Actual[0]-1 , Posicion_Actual[1]])
    if (laberinto[Posicion_Actual[0]+1][Posicion_Actual[1]] == camino and buscar_dato(Posicion_Actual[0]+1 , Posicion_Actual[1],LC) == 0):
        s_caminos += 1
        #print("Camino Abajo", Posicion_Actual[0]+1," ",Posicion_Actual[1])
        caminos_libres.append([Posicion_Actual[0]+1 , Posicion_Actual[1]])
    if (laberinto[Posicion_Actual[0]][Posicion_Actual[1]-1] == camino and buscar_dato(Posicion_Actual[0] , Posicion_Actual[1]-1,LC) == 0):
        s_caminos +=1
        #print("Camino Izquierda", Posicion_Actual[0]," ",Posicion_Actual[1]-1)
        caminos_libres.append([Posicion_Actual[0] , Posicion_Actual[1]-1])
    if (laberinto[Posicion_Actual[0]][Posicion_Actual[1]+1] == camino and buscar_dato(Posicion_Actual[0] , Posicion_Actual[1]+1,LC) == 0):
        s_caminos += 1
        #print("Camino Derecha", Posicion_Actual[0]," ",Posicion_Actual[1]+1)
        caminos_libres.append([Posicion_Actual[0] , Posicion_Actual[1]+1])
    return s_caminos, caminos_libres

def Prueva():
    for lab in laberinto:
        print(lab)
    print("Lista total de camino = ",len(List_total_caminos))
    for lab in List_total_caminos:
        for dato in lab:
            #print(dato)
            a,b = dato
            laberinto[a][b]="W"
            #print(laberinto[a][b])
        #print(laberinto[lab])
        #print("-----")
    print("-----")
    for lab in laberinto:
        print(lab)

def Prueva_2():
    for lab in List_total_caminos:
        print(lab)
        #for dato in lab:
            #print(dato)
            #print(laberinto[a][b])
        #print(laberinto[lab])
        #print("-----")
    print("----------------")
def Mapeo_de_laberinto(PA,PD,LC,contador):
    #print("-------------------------")
    #print("Posicion Actual = ", PA[0]," ",PA[1]," Punto de Difurcacion = ",len(PD), "tamaño de la lista de camino", len(LC))
    if PA[0] != 0 and laberinto[PA[0]][PA[1]] == camino and contador < 24:
        aux_1, aux_2 = mapeo_de_caminos(PA,LC)
        if aux_1 == 0:
            #print("Ninguna opcion")
            LC.append(PA)
            List_total_caminos.append(LC)
            List_nuevo_camino = []
            
            if(len(PD)>=1):
                for dato in LC:
                    if dato == PD[len(PD)-1]:
                        #print("DATO ENCONTRADO, SE PROCEDE A SALIR")
                        break
                    else:
                        #print("dato = ", dato," , PD = ",PD[len(PD)-1])
                        List_nuevo_camino.append(dato)
                LC=[]
                aux_3 = PD[len(PD)-1]
                #print("Punto siguiente = ",aux_3)
                PD.remove(aux_3)
                return Mapeo_de_laberinto(aux_3,PD,List_nuevo_camino,contador+1)
            else:
                print("FIN",contador)
                Prueva_2()#COMENTAR----------------------------------
        if aux_1 > 1:
            #print("Muchas opciones")
            PD.append(PA)
            LC.append(PA)
            PA = aux_2[0]
            return Mapeo_de_laberinto(PA,PD,LC,contador+1)
        if aux_1 == 1:
            #print("Una opcion")
            LC.append(PA)
            PA = aux_2[0]
            for dato in PD:
                if dato == PA:
                    PD.remove(PA)
            return Mapeo_de_laberinto(PA,PD,LC,contador+1)
    else:
        print("MAL")

def Generar_comida(numero_de_comida):
    contador = 0
    for lab in laberinto:
        for dato in lab:
            if(dato == "c"):
                contador=contador+1
    #print("Contador = ", contador)
    #random.randint(1, contador)
    Posiciones_de_caminos = []
    for lab in List_total_caminos:
        for dato in lab:
            Posiciones_de_caminos.append(dato)
    comida = []
    contador_2 = 0
    while(contador_2 < numero_de_comida):
        comida.append(Posiciones_de_caminos[random.randint(2, contador)])
        #print("a = ",a," b= ",b)
        laberinto[comida[contador_2][0]][comida[contador_2][1]] = "O"
        contador_2 = contador_2 + 1
    #print("--")
    return comida
#FALTA ACABAR ESTA FUNCION
def Elegir_camino(CM):
    list_opciones = []
    numero_de_camino = 0
    for dato in CM:
        for lis in List_total_caminos:
            numero_de_camino = numero_de_camino + 1
            posicion_camino = 0
            for dato_cam in lis:
                posicion_camino = posicion_camino + 1
                if dato_cam == dato:
                    print("Se encontro el dato = ",dato," en el camino = ",numero_de_camino, " La posicion es = ",posicion_camino)
                    list_opciones.append([numero_de_camino, posicion_camino])
                    #CM.remove(dato_cam)
        camino_optimo = 0
        for dato in list_opciones:
            if dato[1] > camino_optimo:
                camino_optimo = dato[1]
    #for dato in list_opciones:

laberinto = [['#', '#', '#', '#', '#', '#', '#', '#']
            ,['#', '#', 'c', 'c', 'c', 'c', 'c', '#']     
            ,['#', 'c', 'c', '#', '#', '#', '#', '#']     
            ,['#', '#', 'c', 'c', 'c', 'c', 'c', '#']     
            ,['#', 'c', 'c', '#', 'c', '#', '#', '#']     
            ,['#', 'c', '#', '#', 'c', 'c', 'c', '#']     
            ,['#', '#', '#', '#', '#', '#', '#', '#']]
alto = 7
ancho = 8
y, x = 0, 2
camino = "c"
pared = "#"
Posicion_actual=[1,2]
#Posicion_actual.append()
#laberinto[y][x]="W"
List_total_caminos = []
List_camino = []
Punto_de_difurcacion = []
Comida = []
#persepcion()

#punto de difurcacion
#List_camino.append(Posicion_actual)
Mapeo_de_laberinto(Posicion_actual, Punto_de_difurcacion,List_camino,0)
#for lab in laberinto:
#    print(lab)
Comida = Generar_comida(3)
print("----")
for dato in Comida:
    print(dato)
print("----")
#print("----")
#for lab in laberinto:
#    print(lab)
Elegir_camino(Comida)

#print(List_total_caminos[0][0])
#contro+k , control+c ; control+k , control+u
# List_camino.append([0,0])
# List_camino.append([1,1])
# List_total_caminos.append(List_camino)
# List_camino=[]
# List_camino.append([2,2])
# List_camino.append([3,3])
# List_total_caminos.append(List_camino)
# for total in List_total_caminos:
#     aux_1=total
#     for camino in aux_1:
#         if(camino==[2,2]):
#             print("Encontrado")
#         print(camino)
#     print("--")

#for lab in Posicion_actual:
#    print(lab)
