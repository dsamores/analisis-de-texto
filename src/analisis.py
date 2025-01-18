"""Modulo de analisis de texto. Incluye la clase Oracion."""
import re
from collections import defaultdict


class Oracion:
    """Clase Oracion para analisis de texto de una oracion."""

    def __init__(self, texto, usuario):
        """Constructor de Oracion."""
        self.texto = texto
        self.palabras = texto.split(" ")
        self.usuario = usuario

    def analizar_elementos_basicos(self):
        """Analisis de elementos basicos de la oracion."""
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
        """Analisis para determinar si la oracion es saludo o no."""
        resultado = "<div><p><strong>Analisis de saludo:</strong></p><p>"

        if self.texto.startswith("Hola") or self.texto.startswith("Saludos"):
            resultado += "Esta oracion parece un saludo<br>"
        else:
            resultado += "Esta oracion no parece un saludo<br>"

        patron_de_oracion_completa = re.compile(r"[A-Z][\w\s,]+\.")

        es_oracion = "Si" if patron_de_oracion_completa.match(self.texto) else "No"

        resultado += f"{es_oracion} es una oracion completa<br>"

        if self.usuario not in self.texto:
            resultado += "No es una introduccion<br>"
        else:
            resultado += "Es una introduccion<br>"

        resultado += "</p></div>"
        return resultado

    def analizar_vocales(self):
        """Analisis de vocales en la oracion."""
        resultado = "<div><p><strong>Analisis de vocales:</strong></p><p>"
        contador_vocales = 0
        contador_consonantes = 0
        for letra in self.texto:
            if letra.lower() in 'aeiou':
                contador_vocales += 1
            elif letra.isalpha():  # Verifica si la letra es alfabética (no es un número ni un signo de puntuación)
                contador_consonantes += 1

        resultado += f"La oracion tiene {contador_vocales} vocales<br>"
        resultado += f"La oracion tiene {contador_consonantes} consonantes<br>"

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
        """Analisis de palabras en la oracion."""
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
    
    def analizar_sentimiento(self):
        """Analisis de sentimiento de la oracion."""
        resultado = "<div><p><strong>Analisis de sentimiento:</strong></p><p>"

        palabras_positivas = {'bueno', 'feliz', 'positivo', 'excelente', 'genial'}
        palabras_negativas = {'malo', 'triste', 'negativo', 'terrible', 'horrible'}

        contador_positivo = 0
        contador_negativo = 0

        for palabra in self.palabras:
            if palabra.lower() in palabras_positivas:
                contador_positivo += 1
            elif palabra.lower() in palabras_negativas:
                contador_negativo += 1

        if contador_positivo > contador_negativo:
            resultado += "El sentimiento de la oracion es positivo<br>"
        elif contador_negativo > contador_positivo:
            resultado += "El sentimiento de la oracion es negativo<br>"
        else:
            resultado += "El sentimiento de la oracion es neutral<br>"

        resultado += f"Palabras positivas: {contador_positivo}<br>"
        resultado += f"Palabras negativas: {contador_negativo}<br>"
        resultado += f"Palabras neutrales: {len(self.palabras) - contador_positivo - contador_negativo}<br>"

        resultado += "</p></div>"
        return resultado

    def analizar_oracion(self):
        """Analisis comprehensivo de la oracion, llama a las otras funciones."""
        resultado = self.analizar_elementos_basicos()

        resultado += self.analizar_saludo()

        resultado += self.analizar_vocales()

        resultado += self.analizar_palabras()

        resultado += self.analizar_sentimiento()

        return resultado
