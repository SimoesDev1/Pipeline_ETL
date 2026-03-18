import os
import pandas as pd
from processamento import Dados

# 1. Define os caminhos
path_json = "../Data_raw/dados_empresaA.json"
path_csv = "../Data_raw/dados_empresaB.csv"

# 2. Define os sinônimos
sinonimos_colunas = {
    'Nome do Produto': ['Nome do Item', 'Produto', 'Item'],
    'Categoria do Produto': ['Classificação do Produto', 'Categoria'],
    'Preço do Produto (R$)': ['Valor em Reais (R$)', 'Preço', 'Valor'],
    'Filial': ['Nome da Loja', 'Loja'],
    'Data da Venda': ['Data'],
    'Quantidade em Estoque': ['Estoque', 'Quantidade']
}

# 3. Carrega os dados
try:
    dados_json = Dados(path_json, "json")
    dados_csv = Dados(path_csv, "csv")
except FileNotFoundError as e:
    print(f"Erro ao carregar dados: {e}")
    exit(1)

# 4. Renomeia colunas automaticamente
dados_json.renomear_colunas(sinonimos_colunas)
dados_csv.renomear_colunas(sinonimos_colunas)

# 5. Obtém os DataFrames prontos
df_json = dados_json.get_dataframe()
df_csv = dados_csv.get_dataframe()

# 6. Padroniza colunas e concatena
colunas_padrao = list(dict.fromkeys(list(df_json.columns) + list(df_csv.columns)))
for col in colunas_padrao:
    if col not in df_json.columns:
        df_json[col] = pd.NA
    if col not in df_csv.columns:
        df_csv[col] = pd.NA

df_json = df_json[colunas_padrao]
df_csv = df_csv[colunas_padrao]

# Verificação de duplicatas antes do concat
print("Colunas df_json:", df_json.columns.tolist())
print("Colunas df_csv:", df_csv.columns.tolist())
print("Duplicadas df_json:", df_json.columns[df_json.columns.duplicated()].tolist())
print("Duplicadas df_csv:", df_csv.columns[df_csv.columns.duplicated()].tolist())

df_final = pd.concat([df_json, df_csv], ignore_index=True)

# 7. Salva na camada Silver
os.makedirs("../Data_silver", exist_ok=True)
df_final.to_csv("../Data_silver/dados_combinados.csv", index=False)
print("Dados combinados salvos com sucesso na camada Silver.")