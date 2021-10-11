idades = [18, 22, 15, 50]

# for fora da função

def verifica_se_pode_dirigir(idade):
  if idade >= 18:
    print(f'{idade} anos de idade, TEM permissão para dirigir')
  else:
    print(f'{idade} anos de idade, NÃO TEM permissão para dirigir')

for idade in idades:
  verifica_se_pode_dirigir(idade)

# for dentro da função

def verifica_se_pode_dirigir(idades):
  for idade in idades:
    if idade >= 18:
      print(f'{idade} anos de idade, TEM permissão para dirigir')
    else:
      print(f'{idade} anos de idade, NÃO TEM permissão para dirigir') 

verifica_se_pode_dirigir(idades)


permissoes = []
idades = [20, 14, 40]  

def verificar_se_pode_dirigir(idades, permissoes):
  for idade in idades:
    if idade >= 18:
      permissoes.append(True)
    else:
      permissoes.append(False)

verificar_se_pode_dirigir(idades, permissoes)

permissoes

for permissao in permissoes:
  if permissao == True:
    print('Tem permissão para dirigir')
  else:
    print('Não tem permissão para dirigir')