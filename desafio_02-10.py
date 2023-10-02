import random

# Lista de palavras
listaA = ["amor", "casa", "gato", "livro", "fruta", "tempo", "cidade", "verde", "feliz", "carro", "festa",
          "frio", "sol", "lua", "mar", "rio", "amigo", "escola", "trabalho", "comida", "carro", "livro", "sol",
          "cachorro", "computador", "montanha"]

# Gerar um índice aleatório
indice_aleatorio = random.randint(0, len(listaA) - 1)
# Acessar a palavra aleatória usando o índice gerado
palavra_aleatoria = listaA[indice_aleatorio]

# Testando a junção de letras
tamanho_var = len(palavra_aleatoria)
palavra_mostrada = ['-'] * tamanho_var  # Inicialize a lista com '-' usando compreensão de lista
print("\nEncontre as letras da palavra misteriosa!", "\nAqui está a quantidade de letras:", "".join(palavra_mostrada))

# Definir o número máximo de erros
limiteErros = int(input("\nQuantas chances deseja ter? "))
erros = 0

# Inicializar a lista para armazenar as letras correspondentes
letras_mostradas = []
# Inicializar a lista de letras encontradas
letras_encontradas = []

while erros < limiteErros:
    # Solicitar letra
    letra = input("\nDigite uma letra: ").lower()

    # Inicializar uma variável para controlar se a letra foi encontrada
    encontrada = False

    # Iterar sobre cada letra na palavra aleatória
    for i in range(len(palavra_aleatoria)):
        if palavra_aleatoria[i] == letra:
            letras_mostradas.append(letra)
            palavra_mostrada[i] = letra  # Atualizar a palavra mostrada com a letra correta
            # Adicionar a letra às letras encontradas se ainda não estiver lá
            if letra not in letras_encontradas:
                letras_encontradas.append(letra)

    # Apresentar a palavra com "-" nas letras ausentes
    print(f"Palavra: {' '.join(palavra_mostrada)}")

    # Apresentar as letras correspondentes
    if letra in palavra_aleatoria:
        print(f"A letra '{letra}' está na palavra.")
    else:
        print(f"A letra '{letra}' não está na palavra.")
        erros += 1
        
    # Verifica se a palavra misteriosa foi acertada pelo player
    if "".join(palavra_mostrada) == palavra_aleatoria:

        print ("\nVocê acertou a palavra!")
        break