class Animal():
    def __init__(self, nome ,hp ,dano):
        self.nome = nome
        self.hp = hp
        self.dano = dano

    def falar(self):
        print("Animal: ",self.nome)

    def receberdano(self,dano):
        self.hp -= dano
        if self.hp <= 0:
            print("Morreu!!")

class Lobo(Animal):
    def __init__(self, nome ,hp ,dano,escudo):
        super().__init__(nome,hp,dano)
        self.escudo = escudo

    def falar(self):
        super().falar()
        print("Lobo: AUUUUUU")

    def uivar(self):
        self.escudo += 50

lobo1 = Lobo("Wolf", 50, 50 ,50)
lobo1.falar()
lobo1.uivar()
print(lobo1.escudo)

lobo1.receberdano(60)

animal1 = Animal("Bob",100,100)
