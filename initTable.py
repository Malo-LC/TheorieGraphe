import numpy as np
import pandas as pd


def choisirTXT(choix):
    df = pd.read_fwf('table ' + str(choix) + '.txt',
                     delim_whitespace=True, header=None, engine='python')
    # df = pd.read_fwf('tableauContrainte.txt',
    #                  delim_whitespace=True, header=None, engine='python')
    # print(df)
    tabContr = df.to_numpy(dtype=np.int32)
    tabContr[tabContr < 0] = -1
    return tabContr


def ToutLesArcs(data):
    shape = data.shape
    lin = shape[0]
    col = shape[1]
    a = np.array([], dtype=int)

    for i in range(3, col+1):
        for j in range(0, lin):
            if(data[:, i-1:i][j] >= 0):
                a = np.append(a, data[:, i-1:i][j])
    return a


def AlphaOmega(data):
    shape = data.shape
    indexAlpha = np.array([0, 0], dtype=int)
    lin = shape[0]
    col = shape[1]
    arcs = ToutLesArcs(data)
    for i in range(0, col+1):
        if(data[:, 2:3][i] < 0):
            data[:, 2:3][i] = 0
    while(len(indexAlpha) < col):
        indexAlpha = np.append(indexAlpha, -1)

    data = np.insert(data, 0, indexAlpha, 0)

    indexOmega = np.array([[lin + 1, 0]], dtype=int)
    for i in range(1, lin + 1):
        if i in arcs:
            a = 1
        else:
            indexOmega = np.append(indexOmega, i)

    while(len(indexOmega) < col):
        indexOmega = np.append(indexOmega, -1)

    if(len(indexOmega) > col):
        moins1 = np.full(shape=lin+1, fill_value=-1, dtype=np.int32)
        data = np.insert(data, col, moins1, axis=1)
    data = np.insert(data, lin + 1, indexOmega, 0)

    return data
