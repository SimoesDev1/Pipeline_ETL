import pandas as pd

class Dados:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados.lower()
        self.dataframe = self._carregar_dados()

    def _carregar_dados(self):
        if self.tipo_dados == "csv":
            return pd.read_csv(self.path)
        elif self.tipo_dados == "json":
            return pd.read_json(self.path)
        else:
            raise ValueError("Tipo de dados não suportado. Use 'csv' ou 'json'.")

    def renomear_colunas(self, sinonimos_colunas):
        mapeamento = self._mapear_colunas(self.dataframe.columns, sinonimos_colunas)
        self.dataframe.rename(columns=mapeamento, inplace=True)

    def _mapear_colunas(self, colunas_originais, sinonimos):
        mapeamento = {}
        for nome_padrao, alternativas in sinonimos.items():
            for alt in alternativas:
                for col in colunas_originais:
                    if alt.lower() in col.lower() and nome_padrao not in colunas_originais:
                        mapeamento[col] = nome_padrao
        return mapeamento

    def get_dataframe(self):
        return self.dataframe
