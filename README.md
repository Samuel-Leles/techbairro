# TechBairro — Cadastro de Clientes

## Objetivo

O TechBairro é um sistema de cadastro e gerenciamento de clientes desenvolvido em Python com Tkinter e SQLite.

O sistema permite cadastrar, consultar, editar e excluir clientes, mantendo os dados salvos no banco de dados `techbairro.db`.

## Funcionalidades

- Cadastro de clientes.
- Consulta dos clientes cadastrados.
- Edição dos dados de um cliente.
- Exclusão de clientes.
- Validação dos campos obrigatórios.
- Validação do número de telefone.
- Validação básica do e-mail.
- Contador de clientes cadastrados.
- Armazenamento permanente dos dados em banco SQLite.
- Confirmação antes da exclusão de um cliente.

## Tecnologias utilizadas

- Python
- Tkinter
- SQLite
- Programação Orientada a Objetos (POO)

## Estrutura principal

O sistema possui duas classes principais:

### Cliente

A classe `Cliente` representa os dados de um cliente:

- Nome
- Telefone
- E-mail
- Endereço
- ID

Também possui métodos para gerar um resumo dos dados e obter as iniciais do nome.

### GerenciadorClientes

A classe `GerenciadorClientes` é responsável pelo gerenciamento dos clientes no banco de dados SQLite.

Ela possui operações para:

- Adicionar clientes.
- Listar clientes.
- Atualizar clientes.
- Remover clientes.
- Consultar a quantidade de clientes.

## Banco de dados

O sistema utiliza o banco de dados SQLite:

```text
techbairro.db