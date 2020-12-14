# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:45:43 2020
    
@author: Alvaro Muruchi
"""

import pandas as pd

lista=[]
lista2=[]
mini = []
minimos=[]
datos=pd.read_csv('ruta.csv',header = 0)

for j in range(4):
    fila=datos.iloc[j]
    for i in range(4):
        lista2.append(fila[i])
    lista.append(lista2)
    lista2=[]

print('Matriz de distancias: \n',lista,'\n')
for i in range(4):
    for j in range(4):
        if lista[i][j] != 0:
            mini.append(lista[i][j])
    minimos.append(min(mini))
    mini=[]
print('Nodos Minimos: ',minimos)
print('limite Inferior: ', sum(minimos),'\n')
# In[]
minimoG=sum(minimos)
posicionesglobales=[]
minimosglobales=[]
distanciasrecorridas=[]
sup=0
inf=0

for j in range(4):
    
    posicioneslocales=[]
    supaux=0
    infaux=0    
    minlocal=[]    
    nodoM=9999
    listaM=[]    
    ifal=0
    ifals=[]
    yfals=[]
    k=0
    l=0
    
    if j != 0:
        sup=j
        inf=0
        posicioneslocales.append(inf)
        posicioneslocales.append(sup)
        minlocal.append(lista[0][j])
        supaux=sup
        ifal=inf
        ifals.append(ifal)
        yfals.append(supaux)
       # print(ifals,'/ /',yfals)
        while k < 4:
            ifal = supaux
            if ifal not in ifals :
                ifals.append(ifal)
            #    print('yfals',yfals)
                while l < 4:
             
                    if l not in yfals and l!=0:
                        if lista[ifal][l] != 0:
                            if lista[ifal][l] < nodoM:
                                nodoM = lista[ifal][l]
                              #  print('-',nodoM)
                                infaux=ifal
                                supaux=l
                                ifal=supaux
                    l += 1
                    if l!=0 and supaux not in yfals:
                        yfals.append(supaux)
                        posicioneslocales.append(supaux)
                        minlocal.append(nodoM)
                     
            k += 1
            l=0
            nodoM=9999
            if len(minlocal)==3:
                minlocal.append(lista[supaux][0])
               # print(minlocal)
    k=0
    #print('columnas ',yfals)
    minimosglobales.append(minlocal)
    posicionesglobales.append(posicioneslocales)
    distanciasrecorridas.append(sum(minlocal))
print('Posiciones recorridas: ',posicionesglobales)
print('Distancias recorridas: ',minimosglobales)
print('suma de Distancias recorridas: ',distanciasrecorridas)
