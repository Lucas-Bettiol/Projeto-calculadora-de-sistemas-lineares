import copy
import math

class Matriz:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.matriz = []
        self.matriz_backup = []

    # Cria a matriz com os valores fornecidos pelo usuário
    def criar_matriz(self):
        self.matriz = []
        for i in range(self.linhas):
            linha = []
            for j in range(self.colunas):
                while True:
                    try:
                        valor = int(input(f"Insira o {j+1}° valor da {i+1}° equação, sem a sua variável: "))
                        break
                    except ValueError:
                        print("Por favor, insira um número inteiro válido.")
                linha.append(valor)
            self.matriz.append(linha)
        self.matriz_backup = copy.deepcopy(self.matriz)

    # Mostra a matriz criada
    def mostrar_matriz(self):
        print("--------------------------------------------------------")
        print("Matriz criada:")
        for linha in self.matriz:
            print(linha)
        print("--------------------------------------------------------")

    # Calcula a determinante da matriz
    def determinante(self, matriz=None):
        if matriz is None:
            matriz = self.matriz
        if len(matriz) == 1:
            return matriz[0][0]
        if len(matriz) == 2:
            return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
        det = 0
        for c in range(len(matriz)):
            submatriz = [row[:c] + row[c+1:] for row in matriz[1:]]
            det += ((-1) ** c) * matriz[0][c] * self.determinante(submatriz)
        return det

    # Pede pela ultimo valor da equação
    def pedir_ultimo_valor(self):
        ultimo_valor = []
        for j in range(self.colunas):
            while True:
                try:
                    valor = int(input(f"Insira o valor após a igualdade da {j+1}° equação: "))
                    break
                except ValueError:
                    print("Por favor, insira um número inteiro válido.")
            ultimo_valor.append(valor)
        return ultimo_valor
    
    # Substitui a coluna X, Y ou Z da matriz pela ultima linha
    def substituir_coluna(self, idx_coluna, nova_linha):
        matriz_temp = copy.deepcopy(self.matriz)
        for i in range(len(matriz_temp)):
            matriz_temp[i][idx_coluna] = nova_linha[i]
        return self.determinante(matriz_temp)

    def regra_de_cramer(self, ultima_linha):
        det = self.determinante()
        if det == 0:
            print("--------------------------------------------------------")
            print("A matriz não possui solução única.")
            return None
        else:
            solucoes = []
            for i in range(self.colunas):
                det_i = self.substituir_coluna(i, ultima_linha)
                if det_i % det == 0:
                    x_i = det_i // det
                else:
                    mdc = math.gcd(det_i, det)
                    numerador = det_i // mdc
                    denominador = det // mdc
                    x_i = f"{numerador}/{denominador}"
                solucoes.append(x_i)
            return solucoes
        
    # Restaura a matriz original
    def restaurar_matriz(self):
        self.matriz = copy.deepcopy(self.matriz_backup)