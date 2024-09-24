class Marca:
    def __init__(self, nome,pais,importado):
        self.nome = nome
        self.pais = pais
        self.importado = importado

    def getData(self):
        print(f" A marca {self.nome} é do pais {self.pais}  importado ->{self.importado}")


class Veiculo:
    def __init__(self,modelo,ano,marca):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

marca1 = Marca("Audi","Alemanha",True)
veiculo1 = Veiculo("R8",2019,marca1)
print(veiculo1.marca.getData())