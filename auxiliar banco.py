import os

chack=(input("escreva um numero de codigo:  "))

def comparar(chack, arquivo="sequencia.txt"):
  if os.path.exists(arquivo):
    with open(arquivo, "r") as ler:
      for lido in ler:
        lido_final = lido.strip()
        if lido_final == chack:
          print(f"aqui o valor: {chack}")
          return
      print("valor invalido")
  else :
   print (f"o {arquivo} nao existe")

comparar(chack)