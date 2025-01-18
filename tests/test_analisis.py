import pytest

from src.analisis import Oracion

def test_analizar_elementos_basicos():
    oracion = Oracion("texto de prueba", "David")
    resultado = oracion.analizar_elementos_basicos()

    assert resultado == (
        "<div><p><strong>Analisis basico:</strong></p><p>"
        "El numero de caracteres (con espacios) es: 15<br>"
        "El numero de caracteres (sin espacios) es: 13<br>"
        "El numero de palabras es: 3<br>"
        "Comienza con: t<br>"
        "El segundo caracter es: e<br>"
        "El tercer caracter es: x<br>"
        "Los 5 primeros caracteres son: texto<br>"
        "Termina en: a<br>"
        "El penultimo caracter es: b<br>"
        "El antepenultimo caracter es: e<br>"
        "Los ultimos 5 caracteres son: rueba<br>"
        "</p></div>"
    )


@pytest.mark.parametrize(
    "texto, resultado_esperado",
    [
        (
            "texto de prueba",
            (
                "<div><p><strong>Analisis de saludo:</strong></p><p>"
                "Esta oracion no parece un saludo<br>"
                "No es una oracion completa<br>"
                "No es una introduccion<br>"
                "</p></div>"
            )
        ),
        (
            "Hola, este es un texto de prueba",
            (
                "<div><p><strong>Analisis de saludo:</strong></p><p>"
                "Esta oracion parece un saludo<br>"
                "No es una oracion completa<br>"
                "No es una introduccion<br>"
                "</p></div>"
            )
        ),
        (
            "Hola soy David, este es un texto de prueba",
            (
                "<div><p><strong>Analisis de saludo:</strong></p><p>"
                "Esta oracion parece un saludo<br>"
                "No es una oracion completa<br>"
                "Es una introduccion<br>"
                "</p></div>"
            )
        ),
    ]
)
def test_analizar_saludo(texto, resultado_esperado):
    oracion = Oracion(texto, "David")
    resultado = oracion.analizar_saludo()

    assert resultado == resultado_esperado
