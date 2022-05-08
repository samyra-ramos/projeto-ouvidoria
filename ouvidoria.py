from manifestacao import Manifestacao
from database import Database
class Ouvidoria:

    def __init__(self):
        self.tipos_manifestacao = {
            1: "sugestão",
            2: "reclamação",
            3: "elogio"
        }

        self.database = Database()

    def menu(self):
        return 'Ouvidoria da Universidade JMS\n1) Listar as manifestações\n2) Listar todas as sugestões\n3) Listar todas as reclamações\n4) Listar todas os elogios\n5) Enviar uma manifestação (criar uma nova)\n6) Pesquisar o número de protocolo\n7) Sair'

    def listarManifestacoes(self):
        manifestacoes = self.database.listaManifestacoes("todos")
        if len(manifestacoes) == 0:
            print("Não há manifestacões cadastrados!")
        for manifestacao in manifestacoes:
            print(manifestacao)

    def listarSugestoes(self):
        sugestoes = self.database.listaManifestacoes("sugestão")
        for sugestao in sugestoes:
                print(sugestao)
        if len(sugestoes) == 0:
            print("Não há nenhuma sugestão postada.")

    def listarReclamacoes(self):
        reclamacoes = self.database.listaManifestacoes("reclamação")
        for reclamacao in reclamacoes:
            print(reclamacao)
        if len(reclamacoes) == 0:
            print("Não há nenhuma reclamação postada.")

    def listarElogios(self):
        elogios = self.database.listaManifestacoes("elogio")
        for elogio in elogios:
            print(elogio)
        if len(elogios) == 0:
            print("Não há elogio postado.")

    def criarManifestacao(self):
        nome = input("Digite seu nome: ")
        try:
            tipo = int(input("Digite o tipo da manifestação (1) sugestão, (2) reclamação, (3) elogio: "))
            if tipo not in self.tipos_manifestacao:
                print("Código de manifestação inválido!")
            else:
                descricao = input("Digite a sua manifestação: ")
                manifestacao = Manifestacao(nome, self.tipos_manifestacao[tipo], descricao)
                self.database.criarManifestacao(manifestacao.nome, manifestacao.tipo, manifestacao.descricao, manifestacao.protocolo)
        except:
            print("Digite um número de manifestação válido!")

    def procurarNumeroProtocolo(self):
        numero_protocolo_de_busca = input("digite o número do protocolo: ")
        manifestacao = self.database.buscarManifestacaoPorProtocolo(numero_protocolo_de_busca)
 
        if manifestacao == None:
            print("Protocolo não encontrado!")
        else:
            print(manifestacao)