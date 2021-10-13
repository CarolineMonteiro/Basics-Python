from numpy import arange # Não ocupo espaço com o pacote inteiro, só pego essa função
arange(10)

import numpy as np # Importo o pacote Numpy inteiro

np.arange(10) # Crio um array de tamanho 10: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

km = np.array([1000, 2300, 4987, 1500])
type(km)
km.dtype

km = np.loadtxt('carros-km.txt')
km = np.loadtxt(fname = 'carros-km.txt', dtype = int) # se eu não especificar o tipo ele entende como float
km.shape # dimensão
anos = np.loadtxt('carros-anos.txt')

km_media = km / (2021 - anos)

np_array = np.arange(1000000)
py_list = list(range(1000000))

%time for _ in range(100): np_array *= 2 # vejo o desempenho em tempo em que o código foi executado, posso ver qual performa melhor. Vai multiplicar todos os valores do array por 2 100 vezes
%time for _ in range(100): py_list = [x * 2 for x in py_list] # no python tenho que fazer 1 por 1, o que leva mais tempo. Nesse caso o Numpy performa muito melhor.

# Array Numpy suporta operações entre um número e esse array:
anos = np.array([2003, 1991, 1990, 2019, 2006])
idade = 2021 - anos # retorna um array