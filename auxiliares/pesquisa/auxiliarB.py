from flask import Flask, request, render_template # type: ignore
import os 

app=Flask(__name__)

import os
while True:
  chack = input("escreva um numero de codigo:  ")
  if chack.isdigit() and len(chack) == 6:
    break
  else:
    print("digite até seis caracteries")

def comparar(chack, arquivo="contas"):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as l:
            for lido in l:
                codigo = lido[:6]
                if codigo == chack:
                    return lido.strip()
            print(f"o valor {chack} nao existe")
    else:
        print("arquivo não existe")

linha = comparar(chack, arquivo="contas")
if linha:
    print(f"Linha encontrada: {linha}")