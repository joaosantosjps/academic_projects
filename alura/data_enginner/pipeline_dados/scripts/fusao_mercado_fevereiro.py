from pocessamento_dados import Dados

path_json = "../data_raw/dados_empresaA.json"
path_csv = "../data_raw/dados_empresaB.csv"

# Extract

dados_empresaA = Dados(path_json, "json")
print(dados_empresaA.nome_colunas)

dados_empresaB = Dados(path_csv, "csv")
print(dados_empresaB.nome_colunas)

# Transform

key_mapping = {
    "Nome do Item": "Nome do Produto",
    "Classificação do Produto": "Categoria do Produto",
    "Valor em Reais (R$)": "Preço do Produto (R$)",
    "Quantidade em Estoque": "Quantidade em Estoque",
    "Nome da Loja": "Filial",
    "Data da Venda": "Data da Venda"
}

dados_empresaB.remane_columns(key_mapping)
print(dados_empresaB.nome_colunas)

print(dados_empresaA.qtd_linhas)
print(dados_empresaB.qtd_linhas)

dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)

# Load

path_dados_combinado = "../data_processed/dados_combinados.csv"

dados_fusao.salvando_dados(path_dados_combinado)
print(path_dados_combinado)

#Iniciando a leitura

"""dados_json = leitura_dadods(path_json, "json")
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)

print(f"Nome colunas dados json: {nome_colunas_json}")
print(f"Tamanho dos dados json: {tamanho_dados_json}")

dados_csv = leitura_dadods(path_csv, "csv")
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)

print(f"Nomes colunas dados csv: {nome_colunas_csv}")
print(f"Tamanho dados csv: {tamanho_dados_csv}")

#Transformação dos dados

dados_csv = remane_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)

print(nome_colunas_csv)

dados_fusao = join(dados_csv, dados_json)
nome_colunas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)

print(nome_colunas_fusao)
print(tamanho_dados_fusao)

#Salvando Dados

dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)

path_dados_combinado = "../data_processed/dados_combinados.csv"


salvando_dados(dados_fusao_tabela, path_dados_combinado)

print(path_dados_combinado)
"""