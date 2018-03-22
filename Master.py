from transaction import Build
from account import Details
from tkinter import Tk
from interface.bootstrap import Bootstrap

ALICE = 'GBCKQLHFUZF36FIJUKUW37YFQG5O5MXT3YB2M7ZGVBORLUZMPIITWHZI'
ALICE_SEED = 'SAKM5BVR5OK75VAC4YCUXD4YLPIJEV7WIUY6WJUXNZF6LCJ3CGYD6WU2'
BOB = 'GAATZTOYFZSLGKM6BUTXNWMIWUETMEK74VBJNEPRGB5WW3ELVTKBWNGN'


if __name__ == '__main__':
    root = Tk()
    bootstrap = Bootstrap(parent=root)
    root.title('Stellar Wallet App')
    root.mainloop()
    """if Details(ALICE).check and Details(BOB).check:
        transaction = Build(sender=ALICE_SEED, receiver=BOB, amount=20)
        transaction.send()
        [account, address, balance, asset] = Details(ALICE).get
        print('Balance:{}'.format(balance))
        print('Address:{}'.format(address))
        print('---------------------------')
        [account, address, balance, asset] = Details(BOB).get
        print('Balance:{}'.format(balance))
        print('Address:{}'.format(address))
        print('---------------------------')"""
