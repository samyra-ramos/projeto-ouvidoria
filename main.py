from ouvidoria import Ouvidoria
ouvidoria = Ouvidoria()

while True:
    print(ouvidoria.menu())
    try:
        opcao = int(input('Digite a opção que deseja escolher: '))
        print('\033c')
        if opcao == 1:
            ouvidoria.listarManifestacoes()
        elif opcao == 2:
            ouvidoria.listarSugestoes()
        elif opcao == 3:
            ouvidoria.listarReclamacoes()
        elif opcao == 4:
            ouvidoria.listarElogios()
        elif opcao == 5:
            ouvidoria.criarManifestacao()
        elif opcao == 6:
            ouvidoria.procurarNumeroProtocolo()
        elif opcao == 7:
            print("Saindo")
            break 
        else:
            print("A opção selecionada não existe. Para acessar o menu, digite uma opção entre 1 e 7: ")
    except:
        print('\033c')
        print('Digite uma opcão válida. A entrada precisa ser um número entre 1 e 7.')