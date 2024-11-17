# Python CRUD API

Este projeto é uma API RESTful em Python que implementa operações CRUD (Create, Read, Update, Delete) para gerenciar informações de pessoas em um banco de dados SQLite. Ele utiliza o framework Flask e está estruturado para ser modular e escalável.

---

## **Recursos**

- Criar, consultar, atualizar e deletar registros de pessoas.
- Banco de dados SQLite para armazenamento local.
- Estrutura modular para facilitar manutenção e escalabilidade.

---

## **Instalação**

### **1. Clone o repositório**
```bash
git clone https://github.com/seu-repositorio/python-crud-api.git
cd python-crud-api
```

### **2. Crie e ative o ambiente virtual**

#### No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### No Linux/MacOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

### **3. Instale as dependências**
Com o ambiente virtual ativado, instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```

---

## **Executando o projeto**

1. Com o ambiente virtual ativado, execute o servidor:
   ```bash
   python run.py
   ```
2. O servidor estará disponível em `http://127.0.0.1:5000`.

---

## **Endpoints da API**

### **1. Criar uma nova pessoa**

- **URL:** `POST /people/`
- **Descrição:** Adiciona uma nova pessoa ao banco de dados.
- **Corpo da Requisição (JSON):**
  ```json
  {
    "name": "John Doe",
    "born_date": "1990-01-01",
    "document": "12345678901"
  }
  ```
- **Resposta de Sucesso (201 Created):**
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "born_date": "1990-01-01",
    "document": "12345678901"
  }
  ```

---

### **2. Listar todas as pessoas**

- **URL:** `GET /people/`
- **Descrição:** Retorna uma lista de todas as pessoas registradas.
- **Resposta de Sucesso (200 OK):**
  ```json
  [
    {
      "id": 1,
      "name": "John Doe",
      "born_date": "1990-01-01",
      "document": "12345678901"
    }
  ]
  ```

---

### **3. Obter os detalhes de uma pessoa**

- **URL:** `GET /people/<id>/`
- **Descrição:** Retorna os detalhes de uma pessoa específica com base no ID.
- **Resposta de Sucesso (200 OK):**
  ```json
  {
    "id": 1,
    "name": "John Doe",
    "born_date": "1990-01-01",
    "document": "12345678901"
  }
  ```
- **Erro (404 Not Found):**
  ```json
  {
    "error": "Person not found"
  }
  ```

---

### **4. Atualizar uma pessoa**

- **URL:** `PUT /people/<id>/`
- **Descrição:** Atualiza os dados de uma pessoa específica com base no ID.
- **Corpo da Requisição (JSON):**
  ```json
  {
    "name": "Jane Doe",
    "born_date": "1995-05-15"
  }
  ```
- **Resposta de Sucesso (200 OK):**
  ```json
  {
    "message": "Person updated successfully"
  }
  ```
- **Erro (404 Not Found):**
  ```json
  {
    "error": "Person not found"
  }
  ```

---

### **5. Deletar uma pessoa**

- **URL:** `DELETE /people/<id>/`
- **Descrição:** Remove uma pessoa do banco de dados com base no ID.
- **Resposta de Sucesso (200 OK):**
  ```json
  {
    "message": "Person deleted successfully"
  }
  ```
- **Erro (404 Not Found):**
  ```json
  {
    "error": "Person not found"
  }
  ```

---

## **Testando a API**

Você pode testar a API usando ferramentas como **Postman**, **Insomnia** ou o comando `curl`.

### **Exemplo com `curl`**

- **Criar uma pessoa:**
  ```bash
  curl -X POST http://127.0.0.1:5000/people/ \
       -H "Content-Type: application/json" \
       -d '{"name": "John Doe", "born_date": "1990-01-01", "document": "12345678901"}'
  ```

- **Listar todas as pessoas:**
  ```bash
  curl -X GET http://127.0.0.1:5000/people/
  ```

- **Consultar uma pessoa por ID:**
  ```bash
  curl -X GET http://127.0.0.1:5000/people/1/
  ```

- **Atualizar uma pessoa:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/people/1/ \
       -H "Content-Type: application/json" \
       -d '{"name": "Jane Doe", "born_date": "1995-05-15"}'
  ```

- **Deletar uma pessoa:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/people/1/
  ```

---

## **Estrutura do Projeto**

```plaintext
project-name/
├── app/
│   ├── __init__.py           # Inicializa o aplicativo e o banco de dados
│   ├── routes/               # Define as rotas/endpoints
│   │   ├── __init__.py       # Inicializa o módulo de rotas
│   │   └── people.py         # Rotas para o recurso "pessoas"
│   ├── models.py             # Define os modelos (tabelas do banco de dados)
│   ├── schemas.py            # Validação de dados (opcional)
│   ├── services.py           # Lógica de negócios para o recurso "pessoas"
│   ├── config.py             # Configurações da aplicação
│   └── utils/                # Funções auxiliares (opcional)
│       ├── __init__.py
│       └── helpers.py
├── migrations/               # Arquivos de migração do banco (opcional)
├── tests/                    # Testes automatizados
├── requirements.txt          # Dependências do projeto
├── run.py                    # Ponto de entrada para iniciar a aplicação
└── README.md                 # Documentação do projeto
```

---

## **Contribuição**

Contribuições são bem-vindas! Para contribuir:
1. Faça um fork do repositório.
2. Crie uma nova branch para sua feature ou correção: `git checkout -b minha-feature`.
3. Faça suas alterações e envie um pull request.

---

## **Licença**

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.