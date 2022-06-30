class Pessoa():
    def __init__(self, codigo, nome, endereco, telefone):
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone =telefone

    def imprimirNome(self):
        print("Nome: ",self.nome)
    

    def __imprimirTelefone(self):
        print("Telefone: ", self.__telefone)