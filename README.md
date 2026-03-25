# Calculadora de Sistemas Lineares

Uma calculadora simples em Python para resolver sistemas lineares utilizando a Regra de Cramer. O programa permite ao usuário inserir o número de equações, os coeficientes da matriz e os termos independentes, e calcula as soluções das variáveis.

## Funcionalidades

- Entrada interativa para o número de equações do sistema.
- Criação e exibição da matriz de coeficientes.
- Cálculo da determinante da matriz.
- Aplicação da Regra de Cramer para encontrar as soluções.
- Opção para realizar múltiplos cálculos em sequência.

## Requisitos

- Python 3.x
- Biblioteca padrão do Python (não há dependências externas além do que está incluído no ambiente virtual).

## Como Usar

1. Certifique-se de que o ambiente virtual está ativado (se aplicável):
   ```
   myenv\Scripts\activate
   ```

2. Execute o programa principal:
   ```
   python Codigo Python/main.py
   ```

3. Siga as instruções na tela:
   - Digite o número de equações.
   - Insira os coeficientes da matriz linha por linha.
   - Insira os termos independentes (últimos valores das equações).
   - O programa exibirá as soluções das variáveis.

4. Após o cálculo, você pode escolher fazer outro cálculo ou sair.

## Construindo um Executável

O projeto inclui um arquivo `main.spec` para o PyInstaller. Para criar um executável independente:

1. Ative o ambiente virtual:
   ```
   myenv\Scripts\activate
   ```

2. Instale o PyInstaller (se não estiver instalado):
   ```
   pip install pyinstaller
   ```

3. Execute o PyInstaller com o spec file:
   ```
   pyinstaller Codigo Python/main.spec
   ```

4. O executável será gerado na pasta `dist/`.

## Estrutura do Projeto

- `Codigo Python/main.py`: Arquivo principal do programa.
- `Codigo Python/Matriz.py`: Classe Matriz com métodos para manipulação de matrizes e aplicação da Regra de Cramer.
- `Codigo Python/main.spec`: Arquivo de configuração para o PyInstaller.
- `myenv/`: Ambiente virtual com dependências.
- `build/`: Arquivos temporários de build.

## Licença

Este projeto é de uso livre. Sinta-se à vontade para modificar e distribuir.
