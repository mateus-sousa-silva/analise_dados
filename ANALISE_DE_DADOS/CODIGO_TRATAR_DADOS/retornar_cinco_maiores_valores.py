import pandas as pd

df_excel = pd.read_excel("D:\PROGRAMACAO_FACULDADE\PROGRAMACAO_DE_COMPUTADORES\ANALISE_DE_DADOS\PLANILHAS_TRATADAS\despesas_predio_2025.xlsx")

retornar_cinco = df_excel.sort_values(by='valor R$', ascending=False).head(5)

print(retornar_cinco)