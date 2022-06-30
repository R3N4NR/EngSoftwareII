from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

pf1 = Fisica(987, "Jonas", "Bento 1000", "3333-55-66", "123.126.700-21", 35, 77.5, 1.71)

pf1.imprimeCPF()
# pf1.__calculaIMC()

pf1.imprimirNome()
# pf1.__imprimirTelefone()

pj1 = Juridica(741, "Paulo", "Ipiranga 7200", "3216-55-88", "123528788-52"," 879879878-5151515", 87)

while True:
 try:
        print("\n          Cadastro PJ/PF")
        nome = str(input("Nome: "))
        endereco = str(input("Endereco: "))
        telefone = str(input("Telefone: "))
        cadastro = str(input("Cadastro de pessoa: "))

        converte_cadastro = int(cadastro)

        if len(cadastro) == 14:
            inscricao_estadual = str(input("Inscricao estadual: "))
            qtd_funcionarios = str(input("Numero de funcionarios: "))
            pJ = Juridica(714, nome, endereco, telefone, cadastro,
                      inscricao_estadual, qtd_funcionarios)
            print("Pessoa Juridica")
            pJ.imprimeCNPJ()
        elif len(cadastro) == 11:
            idade = str(input("Idade: "))
            peso = str(input("Peso(kg): "))
            altura = str(input("Altura(cm): "))
            pF = Fisica(987, nome, endereco, telefone,
                    cadastro, idade, peso, altura)
            print("Pessoa Física")
            pF.imprimeCPF()

        else:
            print("Dados Inválidos!")


 except ValueError:
            print("Dado informado em formato incorreto!")

# pj1.__emitirNotaFiscal()


