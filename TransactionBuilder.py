from stellar_base.builder import Builder


class TransactionBuilder:

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

    #Name:Ashwin
    #// Secret:SAKM5BVR5OK75VAC4YCUXD4YLPIJEV7WIUY6WJUXNZF6LCJ3CGYD6WU2
    #// Account ID:GBCKQLHFUZF36FIJUKUW37YFQG5O5MXT3YB2M7ZGVBORLUZMPIITWHZI

    #//Name:Bala
    #//Secret:SB6VNSXJO5FI7ATVP5XEGSUXOU7GFIAM5RDX7C774RXSJGNU2H3TLRG3
    #//Account ID:GAATZTOYFZSLGKM6BUTXNWMIWUETMEK74VBJNEPRGB5WW3ELVTKBWNGN

    #BOB
    #Public Key:GBXS7QVUGYU4BQP2RVNYKSMEYQ5LTF5OXWSZDA6L6N4FO4ZX4BF2EBAJ
    #Secret:SCT6MF6XKEPG7L5A575WQXZYKEXXFEQA2RBIZVERFZK2HLXTRLE4PMDK