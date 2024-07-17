def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes da função")
        funcao(*args, **kwargs)
        print("Faz algo depois da função")


    return envelope

@meu_decorador
def ola_mundo(nome, outro_argumento):
    print(f'Olá, meu nome é {nome}')

ola_mundo("Kaynan", 1000)


