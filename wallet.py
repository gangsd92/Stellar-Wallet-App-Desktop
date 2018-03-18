from stellar_base.builder import Builder
from stellar_base.keypair import Keypair
import requests
"""Class does not work correctly. Needs to be debugged."""
import urllib3


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
        print(self.publicKey)
        self.secret = self.keyPair.seed().decode()
        self.builder = None
        self.url = 'https://friendbot.stellar.org'
        self.http = urllib3.PoolManager()

    def create(self):
                request = self.http.request('GET', '{}?addr={}'.format(self.url, self.publicKey))
                if request.status == 200:
                    return self.publicKey
                else:
                    return False
