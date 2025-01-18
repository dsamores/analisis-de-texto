"""App web de flask para analisis de texto."""
from flask import Flask, render_template, request

from src.analisis import Oracion

app = Flask(__name__)


@app.route("/")
def hola_mundo():
    """Pagina de inicio."""
    return render_template("index.html")


@app.route("/analizar", methods=["POST", "GET"])
def analizar():
    """Pagina de resultados de analisis de texto."""
    texto = request.form.get("texto")

    oracion = Oracion(texto, "David")
    resultado = oracion.analizar_oracion()

    return render_template("index.html", texto=texto, resultado=resultado)
