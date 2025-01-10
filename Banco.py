import time
import random
import os
#arquivo 
txt = "N.contas"
def save(codigo):#salva numero no txt vulgo arquivo
  with open(txt,"a") as f:
    f.write(codigo + "\n")

def load():#carrega os numeros no arquivo
  if not os.path.exists(txt):
    return[]
  with open(txt, "r") as f:
    return[linha.strip() for linha in f.readlines()]
  
def deletar(codigo):#delete
  codigos = load()
  if codigo in codigos:
    codigos.remove(codigo)
    with open(txt, "w") as f:
      for n in codigos:
        f.write(n + "\n")
    return True
  return False

# horas *10
tempo = int(time.time() * 10)

# usndo horas como semente para a aleatoriedade
random.seed(tempo)

# Gera um número aleatório com base na semente
random = random.randint(0, 1000000)  
#formata o numero para ter zeros a esquerda//aleatoriezar o primeiro numero
random_formatado = str(random).zfill(7)

print(f"numero da conta:{random_formatado}")
print(f"esse é o tempo {tempo}")

Final = random_formatado
#teste = ("0342461")
save(Final)
#return Final


