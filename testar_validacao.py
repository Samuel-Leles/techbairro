
# =========================================================
# TESTAR VALIDAÇÃO (Aula 21)
# =========================================================
#
# Testa as regras de negócio SEM abrir a janela e SEM mexer
# no banco.
#
# Execute: python testar_validacao.py

from cliente import Cliente
from validacao import ValidadorCliente

validador = ValidadorCliente()


# Cria um cliente válido, que serve de base para os testes
def cliente_valido():
    return Cliente(
        "Ana Souza",
        "61999990001",
        "ana@email.com",
        "Rua 1 Casa 2"
    )


# T1: cliente com todos os dados certos
def teste_cliente_valido():
    assert validador.validar(cliente_valido()) is None


# T2: endereço vazio
def teste_endereco_vazio():
    cliente = cliente_valido()
    cliente.endereco = ""

    assert validador.validar(cliente) == "Preencha o(s) campo(s): Endereço"


# T3: telefone com letras
def teste_telefone_com_letras():
    cliente = cliente_valido()
    cliente.telefone = "6199ABC0001"

    assert validador.validar(cliente) == "Telefone inválido: use somente números."


# COMPLETE: T4, T5 e T6
#T4: email sem ponto
def teste_email_sem_ponto():
    cliente = cliente_valido()
    cliente.email = "ana@email"

    assert validador.validar(cliente) == "Email inválido: use o formato nome@dominio.com"

#T5 nome e telefone vazios ao mesmo tempo
def teste_nome_telefone_vazios():
    cliente = cliente_valido()
    cliente.nome = ""
    cliente.telefone = ""

    assert validador.validar(cliente) == "Preencha o(s) campo(s): Nome, Telefone"

#T6 email com nada antes do @
def teste_email_vazio_no_inicio():
    cliente = cliente_valido()
    cliente.email = "@email.com"

    assert validador.validar(cliente) == "Email inválido: use o formato nome@dominio.com"

# Roda todas as funções que começam com "teste_"
if __name__ == "__main__":
    for nome, funcao in list(globals().items()):
        if nome.startswith("teste_"):
            funcao()
            print("OK", nome)

    print("Todos os testes passaram.")
