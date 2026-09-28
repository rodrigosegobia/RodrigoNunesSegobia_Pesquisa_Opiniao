excelente = 0
ruim = 0

for entrevistado in range(1, 51):
    print(f"\nEntrevistado {entrevistado}")

    nome = input("Digite o nome: ")

    while True:
        try:
            idade = int(input("Digite a idade: "))

            if idade > 0:
                break
            else:
                print("Idade inválida. Digite uma idade maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite apenas números para a idade.")

    print("\nOpinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    while True:
        try:
            opiniao = int(input("Digite a opção: "))

            if opiniao == 1 or opiniao == 2 or opiniao == 3:
                break
            else:
                print("Opção inválida. Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite apenas números.")

    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

print("\nResultado da pesquisa")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
