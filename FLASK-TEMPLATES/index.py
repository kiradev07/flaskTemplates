from flask import Flask,render_template

app= Flask(__name__)

#MANDAR VARIABLES A LA VISTA
@app.route("/")
def index():
    name="mario"
    edad=44
    ape="bros"
    return render_template('./index.html',nombre=name,anios=edad,apellido=ape)


#eMANDAR DICCIONARIO
app.route("/diccionario")
def diccionario():
    dic= {'nombre':'cristian','edad':'28','pais':'Chile'}
    #se pasa el valor en el return para poder ocupar en el html la variable
    return render_template('dic.html',dicc=dic)

app.route("/listasPersona")
def listaPersona():
    personas= ['martin','cristian','andres','claudia']
    render_template('bucle.html',p=personas)

"""
app.route('/login')
def login():
    return render_template('../login.html')
"""

if __name__ == '__main__':
    app.run(debug=True)
