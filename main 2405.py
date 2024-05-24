#note: using lists for the thingy restocking.
#like so that theres a name list with the titles automatically added
#and then option 1 is name_list[1], which corresponds to book_list[1]. so then it updates the GUI only for book_list[1]
#so like gui_to_update=bookinfogui(root, book_list[name_list_selection])
#then run gui_to_update.update_restock()
#yea hopefully that works. fingers crossed. 


from tkinter import *

######################## BOOKINFO CLASS ##########################
class BookInfo:
  def __init__(self, title, author, stock):
    #Setting up the variables
    self.title = title
    self.author = author
    self.stock = stock
    book_list.append(self)

  def check_out(self):
    if self.stock >= 1:
      self.stock -= 1
      global cart
      global cart_text
      cart+=1
      cart_text.set("Checked Out: {}".format(cart))
      return True
    else:
      return False

  def restock(self):
    text = int(self.restock_var.get())
    print(text)
    if self.stock + text <= 99:
      self.stock += text
      return True
    else:
      return False

######################## GUI CLASS ###############################
class BookInfoGUI:
  def __init__(self, master, book):
    self.book=book
    self.master=master

    stocktext=StringVar()
    stocktext.set("Stock: {}".format(self.book.stock))
    
    show_title = Label(self.master, text ="Title: {}".format( self.book.title))
    show_title.pack()
    show_author = Label(self.master, text="Author: {}".format(self.book.author))
    show_author.pack()
    show_stock = Label(self.master, textvariable = stocktext)
    show_stock.pack()
    check_out_button=Button(self.master, text="Check Out", command=lambda:self.update_checkout(stocktext))
    check_out_button.pack()

  def update_checkout(self, stocktext):
    if self.book.check_out():
      print("Checkout Successful")
      stocktext.set("Stock: {}".format(self.book.stock))
    else:
      print("you FAILED!!!!!!!")

  def update_restock(self, stocktext):
    if self.book.restock():
      print("restock successful!")
      stocktext.set("Stock: {}".format(self.book.stock))
    else: 
      print ("restock FAILED")
    
class RestockEntryGUI:
  def __init__(self, master, book):
    self.book=book
    self.master=master


  


################## FUNCTIONS OUTSIDE THE CLASSES ###################

root = Tk()
root.title("Annie's Library")
book_list = []
cart=0

cart_text=StringVar()
cart_text.set("Checked out: 0")
cart_label=Label(root, textvariable= cart_text,font=("arial","11", "bold"))
cart_label.pack()

book_1 = BookInfo("1984", "George Orwell", 10)
book_2 = BookInfo("to kill a mockingbird", "Dunno", 10)
book_3=BookInfo("Harry Potter", "J.K Rowling", 50)


for book in book_list:
  BookInfoGUI(root, book)



root.mainloop()