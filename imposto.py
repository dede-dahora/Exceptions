try:
    entrada = input("Preço do produto: ")
    
    if entrada == "":
        print("Você não digitou o preço.")
    else:
        preco = float(entrada)
        imposto = 1.1
        print("Preço com imposto:", preco * imposto)

except ValueError:
    print("Por favor, digite um número válido.")