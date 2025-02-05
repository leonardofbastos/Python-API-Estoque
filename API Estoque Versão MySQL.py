import requests 
import json 
import pandas as pd
from datetime import date, timedelta, datetime
import mysql.connector

# Banco de dados local para testes:
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="leonardo",
    database="leonardo"
)

cursor = conn.cursor() # permite interagir com banco de dados

def Estoque():

    data_atual = date.today()
    data_inicial = data_atual - timedelta(days=90)
    data_final = data_atual

    print(f"Iniciando importação de estoque para o período de {data_inicial} até {data_final}.")

    offset = 1
    total_registros = 0

    try:
        while True:
            api = requests.get(
                f'url_ocultada_xxxxxxxxxxxxxxxx_?offset={offset}&campo=dtupdate&de={data_inicial}&ate={data_final}',   # informação real ocultada
                headers={'token': 'inserir_token_xxxxxxxxxxxxx'}                                                       # informação real ocultada
            )

            if api.status_code == 200:
                api = api.json()

                # Verifica se a chave 'data' existe e contém uma lista válida
                if not isinstance(api.get('data'), list) or not api['data']:
                    print("Nenhum dado restante para importar.")
                    break 

                produtos = pd.DataFrame(api['data'])  # Converte JSON em DataFrame
            else:
                print("Erro ao acessar API:", api.status_code)
                break

            remover_colunas = ["0", "1", "2", "3", "4", "5", "6", "7"] 
            produtos = produtos.drop(columns=remover_colunas, errors="ignore")

            data_sincronizacao = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Inserir os dados na tabela
            for _, row in produtos.iterrows():
                sql = """
                INSERT INTO klin_importar_estoque (id, 
                                                   produto_id, 
                                                   codigo, 
                                                   ean, 
                                                   nome, 
                                                   saldo, 
                                                   dtinsert, 
                                                   dtupdate,
                                                   data_sincronizacao)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE 
                    produto_id=VALUES(produto_id), 
                    codigo=VALUES(codigo), 
                    ean=VALUES(ean), 
                    nome=VALUES(nome), 
                    saldo=VALUES(saldo), 
                    dtinsert=VALUES(dtinsert), 
                    dtupdate=VALUES(dtupdate)
                """
                valores = (
                        row["id"], 
                        row["produto_id"], 
                        row["codigo"], 
                        row["ean"], 
                        row["nome"], 
                        row.get("saldo", 0), # aplica zero se vier nulo
                        row["dtinsert"],
                        row["dtupdate"],
                        data_sincronizacao
                )

                cursor.execute(sql, valores)

            total_registros += len(produtos)
            print(f"Lote de {len(produtos)} registros inserido com sucesso. Offset atual = {offset}")
            # print(produtos)

            offset += 1000  # Atualiza o offset para buscar os próximos 1000 registros

        conn.commit()

    except Exception as e:
        print(f"Erro durante a importação: {e}")

    finally:
        conn.close()  # Garantia de fechamento da conexão

    print(f"Importação concluída! Total de registros inseridos: {total_registros}")

Estoque()
