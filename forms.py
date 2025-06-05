from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, DateField
from wtforms.validators import DataRequired, Optional

class TarefaForm(FlaskForm):
    titulo = StringField('Título', validators=[DataRequired()])
    observacao = TextAreaField('Observação', validators=[Optional()])
    data_inicio = DateField('Data de Início', format='%Y-%m-%d', validators=[Optional()])
    data_fim = DateField('Data de Fim', format='%Y-%m-%d', validators=[Optional()])
    submit = SubmitField('Adicionar')