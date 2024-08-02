import bank_accounts
from bank import Bank
import people
from datetime import date


if __name__ == "__main__":
    bank = Bank()
    bank.agencies = [300, 800, 100, 200]

    client1 = people.Client("Bernardo Cezar", date(2000, 12, 18))
    print(client1)  # Person(Bernardo Cezar, 18/12/2000)

    client1.account = bank_accounts.CheckingAccount(100, 200, 400, 500)
    # CheckingAccount(100, 200, 400, 500) -> agência, conta, saldo, limite
    print(client1.account)

    client1.account.withdraw(200)
    print(client1.account)
    # Saldo é 200.00 Valor do saque é 200.00
    # CheckingAccount(100, 200, 200, 500)

    client1.account.deposit(100)
    print(client1.account)
    # Saldo é 300.00 Depositado: R$ 100
    # CheckingAccount(100, 200, 300, 500)

    client2 = people.Client("Rael", date(2024, 1, 26))
    client2.account = bank_accounts.SavingsAccount(555, 500, 200)
    bank.clients.extend([client1, client2])
    bank.accounts.extend([client1.account, client2.account])

    print(bank.authentication(client1.account, client1))  # True
    print(bank.authentication(client2.account, client2))  # False

    print(bank.agencies)  # [300, 800, 100, 200]

    # [CheckingAccount(100, 200, 300, 500), SavingsAccount(555, 500, 200)]
    print(bank.accounts)

    # [Client(Bernardo Cezar, 18/12/2000), Client(Rael, 26/01/2024)]
    print(bank.clients)
