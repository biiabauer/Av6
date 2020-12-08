from config import *
from modelo import Livro, Leitor, Leitura, Biblioteca

@app.route("/")
def inicio():
    return 'Sistema de Cadastro de Livros. '+\
        '<a href="/listar_livros">Listar livros</a>'

@app.route("/listar_livros")
def listar_livros():
    livros = db.session.query(Livro).all()
    livros_em_json = [ x.json() for x in livros]
    resposta = jsonify(livros_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # retornar...

@app.route("/incluir_livro", methods=['post'])
def incluir_livro():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações da nova livro
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    try: # tentar executar a operação
      nova = Livro(**dados) # criar a nova livro
      db.session.add(nova) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

@app.route("/excluir_livro/<int:livro_id>", methods=['DELETE'])
def excluir_livro(livro_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Livro.query.filter(Livro.id == livro_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route("/listar/<string:classe>")
def listar(classe):
    dados = None
    if classe == "Livro":
      dados = db.session.query(Livro).all()
    elif classe == "Leitor":
      dados = db.session.query(Leitor).all()
    elif classe == "Biblioteca":
      dados = db.session.query(Biblioteca).all()
    elif classe == "Leitura":
      dados = db.session.query(Leitura).all()
    lista_jsons = [ x.json() for x in dados ]
    resposta = jsonify(lista_jsons)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listar_leitor")
def listar_leitor():
    leitor = db.session.query(Leitor).all()
    leitor_em_json = [ x.json() for x in leitor]
    resposta = jsonify(leitor_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 
    
@app.route("/incluir_leitor", methods=['post'])
def incluir_leitor():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json() 
    try:
      nova = Leitor(**dados) 
      db.session.add(nova) 
      db.session.commit() 
    except Exception as e:
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route("/listar_biblioteca")
def listar_biblioteca():
    biblioteca = db.session.query(Biblioteca).all()
    biblioteca_em_json = [ x.json() for x in biblioteca]
    resposta = jsonify(biblioteca_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 
    
@app.route("/incluir_biblioteca", methods=['post'])
def incluir_biblioteca():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json() 
    try:
      nova = Biblioteca(**dados) 
      db.session.add(nova) 
      db.session.commit() 
    except Exception as e:
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 

@app.route("/listar_leitura")
def listar_leitura():
    leitura = db.session.query(Leitura).all()
    leitura_em_json = [ x.json() for x in leitura]
    resposta = jsonify(leitura_em_json)
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 
    
@app.route("/incluir_leitura", methods=['post'])
def incluir_leitura():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json() 
    try:
      nova = Leitura(**dados) 
      db.session.add(nova) 
      db.session.commit() 
    except Exception as e:
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 


app.run(debug=True)