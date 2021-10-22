import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from markupsafe import escape
#import productos
from producto import getProducto
from productos import getProductosList, getProductosDeseadosList
from utils import crypto
import sqlite3
from hashlib import sha512
from werkzeug.security import generate_password_hash, check_password_hash

con = sqlite3.connect('ecommerce.db', check_same_thread=False)

def InsertUsuario(con, entities, rol):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO usuario(usuario, password, primer_nombre, segundo_nombre, tipo_id, no_id, direccion, telefono, correo, estado) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entities)
    usuario = cursorObj.lastrowid
    cursorObj.execute('INSERT INTO rol_usuario(id_rol, id_usuario) VALUES(?, ?)', (rol,usuario))
    session['usuario_id'] = usuario
    con.commit()

def buscarUsuario(con, usuario):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, usuario, password, id_rol FROM usuario u JOIN rol_usuario r ON u.id = r.id_usuario WHERE usuario = ?', (usuario,))
    res = cursorObj.fetchone()
    return res

def Login(con, usuario, contrasena):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, usuario, password, id_rol FROM usuario u JOIN rol_usuario r ON u.id = r.id_usuario WHERE usuario = ?', (usuario,))
    res = cursorObj.fetchone()
    if(check_password_hash(res[2],contrasena)):
        session['usuario_id'] = res[0]
        session['usuario'] = res[1]
        session['rol'] = res[3]
        return "puede ingresar"
    else:
        return "no puede ingresar"

userSuperAdmin = 1
userAdmin = 2
userCliente = 3

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET','POST'])
def index():    
    return render_template('index.html')

@app.route('/producto', methods=['GET'])
@app.route('/producto/', methods=['GET'])
def producto():
    return render_template('product.html')

@app.route('/lista-deseos/', methods=['GET','POST'])
def htmlDeseos():    
    return render_template('deseos.html')

@app.route('/productos', methods=['GET','POST'])
@app.route('/productos/', methods=['GET','POST'])
def getProductos():
    return jsonify(getProductosList())

@app.route('/listadeseos/', methods=['GET','POST'])
def getProductosDeseados():    
    if( request.json["UserRef"] == crypto(session["userID"] )):
        return jsonify(getProductosDeseadosList())    
    else:
       return jsonify("")

@app.route("/putListadeseos/", methods=["GET", "POST"])
def putListadeseos():
    salida = {"SUCCESS": "ERROR", "DATA": ""}
    salida["SUCCESS"] = "OK"
    return jsonify(salida)

@app.route('/connect', methods=['GET','POST'])
@app.route('/connect/', methods=['GET','POST'])
def getConnect():
    session["tipoUser"] = userSuperAdmin
    session["userID"] = "1"
    data = {"tipoUser":userSuperAdmin, "ref": crypto(session["userID"])}
    return jsonify(data)

@app.route('/setUsuario/', methods=['GET','POST'])
def setUsuario():
    session["user"] = "jaime"
    session["pass"] = "asdfasdfasdfasd"
    return ""

@app.route('/getUsuario/', methods=['GET','POST'])
def getUsuario():
    return f'{session["user"]} --> {crypto(session["user"])} y password {session["pass"]} SuperAdmin: {session["sadmin"]}'

@app.route('/obtenerProducto', methods=['GET'])
@app.route('/obtenerProducto/', methods=['GET'])
def obtenerProducto():
    print("Entra")
    return jsonify(getProducto());

@app.route('/registro', methods=['GET'])
@app.route('/registro/', methods=['GET'])
def registro():
    return render_template('registro.html')

@app.route('/registrarUsuario', methods=['POST', 'GET'])
@app.route('/registrarUsuario/', methods=['POST', 'GET'])
def registrarUsuario():
    if request.method == 'POST':
        tipo_id = request.json['tipo_id']
        num_id = request.json['num_id']
        primer_nombre = request.json['primer_nombre']
        segundo_nombre = request.json['segundo_nombre']
        primer_apellido = request.json['primer_apellido']
        segundo_apellido = request.json['segundo_apellido']
        correo = request.json['correo']
        direccion = request.json['direccion']
        usuario = request.json['usuario']
        telefono = request.json['telefono']
        contrasena = generate_password_hash(request.json['contrasena'])
        rol = request.json['rol']
        existeUsuario = buscarUsuario(con,usuario)
        if existeUsuario[1]:
            return 'Ya existe un usuario'
        else:
            if tipo_id and num_id and primer_nombre and primer_apellido and correo and direccion and usuario and telefono and contrasena and rol:
                informacion = (usuario, contrasena, primer_nombre, primer_apellido, tipo_id, num_id, direccion, telefono, correo, 1)
                InsertUsuario(con,informacion,rol)
                return 'Registro Exitoso'
            else:
                return 'Datos invalidos'
    else:
        return 'Peticion incorrecta'
    


@app.route('/login', methods=['GET'])
@app.route('/login/', methods=['GET'])
def login():
    return render_template('login.html')

@app.route('/loguearUsuario', methods = ['POST', 'GET'])
@app.route('/loguearUsuario/', methods = ['POST', 'GET'])
def loguearUsuario():
    if request.method == 'POST':
        usuario = request.json['usuario']
        clave = request.json['clave']
        if usuario and clave:
            res = Login(con,usuario,clave)
            if res == 'puede ingresar':
                return 'Autorizado'
            else:
                return 'No autorizado'
        else:
            return 'Datos invalidos'
    else:
        return 'Peticion incorrecta'

@app.route('/logout/', methods=['GET'])
def logout():
    if "usuario_id" in session:
        session.pop('usuario_id')
        return redirect(url_for("login"))
    return redirect(url_for("login"))

@app.route('/gestionUsuario', methods=['GET'])
@app.route('/gestionUsuario/', methods=['GET'])
def gestionUsuario():
    return render_template('gestionUsuario.html')

@app.route('/probar', methods=['GET','POST'])
def fnProbar():    
    if(request.method == 'POST'): 
        txtCedula = escape( request.form['txtCedula'] )
        txtUsuario = 'Jaime'
        txtEmail  = 'Jaime@hotmail.com'
        return render_template('probar.html', txtCedula=txtCedula, txtUsuario=txtUsuario, txtEmail=txtEmail)
    return render_template('probar.html')


if(__name__ == '__main__'):
    app.run(debug=True, port=443, ssl_context=('micertificado.pem', 'llaveprivada.pem'))