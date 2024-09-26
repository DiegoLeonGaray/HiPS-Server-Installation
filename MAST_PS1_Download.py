#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In[4]:

from astroquery.mast import Observations


print("Filtrando Datos PS1...")


"""

La instrucción Observations.query_criteria(*args) retorna las observaciones
que cumplen con el criterio entregado en los argumentos. En específico, se puede
filtrar por misión de cielo (como PS1), por filtro (como el filtro "r"), y por
ascención recta o declinación (como filtrar por hemisferio norte. dec in [0,90].)

"""

products = Observations.query_criteria(obs_collection="PS1",filters='r',s_dec=[0,90])
products.sort(["obsid"])#Ordenar es necesario para saber en que proceso quedó el código en caso de desconexión.


print(len(products))
N=len(products)






print("Comenzando descarga de imágenes...")


"""

Debido a que se espera que la instrucción anterior entregue una cantidad elevada
de observaciones, es necesario descargar el producto de datos de interés de tales
observaciones de forma secuencial, dividiendo las observaciones en conjuntos de 200
observaciones. Lo anterior, dado que el producto de datos del total de observaciones
excede la cantidad límite de descargas aceptadas por la librería.

Se tendrán len(products)//200 procesos, donde en cada proceso se descargarán 200 imágenes 
(pues solo nos interesa el producto de datos "stack image").

El parámetro i define el inicio de descarga de imágenes según el dataframe "products". 
i puede comenzar desde un valor>0 en caso de que el código sufra una desconexión y ya se
hayan descargado imágenes.

El parámetro contador, mantiene la información sobre en que proceso de los len(products)//200 procesos
está siendo ejecutado.

El parámetro fin define el último proceso a realizar.
"""

contador=1
fin=N//200 + 1
i=0

while(i<N):
    if(i==(N//200)*200):
        data_products = Observations.get_product_list(products[i:N])
    else:
        data_products = Observations.get_product_list(products[i:i+200])
    print("Comenzando proceso " + str(contador) + "/" + str(fin))
    manifest = Observations.download_products(data_products, description="stack data image")
    print("Proceso " + str(contador) + " completado.")
    print(str(i)+"/200000 imágenes descargadas.")
    contador=contador+1
    i=i+200
    
print("Descarga completada.")
    




















