import requests 
import pandas as pd
import os
from datetime import date, timedelta, datetime
from sys import argv

def Estoque():

    diretorio_arquivo = os.path.dirname(os.path.abspath(argv[0])) # diretório do programa
    data_hora_geracao = datetime.now().strftime("%d-%m-%Y %H-%M-%S") # momento atual
    data_atual = date.today() # dia atual
    data_inicial = data_atual - timedelta(days=90) # dia atual menos 90
    data_final = data_atual
    offset = 0    # valor inicial do offset na chamada
    total_registros = 0
    todos_produtos = [] # criacao de uma lista que servirá para armazenar os dados de produtos 

    print("\n --------------------------------------------------------------------------------")
    print(f"📢 Iniciando importação de estoque para o período de {data_inicial} até {data_final}.")

    try:
        while True:
            api = requests.get(
                f'url_ocultada_xxxxxxxxxxxxxxxx_?offset={offset}&campo=dtupdate&de={data_inicial}&ate={data_final}',
                headers={'token': 'inserir_token_xxxxxxxxxxxxx'}
            )

            if api.status_code == 200:
                api = api.json()

                # Verifica se a chave 'data' existe e contém uma lista válida
                if not isinstance(api.get('data'), list) or not api['data']:
                    print("❗ Nenhum dado restante para importar.")
                    break 

                produtos = pd.DataFrame(api['data'])  # Converte JSON em DataFrame
            else:
                print("❌ Erro ao acessar API:", api.status_code)
                break

            remover_colunas = ["0", "1", "2", "3", "4", "5", "6", "7"] 
            produtos = produtos.drop(columns=remover_colunas, errors="ignore")

            todos_produtos.append(produtos) # salva produtos em lista

            total_registros += len(produtos)
            print(f"💻 Lote de {len(produtos)} registros inserido com sucesso. Offset atual = {offset}")
            # print(produtos)

            offset += 1000  # Atualiza o offset para buscar os próximos 1000 registros

        if todos_produtos:

            pasta_arquivo = os.path.join(diretorio_arquivo, "Arquivos Gerados")
            os.makedirs(pasta_arquivo, exist_ok=True)
            caminho_arquivo = os.path.join(pasta_arquivo, f"Estoque_Completo_{data_hora_geracao}.xlsx")
            
            df_final = pd.concat(todos_produtos, ignore_index=True)
            df_final.to_excel(caminho_arquivo, index=False, engine="openpyxl") # openpyxl é o motor para salvar em xlsx

            print(f"✅ Arquivo Excel gerado com sucesso! Total de registros: {len(df_final)}")
        else:
            print("❗ Nenhum dado gravado.")

        # print(data_hora_geracao)
        print(f"✔️ O arquivo foi salvo em: {diretorio_arquivo}")

    except Exception as e:
        print(f"❌ Erro durante a importação: {e}")

    print(f"❗ Processamento concluído! Total de registros inseridos: {total_registros}")
    print("\n --------------------------------------------------------------------------------")

Estoque()
