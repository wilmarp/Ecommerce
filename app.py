from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from producto import producto

app = Flask(__name__)

@app.route('/producto/', methods=['GET'])
def getProducto():
    return jsonify({'producto' : producto})

if (__name__ == '__main__'):
    app.run(debug=True, port=8080)