"""This file lets the user check out and restock books in a library."""

from tkinter import *


# BOOKINFO CLASS
class BookInfo:
    """Represent info about a book."""

    def __init__(self, title, author, stock):
        """Initialize book title,  author and stock."""
        self.title = title
        self.author = author
        self.stock = stock
        book_list.append(self)

    def check_out(self):
        """Reduce the stock by one if the stock isn't at 0. Add to cart."""
        if self.stock >= 1:
            self.stock -= 1
            global cart
            global cart_text
            cart += 1
            cart_text.set("Checked Out: {}".format(cart))
            return True
        else:
            return False

    def restock(self):
        """Add the int the user inputs to the stock."""
        global name_var
        try:
            text = int(name_var.get())
            if self.stock + text <= 99 and text >= 0:
                self.stock += text
                return True
            else:
                return False
        except ValueError:
            return False


# GUI CLASS
class BookInfoGUI:
    """GUI to display the book info."""

    def __init__(self, master, book):
        """Set up the root as master and the book variable."""
        self.book = book
        self.master = master

        self.stocktext = StringVar()
        self.stocktext.set("Stock: {}".format(self.book.stock))

        show_title = Label(self.master, text="Title: {}".format(self.book.title))
        show_title.pack()
        show_author = Label(self.master, text="Author: {}".format(self.book.author))
        show_author.pack()
        show_stock = Label(self.master, textvariable=self.stocktext)
        show_stock.pack()
        check_out_button = Button(self.master, text="Check Out", command=lambda: self.update_checkout())
        check_out_button.pack()

    def update_checkout(self):
        """Update the GUI when a book is successfully checked out."""
        global notification_text
        if self.book.check_out():
            notification_text.set("Checkout Successful!")
            self.stocktext.set("Stock: {}".format(self.book.stock))
        else:
            notification_text.set("Checkout failed due to insufficient stock. ")

    def update_restock(self):
        """Update the GUI when a book is successfully restocked."""
        global notification_text
        if self.book.restock():
            notification_text.set("Restock Successful!")
            self.stocktext.set("Stock: {}".format(self.book.stock))
        else:
            notification_text.set("Restock failed. Make sure to enter a positive number."
"\n Keep in mind that stock cannot exceed 100 ")


# FUNCTIONS OUTSIDE THE CLASSES
def create_title_list():
    """Create a list of the book titles to be used in the dropdown menu."""
    title_list = []
    for book in book_list:
        title_list.append(book.title)
    return title_list


def enter_button_command():
    """Command for when the enter button is pressed,  to restock."""
    option_selection = active_string.get()
    if option_selection == create_title_list()[0]:
        gui_1.update_restock()
    elif option_selection == create_title_list()[1]:
        gui_2.update_restock()
    elif option_selection == create_title_list()[2]:
        gui_3.update_restock()
    else:
        notification_text.set("Please make sure to select a book before pressing enter")


def restock_entry():
    """Entry widget for restocking."""
    restock_label = Label(root, text="Enter amount to restock")
    global name_var
    name_var.set("")
    name_entry = Entry(root, textvariable=name_var)
    enter_button = Button(root, text="enter", command=lambda: enter_button_command())
    restock_label.pack()
    name_entry.pack(padx=20)
    enter_button.pack()

# GUI AND MAIN ROUTINE
root = Tk()

root.title("Annie's Library")
book_list = []
title_list = []
cart = 0
active_string = StringVar()
name_var = StringVar()

cart_text = StringVar()
cart_text.set("Checked out: 0")
cart_label = Label(root, textvariable=cart_text, font=("arial", "11", "bold"))
cart_label.pack()

notification_text = StringVar()
notification_text.set("")
notification_label = Label(root, textvariable=notification_text, fg=("red"))
notification_label.pack()

book_1 = BookInfo("1984", "George Orwell", 10)
book_2 = BookInfo("To Kill A Mockingbird", "Harper Lee", 15)
book_3 = BookInfo("Harry Potter", "J.K Rowling", 20)

gui_1 = BookInfoGUI(root, book_1)
gui_2 = BookInfoGUI(root, book_2)
gui_3 = BookInfoGUI(root, book_3)

options = create_title_list()
active_string.set("Pick a Book")
restock_option = OptionMenu(root, active_string, *options)
restock_option.pack()

restock_entry()

root.mainloop()
