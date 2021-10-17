# Criando um DataFrame a partir de uma lista de dicionários:

import pandas as pd
# pd.set_option('display.max_rows', 1000)       aumentando a quantidade de linhas visualizadas no dataframe
# pd.set_option('display.max_columns', 1000)    aumentando a quantidade de colunas visualizadas no dataframe

dados = [
    {'Nome': 'Jetta Variant', 'Motor': 'Motor 4.0 Turbo', 'Ano': 2003, 'Quilometragem': 44410.0, 'Zero_km': False, 'Valor': 88078.64},
    {'Nome': 'Passat', 'Motor': 'Motor Diesel', 'Ano': 1991, 'Quilometragem': 5712.0, 'Zero_km': False, 'Valor': 106161.94},
    {'Nome': 'Crossfox', 'Motor': 'Motor Diesel V8', 'Ano': 1990, 'Quilometragem': 37123.0, 'Zero_km': False, 'Valor': 72832.16}
]
dataset = pd.DataFrame(dados)
dataset

# Mudando a ordem das colunas:

dataset[['Nome', 'Motor', 'Ano', 'Quilometragem', 'Zero_km', 'Valor']]


# Criando um DataFrame a partir de um arquivo externo:

# dataset = pd.read_csv('db.csv', sep = ';')
dataset = pd.read_csv('db.csv', sep = ';', index_col = 0)  # se eu quero assumir essa coluna como índice do dataframe (rótulo da linha)

dataset.loc['Passat'] # quando só quero uma linha
dataset.loc[['Passat', 'DS5']] # selecionando linhas
dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']] # selecionando quais linhas e quais colunas eu quero
dataset.loc[:, ['Motor', 'Valor']] # selecionando todas as linhas

dataset.iloc[[1]] # iloc seleciona de acordo com o índice e não o rótulo como o loc
dataset.iloc[[1, 42, 22], [0, 5, 2]] # as colunas vem na ordem que eu selecionei

dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)]
dataset.query('Motor == "Motor Diesel" and Zero_km == True')


# Tratamento de dados:

dataset.info()
dataset[dataset.Quilometragem.isna()] # retorno onde os valores Quilometragem são na
dataset.fillna(0, inplace = True) # substituindo na por 0, nesse caso faz sentido e não há perda de informação
dataset.dropna(subset = ['Quilometragem'], inplace = True) # se eu quisesse excluir essas informações com na