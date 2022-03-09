from operator import index
from turtle import clear
from unicodedata import name
import numpy as np
import pandas as pd


df= pd.read_table('tableauContrainte.txt', index_col=0)

print(df.index[0])