from main2 import gerar_baralho
import random
from statistics import quantiles

quantas_copias = int(input("Quantas cópias deseja gerar?"))
coringas = str(input("Quer que tenham coringas no jogo?\nDigite 's' para sim e 'n' para não: ")).lower().strip()
embaralhar = str(input("deve ser embaralhado?\nDigite 's' para sim e 'n' para não: ")).lower().strip()


baralho = gerar_baralho(n_copias=quantas_copias, coringas=coringas, embaralhado=embaralhar)
quantas_cartas =  len(baralho)
print (baralho)
print (f"O baralho tem {quantas_cartas} cartas")
embaralhar = str(input("deve ser embaralhado?\nDigite 's' para sim e 'n' para não: ")).lower().strip()
while embaralhar == "s":
  random.shuffle(baralho)     
  print (baralho)
  embaralhar = str(input("deve ser embaralhado?\nDigite 's' para sim e 'n' para não: ")).lower().strip()

n_jogadores = int(input("Qual o numero de jogadores?: "))
n_cartas = int(input("Quantas cartas para cada?: "))


def distribuir(n_j, n_c): 
  mao_dos_jogadores = []

  for _ in range(n_j):
   mao_individual = []
   
   while len(mao_individual) < n_c:
    carta = baralho.pop()
    mao_individual.append(carta)
   mao_dos_jogadores.append(mao_individual)
  
  return mao_dos_jogadores
  
mao_dos_jogadores = distribuir(n_j=n_jogadores, n_c=n_cartas)
print (f"O baralho tem {quantas_cartas} cartas")
if len(baralho) < 0:
   print ("Não ha cartas o suficiente no baralho para distribuir")
else:
   for i, mao in enumerate(mao_dos_jogadores, start=1):
    print (f"Jogador {i}: {mao}") 
    print (len(baralho))