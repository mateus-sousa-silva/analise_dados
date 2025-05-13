import pandas as pd

df = pd.read_csv("D:\PROGRAMACAO_FACULDADE\PROGRAMACAO_DE_COMPUTADORES\ANALISE_DE_DADOS\BASE_DE_DADOS\despesas_predio_2025.csv", sep=',', encoding='utf-8')

df.to_excel("D:\PROGRAMACAO_FACULDADE\PROGRAMACAO_DE_COMPUTADORES\ANALISE_DE_DADOS\PLANILHAS_TRATADAS\despesas_predio_2025.xlsx", index=False)

df_excel = pd.read_excel("D:\PROGRAMACAO_FACULDADE\PROGRAMACAO_DE_COMPUTADORES\ANALISE_DE_DADOS\PLANILHAS_TRATADAS\despesas_predio_2025.xlsx")

print(df_excel)