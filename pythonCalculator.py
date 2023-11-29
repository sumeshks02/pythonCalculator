from tkinter import *

window = Tk()
window.title("Calculator")
window.geometry("570x600+250+100")
window.resizable(False, False)
window.config(bg='light blue')

text= Text(window,
           width=25,
           height=2,

           font=("arial",30))
display_label = Label(window,
                      width=31,
                      height=2,
                      text="",
                      font=("arial", 30),
                      bg="gray")
#text.pack()
display_label.pack()
Button(window, text='C', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=10, y=100)
Button(window, text='/', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=150, y=100)
Button(window, text='%', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=290, y=100)
Button(window, text='x', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=430, y=100)

Button(window, text='7', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=10, y=200)
Button(window, text='8', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=150, y=200)
Button(window, text='9', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=290, y=200)
Button(window, text='-', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=430, y=200)

Button(window, text='4', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=10, y=300)
Button(window, text='5', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=150, y=300)
Button(window, text='6', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=290, y=300)
Button(window, text='+', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=430, y=300)

Button(window, text='1', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=10, y=400)
Button(window, text='2', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=150, y=400)
Button(window, text='3', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=290, y=400)
Button(window, text='0', width=13, height=1, font=("arial", 30, "bold"), bd=1).place(x=10, y=500)

Button(window,text='.', width=5, height=1, font=("arial", 30, "bold"), bd=1).place(x=290, y=500)

Button(window,text='=', width=5, height=4, font=("arial", 30, "bold"), bd=1).place(x=430, y=400)

window.mainloop()
