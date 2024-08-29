class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__historico = []

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            self.__historico.append(f"Depósito: R$ {valor:.2f}")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.append(f"Saque: R$ {valor:.2f}")
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Extrato da conta {self.__numero} - {self.__titular}")
        for transacao in self.__historico:
            print(transacao)
        print(f"Saldo: R$ {self.__saldo:.2f}")

# Criando uma conta
conta1 = Conta(123, "João da Silva")

# Realizando operações
conta1.depositar(1000)
conta1.sacar(500)
conta1.extrato()