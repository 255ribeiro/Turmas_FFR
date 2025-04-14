#AV1 Modelagem Paramétrica e Simulações Digitais
#Equipe: Gabriella Carvalho, Larissa Rios e Sofia Brêda

from math import ceil #importação função ceil

#entrada de dados
dist = input("Entre com a distância entre pavimentos")
dist = float(dist) #transformação o valor em float

#leitura do valor da altura máxima dos espelhos e transformação em float
h_max = float(input("Entre com o valor máximo do espelho"))

valor_01 = dist / h_max #valor temporário para cálculo do número de espelhos
print (valor_01)

num_esp = ceil(valor_01) #arredondar o valor para o menor inteiro maior ou igual a valor_01 
print("Número de espelhos: ", num_esp)

h = dist / num_esp #cálculo da altura dos espelhos
print ("Altura dos espelhos: ", h)

p= .64-2*h #fórmula de blondel
print("Pronfundidade do piso: ", p)
