def mensagem(nome):
    print("Imprimindo mensagem...")
    return f"Olá {nome}"

def mensagem_longa(nome):
    print("Imprimindo mensagem longa...")
    return f"Olá {nome}, seja bem vindo!"

def executar(funcao, nome):
    print("Executando...")
    return funcao(nome)

print(executar(mensagem, "Kaynan"))
print(executar(mensagem_longa, "Kaynan"))