import json
import httpx as x
import pandas as pd
import time
import jmespath
from typing import Dict
    
# CRIAÇÃO DE CLIENT PARA BUSCAR DE API COM IP REMOTO
   
client = x.Client(
    headers={
        # this is internal ID of an instegram backend app. It doesn't change often.
        "x-ig-app-id": "936619743392459",
        # use browser-like features
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
    }
)

# BUSCA NA API PELO NOME DE USUÁRIO E RETORNA TODOS OS DADOS EM JSON

def scrape_user(username: str):
    time.sleep(2)
    result = client.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}",)
    print(username)
    data = json.loads(result.content)
    return data["data"]["user"]

#CRIA UM ARQUIVO EM JSON NA PASTA RESULTADOS COM O NOME DO USUÁRIO PESQUISADO 

def write_user(username: str):
    username = username[0]
    user = scrape_user(username)
    with open(f'resultado/{username}.json', 'w') as f:
        json.dump(user, f)

# UTILIZA DE UM MAP PARA ATIVAR A FUNÇÃO write_user E LISTAR TODOS OS ARQUIVOS

def complete_followers():
    followers = pd.read_csv("followers.csv", usecols=["username"])
    followers.apply(write_user, axis=1)

# ATIVAÇÃO DO ARQUIVO

def main():
    complete_followers()

# CONFIGURAÇÃO DO ARQUIVO

if __name__ == "__main__":
    main()

# CÓDIGO DE BUSCAR BIO - NÃO FUNCIONANDO CORRETAMENTE AINDA

# def parse_user(data: Dict) -> Dict:
#     """Parse instagram user's hidden web dataset for user's data"""
#     logging.debug("parsing user data {}", data['username'])
#     result = jmespath.search(
#         """{
#         bio: biography
#         }""",
#         data,
#     )

# parse_user(user)