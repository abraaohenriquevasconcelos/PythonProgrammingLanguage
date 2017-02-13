class Balde:

    """
    O método __init__ é um método especial para classes. Ele é o construtor, ele inicializa o estado de um objeto. O método
    __init__ é invocado a cada nova instância de uma classe.
    """
    def __init__(self, cap):
        self.capacidade = cap
        self.volume = 0 #volume atual
        self.vol_derramado = 0
        self.cheio = False


    def encherdagua(self, vol):
        self.volume += vol
        if self.volume >= self.capacidade:
            self.cheio = True
            self.vol_derramado = self.volume - self.capacidade
            self.volume = self.capacidade
        return self.volume

    """
    O Java tem um método padrão para transformar um objeto em String que o toString(). Já o Python tem dois métodos para
    trasformar um objeto em uma string.

    __str__ -> exibir o objeto para o usuário final, usado pelo comando print e pela função str

    __repr__ -> exibir o objeto para o programador, usado pelo console do python e pela função repr

    >>> f = 11/10
    >>>f
    1.1000000000000001
    >>>print(f)
    1.1
    >>>str(f)
    '1.1'
    >>>repr(f)
    '1.1000000000000001'

    Nesse caso __repr__ devolve a representação interna do número. Para exibir para o usuário, usamos print, que usa __str__
    e exibe uma aproximação para não deixar o usuário final nervoso

    >>>s = u'avião'
    >>>a
    u'avi\xe3o'
    >>>print(s)
    avião
    >>>print(repr(s))
    u'avi\xe3o'

    Note que, ao exibir uma string Unicode, o repr coloca o prefixo 'u' na frentee troca qq caractere não-ASCII por uma representação
    hexadecimal. Mas o str mostra o resultado de um jeito mais amigável,
    """
    def __repr__(self):
        if self.volume >= self.capacidade:
            return "*%2d*"%self.volume
        else:
            return "[%2d]"%self.volume



"""
A vantagem de usar if __name__ == “__main__”: é que, ao se importar o módulo balde, os testes não são executados, mas a classe pode
ser utilizada. O interpretador Python executa todas as instruções que encontra mas leva em conta alguns atributos especiais que
definem o estado do interpretador. Um deles é o atributo __name__, que recebe o nome especial __main__ quando o módulo é executado
diretamente usando, por exemplo: >>>python3 balde.py
Ao executar o comando import, o conteúdo do módulo é carregado com o nome do módulo que deve ser diferente de __main__ (no caso, é balde)

"""


if __name__ == "__main__":
    # programa de teste da classe Balde
    print(dir(Balde))
    print(Balde.__repr__)
    balde = Balde(10)
    print(balde.__repr__)
    vol1 = balde.encherdagua(3)
    vol2 = balde.encherdagua(4)
    print(balde)
    vol3 = balde.encherdagua(5)
    print(balde)
    print(vol1, vol2, vol3)