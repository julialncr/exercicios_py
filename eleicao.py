'''
---------------------------------
| Programa de votação em Python |
| Por: Julia Dias               |
---------------------------------
'''

import os

candidato_a = 0
candidato_b = 0
brancos = 0
nulos = 0

while True:
    os.system('clear') # mudar para 'cls' se o sistma operacional for windows
    print("Escolha seu candidato ou tecle zero para encerrar\n\n")
    print("  1 -> Candidato A\n")
    print("  2 -> Candidato B\n")
    print("  3 -> Branco\n")
    print("\nQualquer número diferente de 0, 1, 2 e 3 anulará o seu voto\n")
    voto = int(input("Digite seu voto: "))
    os.system('clear')

    if voto == 0:
        print("Votação encerrada!\n")
        break
        
                    
    elif voto == 1 : 
        candidato_a = candidato_a + 1 # Soma um voto para o candidato A
        
                    
    elif voto == 2 : 
        candidato_b = candidato_b + 1 # Soma um voto para o candidado B
        
                    
    elif voto == 3 : 
        brancos = brancos + 1 # Soma um voto em branco
        
                
    else :
        nulos = nulos + 1 # Opção inválida. Soma um voto nulo
    

# Calcula o total de votos
total_votos = candidato_a + candidato_b + brancos + nulos


# Se houve votos, calcula a porcentagem de votos de cada candidato
		
if (total_votos > 0):
	porcentagem_candidato_a = (candidato_a * 100.0) / total_votos  
	porcentagem_candidato_b = (candidato_b * 100.0) / total_votos
	porcentagem_brancos = (brancos * 100.0) / total_votos
	porcentagem_nulos = (nulos * 100.0) / total_votos

	print("\n")
	
	print("Total de votos: ", total_votos, "\n\n")
	print("Candidato A: " , candidato_a, " voto(s). ", porcentagem_candidato_a, " % do total\n" )
	print("Candidato B: ", candidato_b, " voto(s). ", porcentagem_candidato_b, " % do total\n" )
	print("Brancos: ", brancos, " voto(s). ", porcentagem_brancos, " % do total\n")
	print("Nulos: ", nulos, " voto(s). ", porcentagem_nulos, " % do total\n")