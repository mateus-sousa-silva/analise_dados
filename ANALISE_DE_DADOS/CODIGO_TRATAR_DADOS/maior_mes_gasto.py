import pandas as pd

df_excel = pd.read_excel("D:\PROGRAMACAO_FACULDADE\PROGRAMACAO_DE_COMPUTADORES\ANALISE_DE_DADOS\PLANILHAS_TRATADAS\despesas_predio_2025.xlsx")

df_excel['data'] = pd.to_datetime(df_excel['data'])
df_excel['data_mes'] = df_excel['data'].dt.to_period('M')

maior_valor = df_excel.groupby('data_mes')['valor R$'].sum()
maior_valor_mes = maior_valor.idxmax()

gasto_mais_alto = maior_valor.max()

print("mês com maior gasto",maior_valor_mes, "valor gasto:",gasto_mais_alto)