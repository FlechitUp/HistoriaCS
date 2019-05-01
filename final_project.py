from shutil import copyfile
from random import randint, uniform, random
import csv
"""
    para copiar archivos se usa esa libreria con el comando
    copyfile(fuente_origen, fuente_destino)
"""


def tablaNueva(nombre, columnas, tiposCols):
    #Crea file de metadata de Tabla
    ruta = 'BD/' + nombre + '.mtd'
    archivo = open(ruta, 'w')

    textoMetadata = '--MTD,' + str(len(columnas)) + ',0,'
    for cols in columnas:
        textoMetadata += str(cols) + ','
    for tcols in tiposCols:
        textoMetadata += str(tcols) + ','
        #archivo.write(cols + '\n')
    textoMetadata += 'MTD--'
    archivo.write(textoMetadata)
    archivo.close()

    #Crea tabla
    ruta = 'BD/' + nombre + '.txt'
    archivo = open(ruta, 'w')
    texto = ''
    for cols in columnas:
        texto += str(cols) + ','
    texto = texto[:len(texto) - 1]
    archivo.write(texto)
    archivo.close()
    print('tabla creada correctamente!')


def insertar(nombre, elementos):
    ruta = 'BD/' + nombre + '.txt'
    archivo = open(ruta, 'a')
    texto = ''
    for elemento in elementos:
        texto = elemento + ','
    texto = texto[:len(texto) - 1]
    archivo.write(texto+'\n')
    archivo.close()
    print("insertado!")


def insert_n(nombre, elementos, n):
    for i in range(1, n + 1):
        elementos[0] = str(i)
        elementos[1] = "'nombre_" + str(i) + "'"
        elementos[2] = str(randint(0, 100))
        insertar(nombre, elementos)


def borrar(nombre, condicion):
    ruta = 'BD/' + nombre + '.txt'
    archivo = open(ruta, 'r+')
    lineas = archivo.readlines()

    aux = 0
    aux2 = 0
    cabecera = lineas[aux]
    while cabecera != '------\n':
        datos = cabecera.split()
        aux2 += 1
        if datos[0] == condicion[0]:
            aux = aux2 - 1
        cabecera = lineas[aux2]

    archivo.seek(0)
    contLinea = 0
    flag = True
    for linea in lineas:
        if contLinea <= aux2:
            archivo.write(linea)
            contLinea += 1
        else:
            arrLinea = linea.split()
            if condicion[1] == '=':
                if arrLinea[aux] != condicion[2]:
                    archivo.write(linea)
                else:
                    flag = False
    archivo.truncate()
    archivo.close()
    if flag:
        print("no existe la fila")
    else:
        print("borrado!")


def selectA(nombreTabla, cols='*'):
    ruta = 'BD/' + nombreTabla + '.txt'
    archivo = open(ruta, 'r')
    
    if(cols == '*'):
        lineas = csv.reader(archivo)
        for linea in lineas:
            print(linea)
    else:
        #posCols = comprobarCols(nombreTabla)
        lineas = csv.DictReader(archivo)
        print(cols)
        text=''
        for linea in lineas:
            for col in cols:                
                #print(col)
                text += linea[col]+" "
            print(text)
    archivo.close()



def select(nombre, condicion):
    ruta = 'BD/' + nombre + '.txt'
    archivo = open(ruta, 'r')
    lineas = archivo.readlines()

    aux = 0
    aux2 = 0
    cabecera = lineas[aux]
    guia = ''
    while cabecera != '------\n':
        datos = cabecera.split()
        aux2 += 1
        if datos[0] == condicion[0]:
            aux = aux2 - 1
        cabecera = lineas[aux2]

        guia += datos[0] + '|'

    print(guia)

    contLinea = 0
    for linea in lineas:
        if contLinea <= aux2:
            archivo.readline()
            contLinea += 1
        else:
            arrLinea = linea.split()
            if condicion[1] == '=':
                if arrLinea[aux] == condicion[2]:
                    print(linea[:-1])
            elif condicion[1] == '!=':
                if arrLinea[aux] != condicion[2]:
                    print(linea[:-1])
            elif condicion[1] == '<':
                if arrLinea[aux] < condicion[2]:
                    print(linea[:-1])
            elif condicion[1] == '>':
                if arrLinea[aux] > condicion[2]:
                    print(linea[:-1])
            elif condicion[1] == '<=':
                if arrLinea[aux] <= condicion[2]:
                    print(linea[:-1])
            elif condicion[1] == '>=':
                if arrLinea[aux] >= condicion[2]:
                    print(linea[:-1])

    archivo.close()


