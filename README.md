# 🏋️‍♂️ Gym Tracker API (Backend)

API desenvolvida com Flask para gerenciamento de treinos de academia. Permite cadastrar, listar e remover exercícios com informações como nome, séries, repetições e peso.

## 🚀 Tecnologias

- Python
- Flask
- Flask-CORS
- Flask-SQLAlchemy
- flask-openapi3 (Swagger)
- SQLite

## 📂 Estrutura

- `app.py`: Arquivo principal da aplicação Flask.
- `model.py`: Define o modelo da tabela de exercícios.
- `database.db`: Banco de dados SQLite.
- `requirements.txt`: Dependências do projeto.

## To Do

- Atualizar a API para editar os exercícios
- Atualizar a interação do usuário 
- Atualizar a quantidade de repetições dos exercícios para poder receber um range, além de um número

## 🔧 Como rodar o backend

1. **Clone o repositório:**
   ```bash
   git clone (https://github.com/Eduardokwj/back-end_gym_tracker/tree/main/meu_app_api%20(backend))
   cd backend

É recomendado utilizar um ambiente virtual do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

2. **Crie e ative um ambiente virtual:**

```
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/macOS
```

3. **Instale as dependências:**
```
pip install -r requirements.txt
```

4. **Execute a aplicação:**

```
(env)$ flask run --host 0.0.0.0 --port 5000
```

A API estará disponível em: http://127.0.0.1:5000

📌 Rotas da API

GET /exercicios: Lista todos os exercícios.

POST /exercicio: Adiciona um novo exercício.

DELETE /exercicio?nome=...: Remove um exercício pelo nome.
