from abc import ABC, abstractmethod, abstractproperty

# Interfaces definem o que uma classe deve fazer e não como.
# Todas as classes que implementem uma classe abstrata, elas vão ter que obrigatoriamente implementar os metodos abstratos.

class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass



class ControleTV(ControleRemoto):

    def ligar(self):
        print("Ligando TV...")
        print("TV ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada!")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):

    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "Philco"
    
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
