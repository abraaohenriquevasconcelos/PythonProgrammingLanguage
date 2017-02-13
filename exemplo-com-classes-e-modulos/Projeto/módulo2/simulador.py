import random
#from módulo1.balde import Balde
from módulo1 import Balde

#definição de constantes
CAPACIDADE_MIN = 10
CAPACIDADE_MAX = 51 #ja ajustado ao random
VOLUME_MIN = 1
VOLUME_MAX = 11 #ja ajustado ao random

class Simulador:
    def __init__(self, semente):
        random.seed(semente)
        capacidade = random.randrange(CAPACIDADE_MIN, CAPACIDADE_MAX)
        self.baldinho = Balde(capacidade)
        self.volume = 0


    def sorteia(self):
        self.volume = random.randrange(VOLUME_MIN, VOLUME_MAX)
        print()
        print("Volume atual: %dL\n\n" %self.baldinho.volume)
        print("Volume sorteado: %dL\n\n" %self.volume)
        return self.volume


    def encherdaguaSimulador(self):
        self.baldinho.encherdagua(self.volume)
        if self.baldinho.volume < self.baldinho.capacidade:
            print("O volume do balde é menos do que a metadae da capacidade do balde!\n\n")
        elif self.baldinho.volume >= self.baldinho.capacidade:
            print("O volume do balde atingiu/passou a metade!\n\n")
            print("\nE o volume derramado: %dL\n\n" %self.baldinho.vol_derramado)

        return self.baldinho.cheio


if __name__ == "__main__":
    simulador = Simulador(123)
    sorteado = simulador.sorteia()
    resultado = simulador.encherdaguaSimulador()
    if(resultado):
        print("Já encheu na primeira!!")
    else:
        while(resultado != True):
            resultado = simulador.encherdaguaSimulador()