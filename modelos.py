from datetime import date

//criando classe mãe para a receitas e despesas
class Transacao:
    def __init__(self, valor, descricao, data=None):
        self.valor = valor
        self.descricao = descricao
        self.data = data if data else date.today()

class Receita(Transacao):
    def __init__(self, valor, descricao, data=None):
        super().__init__(valor, descricao, data) //aplicação do conceito de herança 

class Despesa(Transacao):
    def __init__(self, valor, descricao, categoria, data=None):
        super().__init__(valor, descricao, data)
        self.categoria = categoria 

