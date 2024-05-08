"""https://web.dio.me/lab/analise-de-dados-com-python-e-pandas/learning/c14c9169-c62d-4d8a-8ed8-04cbb51d5302?back=/play"""

import pandas as pd

df = pd.read_csv("Gapminder.csv", on_bad_lines="skip", sep=";")

#Visualizando as 5 primeiras linhas
"""print(df.head())"""

#trocar os nome das colunas
df = df.rename(columns={"country":"Pais", "continent":"Continente", "year": "Ano", "lifeExp": "Expectativa de vida", "pop": "pop total", "gdpPercap": "PIB"})
"""print(df.head())"""

#Visualizar o total de linhas que temos no arquivo - 3312 linhas e 6 colunas
print(df.shape)

#Retorna apenas o nome das colunas
print(df.columns)

#Tipo de dado em cada coluna
print(df.dtypes)

#Retornando as ultimas linhas
print(df.tail(15))

#Retorna informações estatisticas
print(df.describe())

#Fazer filtro apenas valores do continentes
print(df["Continente"].unique())

#Fazer filtro apenas valores do continente Oceania
oceania = df.loc[df["Continente"] == "Oceania"]
print(oceania.head())

#groupby com pandas agrupar com continente e trazer quantos paises tem para cada continente
print(df.groupby("Continente")["Pais"].nunique())

#Qual a expectativa de vida média para cada ano
print(df.groupby("Ano")["Expectativa de vida"].mean())

#Alternativa para os calculos
print(df["PIB"].mean())

#A soma da coluna PIB
print(df["PIB"].sum())