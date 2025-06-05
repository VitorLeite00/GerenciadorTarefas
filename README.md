# ✅ Gerenciador de Tarefas

Este é um projeto simples e funcional de um **Gerenciador de Tarefas**, desenvolvido com **Flask (Python)**. A aplicação permite **criar, visualizar, editar, concluir e excluir tarefas** (CRUD), com persistência de dados via **SQLite**.

---

## 🎯 Objetivo da Aplicação

O objetivo principal é auxiliar o usuário no **gerenciamento de tarefas diárias**, fornecendo uma interface web intuitiva para:

- Adicionar novas tarefas
- Definir **data de início**, **data de término** e **observações**
- Marcar como concluída
- Editar ou excluir tarefas

Esse projeto também serve como prática para conceitos de **desenvolvimento web, código limpo, banco de dados** e **versionamento com Git/GitHub**.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia           | Finalidade                                 |
|----------------------|--------------------------------------------|
| **Python 3.x**       | Linguagem principal                        |
| **Flask**            | Framework web                              |
| **Flask-WTF**        | Manipulação de formulários com validação  |
| **Flask-SQLAlchemy** | ORM para comunicação com o banco de dados |
| **SQLite**           | Banco de dados relacional local            |
| **HTML5 + CSS3**     | Estrutura e estilo da interface            |
| **Visual Studio Code** | Editor de código recomendado              |

---

## 📦 Instalação e Execução

### ✅ Pré-requisitos

- Python 3 instalado
- Git instalado (opcional, mas recomendado)
- Ambiente virtual (recomendado)

### 🔧 Passos para rodar localmente

Bash / Terminal
# Clone o repositório
git clone https://github.com/VitorLeite00/GerenciadorTarefas.git
cd GerenciadorTarefas

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Execute o projeto
python app.py

Após isso, acesse no navegador: http://127.0.0.1:5000

# Como rodar os testes
Bash / Terminal 
Com o ambiente virtual ativado
python test_app.py

# Criado e desenvolvido por Vitor Hugo Gabriel Lopes Leite
