import unittest
import datetime
from app import app, db, Tarefa  

class GerenciadorTarefasTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_criar_tarefa(self):
        response = self.app.post('/add', data={
            'titulo': 'Tarefa Teste',
            'observacao': 'Observação teste',  
            'data_inicio': '2025-06-01',
            'data_fim': '2025-06-10',
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        with app.app_context():
            tarefa = Tarefa.query.filter_by(titulo='Tarefa Teste').first()
            self.assertIsNotNone(tarefa)
            self.assertEqual(tarefa.observacao, 'Observação teste')

    def test_listar_tarefas(self):
        with app.app_context():
            nova = Tarefa(
                titulo='Teste',
                observacao='teste',
                data_inicio=datetime.date(2025, 6, 1),
                data_fim=datetime.date(2025, 6, 5),
                concluida=False
            )
            db.session.add(nova)
            db.session.commit()

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Teste', response.data)

if __name__ == '__main__':
    unittest.main()
