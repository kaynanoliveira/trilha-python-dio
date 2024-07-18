
def validar(funcao):
    def valida(x, y):
        if x < 0 or y < 0:
            raise ValueError("X e Y não podem ser negativos!")    
        x *= 2
        y *= 2   
        return funcao(x, y)
    
    return valida

@validar
def soma(x, y):
    return x + y 


print(soma(10, 20))