from stellar_base.builder import Builder


class Build:

    def __init__(self, sender, receiver, amount=0, text_memo=None):
        self.text_memo = text_memo
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.builder = None

    def send(self):
        self.builder = Builder(secret=self.sender, horizon='https://horizon-testnet.stellar.org')
        self.builder.append_payment_op(self.receiver, self.amount)
        self.builder.add_text_memo('Hello world!')
        self.builder.sign()
        self.builder.submit()
