from processamento import Dados
import pandas as pd

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
dados_json = Dados(path_json, "json")
dados_csv = Dados(path_csv, "csv")

# 4. Renomeia colunas automaticamente
dados_json.renomear_colunas(sinonimos_colunas)
dados_csv.renomear_colunas(sinonimos_colunas)

# 5. Obtém os DataFrames prontos
df_json = dados_json.get_dataframe()
df_csv = dados_csv.get_dataframe()

# 6. Padroniza colunas e concatena
colunas_padrao = list(set(df_json.columns).union(set(df_csv.columns)))
for col in colunas_padrao:
    if col not in df_json.columns:
        df_json[col] = pd.NA
    if col not in df_csv.columns:
        df_csv[col] = pd.NA

df_json = df_json[colunas_padrao]
df_csv = df_csv[colunas_padrao]

df_final = pd.concat([df_json, df_csv], ignore_index=True)
df_final['Data da Venda'] = df_final['Data da Venda'].fillna("Data não informada")

# 7. Salva o resultado
import os
os.makedirs("./Data_processed", exist_ok=True)
df_final.to_csv("./Data_processed/dados_combinados.csv", index=False)
print(" Dados combinados salvos com sucesso.")
