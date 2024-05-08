import pandas as pd

# Lendo os arquivos excel
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

df = pd.concat([df1, df2, df3, df4, df5])
# Exibindo as 5 aleatórias
#print(df.sample(5))

# Verificando o tipo de dado das planilhas
#print(df.dtypes)

# Passar o LojaId para object
df["LojaID"] = df["LojaID"].astype("object")

# consultando linhas com valores faltantes
#print(df.isnull().sum())

#Substituindo os valores nullos pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

# Podemos valores nulos por zero
df["Vendas"].fillna(0, inplace=True)
print(df.isnull().sum())

# Podemos apagar as linhas com valores nulos
print(df.dropna(inplace=True))

# Apagando apenas as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)

# Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

# Criando novas colunas, coluna receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])
# print(df.sample(5))

# Achar a quantidade de produtos vendidos
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]
# print(df.sample(5))

# Maior receita
print(df["Receita"].max())

# Menor receita
print(df["Receita"].min())

# nlargest top 3 receitas
print(df.nlargest(3, "Receita"))

# Menor receita
print(df.nsmallest(3, "Receita"))

# Agrupando por cidade
print(df.groupby("Cidade")["Receita"].sum())

# Ordenando o conjunto de dados
print(df.sort_values("Receita", ascending=False).head(10))