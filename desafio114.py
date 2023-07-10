import requests
def verificar_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"O site {url} está disponível.")
        else:
            print(f"O site {url} está indisponível (código de status: {response.status_code}).")
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro ao acessar o site {url}: {e}")

# Exemplo de uso
verificar_site("pudim.com.br")
