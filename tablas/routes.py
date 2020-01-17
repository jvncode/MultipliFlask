from tablas import app
from flask import render_template, request

@app.route("/")
def elegir_tabla():
    return render_template("index.html")

@app.route("/tabla", methods=['POST'])
def selecTabla():
    valor = request.values.get("tablas")
    return render_template("tabla.html", vTabla=int(valor))
