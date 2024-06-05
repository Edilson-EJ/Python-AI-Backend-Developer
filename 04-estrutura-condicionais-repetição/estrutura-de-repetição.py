texto = input("Informe um texto:")
vogais = "AEIOU"

for letra in texto:

    if letra.upper() in vogais:
        print(letra, end="")

print()

opcao = -1

while opcao != 0:

    opcao = int(input("[1] sacar \n[2] extrato \n sair \n: "))

    if opcao == 1:
        print("sacando...")
    elif opcao ==2:
        print("exibindo o extratto...")