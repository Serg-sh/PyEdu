import tkinter as tk

root = tk.Tk()

root.title('Test Window')
root.geometry('1020x620')
root.resizable(False, False)
canvas = tk.Canvas(root, width=1020, height=620, bg='#002')
# линии по вертикали
for y in range(21):
    k = 50 * y
    canvas.create_line(10 + k, 610, 10 + k, 10, width=1, fill='#191938')
# линии по горизонтали
for x in range(13):
    k = 50 * x
    canvas.create_line(10, 10 + k, 1010, 10+k, width=1, fill='#191938')


canvas.create_line(10, 10, 10, 610, width=1, arrow=tk.FIRST, fill='white')
canvas.create_line(0, 310, 1010, 310, width=1, arrow=tk.LAST, fill='white')



canvas.pack()

root.mainloop()
