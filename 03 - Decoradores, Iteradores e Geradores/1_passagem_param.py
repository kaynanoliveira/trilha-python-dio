def mensagem(nome):
     print("Executando mensagem")
     return f'Olá {nome}'

def mensagem_longa(nome):
      print("Executando mensagem longa")
      return f'Seja bem vindo {nome}!'

def executar(funcao, nome):
       print("Executando executar")
       return funcao(nome)

print(executar(mensagem, "Kaynan"))
print(executar(mensagem_longa, "Kaynan"))
