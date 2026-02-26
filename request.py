import requests

nome = input("Digite o nome ou número do Pokémon: ").strip().lower()

if not nome:
    print("Você não digitou nada.")
else:
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    
    try:
        resposta = requests.get(url, timeout=10)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            print("Nome:", dados["name"].title())
            print("Altura:", dados["height"])
            print("Peso:", dados["weight"])
        elif resposta.status_code == 404:
            print("Pokémon não encontrado.")
        else:
            print("Erro na requisição:", resposta.status_code)
    
    except requests.exceptions.RequestException:
        print("Erro de conexão. Verifique sua internet.")