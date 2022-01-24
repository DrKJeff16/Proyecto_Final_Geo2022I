#!/usr/bin/env python
# - authors: Guennadi Maximov Cortes, Johan Wences
# - email:  g.maxc.fox@protonmail.com
# - date:   25-Jan-2022
# - filename: conversor.py
# - last modified by:   Guennadi Maximov Cortes
# - last modified time: 25-Jan-2022
# - license: MIT
"""Conversor de coordenadas rectangulares esfericas y vice versa"""


import math
import sys


def get_point():
    """Retorna una tupla conteniendo cada componente de la coordenada rectangular"""
    txt = "Ingrese cada una de las coordenadas, separadas por un espacio: "

    while True:
        try:
            ent = input(txt).split()

            if len(ent) < 3:
                raise ValueError("No hay suficientes componentes.")

            for ind in range(len(ent)):
                try:
                    if ent[ind] == '':
                        del ent[ind]
                    else:
                        ent[ind] = float(ent[ind])
                except IndexError:
                    break

            if len(ent) != 3:
                raise ValueError("No hay suficientes componentes.")

        except ValueError:
            txt = "Intente nuevamente: "

    return tuple(ent)


def rect_to_sph(rect):
    """Convierte de coordenadas rectangulares a esfericas"""
    x = rect[0] * math.cos(rect[1]) * math.sin(rect[2])
    y = rect[0] * math.sin(rect[1]) * math.sin(rect[2])
    z = rect[0] * math.cos(rect[2])

    return (x, y, z)


def sph_to_rect(sph):
    """Convierte de coordenadas esfericas a rectangulares"""
    rho = math.sqrt(sph[0] ** 2 + sph[1] ** 2 + sph[2] ** 2)
    phi = math.acos(sph[2] / rho)
    theta = math.atan(sph[1] / sph[0])

    return (rho, phi, theta)


if __name__ == '__main__':
    print(rect_to_sph((3, 0.0, math.pi / 3)))

    sys.exit()
