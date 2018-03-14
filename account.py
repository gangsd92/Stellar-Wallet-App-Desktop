from stellar_base.address import Address


class Details:
    def __init__(self, address):
        self.address = address
        account = Address(address=self.address)
        account.get()
        print('Balance:{}'.format(account.balances))
        print('Payments:{}'.format(account.payments()))
