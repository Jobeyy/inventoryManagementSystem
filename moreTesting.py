import tkinter as tk

root = tk.Tk()

root.geometry(f"{1100}x{580}")
# create 4x4 grid
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)



sidebar_frame = tk.Frame()
sidebar_frame.grid(row = 0, column = 0, ipadx=20, ipady=20)

for i in range(4):
    for j in range(4):
        button = tk.Button(sidebar_frame, text = f"{i}{j}" ).grid(row = i, column = j, ipadx = 30, ipady =30, padx = 10, pady = 10)

#button_test = tk.Button(sidebar_frame, text = "placeholder")
#button_test.grid(row = 0,column= 1)
#button_test2 = tk.Button(sidebar_frame, text = "second text").grid(row = 2)





root.mainloop()
