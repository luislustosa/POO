class NPC:
    def __init__(self, nomeNPC, aliado, gold):
        self.nomeNPC = nomeNPC
        self.aliado = aliado
        self.gold = gold

    def falarNPC(self):
        print('Olá, meu nome é:', self.nomeNPC)


class Inimigo:
    def __init__(self, nomeInimigo, hp, dano):
        self.nomeInimigo = nomeInimigo
        self.hp = hp
        self.dano = dano

    def falarInimigo(self):
        print('MORRAAAAA!')


class Personagem(NPC, Inimigo):
    def __init__(self, nome, aliado, gold, hp, dano):
        super().__init__(nome, aliado, gold)
        Inimigo.__init__(self, nome, hp, dano)

    def falarPersonagem(self):
        NPC.falarNPC(self)
        Inimigo.falarInimigo(self)


personagem1 = Personagem('Patches', True, 500, 1000, 200)
print(personagem1.nomeNPC)
personagem1.falarNPC()
personagem1.falarInimigo()
personagem1.falarPersonagem()