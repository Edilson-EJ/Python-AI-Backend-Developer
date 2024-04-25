# etapa if/ else elif

# if

saldo = 2000.0
saque = float(input("Informe o valor do saque:"))

if saldo >= saque:

    print("Realizando saque")

if saldo < saque:

    print("saldo insuficiente!")

# if else

saldo = 3000.0
saque = float(input("Informe o valor do saque:"))

if saldo >= saque:

    print("Realizando saque")

else:

    print("saldo insuficiente!")


# elif

opcao = int(input("Informe uma opção: [1] sacar \n[2] Extratto:"))

if opcao ==1:

    valor = float(input("Informe a quantia para o saque:"))

elif opcao == 2:

    print("Exibindo o extrato ...", saldo)

else: 

    sys.exit("Opcção inválida")