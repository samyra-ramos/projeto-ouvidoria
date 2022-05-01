from manifestacao import Manifestacao
class Ouvidoria:

    def __init__(self):
        self.manifestacoes = []
        self.tipos_manifestacao = {
            1: "sugestão",
            2: "reclamação",
            3: "elogio"
            }

    def menu(self):
        return 'Ouvidoria da Universidade JMS\n1) Listar as manifestações\n2) Listar todas as sugestões\n3) Listar todas as reclamações\n4) Listar todas os elogios\n5) Enviar uma manifestação (criar uma nova)\n6) Pesquisar o número de protocolo\n7) Sair'

    def listarManifestacoes(self):
        if len(self.manifestacoes) == 0:
            print("Não há manifestacões cadastrados!")
        for manifestacao in self.manifestacoes:
            print(manifestacao)

    def listarSugestoes(self):
        tem_sugestoes = False
        for manifestacao in self.manifestacoes:
            if manifestacao.tipo == "sugestão":
                print(manifestacao)
                tem_sugestoes = True
        if tem_sugestoes == False:
            print("Não há nenhuma sugestão postada.")

    def listarReclamacoes(self):
        tem_reclamacao = False
        for manifestacao in self.manifestacoes:
            if manifestacao.tipo == "reclamação":
                print(manifestacao)
                tem_reclamacao = True
        if tem_reclamacao == False:
            print("Não há nenhuma reclamação postada.")

    def listarElogios(self):
        tem_elogio = False
        for manifestacao in self.manifestacoes:
            if manifestacao.tipo == "elogio":
                print(manifestacao)
                tem_elogio = True
        if tem_elogio == False:
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
                self.manifestacoes.append(manifestacao)
        except:
            print("digite um número de manifestão válido!")

    def procurarNumeroProtocolo(self):
        numero_protocolo_de_busca = input("digite o número do protocolo: ")
        resultado_busca = None
        for manifestacao in self.manifestacoes:
            if numero_protocolo_de_busca == str(manifestacao.protocolo):
                resultado_busca = manifestacao
                break
 
        if resultado_busca == None:
            print("Protocolo não encontrado!")
        else:
            print(resultado_busca)