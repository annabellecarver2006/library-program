##to do:
#error messages
#valueerrors
#putting the books into seperate frames so they can be displayed side by side
#figure out how the error messages are going to be done


#setting up
from tkinter import *
import _tkinter
root = Tk()
root.title("Library Books")

#Cart variables and making the cart variable changeable
cart = 0
cart_text = StringVar()
cart_text.set("Checked Out: {}".format(cart))

error_text=StringVar()
error_text.set("")

#Class for the books
class Books:
  #initializing and setting up
  def __init__(self, title, author, stock):
    self.title = title
    self.author = author
    self._stock = stock

    self.titletext = StringVar()
    self.titletext.set("Title: {}".format(self.title))

    self.stocktext = StringVar()
    self.stocktext.set("Stock: {}".format(self._stock))
    #labels for the title author and stock
    show_title = Label(root, textvariable = self.titletext)
    show_title.pack()
    show_author = Label(root, text="Author: {}".format(self.author))
    show_author.pack()
    show_stock = Label(root, textvariable= self.stocktext)
    show_stock.pack()

  #function to create a button that lets the user check out a book
  def check_out_button(self):
    #the command
    def check_out():
      if self._stock >= 1:
        self._stock-=1
        self.stocktext.set("Stock: {}".format(self._stock))
        global cart
        global cart_text
        cart +=1
        cart_text.set("Checked Out: {}".format(cart))
        print (cart)
      else: 
        self.stocktext.set("Out of stock!")
    #the button
    button_1 = Button(root, text = "Check Out", command = lambda:check_out())
    button_1.pack()

  def restock_button(self):
    def restock():
      if self._stock <= 99:
        self._stock +=1
        self.stocktext.set("Stock: {}".format(self._stock))
      else:
        self.stocktext.set("Stock limit reached")
    button_2 =Button(root, text="Restock", command = lambda:restock())
    button_2.pack()

  def restock_entry(self):
    restock_label = Label(root, text="Enter amount to restock")
    restock_label.pack()
    name_var = IntVar()
    name_var.set("")
    name_entry = Entry(root, textvariable = name_var)
    name_entry.pack(padx=20)
    def button_command():
      global error_text
      text = int(name_var.get())
      print(text)
      try:
        if self._stock+text <= 99:
          self._stock +=text
          self.stocktext.set("Stock: {}".format(self._stock))
          name_var.set("")
          error_text.set("restock successful!")
        else:
          print("restock failed")
          error_text.set("restock failed")
      except _tkinter.TclError:
        error_text.set("error: please enter a number")
    button_thing = Button(root, text = "enter", command = lambda:button_command())
    button_thing.pack()

cart_label = Label(root, textvariable = cart_text, font=("arial","11", "bold"))
cart_label.pack()

error_label=Label(root, textvariable=error_text, fg = "red")
error_label.pack()

b1 = Books("1984","George Orwell", 10)
b1.check_out_button()
b1.restock_entry()

b2 = Books("To Kill A Mockingbird", "I dunno", 90)
b2.check_out_button()
b2.restock_entry()
root.mainloop()