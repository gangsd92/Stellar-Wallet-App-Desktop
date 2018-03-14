from stellar_base.address import Address


class Details:
    def __init__(self, address):
        self.address = address
        self.account = Address(address=self.address)
        self.account.get()

    def print_details(self):
        print('Balance:{}'.format(self.account.balances))
