import abc


class BankAccount(abc.ABC):
    def __init__(self, agency, num_account, balance):
        self.agency = agency
        self.num_account = num_account
        self.balance = balance

    @abc.abstractmethod
    def withdraw(self, value): ...

    def deposit(self, value):
        self.balance += value
        self.test(f'Depositado: R$ {value}')

    # Método para fim de teste quanto ao andamento do projeto
    def test(self, msg):
        print(f'Saldo é {self.balance:.2f} {msg}')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agency}, {self.num_account}, {self.balance}'

        # Verificação do atributo limit, devido a subclasse "CheckingAccount" possuir
        if hasattr(self, 'limit'):
            attrs += f', {self.limit}'
        attrs += ')'
        return f'{class_name}{attrs}'


class SavingsAccount(BankAccount):
    def withdraw(self, value):

        # Para a utilização do método withdraw(sacar), primeiro verifica-se se há balance(saldo) disponível. Será retornado o valor pós saque.
        postWithdrawalAmount = self.balance - value
        if postWithdrawalAmount >= 0:
            self.balance -= value
            self.test(f'Valor sacado {value:.2f}')
            return self.balance

        # Caso entre na condição, não será executado por conta do return. Caso contrário, o print é executado.
        print(f'Saque negado: R$ {value:.2f}. Confira o seu saldo em conta.')


class CheckingAccount(BankAccount):
    def __init__(self, agency, num_account, balance, limit):
        # Chama o construtor da classe pai para inicializar os atributos comuns
        super().__init__(agency, num_account, balance)
        self.limit = limit
        # Adiciona o atributo específico da classe CheckingAccount.

    def withdraw(self, value):

        # Para a utilização do método withdraw(sacar), primeiro verifica-se se há balance(saldo) disponível. Será retornado o valor pós saque.
        postWithdrawalAmount = self.balance - value

        limit_max = -self.limit  # Limite da conta corrente

        # Caso o cliente possua um saldo baixo e um valor de saque acima, o valor do pós saque seria negativo,logo "-self.limit"
        if postWithdrawalAmount >= 0:
            self.balance -= value
            self.test(f'Valor do saque é {value:.2f}')
            return self.balance
        elif postWithdrawalAmount < 0:
            print(f'Limite utilizado: R$ {self.limit:.2f}. Saque confirmado.')
            return self.balance - limit_max

        # Caso entre na condição, não será executado por conta do return. Caso contrário, o print é executado.
        print(f'Não há limite disponível em sua conta corrente para saque')


if __name__ == "__main__":
    # sa1 = SavingsAccount(100, 200, 300)  # TESTE
    # sa1.withdraw(500)  # Negado
    # ca1 = CheckingAccount(100, 200, 300, 100)  # TESTE
    # ca1.withdraw(400)  # Limite ultizado, saldo -100
    # ca1.withdraw(200)  # Limite não disponível
    pass
