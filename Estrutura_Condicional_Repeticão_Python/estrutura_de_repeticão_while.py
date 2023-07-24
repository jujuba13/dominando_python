opcao = 1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] sair \n: "))

    if opcao == 1:
        print("Sacando dinheiro...")
    elif opcao == 2:
        print("Exibindo extrato bancario...")
else:
    print("Obrigado(a) por ser o nosso cliente!")
    