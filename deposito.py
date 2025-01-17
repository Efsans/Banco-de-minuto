from flask import Flask, request, render_template # type: ignore
import os

app=Flask(__name__)

def deposito():
    arquivo = "contas"
    codigo1 = input("Digite o código da sua conta: ")
    codigo2 = input("Digite o código da conta de destino: ")

    if not os.path.exists(arquivo):
        print("Arquivo de contas não encontrado.")
        return

    with open(arquivo, "r") as f:
        contas = f.readlines()

    conta1 = None
    conta2 = None

    for lido in contas:
        conta = lido[:6]
        if conta == codigo1:
            conta1 = lido.strip().split('\t')
        elif conta == codigo2:
            conta2 = lido.strip().split('\t')

    if not conta1:
        print("Conta de origem não encontrada.")
        return

    if not conta2:
        print("Conta de destino não encontrada.")
        return

    saldo_origem = float(conta1[3].replace(',', '.'))
    saldo_destino = float(conta2[3].replace(',', '.'))
    while True:
      print(f"Saldo na conta de origem {conta1[1]}: {saldo_origem:.2f}")
      transacao = float(input(f"Valor a ser transferido para {conta2[1]}: ").replace(',', '.'))

      if transacao < 10.00:
          print("Valor mínimo para transação é 10,00")
          continue
      elif transacao > saldo_origem:
          print("Saldo insuficiente")
          continue
      else:
        break     

    saldo_origem -= transacao
    saldo_destino += transacao

    conta1[3] = f"{saldo_origem:.2f}".replace('.', ',')
    conta2[3] = f"{saldo_destino:.2f}".replace('.', ',')

    with open(arquivo, "w") as f:
        for lido in contas:
            conta = lido[:6]
            if conta == codigo1:
                f.write('\t'.join(conta1) + '\n')
            elif conta == codigo2:
                f.write('\t'.join(conta2) + '\n')
            else:
                f.write(lido)

    print(f"Transação de {transacao:.2f} realizada com sucesso!")
    print(f"Novo saldo na conta de origem ({conta1[1]}): {saldo_origem:.2f}")
    print(f"Novo saldo na conta de destino ({conta2[1]}): {saldo_destino:.2f}")

if __name__ == "__main__":
    deposito()