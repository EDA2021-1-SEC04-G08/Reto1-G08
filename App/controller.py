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
 """

import config as cf
import model
import csv
from re import split


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros


def initCatalog(tipo):
    catalog = model.newCatalog(tipo)
    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    loadVideos(catalog)
    loadCategories(catalog)


def loadVideos(catalog):
    videofile = cf.data_dir + 'videos/videos-large.csv'
    input_file = csv.DictReader(open(videofile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)


def loadCategories(catalog):
    ctfile = cf.data_dir + 'videos/category-id.csv'
    input_file = csv.DictReader(open(ctfile, encoding='utf-8'))
    for category in input_file:
        dic = {}
        num = split('\D+', category['id\tname'])
        lista = category['id\tname'].split()
        palabra = lista[1:]
        n = "".join(num)
        p = ' '.join(palabra)
        dic[p] = n
        model.addCategory(catalog, dic)


# Funciones de ordenamiento

def sortVideos(catalog, num, orden):
    """
    Ordena los libros por average_rating
    """
    return model.sortVideos(catalog, num, orden)


# Funciones de consulta sobre el catálogo

def categoria_pedida(catalog, pedido):
    return model.categoria_pedida(catalog, pedido)


def sublistReq1(catalog, category, country):
    sublist = model.sublistReq1(catalog, category, country)
    return sublist
