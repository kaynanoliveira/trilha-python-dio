class Conta:
    def __init__(self, nro_agencia, saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def exibir_saldo(self):
        # ...
        return self._saldo


conta = Conta("0001")
conta.depositar(200)
print(conta.nro_agencia)
print(conta.exibir_saldo())
