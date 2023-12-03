import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.geometry("570x490+250+100")
window.resizable(False, False)
window.config(bg='#808080')

value = ""


def click(event):
    global value
    value += event
    display_label.config(text=value)


def clear():
    global value
    value = ""
    display_label.config(text=value)


def calculate():
    global value
    result = ""
    if value != "":
        try:
            result = eval(value)
        except:
            result = "Problem not valued"
            value = ""
    display_label.config(text=result)


display_label = tk.Label(window,
                         width=20,
                         height=2,
                         anchor="center",
                         justify="right",
                         font=("arial", 45,),
                         fg="white",
                         bg="#3d423e",)
display_label.pack()
display_label.place(x=17, y=10)
tk.Button(window, text='C', width=5, height=1, font=("arial", 30, "bold"), bd=1,
          command=lambda: clear()).place(x=20,
                                         y=140)
tk.Button(window, text='%', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("%")).place(
    x=155,
    y=140)
tk.Button(window, text='÷', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("/")).place(
    x=295,
    y=140)
tk.Button(window, text='x', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("*")).place(
    x=430,
    y=140)

tk.Button(window, text='7', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("7")).place(x=20,
                                                                                                                   y=210)
tk.Button(window, text='8', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("8")).place(
    x=155,
    y=210)
tk.Button(window, text='9', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("9")).place(
    x=295,
    y=210)
tk.Button(window, text='-', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("-")).place(
    x=430,
    y=210)

tk.Button(window, text='4', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("4")).place(x=20,
                                                                                                                   y=280)
tk.Button(window, text='5', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("5")).place(
    x=155,
    y=280)
tk.Button(window, text='6', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("6")).place(
    x=295,
    y=280)
tk.Button(window, text='+', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("+")).place(
    x=430,
    y=280)

tk.Button(window, text='1', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("1")).place(x=20,
                                                                                                                   y=350)
tk.Button(window, text='2', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("2")).place(
    x=155,
    y=350)
tk.Button(window, text='3', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("3")).place(
    x=295,
    y=350)
tk.Button(window, text='0', width=13, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click("0")).place(
    x=20,
    y=420)

tk.Button(window, text='.', width=5, height=1, font=("arial", 30, "bold"), bd=1, command=lambda: click(".")).place(
    x=290,
    y=420)

tk.Button(window, text='=', width=5, height=3, font=("arial", 30, "bold"), bd=1, command=lambda: calculate()).place(
    x=430,
    y=350)

window.mainloop()
