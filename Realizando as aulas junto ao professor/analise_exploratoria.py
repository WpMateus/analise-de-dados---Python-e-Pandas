import pandas as pd
import matplotlib.pyplot as plt
# adicionando stylo
plt.style.use("seaborn")

# Upload no google colab via codigo
# from google.colab import files
# arq = files.upload()

#Criando DataFrame
df = pd.read_excel("AdventureWorks.xlsx")

print(df.dtypes)

#Qual a Receita total?
df["Valor Venda"].sum()

#Qual o custo Total?
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"]) #Criando a coluna de custo

#Qual o custo Total?
round(df["custo"].sum(), 2)

#Agora que temos a receita e custo e o total, podemos achar o Lucro total
#Vamos criar uma coluna de Lucro que será Receita - Custo
df["lucro"]  = df["Valor Venda"] - df["custo"] 

#Total Lucro
round(df["lucro"].sum(),2)

#Criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

#Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

#Verificando o tipo da coluna Tempo_envio
df["Tempo_envio"].dtype

#Média do tempo de envio por Marca
df.groupby("Marca")["Tempo_envio"].mean()

#Verificando se temos dados faltantes
df.isnull().sum()

#Vamos Agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format

#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

#Qual o total de produtos vendidos?
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

#Gráfico Total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

#Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro");

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal');

#Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"]);

#Identificando o Outlier
df[df["Tempo_envio"] == 20]

df.to_csv("df_vendas_novo.csv", index=False)