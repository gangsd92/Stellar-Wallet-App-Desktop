from stellar_base.builder import Builder
from stellar_base.keypair import Keypair
import requests
"""Class does not work correctly. Needs to be debugged."""


class Create:
    """Create a new wallet.

    :param name: name of the user (Optional).
    :param amount: Amount to be deposited when the wallet is created.
    """
    def __init__(self, amount, name=None):
        self.name = name
        self.amount = amount
        self.keyPair = Keypair.random()
        self.publicKey = self.keyPair.address().decode()
        print(type(self.publicKey))
        self.secret = self.keyPair.seed().decode()
        self.builder = None
        self.url = 'https://horizon-testnet.stellar.org/'
        requests.get(self.url, params={'addr':self.publicKey})

    def create(self):
        self.builder = Builder(secret=self.secret, horizon='https://horizon-testnet.stellar.org')
        self.builder.append_create_account_op(destination=self.publicKey, starting_balance=20)
        """Error while signing the document."""
        self.builder.sign()
        self.builder.submit()


