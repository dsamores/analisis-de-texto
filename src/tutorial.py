"""Aplicacion de comando de linea de analisis de texto."""

import sys

from src.analisis import Oracion


def saludo():
    """Esta funcion imprime un saludo y pide el nombre al usuario."""
    print("Ingresa tu nombre: ")
    nombre = input()

    apellido = 5

    mensaje_de_saludo = f"> Hola {nombre}! Yo me llamo Robot {apellido}\n"

    introduccion = (
        "> Yo soy un robot de analisis de texto. "
        "Puedes darme una oracion y yo la voy a analizar. "
        "Puedo contar el numero de palabras, "
        "puedo contar el numero de caracteres, "
        "puedo hacer analisis del sentimiento de la oracion y varias cosas mas.\n"
    )

    print(mensaje_de_saludo)

    print(introduccion)

    return nombre


def validar_oracion(oracion):
    """Validacion basica de la oracion ingresada."""

    if len(oracion) < 5:
        print("Error: La oracion es muy corta\n")
        sys.exit()
    elif len(oracion) >= 5 and len(oracion) < 20:
        print("> Esta es una oracion corta\n")
    else:
        print("> Esta es una oracion larga\n")


def main():
    """Funcion de ingreso de la aplicacion."""

    nombre = saludo()

    print("Ingresa una oracion:")
    texto = input()

    validar_oracion(texto)

    oracion = Oracion(texto, nombre)

    oracion.analizar_oracion()


main()
