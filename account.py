from stellar_base.address import Address
from stellar_base.utils import AccountNotExistError


class Details:
    def __init__(self, address):
        self.address = address
        self.account = Address(address=self.address)
        try:
            self.account.get()
        except AccountNotExistError:
            self.account = None
            print('Account does not exist')

    @property
    def get(self):
        if self.account:
            print('Account ID:{}'.format(self.address))
            print('Balance:{}'.format(self.balance))
            print('Asset:{}'.format(self.asset))
            return self.address, self.balance, self.asset
        else:
            return None

    @property
    def balance(self):
        balance = 0
        try:
            balance = self.account.balances[0]['balance']
        except AttributeError:
            balance = None
        finally:
            return balance

    @property
    def asset(self):
        asset = None
        try:
            asset = self.account.balances[0]['asset_type']
            asset = 'XLM' if asset == 'native' else asset
        except AttributeError:
            asset = None
        finally:
            return asset
