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
    def text(self, msg):
        print(f'Saldo é {self.saldo:.2f} {msg}')
