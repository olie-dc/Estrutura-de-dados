class Queue:
    """
    ESTRUTURA DE DADOS FILA
    Trata-se de uma estrutura de dados linear em que a operação de inserção ("enqueue") ocorre no final (ou cauda) da
    estrutura, enquanto a operação de remoção ("dequeue") é feita no inicio (cabeça). Em consequencia, o funcionamento
    da fila pode ser descrito pelo principio FIFO(First In, Fist Out): o primeiro a entrar também é o primeiro a sair.
    """

    def __init__(self):
        """Método construtor"""
        self.__data = []  #liata vazia

    def enqueue(self, val):
        """
        Metodo de inserção
        Em filas, tem nome padronizado: enqueue
        """
        self.__data.append(val)
        
    def is_empty(self):
        """Metodo que retorno se a fila esta ou não vazia"""
        return len(self.__data) == 0
    
    def dequeue(self):
        """
        Metodo de remoção
        Em filas,tem nome padronizado: dequeue 
        """
        if self.is_empty():
            raise Exception("ERRO: impossivel remover de uma fila vazia.")
        return self.__data.pop(0)  #Remoção no inicio
    
    def peek(self):
        """
        metodo para consultar o primeiro item da fila, sem remove-lo
        """
        if self.is_empty():
            raise Exception("ERRO: impossivel consultar uma fila vazia")
        return self.__data[0] #Primeiro item
    
    def __str__(self):
        """
        Metodo que retorna uma represnetação da fila como string
        """
        return str(self.__data)
    
###############################################################################################################
    