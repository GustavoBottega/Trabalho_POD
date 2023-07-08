

import pandas as pd

class ExponentialSearch:
    def __init__(self):
        self.df = None
        self.columns = None
    
    def load_data(self, file_name):
     # Carrega o arquivo CSV utilizando o pandas e define o delimitador como ';'

        self.df = pd.read_csv(file_name, delimiter=';')
        
        # Obtém os nomes das colunas do dataframe e os armazena como uma lista
        self.columns = self.df.columns.tolist()
    
    def exponential_search(self, value):
        if self.columns is None:
            return None
        
        # Verifica se o valor procurado está na primeira coluna

        if self.columns[0] == value:
            return self.columns[0]
        
        n = len(self.columns)
        i = 1
        # Realiza a busca exponencial
        while i < n and self.columns[i] != value:
            i *= 2
        
        if i >= n:
            return None
        
        return self.columns[i]
   # O método exponential_search implementa o algoritmo de pesquisa exponencial. 
   # Ele recebe um valor como argumento e verifica se a lista de colunas está vazia. 
   # Se estiver vazia, retorna None. Em seguida, verifica se o valor procurado está 
   # na primeira coluna. Se estiver, retorna essa coluna. 
   # Caso contrário, realiza a pesquisa exponencial, dobrando o valor de i a cada iteração
   #  até que o valor seja encontrado ou ultrapasse o tamanho da lista de colunas. 
   # Se o valor não for encontrado, retorna None. Caso contrário, retorna a coluna encontrada.

    

# Criar uma instância da Pesquisa Exponencial
exp_search = ExponentialSearch()

# Carregar o arquivo CSV
exp_search.load_data('salary.csv')

# Realizar a pesquisa por um valor
value_to_search = input("Digite o nome da coluna a ser pesquisada: ")
result = exp_search.exponential_search(value_to_search)

if result:
    print(f"Coluna encontrada: {result}")
    
    # Imprimir os valores da coluna correspondente
    column_values = exp_search.df[result].values
    print("Valores da coluna:")
    print(column_values)
    
    # Pesquisar um valor entre os correspondentes da coluna
    if value_to_search == 'age' or value_to_search == 'Years of Experience' or value_to_search == 'salary':
        search_value = int(input("Digite o valor a ser pesquisado: "))
        filtered_values = exp_search.df[exp_search.df[result] == search_value]
        print(f"Valores encontrados para {search_value}:")
        print(filtered_values)
    else:
        search_value = input("Digite o valor a ser pesquisado: ")
        filtered_values = exp_search.df[exp_search.df[result] == search_value]
        print(f"Valores encontrados para {search_value}:")
        print(filtered_values)

    # Salvar os resultados da pesquisa em um arquivo CSV
    result_file_name = "result_pesquisa_exp.txt"
    filtered_values.to_csv(result_file_name, index=False)
    print(f"Resultados da pesquisa salvos no arquivo '{result_file_name}'.")
else:
    print("Coluna não encontrada.")

