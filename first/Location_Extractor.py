# coding=utf-8
import nltk
from geotext import GeoText
text = """
Luis Escala
Piedras 623
Piso 2, depto 4
C1070AAM, Capital Federal
Argentina
"""
places = GeoText(text)
print places.countries
