# Registro de testes da TechBairro

**Versão testada:** 3.3.2  
**Data:** 26/10/2026  
**Responsável:** Samuel Lima leles  
**Sistema operacional e versão do Python:** Windows - Python 3.12

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar um cliente com todos os campos certos | O cliente ser cadastrado com sucesso | O cliente é cadastrado com sucesso | Funcionando |
| CT02 | RF01 | Salvar com Nome e Endereço vazios | Bloquear e surgir uma label de status que manda preencher os campos faltantes | A label de status surge corretamente e manda preencher os campos faltantes | Funciona |
| CT03 | RF02 | Telefone `61 9999 0000` (com espaços) | Não deixar salvar e falar para preenhcer o campo apenas com números | Não deixa salvar e surge a label de status | Funciona |
| CT04 | RF03 | E-mail `ana@email` (sem ponto) | Bloqueia e fala que deve usar o formato nome@domínio.com  | Ele bloqueia com sucesso e fala para usar o formato correto | Funciona |
| CT05 | RF05 | Editar um cliente, trocar o telefone e salvar | Edita o telefone com sucesso e salva o novo no banco de dados | O telefone é editado com syucesso e o novo telefone é salvo no banco de dados | Funciona |
| CT06 | RF06 | Excluir um cliente: responder Não, depois Sim | Ao responder não apenas fecha e não  exclui nada, se responder sim o cliente é excluído | O cliente não é escluuído caso responda não e se responder sim ele é escluído sem problemas | Funciona|

## Testes automáticos

**Saída do `python testar_validacao.py`:** Todos os testes passaram

## Defeitos encontrados

Nenhum

*(Descreva o que falhou, como foi corrigido e em qual commit, ou escreva "nenhum" se não houver defeitos.)*