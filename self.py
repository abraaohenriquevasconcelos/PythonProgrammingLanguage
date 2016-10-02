'''
Para compreender o sentido do parâmetro self, temos de entender o que é uuma classe.

class Person(object)
    pass

E para executarmos operações nessa classe, precisamos definir funções que atuem sobre ela. Por exemplo, funções que armazenem o nome da pessoa. No código abaixo, declaramos a função dentro da classe, ao invés de ficar do lado de fora. A vantagem de fazer isso é que o código que altera a classe fica mais próximo da definição, ficando mais separado e legível. Depois, é só chamar o nome da classe seguido do nome da função:
'''
class Pessoa(object):
    def set_nome(pessoa, nome):
    if len(nome) >= 2:
        pessoa.nome = nome

dara = Pessoa()

#Nome da classe deve vir antes do uso da função, pois a função está dentro da classe
Pessoa.set_nome(dara, 'Dara dos Santos')

print dara.nome

'''
Entretanto, embora essa notação possa ser muito útil, ficar digirando o nome da classe pode ser bem entendiante. Certamente é redundante, pois todo objeto sabe a qual classe pertence. Desse modo, tiveram a ideia de, ao invés de preceder o nome da função com o nome da classe, precedê-lo com o objeto que é o primeiro parâmetro. Obviamente, não faz sentido usar o nome do objeto antes do nome da função e depois como parâmetro, como dara.set_nome(dara, 'Dara dos Santos'). Se o nome do objeto já está lpa antes do nome da função, ele deve ser retirado da lista de parâmetros.

Essas "funções dentro de classes" são chamadas de métodos. Para chamar métodos, tanto faz chamá-los em Classe.metodo(objeto, parametro) quanto chamá-los objeto.metodo(parametro)


As formas são equivalentes, com apenas uma ressalva: "objeto" deve ser um objeto da classe "Classe". Por sinal, mesmo a primeira notação Classe.metodo(objeto, parametro) resultaria em erro se "objeto" não fosse um objeto da classe "Classe".
'''

class Pessoa(object):
    def set_nome(objetoPessoa, nome):
    if len(nome) >= 2:
        objetoPessoa.nome = nome

dara = Pessoa()

Pessoa.set_nome(dara, 'Dara dos Santos')
print dara.nome

dara.set_nome('Dara da Silva')
print dara.nome

'''
O nome "self"

No método Pessoa.set_nome acima, o nome do primeiro parâmetro do método era person. Entretanto, é tradicional chamar esse primeiro parâmetro de self. Por quê?

Bem, não há nenhuma obrigatoriedade de se fazer assim, tanto o é que em nosso método usamos outro nome para o parâmetro. Costuma-se chamar o primeiro parâmetro de self porque a maioria dos programadores Python já reconhece como o nome do objeto a ser invocado no método;
'''

class Pessoa(object):
    def set_nome(self, nome):
    self.nome = nome

dara = Pessoa()
dara.set_nome('Dara da Silva')
print dara.nome

'''
Em outras linguagens orientadas a objetos, o parâmetro correspondente ao self geralmente não é declarado na lista de parâmetros, mas sim passodo implicitamente.


O self explícito tem, também, várias vantagens na prática. Uma das mais notáveis é a habilidade de chamar métodos de classes ancestrais sobre objetos de classes herdadas. Por exemplo, voltando ao nosso exemplo com pessoas, suponhamos que definamos uma nova classe CapitalizedPessoam, herdeira de Pessoa, na qual o nome da pessoa deve começar com uma letra maiúscula. Nessa classe, também queremos que todas as restrições que o método set_nome da classe Pessoa ainda sejam seguidas.
'''

import string

class Pessoa(object):
    def set_nome(self, nome):
    if len(nome) >= 2:
        self.nome = nome

class CapitalizedPessoa(Pessoa):
    def set_nome(self, nome):
    if nome[0] in string.uppercase:
        Pessoa.set_nome(self, nome)