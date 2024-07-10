def meu_decorador(funcao):

    def envelope():
        print("Executa antes da função")
        funcao()
        print("Executa depois da função")

    return envelope

def ola_mundo():
    print("Olá mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()