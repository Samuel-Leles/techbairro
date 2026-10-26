# TechBairro

Techbairro é um cadastro de clientes que serve para cadastrar clientes e manter os dados deles salvos.

**Versão atual:** 3.3.1 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastro de clientes com nome, telefone, e-mail e endereço.
- Consultar clientes, podendo editá-los ou excluí-los.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows |
| Python | 3.12 (versão testada: 3.12) |
| Tkinter | Incluído na instalação do Python, quando disponível |
| Bibliotecas externas | Nenhuma |
| Internet | Não é necessária para executar o sistema localmente |

## Instalação

Antes de executar o sistema, verifique se o Python está instalado. Como o projeto não possui dependências externas, não é necessário instalar bibliotecas adicionais. O arquivo `requirements.txt` documenta os módulos utilizados pelo projeto.

Para verificar o arquivo, execute:

```bash
python -m pip install -r requirements.txt
```

O comando deve terminar sem erros e sem instalar pacotes.

### Opção 1 — Clonar com Git

1. Clone o repositório:

```bash
git clone https://github.com/Samuel-Leles/techbairro
```

2. Entre na pasta do projeto:

```bash
cd Techbairro 3.3.2
```

3. Execute o sistema:

```bash
python techbairro.py
```

### Opção 2 — Baixar pelo GitHub

1. Acesse o repositório no GitHub e clique em **Code → Download ZIP**.
2. Extraia o arquivo ZIP e abra a pasta do projeto no Visual Studio Code.
3. No terminal, execute:

```bash
python techbairro.py
```

Ao abrir o sistema, deve aparecer a janela gráfica da TechBairro e a mensagem `Banco em uso` no terminal.

## Configuração do banco de dados

O banco de dados da TechBairro utiliza o SQLite, por meio do módulo `sqlite3` do Python, e fica salvo no disco local da sua máquina. Ele é criado assim que o sistema é executado pela primeira vez.

O arquivo do banco de dados se chama `techbairro.db` e fica na pasta principal do projeto. Para ver qual banco de dados está sendo utilizado, você deve olhar o caminho exibido no terminal ao iniciar o sistema.

O arquivo `techbairro.db` não pode ser enviado ao GitHub, pois pode conter dados de pessoas reais, comprometendo a privacidade delas.

Para fazer uma cópia de segurança, feche o sistema e copie o arquivo `techbairro.db` para uma pasta segura.

## Como usar

O passo a passo está no [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto

- `techbairro.py`: arquivo principal que cuida da interface gráfica e da interação com o usuário.
- `cliente.py`: arquivo que contém a classe `Cliente`, responsável por estruturar os dados dos clientes.
- `banco.py`: arquivo responsável por criar e gerenciar o banco de dados do sistema.
- `validacao.py`: verifica se os dados informados ao cadastrar um cliente são válidos.
- `techbairro.db`: arquivo local que armazena os dados dos clientes e é criado automaticamente ao executar o sistema.
- `CHANGELOG.md`: registra as alterações do projeto.
- `README.md`: apresenta o projeto, como instalar, sua estrutura e o autor.
- `docs/manual_de_uso.md`: contém as informações para utilizar o sistema.
- `.gitignore`: contém os arquivos que devem ser ignorados pelo Git.
- `scripts`: pasta que contém alguns arquivos para testar o sistema.

## Autor

Samuel Lima Leles — Curso Técnico em Desenvolvimento de Sistemas — Senac.