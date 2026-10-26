# Entrega final da TechBairro

Aluno(a): Samuel Lima Leles · Versão entregue: 3.3.2
Por que esse número de versão: Porque o sistema já sofreu 3 grandes atualizações MAJOR e mais 3 atualizações MINOR e por fim tiveram 2 patchs desde que chegamos a versão 3.3.0 o último sendo o release no GitHub que foi feito hoje dia 26/10/2026

| # | Item | Evidência |
|---|---|---|
| 1 | A aplicação funciona: os 6 casos de teste passaram | `docs/registro_de_testes.md` |
| 2 | A versão aparece na janela e é a mesma do CHANGELOG e do README | `techbairro.py`, `CHANGELOG.md` e `README.md` conferidos |
| 3 | O pacote foi testado numa pasta limpa | `dist/TechBairro-3.3.2.zip` extraído e testado em uma pasta separada |
| 4 | Tag e release publicadas, com o .zip anexado | Link da Release: https://github.com/Samuel-Leles/techbairro/releases/tag/v3.3.2 |
| 5 | O repositório não tem banco, `__pycache__` nem `dist` | Conferência dos arquivos no GitHub |
| 6 | O histórico tem commits com mensagens claras | Link dos commits: https://github.com/Samuel-Leles/techbairro/commits/main/ |
| 7 | README, manual de uso e requirements.txt estão no repositório | `README.md`, `docs/manual_de_uso.md` e `requirements.txt` |


## Roteiro da apresentação

1. O problema principal encontrado foi a dificuldade de organizqação de dados de clientes e a dificuldade e possíveis erros que podem acabar occorendo caso isso seja feito manualmente em uma lista física gigantesca por exemplo. Com isso, surge a TechBairro que é um sistema de cadastro de clientes que facilita a organização dos clientes cadastrados e a visualização das informações deles.
2. A partir disso, O sistema da TechBairro consegue cadastrar clientes, consultar, editar e excluir clientes.(O restante será mostrado na prática ao professor pela interface da propria TechBairro e vou explicar me baseando no que estou mostrando, também é importante lembrar de mostrar uma regra de validação)
3. A TechBairro foi construída em camadas separando de forma organizada partes do código em arquivos diferentes para melhorar o entendimento do sistema. Ela usa sqlite3 como banco de dados que salva as iformações localmente na máquina que está executando o sistema. No desenvolvimento da TechBairro ela passou por vários testes, alguns de validação por exemplo. Isso ate chegar a sua versão final a 3.3.2 que teve seu realese no GitHub no dia 26 de outubro de 2026
4. Tive diversas dificuldades na TechBairro e coisas que penso em melhorar como qa organização dos commits, como ainda estou aprendendo e melhorando no GIt e GitHub acabou que meu commits ficaram meio desorganizados e não tão fáceis de entender pois a mensagem nem sempre ficou tão clara, então, isso é um dos vários pontos a se melhorar na TechBairro.

## Perguntas

1. Porque o arquivo techbairro.db não está no GitHub?
O arquivo techbairro.db não está no GitHub pois ele contém dados de pessoas reais que não podem ser vazados pois caso sejam isso vai contra a LGPD e a pessoa que está controlando esses dados 

2. Abrir a Consulta, selecione a linha "Nenhum cliente cadastrado" e clicar em Editar selecionado. Essa sequência dava um problema em que nada acontecia na interface mas no terminal nós tinhamos um erro pois o código tentava exluir um cliente mas não tinha cliente nenhum no banco de dados, logo dava um erro no terminal. Por isso foi necessário criar uma label de status e um código para caso a pessoa tentar exluir um cliente inexistente ele bloquear essa ação


3. Como baixar só com o link do GitHub?
Caso o usuário tenha apenas o link do GitHub ele deve acessar o repositório no GitHub e clicar em Code → Download ZIP. Depois ele deve extrair a pasta ZIP e abrir ela no Visual Studio Code e depois rodar no terminal o código (isso deve abrir uma janela do Tkinter com o sistema já pronto pra uso):
```bash
python techbairro.py
```



## Autoavaliação
Acho que o roteiro da minha apresentração ficou bom, talvez grande demais, mas acredito que esteja bem explica e que dê para entender bem o que eu explicarei. eu não penso em muito o que mudar, já que se pensasse já teria mudado, então acho que meu roteiro ficou completo e bom. Nessa unidade, acho importante entender o Tkinter, que é o foco da matéria e também aprender outras coisas como criar uma base para sqlite3 já que foiusado no sistema e melhorar a lógica de programação(coisa que sinceramente não consegui muito bem, mas pretendo praticar mais em casa).