#!/usr/bin/env python
# - authors: Guennadi Maximov Cortes, Johan Ulises Herrera Wences
# - email:  g.maxc.fox@protonmail.com
# - date:   25-Jan-2022
# - filename: conversor.py
# - last modified by:   Guennadi Maximov Cortes
# - last modified time: 03-Feb-2022
# - license: MIT
"""Conversor de coordenadas rectangulares esfericas y vice versa"""


from math import pow, sqrt, pi, cos, sin, acos, atan
# import numpy as np
import sys


def get_point(tp):
    """Retorna una tupla conteniendo cada componente de la coordenada rectangular"""
    if tp == 1:
        txt = "Ingrese cada una de las coordenadas rectangulares, separadas por un espacio: "
    elif tp == 2:
        txt = "Ingrese cada una de las coordenadas esfericas, separadas por un espacio: "
    else:
        raise ValueError("Valor invalido.")

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
            else:
                break

        except ValueError:
            txt = "Intente nuevamente: "

    return tuple(ent)


def sph_to_rect(sph):
    """Convierte de coordenadas rectangulares a esfericas"""
    x = sph[0] * cos(sph[1]) * sin(sph[2])
    y = sph[0] * sin(sph[1]) * sin(sph[2])
    z = sph[0] * cos(sph[2])

    return (x, y, z)


def rect_to_sph(rect):
    """Convierte de coordenadas esfericas a rectangulares"""
    rho = sqrt(pow(rect[0], 2) + pow(rect[1], 2) + pow(rect[2], 2))
    phi = acos(rect[2] / rho)
    theta = atan(rect[1] / rect[0])

    return (rho, phi, theta)


if __name__ == '__main__':
    print("\n1) Convertir de Coordenadas Rectangulares a Esfericas\n",
            "2) Convertir de Coordenadas Esfericas a Rectangulares\n\n",
            end='', sep='')
    tipo = int(input("Elija su opcion: "))
    coords = get_point(tipo)

    if tipo == 1:
        print(rect_to_sph(coords))
    elif tipo == 2:
        print(sph_to_rect(coords))
    else:
        sys.exit(1)

    sys.exit(0)
