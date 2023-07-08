import pandas as pd

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir_recursivo(self.raiz, valor)

    def _inserir_recursivo(self, no, valor):
        if not no:
            return No(valor)
        elif valor < no.valor:
            no.esquerda = self._inserir_recursivo(no.esquerda, valor)
        else:
            no.direita = self._inserir_recursivo(no.direita, valor)

        no.altura = 1 + max(self._obter_altura(no.esquerda), self._obter_altura(no.direita))
        fator_balanceamento = self._obter_fator_balanceamento(no)

        if fator_balanceamento > 1:
            if valor < no.esquerda.valor:
                return self._rotacionar_direita(no)
            else:
                no.esquerda = self._rotacionar_esquerda(no.esquerda)
                return self._rotacionar_direita(no)
        if fator_balanceamento < -1:
            if valor > no.direita.valor:
                return self._rotacionar_esquerda(no)
            else:
                no.direita = self._rotacionar_direita(no.direita)
                return self._rotacionar_esquerda(no)

        return no

    def _obter_altura(self, no):
        if not no:
            return 0
        return no.altura

    def _obter_fator_balanceamento(self, no):
        if not no:
            return 0
        return self._obter_altura(no.esquerda) - self._obter_altura(no.direita)

    def _rotacionar_direita(self, z):
        y = z.esquerda
        T3 = y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))

        return y

    def _rotacionar_esquerda(self, z):
        y = z.direita
        T2 = y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self._obter_altura(z.esquerda), self._obter_altura(z.direita))
        y.altura = 1 + max(self._obter_altura(y.esquerda), self._obter_altura(y.direita))

        return y

    def percorrer_em_ordem(self):
        self._percorrer_em_ordem_recursivo(self.raiz)

    def _percorrer_em_ordem_recursivo(self, no):
        if no:
            self._percorrer_em_ordem_recursivo(no.esquerda)
            print(no.valor)
            self._percorrer_em_ordem_recursivo(no.direita)

class PesquisaAVL:
    def __init__(self):
        self.df = None
        self.colunas = None
        self.arvore_avl = ArvoreAVL()

    def carregar_dados(self, nome_arquivo):
        self.df = pd.read_csv(nome_arquivo, delimiter=';')
        self.colunas = self.df.columns.tolist()

        for coluna in self.colunas:
            self.arvore_avl.inserir(coluna)

    def pesquisar_coluna(self, valor):
        no = self.arvore_avl.raiz
        while no:
            if valor == no.valor:
                return no.valor
            elif valor < no.valor:
                no = no.esquerda
            else:
                no = no.direita

        return None
    
    def salvar_resultados(self, resultado, valores_coluna, valor_pesquisa, valores_filtrados):
        with open('ResultadosAVL.txt', 'w') as arquivo:
            arquivo.write(f"Coluna encontrada: {resultado}\n\n")
            arquivo.write("Valores da coluna:\n")
            for valor in valores_coluna:
                arquivo.write(str(valor))
                arquivo.write('\n')
            arquivo.write('\n')

            arquivo.write(f"Valores encontrados para {valor_pesquisa}:\n")
            for indice, linha in valores_filtrados.iterrows():
                arquivo.write(linha.to_string())
                arquivo.write('\n\n\n')

        print("Resultados salvos no arquivo 'resultadosAVL.txt'.")


   

# Criar uma instância da Pesquisa AVL
pesquisa_avl = PesquisaAVL()

# Carregar o arquivo CSV
pesquisa_avl.carregar_dados('salary.csv')

# Realizar a pesquisa por um valor
valor_pesquisa = input("Digite o nome da coluna a ser pesquisada: ")
resultado = pesquisa_avl.pesquisar_coluna(valor_pesquisa)

if resultado:
    print(f"Coluna encontrada: {resultado}")

    # Imprimir os valores da coluna correspondente
    valores_coluna = pesquisa_avl.df[resultado].values
    print("Valores da coluna:")
    print(valores_coluna)


    
    if valor_pesquisa == 'age' or valor_pesquisa == 'Years of Experience' or valor_pesquisa == 'salary':
            valor_pesquisa = int(input("Digite o valor a ser pesquisado: "))
            valores_filtrados = pesquisa_avl.df[pesquisa_avl.df[resultado] == valor_pesquisa]
            print(f"Valores encontrados para {valor_pesquisa}:")
            print(valores_filtrados)
             # Salvar os resultados no arquivo
            pesquisa_avl.salvar_resultados(resultado, valores_coluna, valor_pesquisa, valores_filtrados)
            

    else:



            # Pesquisar um valor entre os correspondentes da coluna
            valor_pesquisa = input("Digite o valor a ser pesquisado: ")
            valores_filtrados = pesquisa_avl.df[pesquisa_avl.df[resultado] == valor_pesquisa]
            print(f"Valores encontrados para {valor_pesquisa}:")
            print(valores_filtrados)
            # Após a pesquisa e obtenção dos resultados
            pesquisa_avl.salvar_resultados(resultado, valores_coluna, valor_pesquisa, valores_filtrados)

            
else:
    print("Coluna não encontrada.")
