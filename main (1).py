from tkinter import *

######################## BOOKINFO CLASS ##########################
class BookInfo:
  def __init__(self, master, title, author, stock):
    #Setting up the variables
    self.title = title
    self.author = author
    self.stock = stock
    self.master = master
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

####################### FUNCTIONS+OTHER ###########################
def create_title_list():
  title_list=[]
  for book in book_list:
    book_list.append(book.title)
  return title_list


# Variables and lists setup
book_list = []
cart = 0

######################## GUI #####################################
root = Tk()
root.title("Annie's Library")

cart_text=StringVar()
cart_text.set:("Checked_out: 0")

book_1 = BookInfo(root, "1984", "George Orwell", 10)
book_2 = BookInfo(root, "to kill a mockingbird", "Dunno", 10)
book_3=BookInfo(root, "Harry Potter", "J.K Rowling", 50)

cart_label=Label(root, textvariable= cart_text)
cart_label.grid()

for book in book_list:
    show_title = Label(root, text="Title: {}".format(book.title))
    show_title.grid()
    show_author = Label(root, text="Author: {}\n".format(book.author))
    show_author.grid()
    cart_button=Button(root, text="Check Out", command=lambda:book.check_out() )
    cart_button.grid()
root.mainloop()