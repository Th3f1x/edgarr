from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
import sqlite3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descr = db.Column(db.Text)
    preco = db.Column(db.Text)
    codigo = db.Column(db.Text)

    def __init__(self, nome, descr, preco, codigo):
        self.nome = nome
        self.descr = descr
        self.preco = preco
        sel.codigo = codigo

@app.route('/')
def index():
    objetos = Item.query.all()
    return render_template('index.html', obejetos=objetos)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form['nome']
        descri = request.form['descri']
        preco = request.form['preco']
        codigo = request.form['codigo']
        item = Item(nome=nome, descri=descri, preco=preco,codigo=codigo)
        db.create_all()
        db.session.add(item)
        db.session.comit()
        return redirect('/')
    return render_template('registro.html')

@app.route('/edita/<int:item_id>', methods=['GET','POST'])
def edita(item_id):
    item = Item.query.get(item_id)
    if request.method == 'POST':
        item.nome = request.form['nome']
        item.descri = request.form['descri']
        item.preco = request.form['preco']
        item.codigo = request.form['codigo']
        db.session.commit()
        return redirect('/')
    return render_template('edita.html', item=item)

@app.route('/deleta/<int:item_id>', methods=['GET','POST'])
def deleta(item_id):
    item = Item.query.get(item)
    if request.method == 'POST':
        db.session.delete(item)
        db.session.commit()
        return redirect('/')
    return render_template('deleta.html', item=item)

if __name__ == "__main__":
    app.run(debug=True)

