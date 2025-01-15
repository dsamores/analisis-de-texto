import re
from collections import defaultdict


class Oracion:

    def __init__(self, texto, usuario):
        self.texto = texto
        self.palabras = texto.split(" ")
        self.usuario = usuario

    def analizar_elementos_basicos(self):
        resultado = "<div><p><strong>Analisis basico:</strong></p><p>"

        resultado += f"El numero de caracteres (con espacios) es: {len(self.texto)}<br>"

        oracion_sin_espacios = self.texto.replace(" ", "")

        resultado += f"El numero de caracteres (sin espacios) es: {len(oracion_sin_espacios)}<br>"

        resultado += f"El numero de palabras es: {len(self.palabras)}<br>"

        resultado += f"Comienza con: {self.texto[0]}<br>"
        resultado += f"El segundo caracter es: {self.texto[1]}<br>"
        resultado += f"El tercer caracter es: {self.texto[2]}<br>"
        resultado += f"Los 5 primeros caracteres son: {self.texto[:5]}<br>"

        resultado += f"Termina en: {self.texto[-1]}<br>"
        resultado += f"El penultimo caracter es: {self.texto[-2]}<br>"
        resultado += f"El antepenultimo caracter es: {self.texto[-3]}<br>"
        resultado += f"Los ultimos 5 caracteres son: {self.texto[-5:]}<br>"

        resultado += "</p></div>"
        return resultado

    def analizar_saludo(self):
        resultado = "<div><p><strong>Analisis de saludo:</strong></p><p>"

        if self.texto.startswith("Hola") or self.texto.startswith("Saludos"):
            resultado += "Esta oracion parece un saludo<br>"
        else:
            resultado += "Esta oracion no parece un saludo<br>"

        patron_de_oracion_completa = re.compile(r"[A-Z][\w\s,]+\.")

        resultado += f"{"Si" if patron_de_oracion_completa.match(self.texto) else "No"} es una oracion completa<br>"

        if self.usuario not in self.texto:
            resultado += "No es una introduccion<br>"
        else:
            resultado += "Es una introduccion<br>"

        resultado += "</p></div>"
        return resultado

    def analizar_vocales(self):
        resultado = "<div><p><strong>Analisis de vocales:</strong></p><p>"
        contador_vocales = 0
        for letra in self.texto:
            if letra.lower() in 'aeiou':
                contador_vocales += 1

        resultado += f"La oracion tiene {contador_vocales} vocales<br>"

        primera_vocal = ""
        i = 0
        while primera_vocal == "":
            if self.texto[i].lower() in 'aeiou':
                primera_vocal = self.texto[i]
            i += 1

        resultado += f"La primera vocal es '{primera_vocal}' en la posicion {i - 1}<br>"

        resultado += "</p></div>"
        return resultado

    def analizar_palabras(self):
        resultado = "<div><p><strong>Analisis de palabras:</strong></p><p>"
        resultado += f"Las palabras de la oracion son: {self.palabras}<br>"
        longitudes = []

        for palabra in self.palabras:
            longitud = len(palabra)
            longitudes.append(longitud)

        resultado += f"Las longitudes de las palabras son: {longitudes}<br>"

        longitud_promedio = sum(longitudes) / len(longitudes)

        resultado += f"La longitud promedio de las palabras es: {longitud_promedio}<br>"

        resultado += f"La palabra mas corta mide: {min(longitudes)}<br>"

        resultado += f"La palabra mas larga mide: {max(longitudes)}<br>"

        contador_de_palabras = defaultdict(lambda: 0)
        for palabra in self.palabras:
            palabra_minusculas = palabra.lower()
            contador_de_palabras[palabra_minusculas] += 1

        resultado += "Contador de palabras:<br>"
        for palabra, contador in contador_de_palabras.items():
            resultado += (f"{palabra}: {contador}<br>")
        
        resultado += "</p></div>"
        return resultado

    def analizar_oracion(self):
        resultado = self.analizar_elementos_basicos()

        resultado += self.analizar_saludo()

        resultado += self.analizar_vocales()

        resultado += self.analizar_palabras()

        return resultado
