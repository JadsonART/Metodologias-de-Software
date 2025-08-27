class ContaBancaria:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor <= 0:
            print("Depósito deve ser maior que zero!")
            return
        self.saldo += valor
        print(f"Depósito de {valor} feito! Novo saldo: {self.saldo}")

    def sacar(self, valor):
        if valor <= 0:
            print("Saque deve ser maior que zero!")
            return
        if valor > self.saldo:
            print("Saldo insuficiente!")
            return
        self.saldo -= valor
        print(f"Saque de {valor} feito! Novo saldo: {self.saldo}")

    def transferir(self, destino, valor):
        if self == destino:
            print("Não pode transferir para a mesma conta!")
            return
        if valor > self.saldo:
            print("Saldo insuficiente para transferência!")
            return
        self.sacar(valor)
        destino.depositar(valor)
        print(f"Transferência de {valor} para {destino.titular} realizada!")

class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, numero, titular, saldo=0):
        if numero in self.contas:
            print("Conta já existe!")
            return
        conta = ContaBancaria(numero, titular, saldo)
        self.contas[numero] = conta
        print(f"Conta {numero} criada para {titular} com saldo {saldo}")

    def obter_conta(self, numero):
        if numero not in self.contas:
            print("Conta não encontrada!")
            return None
        return self.contas[numero]

    def listar_contas(self):
        if not self.contas:
            print("Não há contas cadastradas.")
            return
        for c in self.contas.values():
            print(f"Conta {c.numero} | Titular: {c.titular} | Saldo: {c.saldo}")

# Programa principal
banco = Banco()

print("=== Bem-vindo ao Banco Simples ===")

while True:
    print("\nComandos: criar, depositar, sacar, transferir, listar, sair")
    comando = input("> ").strip().lower()

    if comando == "sair":
        print("Saindo do banco... até mais!")
        break

    elif comando == "criar":
        numero = int(input("Número da conta: "))
        titular = input("Nome do titular: ")
        saldo = float(input("Saldo inicial (0 para nenhum): ") or "0")
        banco.criar_conta(numero, titular, saldo)

    elif comando == "depositar":
        numero = int(input("Número da conta: "))
        conta = banco.obter_conta(numero)
        if conta:
            valor = float(input("Valor para depositar: "))
            conta.depositar(valor)

    elif comando == "sacar":
        numero = int(input("Número da conta: "))
        conta = banco.obter_conta(numero)
        if conta:
            valor = float(input("Valor para sacar: "))
            conta.sacar(valor)

    elif comando == "transferir":
        de_num = int(input("Conta de origem: "))
        para_num = int(input("Conta destino: "))
        conta_de = banco.obter_conta(de_num)
        conta_para = banco.obter_conta(para_num)
        if conta_de and conta_para:
            valor = float(input("Valor para transferir: "))
            conta_de.transferir(conta_para, valor)

    elif comando == "listar":
        banco.listar_contas()

    else:
        print("Comando desconhecido! Tente novamente.")
