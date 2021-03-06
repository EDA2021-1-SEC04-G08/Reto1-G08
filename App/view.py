﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

sys.setrecursionlimit(1000*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar buenos videos por categoria y pais")
    print("3- Encontrar video tendencia por pais")
    print("4- Encontrar video tendencia por categoria individual")
    print("5- Encontrar con mas likes")
    print("6- Salir")


def initCatalog(tipo):
    return controller.initCatalog(tipo)


def loadData(catalog):
    controller.loadData(catalog)


def categoriaID(catalog, pedido):
    return controller.categoria_pedida(catalog, pedido)


def printVideos1(videos, cantidad):
    size = lt.size(videos)
    if size > cantidad:
        print(' Estos son los mejores videos: ')
        i = 0
        while i <= cantidad-1:
            video = lt.getElement(videos, i)
            print('Titulo: ' + video['title'] + ', Trending Date:' +
                  video['trending_date'] + ', Nombre del canal:' +
                  video['channel_title'] + ', Publish Time:' +
                  video['publish_time'] + ', Reproducciones:' +
                  video['views'] + ', Likes:' + video['likes'] +
                  ', Dislikes:' + video['dislikes'])
            i += 1
    else:
        print('No se encontraron videos')


catalog = None


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        data = input("Seleccione el tipo de estructura de datos desea " +
                     "usar (ARRAY_LIST) o (SINGLE_LINKED): ")
        print("Cargando información de los archivos ....")
        catalog = initCatalog(data)
        loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['video'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['category'])))

    elif int(inputs[0]) == 2:
        number = input("Cantidad de datos a listar: ")
        orden = input("seleccionar el tipo de algoritmo de ordenamiento " +
                      "iterativo (selection, insertion, shell," +
                      " quick, merge): ")
        pais = input("Seleccione un pais: ")
        categoria = input("Seleccione una categoria: ")
        top = input('Top?: ')
        catOrd = controller.sortVideos(catalog, int(number), orden)[1]
        cat = categoriaID(catalog, categoria)
        sublist = controller.sublistReq1(catOrd, cat, pais)
        print(printVideos1(sublist, int(top)))

    else:
        sys.exit(0)
sys.exit(0)
