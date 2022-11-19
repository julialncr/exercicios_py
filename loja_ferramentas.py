'''
------------------------------------------------------------
| Programa de criar Nota Fiscal de uma loja de ferramentas |
| Por: Julia Dias                                          |
------------------------------------------------------------
'''

import os

preco_parafuso = 1.50
preco_arruela = 2.00
preco_porca = 2.50

nome = input("Digite seu nome: ")

quant_parafusos = float(input("Digite a quantidade de parafusos que deseja comprar: "))
quant_arruelas = float(input("Digite a quantidade de arruelas que deseja comprar: "))
quant_porcas = float(input("Digite a quantidade de porcas que deseja comprar: "))

total_parafusos = preco_parafuso * quant_parafusos
total_arruelas = preco_arruela * quant_arruelas
total_porcas = preco_porca * quant_porcas

total_pagar = total_parafusos + total_arruelas + total_porcas

os.system('clear')

print("Cliente: ", nome)
print("==========================")
print("Parafusos: ", quant_parafusos)
print("Arruelas: ", quant_arruelas)
print("Porcas: ", quant_porcas)
print("==========================")
print("Total a pagar: R$", total_pagar)
