import re
from collections import defaultdict


class Oracion:

    def __init__(self, texto, usuario):
        self.texto = texto
        self.palabras = texto.split(" ")
        self.usuario = usuario

    def analizar_elementos_basicos(self):
        print(f"> El numero de caracteres (con espacios) es: {len(self.texto)}\n")

        oracion_sin_espacios = self.texto.replace(" ", "")

        print(f"> El numero de caracteres (sin espacios) es: {len(oracion_sin_espacios)}\n")

        print(f"> El numero de palabras es: {len(self.palabras)}\n")

        print(f"> Comienza con: {self.texto[0]}\n")
        print(f"> El segundo caracter es: {self.texto[1]}\n")
        print(f"> El tercer caracter es: {self.texto[2]}\n")
        print(f"> Los 5 primeros caracteres son: {self.texto[:5]}\n")

        print(f"> Termina en: {self.texto[-1]}\n")
        print(f"> El penultimo caracter es: {self.texto[-2]}\n")
        print(f"> El antepenultimo caracter es: {self.texto[-3]}\n")
        print(f"> Los ultimos 5 caracteres son: {self.texto[-5:]}\n")


    def analizar_saludo(self):
        if self.texto.startswith("Hola") or self.texto.startswith("Saludos"):
            print("> Esta oracion parece un saludo\n")
        else:
            print("> Esta oracion no parece un saludo\n")

        patron_de_oracion_completa = re.compile(r"[A-Z][\w\s,]+\.")

        print(f"> {"Si" if patron_de_oracion_completa.match(self.texto) else "No"} es una oracion completa\n")

        if self.usuario not in self.texto:
            print("> No es una introduccion\n")
        else:
            print("> Es una introduccion\n")

    def analizar_vocales(self):
        contador_vocales = 0
        for letra in self.texto:
            if letra.lower() in 'aeiou':
                contador_vocales += 1

        print(f"> La oracion tiene {contador_vocales} vocales\n")

        primera_vocal = ""
        i = 0
        while primera_vocal == "":
            if self.texto[i].lower() in 'aeiou':
                primera_vocal = self.texto[i]
            i += 1

        print(f"> La primera vocal es '{primera_vocal}' en la posicion {i - 1}\n")


    def analizar_palabras(self):
        print(f"> Las palabras de la oracion son: {self.palabras}\n")
        longitudes = []

        for palabra in self.palabras:
            longitud = len(palabra)
            longitudes.append(longitud)

        print(f"> Las longitudes de las palabras son: {longitudes}\n")

        longitud_promedio = sum(longitudes) / len(longitudes)

        print(f"> La longitud promedio de las palabras es: {longitud_promedio}\n")

        print(f"> La palabra mas corta mide: {min(longitudes)}\n")

        print(f"> La palabra mas larga mide: {max(longitudes)}\n")

        contador_de_palabras = defaultdict(lambda: 0)
        for palabra in self.palabras:
            palabra_minusculas = palabra.lower()
            contador_de_palabras[palabra_minusculas] += 1

        print("> Contador de palabras:")
        for palabra, contador in contador_de_palabras.items():
            print(f"> {palabra}: {contador}")
        print()

    def analizar_oracion(self):
        print(f"> Analizando: '{self.texto}'...\n")

        self.analizar_elementos_basicos()

        self.analizar_saludo()

        self.analizar_vocales()

        self.analizar_palabras()
