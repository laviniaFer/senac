contatos = {
    'Bob': {'telefone': '987-654-3210', 'email': 'bob@email.com'},
    'Alice': {'telefone': '123-456-7890', 'email': 'alice@email.com'}
}
# menu inicial para escolher as opções de funcionalidade
while True:
    opcao = (input ("\nBem-vind@ a agenda SENAC!"
                "\nEscolha uma das opções abaixo para prosseguir:"
                "\n 1 - Adiconar"
                "\n 2 - Excluir"
                "\n 3 - Listar"
                "\n 4 - Pesquisar"
                "\n 5 - Sair"
                "\n "))
    # adicionando um contato ao dicionario contato
    if opcao == "1":
            nome = input("Escreva 'sair' para encerrar o programa.\nOu digite o nome do contato: ")
            if nome.lower() == 'sair':
                break  # Sai do loop principal se o usuário digitar 'sair'
        
            numero = input("Informe o número: ")
            email = input("Informe o e-mail: ")
            
            contatos[nome] = {"numero": numero, "email": email}

    # removendo um contao do dicionario
    elif opcao== "2":
            nomedel = input("Digite o nome do contato que deseja deletar: ")
            if nomedel in contatos:
                del contatos[nomedel]
            print(f"Contato {nomedel} deletado.")

    # listando os contatos existentes
    elif opcao== "3":
            print("\nInformações da Agenda:")
            print(contatos)
        
    # pesquisando por nome
    elif opcao =="4":
        procurar = (input("Quem você está procurando? "))
        print('procurar' in contatos)

    # encerrando código
    elif opcao == "5":
        print("\nPrograma finalizado.")
        exit()
    else:
        print("Opção inválida. Tente novamente.")