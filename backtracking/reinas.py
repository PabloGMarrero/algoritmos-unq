def puedoPoner(tablero, fila, col):
    print(fila, col)
    for i in range(0, col):
        if (tablero[fila][i]):
            return False; 

    """for i in range(fila, -1, -1):
        for j in range(col, -1, -1):
            if (tablero[i][j]): 
                return False
    """

    i, j = fila, col
    while i>=0 or j >=0:
        if (tablero[i][j]): 
                return False
        i = i - 1
        j = j - 1
            
    i, j = 0, col
    while i<len(tablero) or j >=0:
        if (tablero[i][j]): 
                return False
        i = i + 1
        j = j - 1

    i, j = fila, col
    while i<len(tablero) or j >=0:
        if (tablero[i][j]): 
                return False
        i = i + 1
        j = j - 1

    """for i in range(fila, len(tablero)):
        for j in range(col, -1, -1):
            if (tablero[i][j]): 
                return False"""

    return True

def agregar(tablero, fila, columna):
    tablero[fila][columna] = True
    return tablero

def sacar(tablero, fila, columna):
    tablero[fila][columna] = False
    return tablero

def reinas(tablero, fila, columna):
    if fila == len(tablero)-1 and columna == len(tablero)-1:
        return tablero
    if fila == len(tablero)-1:
        return reinas(sacar(tablero, fila, columna), fila, columna)
    puedo = puedoPoner(tablero, fila, columna)

    if puedo:
        tablero = reinas(agregar(tablero, fila, columna), 0, columna + 1)
            

    """if puedo:
        return reinas(agregar(tablero, fila, columna), 0, columna + 1)
    else:
        return reinas(tablero, fila + 1, columna)"""


if __name__ == '__main__':
    lis = [False,False,False,False]
    lis2 = [False,False,False,False]
    lis3 = [False,False,False,False]
    lis4 = [False,False,False,False]
    tablero = [lis, lis2, lis3, lis4]
    print(reinas(tablero, 0, 0))