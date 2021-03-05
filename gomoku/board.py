import tkinter as tk

class Board(tk.Frame):
  def __init__(self, master=None):
    super().__init__(master)
    self.master = master
    self.pack()

def main():
  root = tk.Tk()
  board = Board(master=root)
  board.mainloop()

if __name__ == '__main__':
  main()