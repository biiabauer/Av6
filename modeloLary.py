from config import *

class Comida(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    sabor = db.Column(db.String(254))
    origem = db.Column(db.String(254))
    dificuldade_de_preparo = db.Column(db.String(254))
    nota = db.Column(db.Integer)

    def __str__(self):
        return self.sabor + ", " + self.origem + ", " +\
            self.dificuldade_de_preparo + str(self.nota)

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "sabor": self.sabor,
            "origem": self.origem,
            "dificuldade_de_preparo": self.dificuldade_de_preparo,
            "nota": self.nota,
        }

class Classificacao(db.Model):

    id = db.Column(db.Integer, primary_key=True) 
    titulo = db.Column(db.String(254)) 
    categoria = db.Column(db.String(254))
    data_classificacao = db.Column(db.String(254))
    comida_id = db.Column(db.Integer, db.ForeignKey(Comida.id))
    comida = db.relationship("Comida")

    def __str__(self): 
        return self.titulo + ", " + self.data_classificacao +\
            self.categoria + str(self.comida)

    def json(self):
        return ({
            "id": self.id,
            "titulo": self.titulo,
            "data_classificacao": self.data_classificacao,
            "categoria": self.categoria,
            "comida_id": self.comida_id,
            "comida": self.comida.json()
        }) 

class Ranking(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    posicao = db.Column(db.Integer)
    autor = db.Column(db.String(254))
    comida_id = db.Column(db.Integer, db.ForeignKey(Comida.id))
    comida = db.relationship("Comida")

    def __str__(self):
        return str(self.posicao) + ", " +\
            self.autor + str(self.comida)

    def json(self):
        return ({
            "id":self.id,
            "posicao":self.posicao,
            "autor": self.autor,
            "comida_id": self.comida_id,
            "comida": self.comida.json()
        })
