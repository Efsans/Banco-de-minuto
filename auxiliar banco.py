import os
while True:
  chack=(input("escreva um numero de codigo:  "))
  if chack.isdigit() and len(chack) == 6:
    break
  else:
    print ("digite até seis caracteries")


def comparar(chack, arquivo="contas"):
      if os.path.exists(arquivo):
        with open(arquivo, "r") as l:
          for lido in l:
            codigo = lido[:6]
            #lido_final = lido.strip()
            if codigo == chack:
              #print(f"valor {chack} existente")
              return
            else :
              print (f"o valo, {chack} nao existe")

      else:
        print("arquivo não existe")

comparar(chack, arquivo="contas")