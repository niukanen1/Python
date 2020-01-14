from tkinter import *
class student:   
   
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def pr (self):
        win = Tk()
        win.geometry('450x400')
        win.title('Окошечко')
        l = Label(win, text ='Ответ: {}'.format(self.x * self.y), font = ('Arial Bold', 50))
        l.grid(column = 0, row = 0)
        win.mainloop()

a = int(input('a ' ))
b = int(input('b ' ))        
sum1 = student(a,b)
sum1.pr()

        
        



