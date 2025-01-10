import os

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
print(f"Número gerado: {numero_gerado}")


  

