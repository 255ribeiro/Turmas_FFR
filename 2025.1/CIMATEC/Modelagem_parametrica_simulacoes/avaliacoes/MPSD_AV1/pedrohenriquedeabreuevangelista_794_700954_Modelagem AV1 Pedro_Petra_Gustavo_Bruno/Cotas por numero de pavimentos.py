# AV1 Modelagem paramétrica e simulações digitais
# Equipe : Pedro henrique de abreu / Petra Devay / Gustavo Gerson Costa / Bruno Basilio
# Docente:Fernando Ferraz

# Entrada de dados
cota_init = float(input("Valor da cota inicial\n"))
n_pav = int(input("Número de pavimentos\n"))
piso_piso = float(input("Valor da distância piso a piso\n"))

#Utilização do for para delimitar a relação da quntidade da saida e do print para gerar a saida 
cotas = [] # Formatação de como será indicado as relações de cotas e pavimentos 
for i in range(n_pav):
    cotas.append(cota_init + (i*piso_piso))
    print(len(cotas))
print(cotas)#Saida dos valores de cotas
    
