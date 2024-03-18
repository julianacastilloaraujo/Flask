from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")    

@app.route("/eventos")
def eventos():
  return render_template("eventos.html")    

@app.route("/perfil/<n>/<int:n1>/<float:n2>")
def perfil(n, n1, n2):
  info = {
      "nombre": n,
      "entero": n1,
      "flotante": n2
    }
  return render_template("perfil.html", datos=info)

def ruta_parametros():
  print(request)
  print(request.args)
  print(request.args.get("p1"))
  print(request.args.get("p2"))    
  return "¡Hola, mundo!"

if __name__ == '__main__':  
    app.add_url_rule('/ruta_prueba', view_func=ruta_parametros)
    app.run(debug=True, port=3333)

