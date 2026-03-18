import pandas as pd
import os

df = pd.read_csv("../Data_silver/dados_combinados.csv")

os.makedirs("../Data_gold", exist_ok=True)

# Vendas por Filial
vendas_por_filial = (
    df.groupby("Filial")["Preço do Produto (R$)"]
    .sum()
    .reset_index()
    .rename(columns={"Preço do Produto (R$)": "Total Vendas (R$)"})
)
vendas_por_filial.to_csv("../Data_gold/vendas_por_filial.csv", index=False)

# Produtos por Categoria
produtos_por_categoria = (
    df.groupby("Categoria do Produto")["Nome do Produto"]
    .count()
    .reset_index()
    .rename(columns={"Nome do Produto": "Quantidade Vendida"})
    .sort_values("Quantidade Vendida", ascending=False)
)
produtos_por_categoria.to_csv("../Data_gold/produtos_por_categoria.csv", index=False)

# Estoque por Produto
estoque_por_produto = (
    df.groupby("Nome do Produto")["Quantidade em Estoque"]
    .sum()
    .reset_index()
    .sort_values("Quantidade em Estoque", ascending=False)
)
estoque_por_produto.to_csv("../Data_gold/estoque_por_produto.csv", index=False)

print("Camada Gold gerada com sucesso.")