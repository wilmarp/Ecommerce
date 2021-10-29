import os, sys
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from markupsafe import escape
#import productos
import numpy as np
from productos import getProductosList, getProductosDeseadosList
from utils import crypto
import sqlite3
from hashlib import sha512
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import json
from datetime import date

con = sqlite3.connect('ecommerce.db', check_same_thread=False)

def InsertUsuario(entities, rol):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO usuario(usuario, password, primer_nombre, segundo_nombre, tipo_id, no_id, direccion, telefono, correo, estado) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', entities)
    usuario = cursorObj.lastrowid
    cursorObj.execute('INSERT INTO rol_usuario(id_rol, id_usuario) VALUES(?, ?)', (rol,usuario))
    session['usuario_id'] = usuario
    con.commit()

def Login(usuario, contrasena):
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

def obtenerUsuario(usuario):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, usuario, password, primer_nombre, segundo_nombre, tipo_id, no_id, direccion, telefono, correo, id_rol FROM usuario u JOIN rol_usuario r ON u.id = r.id_usuario WHERE usuario = ?', (usuario,))
    res = cursorObj.fetchone()
    return res

def obtenerUsuarioByID(id_usuario):
    cursorObj = con.cursor()
    cursorObj.execute('SELECT id, usuario, password, primer_nombre, segundo_nombre, tipo_id, no_id, direccion, telefono, correo, id_rol FROM usuario u JOIN rol_usuario r ON u.id = r.id_usuario WHERE id = ?', (id_usuario,))
    res = cursorObj.fetchone()
    return res

def getProductosComentariosDB(id_usuario, id_producto):
    cursorObj = con.cursor()
    sql =  'select u.primer_nombre, u.segundo_nombre, c.descripcion, c.fecha, c.id,'
    sql += 'case when c.id_usuario = ? then 1 else 0 end as UsuarioComentario '
    sql += 'from comentario as c join usuario as u on c.id_usuario = u.id where c.estado = 1 and id_producto = ? '
    cursorObj.execute(sql,(id_usuario,id_producto))
    return cursorObj.fetchall()

def getProductosImagenesDB(id_producto):
    cursorObj = con.cursor()
    sql =   'select ruta from imagen where id_producto = ? '
    cursorObj.execute(sql,(id_producto,))
    return cursorObj.fetchall()

def getProductosDB(usuario = 0):
    if "usuario_id" not in session:
        usuario = 0
    print("||||||||||||||||||||||||||||||||||||||"+ str(usuario))
    cursorObj = con.cursor()
    sql =   'select p.Id, '
    sql +=  '   p.Codigo,'
    sql +=  '   p.Nombre,'
    sql +=  '   case when cm.Comentarios is null then 0 else cm.Comentarios end as Comentarios, '
    sql +=  '   case when d.id is null then 0 else 1 end as Deseado, '
    sql +=  '   Precio, '
    sql +=  '   case when ca.calificacion is null then 0 else ca.Calificacion  end as Calificacion '
    sql +=  'from producto p '
    sql +=  'left join (select c.id_producto, count(*) as Comentarios from comentario c group by id_producto) as cm on p.id = cm.id_producto '
    sql +=  'left join (select ca.id_producto, cast(avg(ca.calificacion) as integer) as calificacion from calificacion ca group by id_producto) as ca on p.id = ca.id_producto '
    if usuario != 0:
        sql +=  'inner join producto_deseado d on p.id = d.id_producto '
        sql +=  'and d.id_usuario = ?'
        cursorObj.execute(sql,(usuario,))
    else:
        sql +=  'left join producto_deseado d on p.id = d.id_producto '
        cursorObj.execute(sql)

    data = list()
    res = cursorObj.fetchall()
    for row in res:
        r = list(row)
        images = getProductosImagenesDB(r[0])
        r.append(images)
        data.append(r)

    print(data)
    return jsonify(data)


    #np.asarray(res)
    # print(res[0][0])
    # a = list(res[0])
    # a.append([1,2])
    # return jsonify(a)

def getProductoDB(producto_id, usuario = 0):
    if "usuario_id" not in session:
        usuario = 0
    print("||||||||||||||||||||||||||||||||||||||"+ str(usuario))
    cursorObj = con.cursor()
    sql =   'select p.Id, '
    sql +=  '   p.Codigo,'
    sql +=  '   p.Nombre,'
    sql +=  '   case when cm.Comentarios is null then 0 else cm.Comentarios end as Comentarios, '
    sql +=  '   case when d.id is null then 0 else 1 end as Deseado, '
    sql +=  '   Precio, Descripcion, Stock, Color, Marca,'
    sql +=  '   case when ca.calificacion is null then 0 else ca.Calificacion  end as Calificacion '
    sql +=  'from producto p '
    sql +=  'left join (select c.id_producto, count(*) as Comentarios from comentario c where c.estado = 1 group by id_producto) as cm on p.id = cm.id_producto '
    sql +=  'left join (select ca.id_producto, cast(avg(ca.calificacion) as integer) as calificacion from calificacion ca group by id_producto) as ca on p.id = ca.id_producto '
    sql +=  'left join producto_deseado d on p.id = d.id_producto '
    sql += 'where p.id = ?'
    cursorObj.execute(sql,(producto_id,))

    data = list()
    res = cursorObj.fetchall()
    for row in res:
        r = list(row)
        images = getProductosImagenesDB(r[0])
        r.append(images)
        comentarios = getProductosComentariosDB(usuario, r[0])
        r.append(comentarios)
        data.append(r)

    print(data)
    return jsonify(data)

def InsertComentario(entities):
    cursorObj = con.cursor()
    cursorObj.execute('INSERT INTO comentario(id_producto, id_usuario, descripcion, fecha, estado) VALUES(?, ?, ?, ?, ?)', entities)
    con.commit()

def UpdateComentario(id, comentario):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE comentario SET descripcion = ? WHERE id = ?', (comentario,id))
    con.commit()

def DeleteComentario(id):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE comentario SET estado = 0 WHERE id = ?', (id,))
    con.commit()