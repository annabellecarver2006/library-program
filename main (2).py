##to do:
#error messages
#valueerrors
#putting the books into seperate self.masters so they can be displayed side by side
#figure out how the error messages are going to be done
#make the classes mor eefficient- one check out button with a drop down menu, one restock button with a drop out menu etc. 

#setting up
from tkinter import *

#Cart variables and making the cart variable changeable


#Class for the books
class Books:
  #initializing and setting up
  def __init__(self, master, title, author, stock):
    self.title = title
    self.author = author
    self._stock = stock
    self.master=master

    self.titletext = StringVar()
    self.titletext.set("Title: {}".format(self.title))

    self.stocktext = StringVar()
    self.stocktext.set("Stock: {}".format(self._stock))
    
    #labels for the title author and stock
    show_title = Label(self.master, textvariable = self.titletext)
    show_title.pack()
    show_author = Label(self.master, text="Author: {}".format(self.author))
    show_author.pack()
    show_stock = Label(self.master, textvariable= self.stocktext)
    show_stock.pack()

    button_1 = Button(self.master, text = "Check Out", command = lambda:self.check_out())
    button_1.pack()



  #function to create a button that lets the user check out a book
  def check_out(self):
    global error_text
    if self._stock >= 1:
      self._stock-=1
      self.stocktext.set("Stock: {}".format(self._stock))
      global cart
      global cart_text
      cart +=1
      cart_text.set("Checked Out: {}".format(cart))
      print (cart)
      error_text.set("checkout of '{}' successful".format(self.title))
    else: 
      self.stocktext.set("Out of stock!")
      error_text.set("checkout failed due to lack of stock")

  def restock_entry(self,frame):
    restock_label = Label(frame, text="Enter amount to restock")
    restock_label.pack()
    self.name_var = StringVar()
    self.name_var.set("")
    name_entry = Entry(frame, textvariable = self.name_var)
    name_entry.pack(padx=20)
    button_thing = Button(frame, text = "enter", command = lambda:self.enter_button())
    button_thing.pack()

  def enter_button(self):
    global error_text
    try:
      text = int(self.name_var.get())
      print(text)
      if self._stock+text <= 99:
        self._stock +=text
        self.stocktext.set("Stock: {}".format(self._stock))
        self.name_var.set("")
        error_text.set("restock successful!")
      else:
        print("restock failed")
        error_text.set("restock failed")
    except ValueError:
      print("enter a number pleadse")

root = Tk()
root.title("Library Books")
cart = 0
cart_text = StringVar()
cart_text.set("Checked Out: {}".format(cart))

error_text=StringVar()
error_text.set("")

cart_label = Label(root, textvariable = cart_text, font=("arial","11", "bold"))
cart_label.grid(row = 0, columnspan = 2, sticky=E+W)

error_label=Label(root, textvariable=error_text, fg = "red")
error_label.grid(row = 1, columnspan = 2, sticky=E+W)

frame_1=Frame(root)
frame_2=Frame(root)
b1 = Books(frame_1,"1984","George Orwell", 10)
frame_1.grid(row = 2, column =0)
frame_3=Frame(root)
restock_button=Button(root, text ="Restock", command = lambda:b1.restock_entry(frame_3))
restock_button.grid(row = 3, columnspan = 2, sticky = E+W, padx = 70)
frame_3.grid(row = 4, columnspan = 2, sticky=E+W)


b2 = Books(frame_2,"To Kill A Mockingbird", "I dunno", 90)
frame_2.grid(row = 2, column = 1)
root.mainloop()
