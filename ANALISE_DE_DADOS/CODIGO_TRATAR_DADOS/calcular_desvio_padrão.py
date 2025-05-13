import pandas as pd

df_excel = pd.read_excel("D:\PROGRAMACAO_FACULDADE\PROGRAMACAO_DE_COMPUTADORES\ANALISE_DE_DADOS\PLANILHAS_TRATADAS\despesas_predio_2025.xlsx")

gastos = df_excel.groupby('categoria')['valor R$'].std()

print('\no desvio padrão baseado na categoria é: \n',gastos)