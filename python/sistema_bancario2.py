import textwrap

def menu():
    menu = """\n
    ==========MENU===========
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuario
    [5]\tcriar conta
    [6]\tlistar contas
    [7]\tSair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
              # valores por posiçao
    if valor > 0 :
        saldo += valor 
        extrato += f'Depósito: \tR$ {valor:.2f}\n'
        print("\n === Depósito realizado com sucesso! ===")
        # === significa mensagem de sucesso
    else:
        print("\n@@@ Operaçao falhou! O valor informado é inválido. @@@")
        # @@@ significa mesnagem de falha
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # * significa valores nomeados
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operaçao falhou! Voce nao tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operacao falhou! o valor do sque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operacao falhou! Numero maximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR${valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operacao falhou! o valor informado é invalido. @@@")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n========== EXTRATO ===========")
    print("Nao foram realizadas movimentaçoes." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("===============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Ja existe usuario com esse CPF! @@@")
        return 
    nome = input(" Informe o nome completo: ")
    data_nascimento = input("Informe data de nascimento (dd-mm-aaa): ")
    endereço = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})
    print("=== Usuario criado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuario nao encontrado, fluxo de criaçao de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            agencia:\t{conta['agencia']}
            C/C\t\t{conta['numero_conta']}
            titular:\t{conta['usuario']['nome']}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios =[]
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito:"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao =='2':
            valor = float(input("Informe o valor do saque:"))

            saldo, extrato = sacar(
                saldo= saldo,
                valor= valor,
                extrato= extrato,
                limite= limite,
                numero_saques= numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            criar_usuario(usuarios)
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)
        elif opcao == "7":
            break
        else:
            print("Operaçao invalida, por favor selecione novamente a operaçao desejada.")

main()