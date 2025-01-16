from flask import Flask, request, render_template # type: ignore
import os 

app=Flask(__name__)


@app.route('/')
def pesquisa():
  return render_template('pesquisa.html')
@app.route('/pesquisa', methods=['post'])
def pesquisar(arquivo="contas"):
  chack = request.form['conta']
  rsultado = None
#def comparar(chack, arquivo="contas"):
  if os.path.exists(arquivo):
    with open(arquivo, "r") as l:
      for lido in l:
        codigo = lido[:6]
        if codigo == chack:
          dados = lido.strip().split('\t')
          resultado = {
            'codigo': dados[0],
            'nome': dados[1],
            'telefone': dados[2],
            'saldo': dados[3] if len(dados) > 3 else '0,00',
          }
          break
      else:
        resultado = "codigo não encontrado"
  else:
    resultado = "arquivo não encontrado"
  return render_template('pesquisa.html', resultado=resultado)        
        
if __name__ == '__main__':
  app.run(debug=True)
#linha = comparar(chack, arquivo="contas")
#if linha:
    #print(f"Linha encontrada: {linha}")