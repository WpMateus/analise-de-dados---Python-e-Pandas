import pandas as pd

# Lendo os arquivos excel
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

df = pd.concat([df1, df2, df3, df4, df5])
df["Receita"] = df["Vendas"].mul(df["Qtde"])

# print(df.dtypes)

# colocando a coluna data para int
df["Data"] = df["Data"].astype("int64")
# print(df.dtypes)

# colocando a coluna data para datetime
df["Data"] = pd.to_datetime(df["Data"])
# print(df.dtypes)

# Agrupando por ano
# print(df.groupby(df["Data"].dt.year)["Receita"].sum())

# Criando coluna de ano
df["Ano_Venda"] = df["Data"].dt.year
# print(df.sample(5))

# mes e dia da venda
df["mes_venda"], df["dia_venda"] = df["Data"].dt.month, df["Data"].dt.day
# print(df.sample(5))

# Data mais antiga
# print(df["Data"].min())

# Diferença de dias
df["diferenca_dias"] = df["Data"] - df["Data"].min()
# print(df.sample(5))

# Coluna trimestre
df["trimestre_venda"] = df["Data"].dt.quarter
# print(df.sample(5))

#Filtrando vendas 2019 mês março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
print(vendas_marco_19.sample(5))