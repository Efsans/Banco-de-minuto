import os

nome = input("nome: ")

tele= input ("telefone: ")

saldo=input ("deposito inicial: ")

def gerar_numero_sequencial(arquivo="sequencia.txt"):
    if not os.path.exists(arquivo):
        with open(arquivo, "w") as f:
            f.write("000001\n")
        return "000001"
    with open(arquivo, "r") as f:
        linhas = f.readlines()
        ultimo_numero = linhas[-1].strip()
    
    # Incrementa o número
    proximo_numero = int(ultimo_numero) + 1
    proximo_numero_formatado = f"{proximo_numero:06d}"  
    with open(arquivo, "a") as f:
        f.write(f"{proximo_numero_formatado}\n")


    return proximo_numero_formatado


numero_gerado = gerar_numero_sequencial()
#print(f"Número gerado: {numero_gerado}")
def tabelinha():
    print("cadastro feito")
    print("%s\t%s\t\t%s\t\t%s" % (numero_gerado, nome, tele, saldo))
    with open("contas", "a") as arquiv:
        line = "%s\t%s\t\t%s\t\t%s" % (numero_gerado, nome, tele, saldo)
        arquiv.write(f"{line}\n")

tabelinha()



  

