import tkinter as tk

def press(num):
    entry_text.set(entry_text.get()+str(num))

def equalpress():
    try:
        total = str(eval(entry_text.get()))
        entry_text.set(total)
    except:
        entry_text.set("Error")

def clear():
    entry_text.set("")

root = tk.Tk()
root.geometry("350x450")
root.title("Calcukator")
root.resizable(False,False)

entry_text = tk.StringVar()
entry = tk.Entry(root,textvariable=entry_text,font=("Arial",20),justify="right",bd=10,relief="sunken")
entry.grid(row=0,column=0,columnspan=4,pady=10)

buttons=[
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3)
]
for (text,row,col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Arial", 18), bg="lightgreen", command=equalpress)
    else:
        btn = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: press(t))
    btn.grid(row=row, column=col, ipadx=10, ipady=10, sticky="nsew")

clear_btn = tk.Button(root,text="C",font=("Arial",18),bg="tomato",command=clear)
clear_btn.grid(row=5,column=0,columnspan=4,ipadx=100,ipady=10,pady=10)

root.mainloop()