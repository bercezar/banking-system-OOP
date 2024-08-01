import bank_accounts
import people
from datetime import date


class Bank:
    def __init__(
        self,
        # Cada atributo é uma lista de inteiros, sendo também cada atributo -> None como opcional
        # Valor padrão
        agencies: list[int] | None = None,
        clients: list[people.Person] | None = None,
        num_accounts: list[bank_accounts.BankAccount] | None = None

        # Sem valor padrão -> Instanciando: bank = Bank(agencies=None, clients=None, num_accounts=None)
        # agencies: list[int] | None,
        # clients: list[people.Person] | None,
        # num_accounts: list[bank_accounts.BankAccount] | None
    ):
        # Para cada valor de atributo, caso não seja None, é uma lista de inteiro. Porém caso seja None, é uma lista vazia
        self.agencies = agencies or []
        self.clients = clients or []
        self.num_accounts = num_accounts or []

    def check_client(self, client):
        if client in self.clients:
            return True
        return False

    def check_agency(self, agency):
        if agency in self.agencies:
            return True
        return False

    def check_bank_account(self, bank_account):
        if bank_account in bank_accounts:
            return True
        return False

    def authentication(self, bank_account, client, agency):
        return self.check_agency(agency) and self.check_bank_account(bank_account) and self.check_client(client)

    def __repr__(self):
        try:
            class_name = type(self).__name__
            attrs = f'({self.agencies}, {self.num_accounts}, {
                self.clients})'
            return f'{class_name}{attrs}'
        except AttributeError:
            return f'Cliente não possui convênio'


cl1 = people.Client("Bernardo", date(2000, 12, 18))  # Teste
cl1.account = bank_accounts.CheckingAccount(200, 300, 500, 100)

cl2 = people.Client("Rael", date(2024, 1, 26))  # Teste
cl2.account = bank_accounts.SavingsAccount(100, 500, 500)

bank = Bank()
bank.clients.extend([cl1.account, cl2.account])
print(bank)
