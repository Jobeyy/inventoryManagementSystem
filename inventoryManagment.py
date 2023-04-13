import customtkinter
from header import *

# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue") 


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Inventory Managment System")
        self.geometry(f"{1100}x{580}")

 

        self.geometry("1100x580")
        self.title("Inventory Management System")
#sidebar Framef
        self.sidebar_frame = ctk.CTkFrame(self, width = 150, corner_radius=0)
        self.sidebar_frame.pack(side = 'left', fill = 'y')

# Main Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(side= "right", fill= "both", expand = True )

# Sidebar stuff
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Inventory \n Managment \n System", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx = 20, pady = 20)

#Sidebar Buttons
        self.product_button = ctk.CTkButton(self.sidebar_frame, text= "Products", command = self.sidebar_products_event).pack(pady = 10)
        self.supplier_button = ctk.CTkButton(self.sidebar_frame, text= "Suppliers", command = self.sidebar_suppliers_event).pack(pady = 10)
        self.transaction_button = ctk.CTkButton(self.sidebar_frame, text = "Transactions",command = self.sidebar_transactions_event).pack(pady = 10)
        self.inventory_button = ctk.CTkButton(self.sidebar_frame, text = "Inventory", command = self.sidebar_inventory_event).pack(pady = 10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w").pack()
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"],command=self.change_appearance_mode_event).pack()
        
        
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w").pack()
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["100%", "110%", "120%", "90%", "80%"],command=self.change_scaling_event).pack()
        

        
    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def sidebar_products_event(self):
        self.clear_frame(self.main_frame)
        self.entry = customtkinter.CTkEntry(self.main_frame, placeholder_text="Enter new product")
        self.entry.pack()

    def sidebar_suppliers_event(self):
        self.clear_frame(self.main_frame)
        
        self.button = customtkinter.CTkButton(self.main_frame, text = "Test")
        self.button.pack()
        self.entry = customtkinter.CTkEntry(self.main_frame, placeholder_text="CTkEntry")
        self.entry.pack()


    def sidebar_transactions_event(self):
        self.clear_frame(self.main_frame)
       

    def sidebar_inventory_event(self):
        self.clear_frame(self.main_frame)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()





