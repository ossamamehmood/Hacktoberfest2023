import numpy as np
import time

def game(tamaño1,tamaño2):
    matriz = np.zeros(shape=(tamaño1,tamaño2))
    return matriz


plano=game(21,13)



def patron(matriz):
    matriz[2][5] = 1
    matriz[3][6] = 1
    matriz[4][7] = 1
    matriz[7][5] = 1
    matriz[8][6] = 1
    matriz[8][7] = 1
    matriz[12][5] = 1
    matriz[12][6] = 1
    matriz[12][7] = 1
    matriz[13][5] = 1
    matriz[13][7] = 1
    matriz[14][5] = 1
    matriz[14][6] = 1
    matriz[14][7] = 1
    matriz[17][6] = 1
    matriz[18][5] = 1
    matriz[19][6] = 1
    return matriz


seed=patron(plano)
print(seed)
def conditions(matriz):
    new_matriz=game(21,13)
    print("matriz funcion")
    print(matriz)
    print("matriz funcion")
    for i  in range(len(matriz)):
        for j in range(len(matriz[0])):
            value = 0
            if i == 0 and j == 0:
                value = matriz[i][j+1]+matriz[i+1][j]+matriz[i+1][j+1]
            elif i == 0 and j == 12:
                value = matriz[i][j-1]+matriz[i+1][j-1]+matriz[i+1][j]
            elif i == 20 and j == 0:
                value = matriz[i-1][j]+matriz[i-1][j+1]+matriz[i][j+1]
            elif  i == 20 and j == 12:
                value = matriz[i-1][j]+matriz[i-1][j-1]+matriz[i][j-1]
            elif i == 0 and j != 0 and j != 12:
                value = matriz[i][j-1]+matriz[i+1][j-1]+matriz[i+1][j]+matriz[i+1][j+1]+matriz[i][j+1]
            elif j == 0 and i != 0 and i != 20:
                value = matriz[i-1][j]+matriz[i-1][j+1]+matriz[i][j+1]+matriz[i+1][j+1]+matriz[i+1][j]
            elif i == 20 and j != 0 and j!= 12:
                value = matriz[i][j-1]+matriz[i-1][j-1]+matriz[i-1][j]+matriz[i-1][j+1]+matriz[i][j+1]
            elif j == 20 and i != 0 and i != 20:
                value = matriz[i-1][j]+matriz[i-1][j-1]+matriz[i][j-1]+matriz[i+1][j-1]+matriz[i+1][j]
            elif j > 0 and j < 12 and i > 0 and i < 20 :
                print(i)
                print(j)
                value = matriz[i-1][j-1]+matriz[i-1][j]+matriz[i+1][j+1]+matriz[i][j-1]+matriz[i][j+1]+matriz[i+1][j-1]+matriz[i+1][j]+matriz[i+1][j+1]

            new_matriz[i][j]=rule(value)
    print("nueva matriz")        
    print(new_matriz)
    print("nueva matriz")        
    return new_matriz



def rule(mount):
    res = 0
    if mount < 2:
        res = 0
    elif mount == 2 or mount == 3:
        res = 1
    else: 
        res = 0
    return res

def iteration(seed):
    for i in range(8):
        nm=conditions(seed)
        print(nm)
        seed=nm
        time.sleep(3)

iteration(seed)
