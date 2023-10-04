#atividade 01 - no caso 08

contatos = {
    'Bob': {'email': 'bob@email.com'},
    'Peba': {'email': 'peba.com'},
    'Ioio': {'email': 'duaninha.com'},
    'Alice': {'email': 'alice@email.com'}
}

#01. Acessar as informações de contato de uma pessoa específica a partir do dicionário "contatos".
# Por exemplo, imprimir o telefone e o email de "Alice".
print ("Mostrando o contato da Alice", contatos ["Alice"])
#02. Adicionar novas pessoas e suas informações de contato ao dicionário "contatos".
print("\nAdicioanndo novas pessoas e infos")
nome = input("Digite o nome do contato: ").capitalize()
email = input("Informe o e-mail: ")
contatos[nome] = {"email:", email}
#03. Modificar as informações de contato de uma pessoa existente no dicionário "contatos". Por exemplo, atualizar o email de "Bob".
print("\nModificando o email do Bob")
contatos['Bob'] = {"email": "bobzinho_do_grau@gmail.com"}
print(contatos['Bob'])
#04. Excluir um contato específico do dicionário "contatos". Por exemplo, remover o contato de "Alice".
del (contatos['Alice'])
print ("\nO contato de Alice foi deletado")
print ("Mostrando os contatos na lista: ", contatos)
#05. Desafio (+1 pt): listar todos os nomes de pessoas no dicionário "contatos" em ordem alfabética.
print(sorted (contatos))