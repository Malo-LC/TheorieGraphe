from re import A
import numpy as np
import pandas as pd


df = pd.read_fwf('tableauContrainte2.txt',
                 delim_whitespace=True, header=None, engine='python')
print(df)
tabContr = df.to_numpy(dtype=np.int32)


def nbSommets(data):
    shape = data.shape
    return shape[0]


def nbArcs(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    somme = 0

    for i in range(3, col+1):
        for j in range(0, lin):
            if(data[:, i-1:i][j] >= 0):
                somme += 1
    return somme


def ToutLesArcs(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    a = np.array([], dtype=int)

    for i in range(3, col+1):
        for j in range(0, lin):
            if(data[:, i-1:i][j] >= 0):
                a = np.append(a, data[:, i-1:i][j])
                print(data[:, i-1:i][j])
    return a


print('il y a ', nbSommets(tabContr), ' sommets')

print('il y a ', nbArcs(tabContr), ' arcs')

print(ToutLesArcs(tabContr))
