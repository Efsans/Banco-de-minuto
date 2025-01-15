from flask import Flask, request, render_template # type: ignore
import os

app = Flask(__name__)

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

@app.route('/')
def cadastro():
    return render_template('cadastroconta².html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome = request.form['name']
    telefone = request.form['tele']
    saldo = request.form['deposito']
    numero_gerado = gerar_numero_sequencial()

    
    with open("contas", "a") as arquiv:
        line = "%s\t%s\t\t%s\t\t%s" % (numero_gerado, nome, telefone, saldo)
        arquiv.write(f"{line}\n")
    
    return f"Cadastro feito com sucesso! Número da conta: {numero_gerado}"

if __name__ == '__main__':
    app.run(debug=True)