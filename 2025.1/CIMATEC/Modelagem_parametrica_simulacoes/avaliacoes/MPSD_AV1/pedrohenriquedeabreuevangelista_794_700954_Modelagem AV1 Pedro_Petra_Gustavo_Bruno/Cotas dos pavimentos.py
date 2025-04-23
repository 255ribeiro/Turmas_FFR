# AV1 Modelagem paramétrica e simulações digitais
# Equipe : Pedro henrique de abreu / Petra Devay / Gustavo Gerson Costa / Bruno Basilio
# Docente:Fernando Ferraz

# Entrada de dados
cota_terreno = float(input("Entre com a cota do terreno"))
piso_piso = float(input("Entre a distância piso a piso"))
cota_max = float(input("Entre com o valor máximo de altura"))

# Relação das cotas para a cota do terreno e da cota máxima
count = 0
while cota_terreno <= cota_max:
    count = count + 1
    print(cota_terreno)
    cota_terreno = cota_terreno + piso_piso
print("Total de pisos: ",count) #Indicar a quantidade de pisos que existem até alcançar a altura máxima
