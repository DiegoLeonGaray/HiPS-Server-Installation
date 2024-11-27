#!/usr/bin/env python
# -*- coding: utf-8 -*-

# In[4]:

from astroquery.mast import Observations



def get_observations(collection="PS1", filters_list=["r"], ra_range=[30,35],dec_range=[10, 15]):
    """
    Observations are filtered according to the collection, filter,  declination range parameters.

    Parameters:
    - collection (str): Name of the mission or collection. For example "PS1".
    - filters_list (list): Filters to use for the search.
    - dec_range (list): Declination range [min, max].

    Returns:
    - products (list): List of filtered observation products.
    """
    print("Filtering Data...")
    try:
        products = Observations.query_criteria(obs_collection=collection, filters=filters_list, s_dec=dec_range, s_ra=ra_range)
        products.sort(["obsid"])
        print(f"Found {len(products)} observations.")
        return products
    except Exception as e:
        print(f"Error filtering observations: {e}")
        return []
    
def download_products_in_batches(products, batch_size=200):
    """
    Downloads the products in smaller batches to avoid exceeding
    download limits.

    Parameters:
    - products (list): List of observation products.
    - batch_size (int): The batch size to download the products in.
    """
    total_products = len(products)
    num_batches = (total_products // batch_size) + 1

    # Download in batches
    for batch in range(num_batches):
        start = batch * batch_size
        end = min((batch + 1) * batch_size, total_products)

        # Get the products for the batch
        products_batch = products[start:end]

        # Download the products
        print(f"Starting download for batch {batch + 1} of {num_batches}...")
        try:
            data_products = Observations.get_product_list(products_batch)
            manifest = Observations.download_products(data_products, description="stack data image")
            print(f"Batch {batch + 1} completed. {start + len(products_batch)}/{total_products} images downloaded.")
        except Exception as e:
            print(f"Error downloading batch {batch + 1}: {e}")

def main():
    """
    Main function to coordinate the program flow.
    """
    # Get the filtered observations
    products = get_observations(dec_range=[10,10.6])

    if not products:
        print("No products found. The process will terminate.")
        return

    # Display the first 20 products for reference
    print("First 20 filtered products:")
    print(products[:20])

    # Download the products in batches
    download_products_in_batches(products,batch_size=2)

    print("Download completed.")

if __name__ == "__main__":
    main()


"""

La instrucción Observations.query_criteria(*args) retorna las observaciones
que cumplen con el criterio entregado en los argumentos. En específico, se puede
filtrar por misión de cielo (como PS1), por filtro (como el filtro "r"), y por
ascención recta o declinación (como filtrar por hemisferio norte. dec in [0,90].)

"""

"""

products = Observations.query_criteria(obs_collection="PS1",filters=['r'],s_dec=[10,15])
products.sort(["obsid"])#Ordenar es necesario para saber en que proceso quedó el código en caso de desconexión.


print(len(products))
N=len(products)
print(products[0:20])


"""




#print("Comenzando descarga de imágenes...")


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
"""
    
#print("Descarga completada.")





















