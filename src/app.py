from flask import Flask, render_template, request

from src.analisis import Oracion

app = Flask(__name__)

@app.route("/")
def hola_mundo():
    return render_template("index.html")


@app.route("/analizar", methods=["POST", "GET"])
def analizar():
    texto = request.form.get("texto")

    oracion = Oracion(texto, "David")
    resultado = oracion.analizar_oracion()

    return render_template("index.html", texto=texto, resultado=resultado)
