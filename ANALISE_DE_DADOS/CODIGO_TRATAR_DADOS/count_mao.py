import pandas as pd

df_excel = pd.read_excel("D:\PROGRAMACAO_FACULDADE\PROGRAMACAO_DE_COMPUTADORES\ANALISE_DE_DADOS\PLANILHAS_TRATADAS\despesas_predio_2025.xlsx")

df_excel["data"] = pd.to_datetime(df_excel["data"])
mao_marco = df_excel[(df_excel['categoria'] == 'MAO') & (df_excel["data"].dt.month == 3)]

count_mao = len(mao_marco)

print('Um total de',count_mao,'mão de obra')