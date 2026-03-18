import pandas as pd

class Dados:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados.lower()
        self.dataframe = self._carregar_dados()

    def _carregar_dados(self):
        try:
            if self.tipo_dados == "csv":
                return pd.read_csv(self.path)
            elif self.tipo_dados == "json":
                return pd.read_json(self.path)
            else:
                raise ValueError("Tipo não suportado. Use 'csv' ou 'json'.")
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo não encontrado: {self.path}")

    def renomear_colunas(self, sinonimos_colunas):
        mapeamento = self._mapear_colunas(sinonimos_colunas)
        self.dataframe.rename(columns=mapeamento, inplace=True)

    def _mapear_colunas(self, sinonimos):
        colunas_originais = list(self.dataframe.columns)
        mapeamento = {}
        nomes_ja_mapeados = set()  # evita mapear duas colunas para o mesmo nome

        for nome_padrao, alternativas in sinonimos.items():
            for alt in alternativas:
                for col in colunas_originais:
                    if (
                            alt.lower() in col.lower()
                            and nome_padrao not in colunas_originais
                            and col not in mapeamento
                            and nome_padrao not in nomes_ja_mapeados  # novo
                    ):
                        mapeamento[col] = nome_padrao
                        nomes_ja_mapeados.add(nome_padrao)  # novo
        return mapeamento

    def get_dataframe(self):
        return self.dataframe

    def __repr__(self):
        return f"Dados(path='{self.path}', tipo='{self.tipo_dados}', shape={self.dataframe.shape})"