from header import *
from tkinter import ttk
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Inventory Managemnet System")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.sidebar_width = 140
        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=self.sidebar_width, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        # create frame for main area
        self.main_frame = customtkinter.CTkFrame(self, width = 1100 - self.sidebar_width, height = 580)
        self.main_frame.grid(row = 0, column = 1, columnspan = 3, rowspan =4)


        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Inventory \n Managment \n System", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text= "Products", command=self.sidebar_products_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text= "Suppliers", command=self.sidebar_suppliers_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text= "Transactions", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text= "Inventory", command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)



        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        '''self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        '''
       

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
      
       
       
    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text= "test", command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text= "2", command=self.sidebar_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text= "3", command=self.sidebar_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text= "4", command=self.sidebar_button_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)

    def sidebar_products_event(self):
        self.clear_frame(self.main_frame)
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter new product")
        self.entry.grid(row=0, column=1, columnspan = 1, padx=(20, 0), pady=(20,20))

    def sidebar_suppliers_event(self):
        self.button = customtkinter.CTkButton(self, text = "Test")
        self.button.grid(row=0, column=1, padx=10, pady=10)
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=0, column = 2, columnspan = 2, padx=10)


    def sidebar_transactions_event(self):
        pass

    def sidebar_inventory_event(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()