
try:
    entrada = input("Quantas notas? ")
    
    if entrada == "":
        print("Você não informou a quantidade.")
    else:
        qtd = int(entrada)
        
        if qtd <= 0:
            print("A quantidade deve ser maior que zero.")
        else:
            soma = 0
            
            for i in range(qtd):
                while True:
                    try:
                        nota = float(input(f"Nota {i+1}: "))
                        soma += nota
                        break
                    except ValueError:
                        print("Digite uma nota válida.")

            media = soma / qtd
            print("Média:", media)

except ValueError:
    print("Digite um número inteiro válido para a quantidade.")
