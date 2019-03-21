import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")


def calc(key):
    global memory
    if key == "=":
        str1 = "1234567890.+-*/"
        if calcEntry.get()[0] not in str1:
            calcEntry.insert(tk.END, 'Error')
        try:
            result = eval(calcEntry.get())
            calcEntry.insert(tk.END, " = " + str(result))
        except:
            calcEntry.insert(tk.END, "Error")

    elif key == "C":
        calcEntry.delete(0, tk.END)

    elif key == "+/-":
        if "=" in calcEntry.get():
            calcEntry.delete(0, tk.END)
    else:
        if "=" in calcEntry.get():
            calcEntry.delete(0, tk.END)
        calcEntry.insert(tk.END, key)


btnList = [
    "7", "8", "9", "+", "-",
    "4", "5", "6", "*", "/",
    "1", "2", "3", "+/-", "=",
    "0", ".", "C", "", ""
]
row = 1
col = 0

for i in btnList:
    rel = ""
    cmd = lambda x=i: calc(x)
    tk.Button(root, text=i, command=cmd, width=5).grid(row=row, column=col)
    col += 1
    if col > 4:
        col = 0
        row += 1

calcEntry = tk.Entry(root, width=40)
calcEntry.grid(row=0, column=0, columnspan=5)
i = tk.IntVar()

calcEntry1 = tk.Checkbutton(root, variable=i, command=lambda x=i: print(x.get()))
calcEntry1.grid(row=5)
calcEntry1.lift()

root.mainloop()
