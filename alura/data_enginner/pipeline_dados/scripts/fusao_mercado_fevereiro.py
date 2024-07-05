import json
import csv

def leitura_json(path_json):
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    
    return dados_json

def leitura_csv(path_csv):
    dados_csv = []
    
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
            
    return dados_csv

def leitura_dadods(path, tipo_arquivo):
    dados = []
    
    if tipo_arquivo == "csv":
        dados = leitura_csv(path)

    elif tipo_arquivo == "json":
        dados = leitura_json(path)

    return dados

def get_columns(dados):
    return list(dados_json[0].keys())

def remane_columns(dados, key_mapping):
    new_dados_csv = []

    for old_dict in dados:
        dict_temp ={}

        for old_key, value in old_dict.items():
            dict_temp[key_mapping[old_key]] = value

        new_dados_csv.append(dict_temp)

    return new_dados_csv

path_json = "../data_raw/dados_empresaA.json"
path_csv = "../data_raw/dados_empresaB.csv"


#Iniciando a leitura

dados_json = leitura_dadods(path_json, "json")
nome_colunas_json = get_columns(dados_json)
print(nome_colunas_json)

dados_csv = leitura_dadods(path_csv, "csv")
nome_colunas_csv = get_columns(dados_csv)
print(nome_colunas_csv)

key_mapping = {
    "Nome do Item": "Nome do Produto",
    "Classificação do Produto": "Categoria do Produto",
    "Valor em Reais (R$)": "Preço do Produto (R$)",
    "Quantidade em Estoque": "Quantidade em Estoque",
    "Nome da Loja": "Filial",
    "Data da Venda": "Data da Venda"
}


#Transformação dos dados

dados_csv = remane_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(nome_colunas_csv)


