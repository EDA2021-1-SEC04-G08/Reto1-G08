"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import mergesort as ms
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos
listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def newCatalog(tipo):
    catalog = {'video': None,
               'category': None}

    catalog['video'] = lt.newList(datastructure=tipo.upper())
    catalog['category'] = lt.newList(datastructure=tipo.upper())

    return catalog


# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    lt.addLast(catalog['video'], video)


def addCategory(catalog, category):
    lt.addLast(catalog['category'], category)


# Funciones para creacion de datos


def sublistReq1(catalog, category, country):
    sublist = lt.newList()
    size = lt.size(catalog)
    for i in range(0, size-1):
        video = lt.getElement(catalog, i)
        if video["category_id"] == category and video["country"] == country:
            lt.addLast(sublist, video)
    return sublist

# Funciones de consulta


def categoria_pedida(catalog, pedido):
    cat = catalog['category']
    for category in cat:
        if pedido == category:
            return cat[category]
        else:
            return 'No se encontro la categoria escrita'

# Funciones utilizadas para comparar elementos dentro de una lista


def cmpVideosByViews(video1, video2):
    """
    Devuelve verdadero (True) si los 'views' de video1 son menores que los del
    video2.
    Args:
    video1: informacion del primer video que incluye su valor 'views'
    video2: informacion del segundo video que incluye su valor 'views'
    """
    return ((video1['views']) < (video2['views']))


# Funciones de ordenamiento

def sortVideos(catalog, num, orden):
    sub_list = lt.subList(catalog['video'], 0, num)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if orden.lower() == "selection":
        sorted_list = ss.sort(sub_list, cmpVideosByViews)

    elif orden.lower() == "insertion":
        sorted_list = ins.sort(sub_list, cmpVideosByViews)

    elif orden.lower() == "shell":
        sorted_list = sa.sort(sub_list, cmpVideosByViews)

    elif orden.lower() == "quick":
        sorted_list = qs.sort(sub_list, cmpVideosByViews)

    elif orden.lower() == "merge":
        sorted_list = ms.sort(sub_list, cmpVideosByViews)

    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return [elapsed_time_mseg, sorted_list]
