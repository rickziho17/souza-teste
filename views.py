from main import app
from flask import render_template, request, redirect, make_response

@app.route('/', methods = ['GET', "POST"])
def home():
    if request.method == 'POST':
        usuario = request.form['nome']
        if usuario.strip() == '':
            txt = "Por favor, digite um nome de usuario!"
            return render_template('index.html', info = txt)
        else:
            res = redirect('/inicio')
            res.set_cookie('nome', usuario)

            return res
            
    return render_template('index.html')

@app.route('/inicio')
def inico():
    nome = request.cookies.get('nome') 
    return render_template('inicio.html', nome = nome)