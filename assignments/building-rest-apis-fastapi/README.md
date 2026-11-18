# 📘 Atividade: Building REST APIs com FastAPI

## 🎯 Objetivo

Construa uma API REST para administrar livros usando o framework FastAPI. Você vai praticar rotas HTTP, validação de dados com modelos Pydantic e respostas de erro para recursos que não existem.

## 📝 Tarefas

### 🛠️ Iniciar a API e explorar a documentação

#### Descrição
Instale as dependências, execute o starter code e explore a documentação interativa do FastAPI. Depois, atualize as informações da aplicação e a mensagem da rota inicial para identificar sua API.

Para instalar as dependências, execute `python -m pip install fastapi uvicorn` no terminal. Na pasta da atividade, inicie o servidor com `python -m uvicorn starter-code:app --reload` e abra `http://127.0.0.1:8000/docs` no navegador.

#### Requisitos
A aplicação concluída deve:

- Iniciar sem erros e responder à rota `GET /`
- Exibir um título e uma descrição que identifiquem a API
- Permitir que as rotas sejam exploradas em `/docs`


### 🛠️ Criar e listar livros

#### Descrição
Implemente os endpoints da coleção de livros. Use o modelo `Book` fornecido para validar os dados recebidos e armazene os livros em memória, associados a um ID inteiro único.

#### Requisitos
A API concluída deve:

- Responder a `GET /books` com a lista de livros e seus IDs
- Aceitar `POST /books` com título, autor e ano de publicação
- Atribuir um ID único a cada livro criado e incluí-lo na resposta
- Retornar os dados do livro criado como JSON


### 🛠️ Gerenciar livros por ID

#### Descrição
Adicione operações para consultar, atualizar e remover um livro específico. Use o ID recebido na URL para localizar o recurso e informe claramente quando ele não existir.

#### Requisitos
A API concluída deve:

- Responder a `GET /books/{book_id}` com o livro correspondente
- Aceitar `PUT /books/{book_id}` para substituir os dados do livro
- Aceitar `DELETE /books/{book_id}` para remover o livro
- Retornar o status HTTP `404` com uma mensagem útil quando o ID não existir
- Confirmar a remoção com uma resposta apropriada
