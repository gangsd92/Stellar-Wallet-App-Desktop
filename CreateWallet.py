from stellar_base.builder import Builder
from stellar_base.keypair import Keypair
import requests


class CreateWallet:
    def __init__(self, name, amount):
        self.name = name
        self.keyPair = Keypair.random()
        self.publicKey = self.keyPair.address().decode()
        print(type(self.publicKey))
        self.secret = self.keyPair.seed().decode()
        self.builder = None
        self.amount = amount
        self.url = 'https://horizon-testnet.stellar.org/'
        requests.get(self.url, params={'addr':self.publicKey})

    def create(self):
        self.builder = Builder(secret=self.secret, horizon='https://horizon-testnet.stellar.org')
        self.builder.append_create_account_op(destination=self.publicKey, starting_balance=20)
        self.builder.sign()
        self.builder.submit()