def update(nombre, actualizacion, condicion):
    ruta = 'BD/' + nombre + '.txt'
    archivo = open(ruta, 'r+')
    lineas = archivo.readlines()

    auxc = 0
    auxa = 0
    aux2 = 0
    cabecera = lineas[auxc]
    while cabecera != '------\n':
        datos = cabecera.split()
        aux2 += 1
        if datos[0] == condicion[0]:
            auxc = aux2 - 1
        if datos[0] == actualizacion[0]:
            auxa = aux2 - 1
        cabecera = lineas[aux2]

    archivo.seek(0)
    contLinea = 0
    for linea in lineas:
        if contLinea <= aux2:
            archivo.write(linea)
            contLinea += 1
        else:
            arrLinea = linea.split()
            if condicion[1] == '=':
                if arrLinea[auxc] != condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
            elif condicion[1] == '!=':
                if arrLinea[auxc] == condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
            elif condicion[1] == '<':
                if arrLinea[auxc] >= condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
            elif condicion[1] == '>':
                if arrLinea[auxc] <= condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
            elif condicion[1] == '<=':
                if arrLinea[auxc] > condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
            elif condicion[1] == '>=':
                if arrLinea[auxc] < condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')

    archivo.truncate()
    archivo.close()
    print("actualizado!")


def verificarTipo(tipo):
    #print("tipo ", tipo)
    if tipo == 'int' or 'varchar':
        return True
    else:
        print(' * Error tipo ', tipo)
        return False

def getPosAND_OR(strComm):
    posA = strComm.find('AND')
    posO = strComm.find('OR')
    return min(posA, posO) if min(posA, posO)>0 else max(posO,posA)

def formatearConditions(strComm):
    #print(strComm)
    coumt = 1
    posAND_OR = getPosAND_OR(strComm)
    i = 0

    if posAND_OR > 0:
        coumt = 2
    else: posAND_OR = len(strComm)

    while(i < posAND_OR and coumt>0):
        p = strComm.find('>', i,posAND_OR)
        if (p >0):
            if strComm[p] != ' ':
                strComm = strComm[:p]+" "+strComm[p:]                
            if strComm[p + 1] != ' ':
                strComm = strComm[:p+2]+" "+strComm[p+2:]
                print('a',strComm)
            i = posAND_OR
            posAND_OR = len(strComm)
            coumt -=1
        else:
            p = strComm.find('<',i,posAND_OR)
            if (p > 0):
                if strComm[p] != ' ':
                    strComm = strComm[:p] + " " + strComm[p:]
                if strComm[p + 1] != ' ':
                    strComm = strComm[:p + 2] + " " + strComm[p + 2:]
                i = posAND_OR
                posAND_OR = len(strComm)
                coumt-=1
            else:
                p = strComm.find('=',i,posAND_OR)
                if (p > 0):
                    if strComm[p] != ' ':
                        strComm = strComm[:p] + " " + strComm[p:]
                    if strComm[p + 2] != ' ':                        
                        strComm = strComm[:p + 2] + " " + strComm[p+2:]                    
                    i = posAND_OR
                    posAND_OR = len(strComm)
                    coumt-=1
    #print(": ", strComm)

    return strComm

def getConditions(strComm):
    strComm = formatearConditions(strComm)
    ArrComm = strComm.split()
    print(ArrComm)

"""def getNameTable(commOri, keyWord):
    posF = commOri.find(keyWord)
    return comandoOrig[:posF-1]"""

def printHelp():
    print("COMANDOS:")
    print("CREA_TABLA [nombre] (columna tipo);")
    print("INSERTA [tabla] ([..elementos..]);")
    print("delete [tabla] DONDE [condicion]")
    print("SELECCIONA [tabla] DONDE [condicion]")
    print("update [tabla] set [a_actualizar] DONDE [condicion]")


