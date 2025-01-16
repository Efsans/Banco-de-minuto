from flask import Flask, request, render_template # type: ignore
import os

app=Flask(__name__)

def deposito(arquivo="contas"):
  codigo1 = "000002"  #input("numero da conta ")
  codigo2 = "000003" #input("numero da conta dois ")
  with open(arquivo, "r") as l:
    for ler in l:
      conta = ler[:6]
      if conta == codigo1:
        titular = ler.strip()
        valor1 = ler.strip().split('\t')
        dinheiro =  {
          'saldo_do_titular' : valor1[3],
        }
      

        with open(arquivo, "r") as v:
          for lido in v:
            conta = lido[:6]
            if conta == codigo2:
              alheio= lido.strip()
              valor2 = lido.strip().split('\t')
              money = {
                'saldo_alheio' : valor2[3],
                '' : valor2[1]
  
              }
              print(f"valor na conta {valor1[3]}")
              transação = input(f"valor a ser mandado para {valor2[1]} ")
              if transação < "10,00":
                print("valor minimo para trasação 10,00")
                return
              elif transação > valor1[3]:
                print("saldo insufciente")
                return  
                

              
            #else:
              #print(f"conta não encontrada")  
      #else:
        #print(f"conta não encontrada")

deposito()


      