from random import randrange
manifestacoes = []
opcao = 8
 
tipos_manifestacao = {
   1: "sugestão",
   2: "reclamação",
   3: "elogio"
}
 
while opcao != 7:
   print()
   print('Ouvidoria da Universidade JMS')
   print('1) Listar as manifestações')
   print('2) Listar todas as sugestões')
   print('3) Listar todas as reclamações')
   print('4) Listar todas os elogios')
   print('5) Enviar uma manifestação (criar uma nova)')
   print('6) Pesquisar o número de protocolo')
   print('7) Sair')
 
   try:
       opcao = int(input('Digite a opção que deseja escolher: '))
 
       #testar se a entrada é válida
       if opcao < 0 or opcao > 8:
           print('Digite uma opcão válida!!!')
           print()
       else:
           if opcao == 1:
               if len(manifestacoes) == 0:
                   print("Não há manifestacões cadastrados!")
               for manifestacao in manifestacoes:
                   print(manifestacao)
           elif opcao == 2:
               tem_sugestoes = False
               for manifestacao in manifestacoes:
                   tipo = manifestacao.split("#")[2]
                   if tipo == "sugestão":
                       print(manifestacao)
                       tem_sugestoes = True
 
               if tem_sugestoes == False:
                   print("Não há nenhuma sugestão postada.")
 
           elif opcao == 3:
               tem_reclamacao = False
               for manifestacao in manifestacoes:
                   tipo = manifestacao.split("#")[2]
                   if tipo == "reclamação":
                       print(manifestacoes)
                       tem_reclamacao = True
               if tem_reclamacao == False:
                   print("Não há nenhuma reclamação postada.")
           elif opcao == 4:
               tem_elogio = False
               for manifestacao in manifestacoes:
                   tipo = manifestacao.split("#")[2]
                   if tipo == "elogio":
                       print(manifestacoes)
                       tem_elogio = True
               if tem_elogio == False:
                   print("Não há elogio postado.")
           elif opcao == 5:
               protocolo = randrange(99999999)
               nome = input("Digite seu nome: ")
               try:
                   tipo = int(input("Digite o tipo da manifestação (1) sugestão, (2) reclamação, (3) elogio: "))
                   if tipo not in tipos_manifestacao:
                       print("Código de manifestação inválido!")
                   else:
                       descricao = input("Digite a sua manifestação: ")
                       manifestacao = f'{str(protocolo)}#{nome}#{tipos_manifestacao[tipo]}#{descricao}'
                       manifestacoes.append(manifestacao)
               except:
                   print("digite um número de manifestão válido!")
          
           elif opcao == 6:
               numero_protocolo_de_busca = input("digite o número do protocolo: ")
               resultado_busca = None
               for manifestacao in manifestacoes:
                   protocolo = manifestacao.split('#')[0]
                   if numero_protocolo_de_busca == protocolo:
                       resultado_busca = manifestacao
                       break
 
               if resultado_busca == None:
                   print("Protocolo não encontrado!")
               else:
                   print(resultado_busca)
 
 
 
   except:
       print('Digite uma opcão válida!!!')
       print('A entrada precisa ser um número entre 1 e 7!!')