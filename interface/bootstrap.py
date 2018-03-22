from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Frame


class Bootstrap(Frame):
    def __init__(self, parent):
        self.parent = parent
        Frame.__init__(self, self.parent)
        self.address_entry().pack()
        self.login().pack()
        self.or_label().pack()
        self.create_new_wallet_button().pack()

    def or_label(self):
        return Label(self.parent, text='OR')

    def address_entry(self):
        return Entry(self.parent)

    def create_new_wallet_button(self):
        return Button(self.parent, text='Create A New Wallet')

    def login(self):
        return Button(self.parent, text='Login')