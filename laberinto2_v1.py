#Nombre: laberinto2_v2
import random
def buscar_dato(dato_y, dato_x,LC,List_total_caminos):
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
def mapeo_de_caminos(Posicion_Actual,LC,List_total_caminos):
    s_caminos = 0
    caminos_libres = []
    if ((laberinto[Posicion_Actual[0]-1][Posicion_Actual[1]] == camino or laberinto[Posicion_Actual[0]-1][Posicion_Actual[1]] == comida) and buscar_dato(Posicion_Actual[0]-1 , Posicion_Actual[1],LC,List_total_caminos) == 0):
        s_caminos += 1
        caminos_libres.append([Posicion_Actual[0]-1 , Posicion_Actual[1]])
    if ((laberinto[Posicion_Actual[0]+1][Posicion_Actual[1]] == camino or laberinto[Posicion_Actual[0]+1][Posicion_Actual[1]] == comida) and buscar_dato(Posicion_Actual[0]+1 , Posicion_Actual[1],LC,List_total_caminos) == 0):
        s_caminos += 1
        caminos_libres.append([Posicion_Actual[0]+1 , Posicion_Actual[1]])
    if ((laberinto[Posicion_Actual[0]][Posicion_Actual[1]-1] == camino or laberinto[Posicion_Actual[0]][Posicion_Actual[1]-1] == comida) and buscar_dato(Posicion_Actual[0] , Posicion_Actual[1]-1,LC,List_total_caminos) == 0):
        s_caminos +=1
        caminos_libres.append([Posicion_Actual[0] , Posicion_Actual[1]-1])
    if ((laberinto[Posicion_Actual[0]][Posicion_Actual[1]+1] == camino or laberinto[Posicion_Actual[0]][Posicion_Actual[1]+1] == comida) and buscar_dato(Posicion_Actual[0] , Posicion_Actual[1]+1,LC,List_total_caminos) == 0):
        s_caminos += 1
        caminos_libres.append([Posicion_Actual[0] , Posicion_Actual[1]+1])
    return s_caminos, caminos_libres

def Prueva():
    for lab in laberinto:
        print(lab)
    for lab in List_total_caminos:
        for dato in lab:
            a,b = dato
            laberinto[a][b]="W"
    print("-----")
    for lab in laberinto:
        print(lab)

def Prueva_2(List_total_caminos):
    for lab in List_total_caminos:
        print(lab)
    print("----------------")

def Mapeo_de_laberinto(PA,PD,LC, List_total_caminos):
    if PA[0] != 0 and (laberinto[PA[0]][PA[1]] == camino or laberinto[PA[0]][PA[1]] == comida):
        aux_1, aux_2 = mapeo_de_caminos(PA,LC,List_total_caminos)
        if aux_1 == 0:
            LC.append(PA)
            List_total_caminos.append(LC)
            List_nuevo_camino = []
            
            if(len(PD)>=1):
                for dato in LC:
                    if dato == PD[len(PD)-1]:
                        break
                    else:
                        List_nuevo_camino.append(dato)
                LC=[]
                aux_3 = PD[len(PD)-1]
                PD.remove(aux_3)
                return Mapeo_de_laberinto(aux_3,PD,List_nuevo_camino, List_total_caminos)
            else:
                print("FIN")
                return List_total_caminos #--------------------------------------------------------------------------------------
        if aux_1 > 1:
            PD.append(PA)
            LC.append(PA)
            PA = aux_2[0]
            return Mapeo_de_laberinto(PA,PD,LC, List_total_caminos)
        if aux_1 == 1:
            LC.append(PA)
            PA = aux_2[0]
            for dato in PD:
                if dato == PA:
                    PD.remove(PA)
            return Mapeo_de_laberinto(PA,PD,LC, List_total_caminos)
    else:
        print("MAL")

def Generar_comida(numero_de_comida,Posicion_Actual):
    contador = 0
    for lab in laberinto:
        for dato in lab:
            if(dato == "c"):
                contador=contador+1
    Posiciones_de_caminos = []
    for lab in List_total_caminos:
        for dato in lab:
            Posiciones_de_caminos.append(dato)
    posicion_de_comida = []
    contador_2 = 0
    Aux_1 = []
    aux_2 = 1
    #print("Entrando al WHILE ")
    while(contador_2 < numero_de_comida):
        #Modificar para que no aparezca el primer punto
        Aux_1 = Posiciones_de_caminos[random.randint(2, contador)]
        if (contador_2 > 0):
            for t in posicion_de_comida:
                if(Aux_1 == Posicion_Actual or Aux_1 == t):
                    aux_2 = 0
            if(aux_2):
                posicion_de_comida.append(Aux_1)
                laberinto[posicion_de_comida[contador_2][0]][posicion_de_comida[contador_2][1]] = comida
                contador_2 = contador_2 + 1
        elif(Aux_1 != Posicion_Actual):
            posicion_de_comida.append(Aux_1)
            laberinto[posicion_de_comida[contador_2][0]][posicion_de_comida[contador_2][1]] = comida
            contador_2 = contador_2 + 1
        else:
            print("Punto fallido = ",Aux_1)
    return posicion_de_comida

def imprimir_array(abc):
    print("-----------------------------------------")
    for fg in abc:
        print(fg)
    print("-----------------------------------------")

