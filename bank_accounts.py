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
        self.text(f'Depositando...R$ {value}')

    # Método para fim de teste quando ao andamento do projeto
    def test(self, msg):
        print(f'Saldo é {self.balance:.2f} {msg}')


class SavingsAccount(BankAccount):
    def withdraw(self, value):

        # Para a utilização do método withdraw(sacar), primeiro verifica-se se há balance(saldo) disponível. Será retornado o valor pós saque.
        postWithdrawalAmount = self.balance - value

        if postWithdrawalAmount >= 0:
            self.balance -= value
            self.test(f'Valor do saque é {value:.2f}')
            return self.balance
        # Caso entre na condição, não será executado por conta do return. Caso contrário, o print é executado.
        print(f'Saque negado: R$ {value:.2f}. Confira o seu saldo em conta.')


if __name__ == "__main__":
    sa1 = SavingsAccount(100, 200, 300)  # TESTE
