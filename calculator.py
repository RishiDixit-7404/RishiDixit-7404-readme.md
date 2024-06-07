from tkinter import *

root = Tk()
root.geometry("470x800")
root.resizable(False, False)
root.title("Calculator")

a = StringVar()
answer_displayed = False  # Flag to check if the answer is displayed

entry = Entry(root, textvariable=a, borderwidth=10, width=13, font="helvetica 50 bold", fg="grey", bg="black", justify="right") 
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")  

def show(op):
    global answer_displayed
    current_content = a.get()
    if current_content == "Error" or answer_displayed:
        a.set(op)
        answer_displayed = False
    elif op == "⌫":
        if answer_displayed:
            a.set("")
            answer_displayed = False
        else:
            a.set(current_content[:-1])
    else:
        a.set(current_content + op)
    
    
def eql():
    global answer_displayed
    try:
        exp = a.get()
        exp = exp.replace('^', '**').replace('x', '*').replace('÷', '/')
        result = eval(exp)
        a.set(result)
        answer_displayed = True
    except ZeroDivisionError:
        a.set("Cannot divide by zero")
        answer_displayed = True
    except SyntaxError:
        a.set("Invalid expression")
        answer_displayed = True
    except Exception as e:
        a.set("Error")
        answer_displayed = True

def clr():
    a.set("")
    global answer_displayed
    answer_displayed = False

buttons = [
    ('C', 1, 0), ('⌫', 1, 1), ('%', 1, 2), ('/', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('x', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('00', 5, 1),('.', 5, 2),('=', 5, 3)
]

for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, font="helvetica 35 bold", command=eql, bg="gray", padx=25, pady=20, bd=5).grid(row=row, column=col, sticky=N+S+E+W)
    elif text == "C":
        Button(root, text=text, font="helvetica 35 bold", command=clr, bg="gray", padx=25, pady=20, bd=5).grid(row=row, column=col, sticky=N+S+E+W)
    else:
        Button(root, text=text, font="helvetica 35 bold", command=lambda t=text: show(t), bg="yellow" if text.isdigit() else "lavender", padx=25, pady=20, bd=5).grid(row=row, column=col, sticky=N+S+E+W)

for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    for j in range(4):
        root.grid_columnconfigure(j, weight=1)

root.mainloop()
