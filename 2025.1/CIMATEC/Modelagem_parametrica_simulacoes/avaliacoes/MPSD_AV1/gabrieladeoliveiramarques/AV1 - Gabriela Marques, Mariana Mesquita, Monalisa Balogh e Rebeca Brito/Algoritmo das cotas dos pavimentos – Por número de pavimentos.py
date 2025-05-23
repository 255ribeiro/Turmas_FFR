# -*- coding: utf-8 -*-
"""Algoritmo das cotas dos pavimentos – Por número de pavimentos

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wj8Gtudco9tochSQL1Ae9Tt-6D7W9ViH
"""

# Entrada de dados
cota_inicial = float(input("Digite a cota inicial (em metros): "))
altura_pavimento = float(input("Digite a altura entre pavimentos (em metros): "))
altura_maxima_total = float(input("Digite a altura máxima do edifício (em metros): "))

# Lista para armazenar as cotas
cotas = [cota_inicial]

# Cálculo das cotas: somando enquanto não ultrapassar a altura máxima
proxima_cota = cota_inicial + altura_pavimento

while proxima_cota <= (cota_inicial + altura_maxima_total):
    cotas.append(proxima_cota)
    proxima_cota += altura_pavimento

# Exibindo as cotas formatadas
print("\n=== Cotas dos Pavimentos ===")
for i, cota in enumerate(cotas):
    print(f"Nível {i}: {cota:.2f} m")