# elementos = []
# elementos.append('0')
# elementos.append('nombre_x')
# elementos.append('0')
# insert_n('estudiantes', elementos, 500)
while(1):
    #printHelp()
    #comandoOrig = 'CREA_TABLA a(a1, int; a2 , int; a3, int)'  # input()
    #comandoOrig = 'INSERTA a (a1, a2, a3) VALORES (-1,8,4)'  # input()
    #comandoOrig= 'SELECCIONA * DESDE a;'  # input()
    #comandoOrig= 'SELECCIONA a1, a3 DESDE a;'  # input()
    comandoOrig = 'SELECCIONA a1, a3 DESDE a DONDE a1> 0 AND a2<8 ;'  # input()
    print(comandoOrig)
    comandoOrig = comandoOrig[:len(comandoOrig) - 1]  # quita ; final
    comando = comandoOrig.split()
    size = len(comando)
    #comando[size - 1] = comando[size - 1].replace(';', '')  # quita ; final
    # create table [nombre] (columna tipo);
    if comando[0] == 'CREA_TABLA':
        nombreTabla = comando[1]
        cols = []
        tiposCols = []
        cols2 = []
        comando[2] = comando[2][1:]  # borra (
        print("ALL C", comando)
        """for i in range(2, size-1,2):
            print(comando[i].replace(',', ''))
            cols.append(comando[i].replace(',', ''))
            tiposCols.append(comando[i + 1].replace(';', ''))
        tablaNueva(nombreTabla, cols, tiposCols)"""

        cols = comandoOrig[comandoOrig.find('(') + 1:comandoOrig.find(')')]
        cols = cols.split(';')
        #print("las" ,(cols))
        for i in range(0, len(cols)):
            tC = (cols[i].split(','))
            for j in range(len(tC)):
                tC[j] = tC[j].strip()  # strip() quita espacios blamco
            #print("TC",tC)
            if (not(verificarTipo(tC[1]))):
                break
            else:
                cols2.append(tC[0])
                tiposCols.append(tC[1])
        tablaNueva(nombreTabla, cols2, tiposCols)

    # insert [tabla] (a1, a2, a2 )VALORES (v1, v2, v3);
    elif comando[0] == 'INSERTA':
        nombreTabla = comando[1]
        elms = []

        """comando[2] = comando[2][1:]
        for i in range(2, size):
                elms.append(comando[i][:-1])
        insertar(nombreTabla, elms)"""
        cols = comandoOrig[comandoOrig.find('(') + 1:comandoOrig.find(')')]
        cols = cols.split(',')
        posVal = comandoOrig.find('VALORES')
        if (posVal > 0):
            values = comandoOrig[comandoOrig.find(
                '(', posVal + 1) + 1: comandoOrig.find(')', len(comandoOrig))]
            values = values.split()
        print(cols)
        print(values)
        insertar(nombreTabla, values)

    # for_insert [n] [nombre_tabla] [condicion]
    elif comando[0] == 'for_insert':
        n = int(comando[1])
        nombre = comando[2]
        elms = []
        comando[2] = comando[2][1:]
        for i in range(3, size):
                elms.append(comando[i][:-1])
        insert_n(nombre, elms, n)

    # delete [tabla] DONDE [condicion]
    elif comando[0] == 'BORRAR':  # considerar que la condicion va separada por ' '
        nombreTabla = comando[1]
        cndn = []
        for i in range(3, size):
            cndn.append(comando[i])
        borrar(nombreTabla, cndn)

    # select * DESDE [tabla];
    # select c1,c2 DESDE [tabla] DONDE [condicion]
    # select c1,c2 DESDE [tabla] DONDE [condicion] and [condicion]

    elif comando[0] == 'SELECCIONA':  # considerar que la condicion va separada por ' '
        nombreTabla = ''        
        colsSelect = []
        if (comando[1] == '*'):
            nombreTabla = comando[3]
            selectA(nombreTabla)
        else:                     
            posFim = comandoOrig.find('DESDE')
            colsSelect = comandoOrig[comandoOrig.find('SELECCIONA') + 11: posFim-1]
            colsSelect = colsSelect.split(',') 
            posDomde = comandoOrig.find('DONDE')           
            
            if (posDomde <0):                
                nombreTabla = comandoOrig[posFim + 6:]
                #print(colsSelect)
                for j in range(len(colsSelect)):
                    colsSelect[j] = colsSelect[j].strip()  # strip() quita espacios blamco
                selectA(nombreTabla, colsSelect)

            else:  # case de where
                nombreTabla = comandoOrig[posFim + 6:posDomde].strip()                
                strConditions = comandoOrig[posDomde + 5:]
                getConditions(strConditions)
                #print(colsSelect)
            """cndn = []
            for i in range(3, size):
                cndn.append(comando[i])
            select(nombreTabla, cndn)"""

    # update [tabla] set [a_actualizar] DONDE [condicion]
    elif comando[0] == 'update':
        nombreTabla = comando[1]
        cndn = []
        actu = []
        actu.append(comando[3])
        actu.append(comando[5])
        for i in range(7, size):
            cndn.append(comando[i])
        update(nombreTabla, actu, cndn)

    else:
        print("comando no encontrado, pruebe otra vez")
    comandoOrig = input()
