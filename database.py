from manifestacao import Manifestacao
import pymysql

class Database: 

    def __init__(self):
        try:
            self.connection = pymysql.connect(
                                        user = "root",
                                        password = "password123",
                                        database = "ouvidoria_db",
                                        host = "localhost"                                
                                        )
            self.cursor = self.connection.cursor()
            self.criarTabela()
        except:
            print('Problema de conexão com o banco de dados. Veja se o banco está conectado e tente novamente!')
            exit(1)
        
    def listaManifestacoes(self, tipo):
        if tipo == "todos":
            sqlQuery = "select * from manifestacao"
        else:
            sqlQuery = f"select * from manifestacao where tipo = '{tipo}'"
        self.cursor.execute(sqlQuery)
        results = self.cursor.fetchall()
        manifestacoes = []
        for result in results:
            manifestacao = Manifestacao(result[1], result[2], result[3], result[4])
            manifestacoes.append(manifestacao)
        return manifestacoes

    def criarManifestacao(self, nome, tipo, descricao, protocolo):
        sqlQuery = """insert into `manifestacao` (nome, tipo, descricao, protocolo)
                            values (%s, %s, %s, %s) 
                   """
        self.cursor.execute(sqlQuery,(nome, tipo, descricao, protocolo))
        self.connection.commit()

    def buscarManifestacaoPorProtocolo(self, protocolo):
        sqlQuery = f'select * from manifestacao where protocolo = {protocolo}'
        self.cursor.execute(sqlQuery)
        result = self.cursor.fetchone()
        if result is not None:
            return  Manifestacao(result[1], result[2], result[3], result[4])
        return None

    def criarTabela(self):
        sqlQuery = """
                    CREATE TABLE IF NOT EXISTS manifestacao(
                                                id INT not null auto_increment,
                                                nome VARCHAR(100),
                                                tipo VARCHAR(30) ,
                                                descricao VARCHAR(300),
                                                protocolo INT,
                                                CONSTRAINT manifestacao_pk PRIMARY KEY (id)
                                                )
                    """
        self.cursor.execute(sqlQuery)
