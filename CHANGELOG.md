# Changelog da TechBairro

## Em desenvolvimento
### Adicionado
- Código publicado no GitHub, com histórico de versões.

## v3.3.1 (Aula 20)
### Alterado
- O número da versão passou a ficar em um único lugar.
### Adicionado
- Script scripts/gerar_pacote.py, que gera o pacote ZIP da versão .
- Arquivo COMO_EXECUTAR.txt, com as instruções para executar a TechBairro.

### Alterado
- O banco agora é aberto pelo caminho completo (`os.path` + `__file__`), sempre na pasta do projeto, não importa de onde o programa seja executado.

### Adicionado
- Mensagem "Banco em uso" no terminal, mostrando qual arquivo de banco está sendo usado.

## v3.1 (Aula 15)

### Corrigido
- Corrigida a exclusão de clientes para remover o registro correto do banco de dados.
- Corrigida a atualização dos dados do cliente selecionado.
- Corrigida a seleção do cliente na Listbox utilizando `curselection()`.
- Corrigida a atualização da Listbox após alterar ou remover um cliente.
- Corrigido o carregamento dos clientes para manter a tela sincronizada com o banco de dados.

## v3.0 (Aula 14)

### Alterado
- O `GerenciadorClientes` deixou de guardar os clientes numa lista em memória e passou a gravar no banco SQLite `techbairro.db`.
- O cadastro de clientes passou a ser persistido no banco de dados.
- A aplicação passou a consultar os clientes diretamente no banco SQLite.

### Adicionado
- Criação e utilização da tabela `clientes` no banco de dados SQLite.

## v2.0 (Aulas 11 e 12)

### Adicionado
- Criação das classes `Cliente` e `GerenciadorClientes` para organizar melhor o código utilizando programação orientada a objetos.
- Criação da tela de Consulta para visualizar os clientes cadastrados.
- Implementação das operações de cadastro, listagem, atualização e remoção de clientes.

## Antes da v2.0 (Aulas 5 a 10)

- Criação da interface gráfica da TechBairro com Tkinter, incluindo janela, cabeçalho, campos de entrada e botões.
- Implementação de eventos e validações para o preenchimento correto dos dados dos clientes.
