from random import randrange

class Manifestacao:

    def __init__(self, nome, tipo, descricao, protocolo= randrange(99999999)):
        self.protocolo = protocolo
        self.nome = nome 
        self.tipo = tipo
        self.descricao = descricao 

    def __str__(self):
        return f'###################\n Número de Protocolo: {self.protocolo}\n Nome: {self.nome}\n Tipo: {self.tipo}\n Descrição: {self.descricao}'

