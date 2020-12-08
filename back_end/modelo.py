from config import *

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    autor = db.Column(db.String(254))
    ano_publi = db.Column(db.String(254))

    def __str__(self):
        return self.nome + "[id="+str(self.id)+ "], " +\
            self.autor + ", " + self.ano_publi
            
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "autor": self.autor,
            "ano_publi": self.ano_publi
        }

class Leitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254)) 
    
    livro_id = db.Column(db.Integer, db.ForeignKey(Livro.id)) 
    #NULLABLE SERVE PARA QUANDO É DEPENDENTE UM DO OUTRO
    livro = db.relationship("Livro")

    def __str__(self):
        return  self.nome + ", " + str(self.livro) 

    def json(self):
        return {
            "id":self.id,
            "nome":self.nome,
            "livro_id":self.livro_id,
            "livro":self.livro.json() 
        }

class Biblioteca(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(254)) 
    data_aquisicao = db.Column(db.String(254))
    data_emprestimo = db.Column(db.String(254)) 

    livro_id = db.Column(db.Integer, db.ForeignKey(Livro.id))
    livro = db.relationship("Livro")

    def __str__(self): 
        s = f"Livro {self.nome} adquirido em {self.data_aquisicao}"
        if self.livro != None:
            s += f", foi emprestado o livro {self.livro} desde {self.data_aquisicao}"
        return s

    def json(self):
        if self.livro is None: 
            livro_id = ""
            livro = ""
            data_emprestimo = ""
        else: 
            livro_id = self.livro_id
            livro = self.livro.json()
            data_emprestimo = self.data_emprestimo
            
        return {
            "id": self.id,
            "nome": self.nome,
            "data_aquisicao": self.data_aquisicao,
            "livro_id": livro_id,
            "livro": livro,
            "data_emprestimo": data_emprestimo
        } 
    
class Leitura(db.Model):
    id = db.Column(db.Integer, primary_key=True) 

    livro_id = db.Column(db.Integer, db.ForeignKey(Livro.id))
    livro = db.relationship("Livro")

    leitor_id = db.Column(db.Integer, db.ForeignKey(Leitor.id))
    leitor = db.relationship("Leitor")

    def __str__(self):
        return  self.nome + ", " + str(self.livro) 

    def json(self):
        return {
            "id":self.id,
            "livro_id":self.livro_id,
            "livro":self.livro.json(),
            "leitor_id":self.leitor_id,
            "leitor":self.leitor.json()  
        }


if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    l1 = Livro(nome = "Cidade de papel", autor = "John Green", 
        ano_publi = "2008")   
    l2 = Livro(nome = "A culpa é das estrelas", autor = "John Green", 
        ano_publi = "2012")     
    db.session.add(l1)
    db.session.add(l2)
    db.session.commit()
    
    print(l2)
    print(l2.json())
    print("\n" + "\n") 

    le1 = Leitor(nome="Beatriz Bauer", livro=l1)
    db.session.add(le1)
    db.session.commit()
    print(f"Exame realizado: {le1}")
    print(f"Exame realizado em json: {le1.json()}")
    print("\n" + "\n")
    
    
    a1 = Biblioteca(nome="A culpa é das estrelas", data_aquisicao="24/03/2020")
    db.session.add(a1)
    db.session.commit()
    print(f"Biblioteca 1: {a1}")
    print(f"Biblioteca 1 (em json): {a1.json()}")
    print("\n" + "\n")
    
    a2 = Biblioteca(nome="Cidade de papel", data_aquisicao="01/02/2020", livro = l1, data_emprestimo="04/02/2020")
    db.session.add(a2)
    db.session.commit()
    print(f"Biblioteca 2: {a2}")
    print(f"Biblioteca 2 (em json): {a2.json()}")
    