
nome_arquivo = input("Arquivo: ")

if nome_arquivo == "":
    print("Você não digitou o nome do arquivo.")
else:
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except PermissionError:
        print("Sem permissão para abrir o arquivo.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
