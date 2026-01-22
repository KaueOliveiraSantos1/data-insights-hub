import pandas as pd    # importar qualquer biblioteca
df = pd.read_excel('base_vendas_tabela_dinamica.xlsx')   # importar arquivo
print(df.head(10))   # ver linhas da tabela *focado nas primeiras linhas*
print(df.tail(5))    # ver linhas da tabela *focado nas ultimas linhas*
print(df.info())     # ver nomes das colunas da tabela
print(df.describe())    # mostra valores *QUANTIDADE DE VALORES* *MEDIA DOS VALORES* * DESVIO PADRAO* *MENOR VALOR ENCONTRADO* *25%, 50%, 75%: Quartis (o valor de 50% é a mediana).* *MAX:MAIOR VALOR ENCONTRADO*
print(df['Quantidade'])   # selecionar, acessar ou criar uma coluna específica
print(df.isnull().sum())   # mostra quantos nulos há em cada coluna
print(df.dropna())          # remove linhas que contenham qualquer valor vazio
df.drop_duplicates(inplace=True)     # remover duplicatas