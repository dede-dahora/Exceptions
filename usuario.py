
pessoa = {"nome": "João", "idade": 20}

chave = input("Qual campo quer ver? ").strip().lower()

try:
    if chave == "":
        print("Você não digitou nenhum campo.")
    else:
        print("Valor:", pessoa[chave])
        
except KeyError:
    print("Campo não encontrado.")
    print("Campos disponíveis:", ", ".join(pessoa.keys()))
