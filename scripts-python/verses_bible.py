#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (c) 2022 Jakepy Perdomo <j4kyjak3@protonmail.com>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random


class Colors:
    def __init__(self):
        self.__off = "\033[0m"
        self.__red = "\033[31m"
        self.__green = "\033[32m"

    @property
    def off(self):
        return self.__off

    @property
    def red(self):
        return self.__red

    @property
    def blue(self):
        return self.__blue

    @property
    def green(self):
        return self.__green


c = Colors()


verses = {
    "Génesis 1:1": "En el principio creó Dios los cielos y la tierra.",
    "Juan 3:16": "Porque de tal manera amó Dios al mundo, que ha dado a su Hijo unigénito, para que todo aquel que en él cree, no se pierda, mas tenga vida eterna.",
    "Romanos 3:23": "por cuanto todos pecaron, y están destituidos de la gloria de Dios.",
    "Filipenses 4:13": "Todo lo puedo en Cristo que me fortalece.",
    "Proverbios 3:5-6": "Fíate de Jehová de todo tu corazón, Y no te apoyes en tu propia prudencia. Reconócelo en todos tus caminos, Y él enderezará tus veredas.",
    "Salmos 23:1": "Jehová es mi pastor; nada me faltará.",
    "Romanos 6:23": "Porque la paga del pecado es muerte, mas la dádiva de Dios es vida eterna en Cristo Jesús Señor nuestro.",
    "Salmos 119:105": "Lámpara es a mis pies tu palabra, Y lumbrera a mi camino.",
    "Juan 14:6": "Jesús le dijo: Yo soy el camino, y la verdad, y la vida; nadie viene al Padre, sino por mí.",
    "2 Timoteo 3:16-17": "Toda la Escritura es inspirada por Dios, y útil para enseñar, para redargüir, para corregir, para instruir en justicia, a fin de que el hombre de Dios sea perfecto, enteramente preparado para toda buena obra.",
    "Salmos 37:4": "Deléitate asimismo en Jehová, Y él te concederá las peticiones de tu corazón.",
    "Efesios 2:8-9": "Porque por gracia sois salvos por medio de la fe; y esto no de vosotros, pues es don de Dios; no por obras, para que nadie se gloríe.",
    "Juan 1:1": "En el principio era el Verbo, y el Verbo era con Dios, y el Verbo era Dios.",
    "Salmos 46:1": "Dios es nuestro amparo y fortaleza, Nuestro pronto auxilio en las tribulaciones.",
    "Proverbios 18:10": "Torre fuerte es el nombre de Jehová; A él correrá el justo, y será levantado.",
    "Juan 8:12": "Otra vez Jesús les habló, diciendo: Yo soy la luz del mundo; el que me sigue, no andará en tinieblas, sino que tendrá la luz de la vida.",
    "Efesios 4:32": "Antes sed benignos unos con otros, misericordiosos, perdonándoos unos a otros, como Dios también os perdonó a vosotros en Cristo.",
    "Salmos 103:12": "Cuanto está lejos el oriente del occidente, Hizo alejar de nosotros nuestras rebeliones.",
}


def get_random_verse() -> str:
    random_key = random.choice(list(verses.keys()))
    return f"{c.red}{random_key} -> {c.green} {verses[random_key]}{c.off}"


if __name__ == "__main__":
    verse = get_random_verse()
    print(verse)
