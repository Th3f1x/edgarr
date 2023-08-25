from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100))
    idade = db.Column(db.Text)
    cpf = db.Column(db.Text)
    cep = db.Column(db.Text)


    def __init__(self, nome, idade, cpf, cep):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cep = cep

@app.route('/')
def index():
    tudo = Item.query.all()
    return render_template('index.html', tudo=tudo)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        cpf = request.form['cpf']
        cep = request.form['cep']
        item = Item(nome=nome, idade=idade, cpf=cpf, cep=cep)
        db.create_all()
        db.session.add(item)
        db.session.commit()
        return redirect('/')
    return render_template('registro.html')

@app.route('/edita/<int:item_id>', methods=['GET', 'POST'])
def edita(item_id):
    item = Item.query.get(item_id)

    if request.method == 'POST':
        item.nome = request.form['nome']
        item.idade = request.form['idade']
        item.cpf = request.form['cpf']
        item.cep = request.form['cep']
        db.session.commit()
        return redirect('/')
    
    return render_template('edita.html', item=item)

@app.route('/deleta/<int:item_id>', methods=['GET', 'POST'])
def deleta(item_id):
    item = Item.query.get(item_id)
    if request.method == 'POST':
        db.session.delete(item)
        db.session.commit()
        return redirect('/')
    return render_template('deletar.html', item=item)

if __name__ == '__main__':
    app.run(debug=True)
    