import tkinter as tk

root = tk.Tk()

root.geometry(f"{1100}x{580}")
# create 4x4 grid
for i in range(4):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# create 16 labels and place them in the grid
sidebar_frame = tk.Frame()
sidebar_frame.grid(row = 0, column = 0)

button_test = tk.Button(sidebar_frame, text = "placeholder")
button_test.grid(row = 0)
button_test2 = tk.Button(sidebar_frame, text = "second text").grid(row = 2)

root.mainloop()
