import pandas as pd

class Node:
    def __init__(self, value):
        # Inicializa um nó com um valor e define os nós esquerdo e direito como None
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        # Inicializa uma árvore binária com a raiz definida como None
        self.root = None
    
    def insert(self, value):
        # Se a árvore estiver vazia, insere o valor como a raiz
        if self.root is None:
            self.root = Node(value)
        else:
            # Caso contrário, chama o método _insert_recursive para inserir o valor de forma recursiva
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                # Se o valor for menor que o valor do nó atual e o nó esquerdo for None, insere o valor como nó esquerdo
                node.left = Node(value)
            else:
                # Caso contrário, chama o método _insert_recursive no nó esquerdo para inserir o valor de forma recursiva
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                # Se o valor for maior que o valor do nó atual e o nó direito for None, insere o valor como nó direito
                node.right = Node(value)
            else:
                # Caso contrário, chama o método _insert_recursive no nó direito para inserir o valor de forma recursiva
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        # Chama o método _search_recursive para procurar o valor na árvore
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            # Se o nó atual for None ou tiver o valor procurado, retorna o nó atual
            return node
        if value < node.value:
            # Se o valor for menor que o valor do nó atual, chama o método _search_recursive no nó esquerdo
            return self._search_recursive(node.left, value)
        # Caso contrário, chama o método _search_recursive no nó direito
        return self._search_recursive(node.right, value)

# Carregar o arquivo CSV
df = pd.read_csv('salary.csv', delimiter=';')

# Criar uma instância da árvore binária
tree = BinaryTree()

# Inserir os valores das colunas na árvore binária
for column in df.columns:
    tree.insert(column)

# Realizar a busca por um valor na árvore binária
value_to_search = input("Digite o nome da coluna a ser pesquisada: ")
result = tree.search(value_to_search)



# Criar um arquivo chamado "result_pesquisa_binaria.txt" para gravar os resultados da pesquisa
with open("result_pesquisa_binaria.txt", "w") as arquivo:
    if result:
        arquivo.write(f"Coluna encontrada: {result.value}\n")
        
        # Gravar os valores da coluna correspondente
        column_values = df[result.value].values
        arquivo.write("Valores da coluna:\n")
        arquivo.write("\n".join(str(value) for value in column_values))
        arquivo.write("\n\n")
        
        if value_to_search == 'age' or value_to_search == 'Years of Experience' or value_to_search == 'salary':
            # Solicitar o valor a ser pesquisado
            search_value = int(input("Digite o valor a ser pesquisado: "))
            
            # Filtrar os valores no DataFrame
            filtered_values = df[df[result.value] == search_value]
            
            arquivo.write(f"Valores encontrados para {search_value}:\n")
            arquivo.write(filtered_values.to_string(index=False, justify='left', col_space=15))
            arquivo.write("\n\n")
        else:
            # Solicitar o valor a ser pesquisado
            search_value = input("Digite o valor a ser pesquisado: ")
            
            # Filtrar os valores no DataFrame
            filtered_values = df[df[result.value] == search_value]
            
            arquivo.write(f"Valores encontrados para {search_value}:\n")
            arquivo.write(filtered_values.to_string(index=False, justify='left', col_space=15))
            arquivo.write("\n\n")
    else:
        arquivo.write("Coluna não encontrada na árvore binária.\n")





