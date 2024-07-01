import json
import httpx as x
import pandas as pd
import time
import jmespath
import os
import random
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
    timer = random.uniform(45 , 75)
    time.sleep(timer)
    result = client.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}",)
    print(username)
    data = json.loads(result.content)
    return data["data"]["user"]

#CRIA UM ARQUIVO EM JSON NA PASTA RESULTADOS COM O NOME DO USUÁRIO PESQUISADO 

def write_user(username: str):
    username = username[0]

# VERIFICA SE O ARQUIVO COM O NOME JÁ EXISTE
    filepath = f'resultado/{username}.json'

    if os.path.exists(filepath):
        return
    
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


# ## codigo teste

# import json
# import httpx as x
# import pandas as pd
# import time

# # CRIAÇÃO DE CLIENT PARA BUSCAR DE API COM IP REMOTO
# client = x.Client(
#     headers={
#         # this is internal ID of an Instagram backend app. It doesn't change often.
#         "x-ig-app-id": "936619743392459",
#         # use browser-like features
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
#         "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Accept": "*/*",
#     }
# )

# # BUSCA NA API PELO NOME DE USUÁRIO E RETORNA TODOS OS DADOS EM JSON
# def scrape_user(username: str):
#     try:
#         result = client.get(f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}")
#         if result.status_code == 200:
#             data = json.loads(result.content)
#             return data["user"]
#         else:
#             print(f"Failed to fetch data for {username}. Status code: {result.status_code}")
#             return None
#     except Exception as e:
#         print(f"Error fetching data for {username}: {str(e)}")
#         return None

# # CRIA UM ARQUIVO EM JSON NA PASTA RESULTADOS COM O NOME DO USUÁRIO PESQUISADO
# def write_user(username: str):
#     try:
#         user = scrape_user(username)
#         if user is not None:  # Verifica se o usuário retornado não é None
#             with open(f'resultado/{username}.json', 'w') as f:
#                 json.dump(user, f)
#     except Exception as e:
#         print(f"Error writing data for {username}: {str(e)}")

# # UTILIZA DE UM MAP PARA ATIVAR A FUNÇÃO write_user E LISTAR TODOS OS ARQUIVOS
# def complete_followers():
#     try:
#         followers = pd.read_csv("followers.csv", usecols=["username"])
#         followers.apply(write_user, axis=1)
#     except Exception as e:
#         print(f"Error processing followers: {str(e)}")

# # ATIVAÇÃO DO ARQUIVO
# def main():
#     complete_followers()

# # CONFIGURAÇÃO DO ARQUIVO
# if __name__ == "__main__":
#     main()
