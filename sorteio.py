
nomes = ["Arthur", "Gabriel", "Enzo", "Julia"]

entrada = input(f"Indique um número (0 a {len(nomes)-1}) para sortear uma pessoa: ")

try:
    if entrada == "":
        print("Você não digitou nenhum número.")
    else:
        i = int(entrada)
        
        if 0 <= i < len(nomes):
            print("Nome:", nomes[i])
        else:
            print("Número fora do intervalo permitido.")

except ValueError:
    print("Por favor, digite um número inteiro válido.")
