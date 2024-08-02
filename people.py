import bank_accounts
from datetime import date


class Person:
    def __init__(self, name, date_of_birth):
        self._name = name
        self._date_of_birth = date_of_birth

    # Getter e Setter para o acesso e definição do nome e data de aniversário
    # Garantir que o acesso e modificação sejam controlados

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def date_of_birth(self):
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        self._date_of_birth = date_of_birth

    def __repr__(self):
        try:
            class_name = type(self).__name__
            attrs = f'({self.name}, {self.formatted_date_of_birth()})'
            return f'{class_name}{attrs}'
        except AttributeError:
            return f'Error {type(self).__name__}'

    # Método para formatação da data
    def formatted_date_of_birth(self):
        return self.date_of_birth.strftime("%d/%m/%Y")


class Client(Person):
    def __init__(self, name, date_of_birth):
        super().__init__(name, date_of_birth)

        # Armazenar a conta bancária do cliente.
        self.account: bank_accounts.BankAccount | None = None


if __name__ == "__main__":
    # cl1 = Client("Bernardo", date(2000, 12, 18))  # Teste
    # cl1.account = bank_accounts.CheckingAccount(200, 300, 500, 100)
    # cl1.account.withdraw(200)
    # print(cl1)
    # print(cl1.account)

    # cl2 = Client("Rael", date(2024, 1, 26))  # Teste
    # cl2.account = bank_accounts.SavingsAccount(100, 500, 500)
    # cl2.account.withdraw(200)
    # print(cl2)
    # print(cl2.account)
    pass
