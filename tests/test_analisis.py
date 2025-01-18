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