def Elegir_camino(CM, Pos_Act, List_total_caminos):
    list_opciones = []
    Opciones = []
    Camino_Optimo = []
    numero_de_camino = 0
    inicio = 0
    for dato in CM:
        for lis in List_total_caminos:
            numero_de_camino = numero_de_camino + 1
            posicion_camino = 0
            for dato_cam in lis:
                if (dato_cam == Pos_Act):
                    inicio = 1
                if (inicio == 1):
                    posicion_camino = posicion_camino + 1
                    if dato_cam == dato:
                        list_opciones.append([numero_de_camino, posicion_camino])
        numero_de_camino = 0
        posicion_camino = 0
        camino_rapido = 0
        inicio = 0
        aux_1 =[]
        for dato_2 in list_opciones:
            if camino_rapido < dato_2[1]:
                camino_rapido = dato_2[1]
        for dato_2 in list_opciones:
            if camino_rapido == dato_2[1]:
                aux_1.append(dato_2[0])
        Camino_Optimo.append(camino_rapido)
        Opciones.append(aux_1)
        list_opciones = []
    Distancia_a_caminar = 10000 #NUMERO ALTO --------------------------------
    for CO in Camino_Optimo:
        #indice = indice + 1
        if CO < Distancia_a_caminar:
            Distancia_a_caminar = CO
    aux_2 = -1
    aux_3 = 10000 #numero grande, len(list_total_camino)--------------------------------
    list_camino_optimo = []
    indice = 0
    for a in Camino_Optimo:
        aux_2 = aux_2+1
        if (Distancia_a_caminar == a):
            if (len(Opciones[aux_2]) < aux_3):
                indice = aux_2
                list_camino_optimo.append(Opciones[aux_2])
    indice = -1
    contador = -1
    for b in list_camino_optimo:
        contador = contador + 1
        if(indice < len(b)):
            indice = contador
    indice_cm = Opciones.index(list_camino_optimo[indice])
    aux_4 = []
    aux_4 = CM[indice_cm]
    CM.remove(CM[indice_cm])
    #IMPRIME LA RUTA QUE TEIENE QUE RECORRER PARA COMER LA COMIDA
    #imprimir_array(List_total_caminos)
    #print(List_total_caminos[Opciones[indice_cm][0]-1])
    print("Ubicacion de la comida = ",aux_4)
    print("Los pasos que hacer para llegar al objetivo (comida)")
    if (len(List_total_caminos[list_camino_optimo[indice][0]]) >1) :
        #List_total_caminos[Opciones[indice_cm][0]]
        for agh in List_total_caminos[Opciones[indice_cm][0]-1]:
            if (agh != aux_4):
                print(agh)#Indica la posicion en la que avanzar (o mas bien el punto) para llegar a su objetivo
                laberinto[agh[0]][agh[1]] = "A"#Se marca el camino que hace el agente en el laberinto
            else:
                print(agh)
                laberinto[agh[0]][agh[1]] = "A"
                break
    
    if(len(CM)> 0):
        laberinto[aux_4[0]][aux_4[1]] = "c"
        print("Encontrado ... ")
        imprimir_array(laberinto)
        Punto_de_difurcacion = []
        list_opciones = []
        List_total_caminos = []
        List_camino = []
        List_total_caminos = Mapeo_de_laberinto(aux_4, Punto_de_difurcacion,List_camino, List_total_caminos)
        print("__________________________________________________________________")
        return Elegir_camino(CM, aux_4, List_total_caminos)
    else:
        laberinto[aux_4[0]][aux_4[1]] = "c"
        print("Encontrado ... ")
        imprimir_array(laberinto)
        print("__________________________________________________________________")
        print("FIN DEL CAMINO")

def definir_punto_de_inicio(al,anc,lab):
    estado = 0
    while (estado==0):
        aux_1 = random.randint(1, al)
        aux_2 = random.randint(1, anc)
        if lab[aux_1][aux_2] == comida:
            estado == 1
    return aux_1,aux_2
    

laberinto = [['#', '#', '#', '#', '#', '#', '#', '#']
            ,['#', '#', 'c', 'c', 'c', 'c', 'c', '#']     
            ,['#', 'c', 'c', '#', '#', '#', '#', '#']     
            ,['#', '#', 'c', 'c', 'c', 'c', 'c', '#']     
            ,['#', 'c', 'c', '#', 'c', '#', '#', '#']     
            ,['#', 'c', '#', '#', 'c', 'c', 'c', '#']     
            ,['#', '#', '#', '#', '#', '#', '#', '#']]
alto = 7
ancho = 8
#y, x = 0, 2
camino = "c"
pared = "#"
#vacio = "v"
comida = "O"
Posicion_actual=[1,2]#Inician desde este punto de inicio
List_total_caminos = []
List_camino = []
Punto_de_difurcacion = []
List_Comida = []
List_Opciones = []
#a,b = definir_punto_de_inicio(alto-1,ancho-1,laberinto)
#print ("punto de inicio opcional = ",a," ",b)
imprimir_array(laberinto)
Mapeo_de_laberinto(Posicion_actual, Punto_de_difurcacion,List_camino, List_total_caminos)
#List_Comida = Generar_comida(3,Posicion_actual)
List_Comida = [[3,4],[5,4],[3,2]]
laberinto[3][4]=comida
laberinto[5][4]=comida
laberinto[3][2]=comida
print("Imprimir la ubicacion de las comidas")
print(List_Comida)
imprimir_array(laberinto)
Elegir_camino(List_Comida, Posicion_actual, List_total_caminos)
print("YA TERMINO TODO")
