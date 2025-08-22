# 🖥️ CRUD Simples com Tkinter e SQLite

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-UI%20Framework-008080)
![SQLite](https://img.shields.io/badge/SQLite-Database%20Management-006400)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 📌 Sobre o Projeto
Este projeto foi desenvolvido com o objetivo de praticar operações CRUD (Create, Read, Update, Delete) em Python, utilizando a interface gráfica Tkinter e um banco de dados SQLite. A aplicação gerencia informações de clientes, com funções de inserir, atualizar, excluir e visualizar registros. 
O projeto tem a intenção de ser uma base simples para implementar sistemas de gestão de dados utilizando Python.


## 🚀 Funcionalidades
- **Inserir Cliente: Cadastrar um novo cliente no banco de dados.**
- **Visualizar Todos: Exibir todos os clientes cadastrados.**
- **Buscar Cliente: Buscar clientes com base em nome, sobrenome, email ou CPF.**
- **Atualizar Cliente: Modificar dados de clientes já cadastrados.**
- **Deletar Cliente: Excluir clientes selecionados da base de dados.**

## 🛠 Tecnologias Utilizadas
- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) Framework para a interface gráfica
- [SQLite](https://sqlite.org/) Banco de dados leve embutido

## 📁 Estrutura do Projeto
```
projeto-crud-python/
├── aplicacao.py            # Arquivo principal para rodar o aplicativo
├── Backend.py              # Lógica de interação com o banco de dados (SQLite)
├── interface.py            # Interface gráfica (Tkinter)
├── README.md               # Este arquivo
├── requirements.txt        # Bibliotecas necessárias
```
## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/Gabriel4002/projeto-crud-python.git
cd projeto-crud-python
```

2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Gere o executável:
```bash
pyinstaller --onefile --windowed --noconsole aplicacao.py
```
- Isso gerará um arquivo .exe no diretório dist/ que pode ser executado sem precisar de um terminal.

## 📝 Observações

- A aplicação utiliza um banco de dados SQLite local, que será automaticamente criado no diretório do projeto ao inserir o primeiro registro.
- O código é um exemplo básico de como usar operações CRUD com Tkinter e SQLite e serve como base para sistemas maiores.

## ✍️ Autor

Gabriel Lobato  
[LinkedIn](https://www.linkedin.com/in/gabriel-lobato-314096371)

---

> Este projeto foi desenvolvido como parte do meu aprendizado sobre Python, Tkinter, SQLite e manipulação de bancos de dados relacionais.
