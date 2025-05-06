class Pessoa():
    def __init__(self, peso, nome, idade):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.falando = False
        self.comendo = False
        self.dormindo = False
    def pararComer(self):
        if self.comendo == False:
            print(f"{self.nome}, Não está Comendo")
        else:
            print(f"{self.nome} Parar de comer")
        self.comendo = True

    def pararFalar(self):
        if self.falando == False:
            print(f"Não está Falando")
        else:
            print(f"Parar de Falar")
        self.falando = True

    def pararDormir(self):
        if self.dormindo == False:
            print(f"Não está Dormindo")
        else:
            print(f"Parar de Dormir")
        self.dormindo = True

    def comer(self, comida):
        if self.comendo == True:
            print(f"{self.nome}, ja está comendo")
        elif self.falando == True:
            print(f"{self.nome}, não pode comer porque está falando")
        else:
            print(f"{self.nome}, foi comer {comida}")
            self.comendo = True

    def falar(self):
        if self.falando == True:
            print(f"{self.nome}, ja está falando")
        elif self.comendo == True:
            print(f"{self.nome}, não pode falar, porque está comendo")
        else:
            print(f"{self.nome} está falando")
            self.comendo = True

    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome}, ja está Dormindo")
        elif self.comendo == True:
            print(f"{self.nome}, não pode dormir, porque está comendo")
        else:
            print(f"{self.nome} foi comer")
            self.comendo = True