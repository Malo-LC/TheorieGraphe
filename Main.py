import numpy as np
import pandas as pd


#df = pd.read_table('tableauContrainte.txt', sep='\t')

df = pd.read_fwf('tableauContrainte2.txt',
                 delim_whitespace=True, header=None, engine='python')

print(df)

tabContr = df.to_numpy(dtype=np.int32)

print(tabContr)


nbSommets = len(tabContr[:, 1:])
print(nbSommets, ' sommets')


def nbArcs(data):
    somme = 0
    taille = len(data) + 2

    for i in range(0, taille):
        if(data[:i-1, i] < 0):
            somme += 1
    return somme


print(nbArcs(tabContr), ' arcs')
