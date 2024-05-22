from tkinter import *

########################BOOKINFO CLASS##############################
class BookInfo:
  def __init__(self, master, title, author, stock):
    #Setting up the variables
    self.title=title
    self.author=author
    self.stock=stock
    self.master=master
    book_list.append(self)

  def check_out(self):
    if self.stock >= 1:
      self.stock-=1
      return True
    else: 
      return False


  def restock(self):
    text = int(self.restock_var.get())
    print(text)
    if self.stock+text <= 99:
      self.stock +=text
      return True
    else:
     return False
    
#######################FUNCTIONS####################################
