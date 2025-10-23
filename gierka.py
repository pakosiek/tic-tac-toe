import tkinter as tk

root = tk.Tk()
root.geometry("500x500")
root.title("Kolko i krzyzyk")

label=tk.Label(root, text="Kolko i krzyzyk!", font=('Arial', 20))
label.pack(pady=30)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="", font=('Arial', 18), height=3)
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)


btn2 = tk.Button(buttonframe, text="", font=('Arial', 18), height=3)
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text="", font=('Arial', 18), height=3)
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonframe, text="", font=('Arial', 18), height=3)
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(buttonframe, text="", font=('Arial', 18), height=3)
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(buttonframe, text="", font=('Arial', 18), height=3)
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

btn7 = tk.Button(buttonframe, text="", font=('Arial', 18), height=3)
btn7.grid(row=2, column=0, sticky=tk.W + tk.E)

btn8 = tk.Button(buttonframe, text="", font=('Arial', 18), height=3)
btn8.grid(row=2, column=1, sticky=tk.W + tk.E)

btn9 = tk.Button(buttonframe, text="", font=('Arial', 18), height=3)
btn9.grid(row=2, column=2, sticky=tk.W + tk.E)

buttonframe.pack(fill='x')
root.mainloop()