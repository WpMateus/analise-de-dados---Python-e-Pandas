import pandas as pd
import matplotlib.pyplot as plt

# Lendo os arquivos excel
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

df = pd.concat([df1, df2, df3, df4, df5])
df["Receita"] = df["Vendas"].mul(df["Qtde"])
df["mes_venda"], df["dia_venda"] = df["Data"].dt.month, df["Data"].dt.day
df["Ano_Venda"] = df["Data"].dt.year

# value_couts fazer uma contagem, quantas linhas temos de cada
# print(df["LojaID"].value_counts(ascending=False))

# Mostrar em gráfico apenas passar no final .plot.bar()
# df["LojaID"].value_counts(ascending=False).plot.bar()

# mostrar em barras horizontais
# df["LojaID"].value_counts(ascending=True).plot.barh()

# Para exibir 
# plt.show()

# Mostrar em gráfico de pizza
# df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()
# plt.show()

# Total vendas por cidade
# print(df["Cidade"].value_counts())

# Adicionando um titulo e alterando o nome dos eixos e alterando a cor
# df["Cidade"].value_counts().plot.bar(title="Total de vendas por cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")
# plt.show()

# Alterando o estilo
plt.style.use("ggplot")
# df.groupby(df["mes_venda"])["Qtde"].sum().plot(title="Total produtos vendidos x mês")
# plt.xlabel("Mês")
# plt.ylabel("Total produtos vendidos")
# plt.legend()
# plt.show()

df.groupby(df["mes_venda"])["Qtde"].sum()

# Selecionando apenas vendas do ano de 2019
df_2019 = df[df["Ano_Venda"] == 2019]
# Total de produtos vendidos por mês
# df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
# plt.xlabel("Mês")
# plt.ylabel("Total produtos vendidos")
# plt.legend()
# plt.show()

# Hisograma
# plt.hist(df["Qtde"], color="magenta")
# plt.show()

# Grafico de dispersão
# plt.scatter(x = df_2019["dia_venda"], y = df_2019["Receita"])
# plt.show()

# Salvando em png
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total produtos vendidos")
plt.legend()
plt.savefig("grafico Qtde x Mes.png")