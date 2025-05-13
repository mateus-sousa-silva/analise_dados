import pandas as pd

nome_planilha = ""

df = pd.read_csv(f"D:\PROGRAMACAO_FACULDADE\PROGRAMACAO_DE_COMPUTADORES\ANALISE_DE_DADOS\BASE_DE_DADOS\{nome_planilha}.csv", sep=',', encoding='utf-8')

df.to_excel("D:\PROGRAMACAO_FACULDADE\PROGRAMACAO_DE_COMPUTADORES\ANALISE_DE_DADOS\PLANILHAS_TRATADAS\{nome_planilha}.xlsx", index=False)

df_excel = pd.read_excel("D:\PROGRAMACAO_FACULDADE\PROGRAMACAO_DE_COMPUTADORES\ANALISE_DE_DADOS\PLANILHAS_TRATADAS\{nome_planilha}.xlsx")

print(df_excel)
