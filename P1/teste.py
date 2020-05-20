import pymongo
from clube import Clube
from estadio import Estadio
from torcedor import Torcedor
from ingresso import Ingresso

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["dbfutebol"]

clube = Clube()
estadio = Estadio()
torcedor = Torcedor()
ingresso = Ingresso()


while True:
    option = input("\n1 - Manter Clube\n"
                   "2 - Manter Estádio\n"
                   "3 - Manter Torcedor\n"
                   "4 - Manter Ingresso\n"
                   "5 - Gerar Resultado do Jogo\n"
                   "0 - Sair\n"
                   "Opção escolhida: ")

    if option == "1":
        option = input("\n1 - Cadastrar Clube\n"
                       "2 - Alterar Clube\n"
                       "3 - Excluir Clube\n"
                       "4 - Consultar Clube\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            clube.cadastrar_clube()
        elif option == "2":
            clube.alterar_clube()
        elif option == "3":
            opcao = input("\n1 - Excluir funcionário específica\n"
                          "2 - Excluir todas as funcionários\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                clube.excluir_clube(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todas as funcionários? (s/n): ")
                if opcao == "s":
                    clube.excluir_clube(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todas as funcionários\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                clube.consultar_clube(True)
            elif opcao == "2":
                clube.consultar_clube(False)
        else:
            continue

    elif option == "2":
        option = input("\n1 - Cadastrar Estádio\n"
                       "2 - Alterar Estádio\n"
                       "3 - Excluir Estádio\n"
                       "4 - Consultar Estádio\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            estadio.cadastrar_estadio()
        elif option == "2":
            estadio.alterar_estadio()
        elif option == "3":
            opcao = input("\n1 - Excluir estadio específico\n"
                          "2 - Excluir todos os estadios\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                estadio.excluir_estadio(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todos os estadios? (s/n): ")
                if opcao == "s":
                    estadio.excluir_estadio(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todos os estadios\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                estadio.consultar_estadio(True)
            elif opcao == "2":
                estadio.consultar_estadio(False)
        else:
            continue

    elif option == "3":
        option = input("\n1 - Cadastrar Torcedor\n"
                       "2 - Alterar Torcedor\n"
                       "3 - Excluir Torcedor\n"
                       "4 - Consultar Torcedor\n"
                       "0 - Sair\n"
                       "Opção escolhida: ")

        if option == "1":
            torcedor.cadastrar_torcedor()
        elif option == "2":
            torcedor.alterar_torcedor()
        elif option == "3":
            opcao = input("\n1 - Excluir torcedor específico\n"
                          "2 - Excluir todos os torcedors\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                torcedor.excluir_torcedor(False)
            elif opcao == "2":
                opcao = input("Tem certeza que deseja excluir todos os torcedors? (s/n): ")
                if opcao == "s":
                    torcedor.excluir_torcedor(True)
                else:
                    continue

        elif option == "4":
            opcao = input("\n1 - Consultar todos os torcedors\n"
                          "2 - Consulta personalizada\n"
                          "Informe qualquer outro caractere para voltar\n"
                          "Opção escolhida: ")
            if opcao == "1":
                torcedor.consultar_torcedor(True)
            elif opcao == "2":
                torcedor.consultar_torcedor(False)
        else:
            continue

    elif option == "4":
        pass

    elif option == "0":
        break

    else:
        print("Informe uma opção válida!")