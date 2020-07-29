from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/equipo")
def equipo():
    return render_template("equipo.html")

@app.route("/noticia")
def noticia():
    return render_template("noticia1.html")

if __name__ == "__main__":
    app.run(debug=True)
