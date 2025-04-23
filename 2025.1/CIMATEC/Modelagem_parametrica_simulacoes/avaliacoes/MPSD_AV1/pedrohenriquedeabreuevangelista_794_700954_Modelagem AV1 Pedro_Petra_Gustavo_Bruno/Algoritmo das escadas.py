# AV1 Modelagem paramétrica e simulações digitais
# Equipe : Pedro henrique de abreu / Petra Devay / Gustavo Gerson Costa / Bruno Basilio
# Docente:Fernando Ferraz

import math 

# Entrada de dados
dist = input("Entre com a distancia entre pavimentos\n")
dist = float(dist) # Transformando o valor em float

# Lendo o valor da altura dos espelhos e transformando o mesmo em float
h_max = float(input("Entre com o valor máximo do espelho\n"))

valor_01 = dist / h_max #Valor do calculo do número de espelhos

print(valor_01)

num_esp = math.ceil(valor_01) #Adicionando comendo de transformar o número em inteiro maior ou igual a valor_01

print("Numero de espelhos: ",num_esp)

h = dist / num_esp #Calculando altura dos espelhos
print("Altura dos espelhos: ", h)

p = .64 - 2*h #Adicionando a formula de blondel

print("Profundidade do piso", p)
