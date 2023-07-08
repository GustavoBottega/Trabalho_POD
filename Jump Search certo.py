import pandas as pd
import math

# Carregar o arquivo CSV
df = pd.read_csv('salary.csv', delimiter=';')

# Ordenar a lista pela coluna 'age'
df.sort_values(by='age', inplace=True)
column_values = df['age'].values

# Realizar a pesquisa por um valor usando Jump Search
def jump_search(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))  # Determina o tamanho do salto
    prev = 0  # Índice anterior

    # Enquanto o elemento no índice atual for menor que x
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))  # Aumenta o tamanho do salto
        if prev >= n:  # Se o tamanho do salto for maior ou igual ao tamanho do array
            return -1

    # Realiza uma busca linear a partir do índice prev
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):  # Se o índice prev alcançar o tamanho do salto ou o tamanho do array
            return -1

    # Se o elemento no índice prev for igual a x, retorna prev
    if arr[prev] == x:
        return prev

    # Caso contrário, o valor não foi encontrado
    return -1

# Solicitar o valor a ser pesquisado
search_value = input("Digite o valor a ser pesquisado: ")

# Realizar a pesquisa usando Jump Search
result = jump_search(column_values, search_value)

if result != -1:
    print(f"Valores encontrados para {search_value}:\n")
    indices = []

    # Encontrar todos os índices correspondentes ao valor pesquisado
    while result != -1:
        indices.append(result)

        # Realizar a próxima pesquisa a partir do próximo índice
        result = jump_search(column_values[result + 1:], search_value)

        # Se a pesquisa encontrar um novo índice correspondente, ajustar o índice encontrado
        if result != -1:
            result += indices[-1] + 1

    # Mostrar todas as linhas correspondentes ao valor pesquisado
    for index in indices:
        print(df.iloc[index])
        print()

    # Salvar os resultados da pesquisa em um arquivo de texto
    result_file_name = "result_pesquisa_jump.txt"
    with open(result_file_name, 'w') as file:
        for index in indices:
            file.write(str(df.iloc[index]) + '\n\n\n')
    print(f"Resultados da pesquisa salvos no arquivo '{result_file_name}'.")
else:
    print(f"Nenhum valor encontrado para {search_value}.")
