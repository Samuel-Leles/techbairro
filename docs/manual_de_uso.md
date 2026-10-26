# Manual de uso da TechBairro

## A tela principal

A tela principal da TechBairro serve para cadastrar e gerenciar os clientes. Nela, temos os campos para colocar o nome, telefone, e-mail e endereço, além dos botões para cadastrar, editar e excluir clientes. Também temos a lista de clientes cadastrados e as mensagens que aparecem quando fazemos alguma ação.

## Cadastrar um cliente

1. Abra o sistema TechBairro.
2. Preencha os campos com o nome, telefone, e-mail e endereço do cliente.
3. Confira se os dados estão corretos.
4. Clique no botão para cadastrar o cliente.
5. Veja se o sistema confirmou o cadastro e se o cliente apareceu na lista.

## Consultar os clientes cadastrados

1. Abra a tela principal do sistema.
2. Veja a lista de clientes cadastrados.
3. Procure o cliente que deseja consultar.

## Alterar os dados de um cliente

1. Encontre o cliente na lista e selecione ele.
2. Clique no botão de editar.
3. Altere os dados que precisar.
4. Confirme a alteração.
5. Confira se os dados foram atualizados na lista.

## Excluir um cliente

1. Encontre o cliente que deseja excluir e selecione ele.
2. Clique no botão de excluir.
3. Confira se o cliente mostrado na confirmação é o correto.
4. Confirme a exclusão se tiver certeza.
5. Veja se o cliente saiu da lista.

## Regras de preenchimento

| Campo | Obrigatório? | Regra |
|---|---|---|
| Nome | Sim | Deve ser preenchido com o nome do cliente. |
| Telefone | Sim | Deve ser preenchido com o telefone do cliente. |
| E-mail | Sim | Deve ser preenchido com o e-mail do cliente. |
| Endereço | Sim | Deve ser preenchido com o endereço do cliente. |

## Mensagens do sistema

| Mensagem | O que significa | O que fazer |
|---|---|---|
| Cliente cadastrado com sucesso. | O cliente foi cadastrado. | Confira se ele apareceu na lista. |
| Cliente atualizado com sucesso. | Os dados do cliente foram alterados. | Confira se as alterações estão corretas. |
| Cliente excluído com sucesso. | O cliente foi excluído. | Confira se ele não aparece mais na lista. |
| Preencha os campos obrigatórios. | Algum campo ficou vazio. | Preencha os campos que faltam e tente novamente. |
| Nenhum cliente selecionado. | Você tentou editar ou excluir sem selecionar um cliente. | Selecione um cliente na lista e tente novamente. |
| Confirma a exclusão do cliente? | O sistema está perguntando se você realmente quer excluir o cliente. | Confira se o cliente está correto antes de confirmar. |
| Cliente não encontrado. | O sistema não encontrou o cliente que você tentou consultar ou alterar. | Confira a lista e tente novamente. |

## Dúvidas frequentes

**1. O que faço se não conseguir cadastrar um cliente?**

Confira se todos os campos obrigatórios foram preenchidos e tente novamente.

**2. Como faço para alterar o telefone ou o endereço de um cliente?**

Selecione o cliente na lista, clique no botão de editar, altere os dados e confirme a operação.

**3. Como faço para excluir um cliente cadastrado errado?**

Selecione o cliente, clique no botão de excluir e confira os dados na mensagem de confirmação antes de confirmar.

**4. Os dados continuam salvos quando fecho o sistema?**

Sim. Os dados ficam armazenados no arquivo `techbairro.db` e podem ser consultados quando o sistema for aberto novamente.

**5. O que faço se tentar editar um cliente sem selecionar ninguém?**

Selecione o cliente desejado na lista antes de clicar no botão de editar.

**6. Como faço uma cópia de segurança dos clientes?**

Feche o sistema e copie o arquivo `techbairro.db` para outra pasta segura.