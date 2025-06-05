from flask import Flask, render_template, redirect, url_for, request
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from forms import TarefaForm
from models import db, Tarefa

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app) 
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tarefas = Tarefa.query.all()
    form = TarefaForm()  
    return render_template('index.html', tarefas=tarefas, form=form)  

@app.route('/add', methods=['POST'])
def add():
    form = TarefaForm()
    if form.validate_on_submit():
        nova_tarefa = Tarefa(
            titulo=form.titulo.data,
            observacao=form.observacao.data,
            data_inicio=form.data_inicio.data,
            data_fim=form.data_fim.data,
            concluida=False
        )
        db.session.add(nova_tarefa)
        db.session.commit()
        flash('Tarefa adicionada com sucesso!')
    return redirect(url_for('index'))


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    tarefa = Tarefa.query.get_or_404(id)
    form = TarefaForm(obj=tarefa)
    if form.validate_on_submit():
        tarefa.titulo = form.titulo.data
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('form.html', form=form)

@app.route('/concluir/<int:id>')
def concluir(id):
    tarefa = Tarefa.query.get_or_404(id)
    tarefa.concluida = not tarefa.concluida
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/excluir/<int:id>')
def excluir(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
