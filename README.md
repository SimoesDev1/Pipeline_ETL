# Pipeline_ETL

Uma pipeline de ETL (Extract, Transform, Load) para processar e analisar dados de forma eficiente e escalável.

🧩 Sumário
- [Sobre](#sobre)
- [Arquitetura](#arquitetura)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias](#tecnologias)
- [Instalação](#instalação)
- [Uso](#uso)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)

📖 Sobre:
Este projeto implementa uma pipeline ETL para extrair dados de fontes diversas, transformá-los conforme regras de negócio e carregá-los em destinos específicos para análise e visualização.

 🏗 Arquitetura
A arquitetura da pipeline segue o padrão clássico ETL:
1. Extract: Coleta de dados de fontes variadas.
2. Transform: Processamento e transformação dos dados.
3. Load: Carregamento dos dados transformados para os destinos definidos.

🗂 Estrutura do Projeto
├── Data_raw/ # Dados brutos extraídos
├── Data_processed/ # Dados processados prontos para análise
├── Notebooks/ # Jupyter Notebooks para análise exploratória
├── Scripts/ # Scripts Python para execução da pipeline
├── requirements.txt # Dependências do projeto
└── README.md # Este arquivo

🛠 Tecnologias
- Python: Linguagem principal para desenvolvimento.
- Pandas: Biblioteca para manipulação de dados.
- Jupyter Notebook: Ambiente para análise exploratória.
- Outras bibliotecas: Dependências listadas no `requirements.txt`.

🚀 Instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/SimoesDev1/Pipeline_ETL.git
   cd Pipeline_ETL
