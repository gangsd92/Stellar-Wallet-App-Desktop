import TransactionBuilder
import AccountDetails
import CreateWallet
import tkinter


class App:
    def __init__(self, master):
        master.title('Stellar Wallet')
        self.welcome = tkinter.Label(master=master, text='Welcome')
        self.enter_name_label = tkinter.Label(master=master, text='Enter your name to create a wallet')
        self.enter_address_label = tkinter.Label(master=master, text='Enter an existing address')
        self.enter_name_entry = tkinter.Entry(master=master)
        self.enter_address_entry = tkinter.Entry(master=master)
        self.welcome.pack()
        self.enter_name_label.pack()
        self.enter_name_entry.pack()
        self.enter_address_label.pack()
        self.enter_address_entry.pack()


if __name__ == '__main__':
    root = tkinter.Tk()
    App(root)
    root.mainloop()
    #FROM_ADDRESS = 'GBCKQLHFUZF36FIJUKUW37YFQG5O5MXT3YB2M7ZGVBORLUZMPIITWHZI'
    #FROM_SECRET = 'SAKM5BVR5OK75VAC4YCUXD4YLPIJEV7WIUY6WJUXNZF6LCJ3CGYD6WU2'
    #TO_ADDRESS = 'GAATZTOYFZSLGKM6BUTXNWMIWUETMEK74VBJNEPRGB5WW3ELVTKBWNGN'
    #TO_SECRET = 'SB6VNSXJO5FI7ATVP5XEGSUXOU7GFIAM5RDX7C774RXSJGNU2H3TLRG3'
    #AMOUNT = 10

    #CreateWallet.CreateWallet('Bob', 20)
    #transaction = TransactionBuilder.TransactionBuilder(FROM_SECRET, TO_ADDRESS, AMOUNT)
    #transaction.send()
    #AccountDetails.AccountDetails('GAATZTOYFZSLGKM6BUTXNWMIWUETMEK74VBJNEPRGB5WW3ELVTKBWNGN')
    #AccountDetails.AccountDetails('GBCKQLHFUZF36FIJUKUW37YFQG5O5MXT3YB2M7ZGVBORLUZMPIITWHZI')

