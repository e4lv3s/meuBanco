def exibir_menu():
    menu = """
    ========== MENU ==========
    [0] Depositar
    [1] Sacar
    [2] Extrato
    [3] Sair
    ==========================
    => """
    return input(menu)


def realizar_deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def realizar_saque(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! O valor excede o limite por saque.")
    elif numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("===============================")


def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = exibir_menu()

        if opcao == "0":
            saldo, extrato = realizar_deposito(saldo, extrato)

        elif opcao == "1":
            saldo, extrato, numero_saques = realizar_saque(
                saldo, extrato, limite, numero_saques, LIMITE_SAQUES
            )

        elif opcao == "2":
            exibir_extrato(saldo, extrato)

        elif opcao == "3":
            print("Encerrando o sistema. Obrigado por utilizar nosso banco!")
            break

        else:
            print("Operação inválida. Tente novamente.")


if __name__ == "__main__":
    main()
