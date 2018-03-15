from stellar_base.builder import Builder
from account import Details


class Build:
    """Creates a transaction between the sender and receiver.

    :param: sender: Account that sends the money (seed).
    :param: receiver: Account that receives the money (Account ID).
    :param: amount: Amount that needs to be sent.
    """
    def __init__(self, sender, receiver, amount=0):
        self.sender, self.receiver, self.amount = sender, receiver, amount
        self.builder = None

    def send(self):
        """Text Memo needs to be added."""
        if self.check_account_validity:
            self.builder = Builder(secret=self.sender, horizon='https://horizon-testnet.stellar.org')
            self.builder.append_payment_op(self.receiver, self.amount)
            self.builder.sign()
            self.builder.submit()
            return True
        return False

    @property
    def check_account_validity(self):
        return Details(self.receiver).check
