from Matriz import Matriz

def main():
    print("--------------------------------------------------------")
    input("Pressione Enter para começar")
    print("--------------------------------------------------------")

    # Pede ao usuario o numero de equações do sistema (linhas e colunas da matriz)
    print("Qual o numero de equações do sistema?")
    numero_matriz = int(input(""))
    print("--------------------------------------------------------")

    # Cria uma matriz
    matriz = Matriz(numero_matriz, numero_matriz)

    # Pede a matriz do usuário
    matriz.criar_matriz()

    # Mostra a matriz criada
    matriz.mostrar_matriz()

    # Calcula a determinante da matriz
    det = matriz.determinante()

    # Pede o ultimo valor da equação
    ultimo_valor = matriz.pedir_ultimo_valor()

    # Aplica a regra de Cramer
    resultado = matriz.regra_de_cramer(ultimo_valor)

    if resultado:
        solucoes = resultado
        print("--------------------------------------------------------")
        print(f"Valores das variaveis em ordem: {solucoes}")

    print("--------------------------------------------------------")

    while True:
        resposta = input("Gostaria de fazer outro cálculo? (s/n): ").strip().lower()
        if resposta == 's':
            main()
            break
        elif resposta == 'n':
            print("--------------------------------------------------------")
            input("Pressione Enter para sair")
            break
        else:
            print("Resposta inválida. Por favor, digite 's' ou 'n'.")

if __name__ == "__main__":

    print("--------------------------------------------------------")
    print("Calculadora de Sistemas Lineares")
    main()