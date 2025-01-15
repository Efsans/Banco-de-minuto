from flask import Flask, request, render_template # type: ignore
import os 

app=Flask(__name__)


@app.route('/')
def pesquisa():
  return render_template('pesquisa.html')
@app.route('/pesquisa', methods=['post'])
def pesquisar(arquivo="contas"):
  chack = request.form['conta']
#def comparar(chack, arquivo="contas"):
  if os.path.exists(arquivo):
    with open(arquivo, "r") as l:
      for lido in l:
        codigo = lido[:6]
        if codigo == chack:
          linha=pesquisa(chack, arquivo="contas")
          return f"{linha}"
        else:
          return f"codigo não encontrado"
  else:
    return f"arquivo não encontrado"        
        
if __name__ == '__main__':
  app.run(debug=True)
#linha = comparar(chack, arquivo="contas")
#if linha:
    #print(f"Linha encontrada: {linha}")