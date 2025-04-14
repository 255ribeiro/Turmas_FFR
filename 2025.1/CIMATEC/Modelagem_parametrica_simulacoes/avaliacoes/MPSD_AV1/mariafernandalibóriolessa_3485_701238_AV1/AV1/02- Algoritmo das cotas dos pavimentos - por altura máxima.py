#AV1 Modelagem Paramétrica e Simulações Digitais
#Grupo: Larissa Rios, Gabriella Carvalho, Sofia Brêda e Maria Fernanda Lessa
#Algoritmo da cota máxima - aula 02
cota_piso = float(input("Entre com a cota do piso"))
pap = float(input("Entre com a distância piso a piso"))
cota_max = float(input("Entre com o valor máximo de altura"))

count = 0 #variável do número total de pisos
#usamos o while para que o algoritmo continue rodando enquanto a premissa for verdadeira.
while cota_piso <= cota_max:
    count = count + 1
    print (cota_piso)
    cota_piso = cota_piso + pap #soma do nível dos pisos com a distância entre pavimentos até a cota máxima (altura do prédio)
print ("Total de pisos: ", count) 
