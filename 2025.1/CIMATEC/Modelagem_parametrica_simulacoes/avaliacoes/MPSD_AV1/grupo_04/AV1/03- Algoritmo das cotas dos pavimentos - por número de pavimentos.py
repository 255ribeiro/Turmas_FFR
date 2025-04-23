#AV1 Modelagem Paramétrica e Simulações Digitais
#Equipe: Gabriella Carvalho, Larissa Rios, Sofia Brêda e Maria Fernanda Lessa

#Cálculo das cotas dos pavimentos de um edifício

#Entrada de dados 
cota_init = float(input("valor da cota inicial\n")) #Cota inicial do primeiro pavimento 

n_pav = int(input("Numero de pavimentos\n")) #Número total de pavimentos 

pap = float(input("valor da distância de piso a piso\n")) #Distância entre pisos (piso a piso)

#Lista para armazenar as cotas dos pavimentos 
cotas = []

#Cálculo das cotas para cada pavimento 
for i in range(n_pav):
    cotas.append(cota_init + (i * pap)) #Adiciona a cota correspondente ao pavimento atual 
    print(len(cotas)) #Exibe a quantidade de cotas já adicionadas (opcional para depuração)

#Exibe a lista completa de cotas calculadas 
print(cotas)
