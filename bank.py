import bank_accounts
import people
from datetime import date


class Bank:
    def __init__(
        self,
        # Cada atributo é uma lista de inteiros, sendo também cada atributo -> None como opcional
        # Valor padrão
        agencies: list[int] | None = None,
        accounts: list[bank_accounts.BankAccount] | None = None,
        clients: list[people.Person] | None = None

        # Sem valor padrão -> Instanciando: bank = Bank(agencies=None, clients=None, accounts=None)
        # agencies: list[int] | None,
        # clients: list[people.Person] | None,
        # accounts: list[bank_accounts.BankAccount] | None
    ):
        # Para cada valor de atributo, caso não seja None, é uma lista de inteiro. Porém caso seja None, é uma lista vazia
        self.agencies = agencies or []
        self.accounts = accounts or []
        self.clients = clients or []

    def check_client(self, client):
        return client in self.clients

    # Método check_agency faz parte da verificação da conta bancária
    def check_agency(self, bank_account):
        return bank_account.agency in self.agencies

    def check_account(self, bank_account):
        return bank_account in self.accounts

    def is_account_for_client(self, bank_account, client):
        # Verifica se a conta do cliente é a conta fornecida
        return bank_account is client.account

    # Método check_agency faz parte da verificação da conta bancária

    def authentication(self, bank_account: bank_accounts.BankAccount, client: people.Person):
        return (self.check_agency(bank_account) and
                self.check_account(bank_account) and
                self.check_client(client) and
                self.is_account_for_client(bank_account, client))

    def __repr__(self):
        try:
            class_name = type(self).__name__
            attrs = f'({self.agencies}, {self.accounts}, {self.clients})'
            return f'{class_name}{attrs}'
        except AttributeError:
            return 'Error'


# Teste
if __name__ == "__main__":
    bank = Bank()
    bank.agencies = [300, 800, 100, 200]

    cl1 = people.Client("Bernardo", date(2000, 12, 18))
    cl1.account = bank_accounts.CheckingAccount(200, 300, 500, 100)

    cl2 = people.Client("Rael", date(2024, 1, 26))
    cl2.account = bank_accounts.SavingsAccount(100, 500, 200)

    bank.clients.extend([cl1, cl2])
    bank.accounts.extend([cl1.account, cl2.account])

    print(bank.authentication(cl1.account, cl1))  # Esperado: True
    print(bank.authentication(cl2.account, cl2))  # Esperado: True

    # if (bank.authentication(cl2.account, cl2)):
    #     cl2.account.deposit(300)
    #     print(cl2.account)
