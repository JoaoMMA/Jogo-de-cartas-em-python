import random

def gerar_baralho(n_copias, coringas, embaralhado):
 baralho =  []

 naipes = list("♠♣♥♦")
 numeros = list("A23456789") + ["10"] + list("JQK")
 
 for _ in range(n_copias):
  for naipe in naipes:
    for numero in numeros:
        carta =  numero + naipe
        baralho.append(carta)


 if coringas.lower() == "s":
  for _ in range(n_copias):
   baralho.extend(["JK1", "JK2"])


 if embaralhado.lower() == "s":
  random.shuffle(baralho)
    
 return baralho 