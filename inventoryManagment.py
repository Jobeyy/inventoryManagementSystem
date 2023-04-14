import customtkinter
import tkinter as tk

from header import *

# Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue") 



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        
        self.geometry("1100x580")
        self.title("Inventory Management System")

        self.createMainView()

# Main Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(side= "right", fill= "both", expand = True )


        


        
       
        

        
        

    def createMainView(self):
        # sidebar Frame
        self.sidebar_frame = ctk.CTkFrame(self, width = 150, corner_radius=0, border_color = "gray30", border_width = 1)
        self.sidebar_frame.pack(side = 'left', fill = 'y')

        # Sidebar stuff
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Inventory \n Managment \n System", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx = 20, pady = 20)

        #Sidebar Buttons
        self.product_button = ctk.CTkButton(self.sidebar_frame, text= "Products", command = self.sidebar_products_event).pack(pady = 10)
        #self.supplier_button = ctk.CTkButton(self.sidebar_frame, text= "Suppliers", command = self.sidebar_suppliers_event).pack(pady = 10)
        self.transaction_button = ctk.CTkButton(self.sidebar_frame, text = "Transactions",command = self.sidebar_transactions_event).pack(pady = 10)
        self.inventory_button = ctk.CTkButton(self.sidebar_frame, text = "Inventory", command = self.sidebar_inventory_event).pack(pady = 10)
        
        # Sidebar Appearance and Scaling
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w").pack(pady = 30)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"],command=self.change_appearance_mode_event).pack()

    def authenticate(self):
        pass

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()

    def sidebar_products_event(self):
        self.clear_frame(self.main_frame)
        self.drinks_label = customtkinter.CTkLabel(self.main_frame, text = "Drinks",font=ctk.CTkFont(size=20, weight="bold"))
        self.drinks_label.place(x = 170, y = 150)
        self.drinks_button = customtkinter.CTkButton(self.main_frame, text = "Drinks", width = 200, height =100, command = self.drinks_products)
        self.drinks_button.place(x = 100, y = 200) 
        self.snacks_label = customtkinter.CTkLabel(self.main_frame, text = "Snacks",font=ctk.CTkFont(size=20, weight="bold"))
        self.snacks_label.place(x = 442, y = 150)
        self.snacks_button = customtkinter.CTkButton(self.main_frame, text = "Snacks", width = 200, height = 100)
        self.snacks_button.place(x = 375, y = 200)
        self.items_label = customtkinter.CTkLabel(self.main_frame, text = "Items",font=ctk.CTkFont(size=20, weight="bold"))
        self.items_label.place(x= 725, y = 150)
        self.items_button = customtkinter.CTkButton(self.main_frame, text = "Items",width = 200, height = 100 )
        self.items_button.place(x = 650, y = 200)
    def drinks_products(self):
        self.clear_frame(self.main_frame)
        self.blue_gatorade = customtkinter.CTkButton(self.main_frame, text = "Gatorade" )
        self.blue_gatorade.place(x = 500, y = 100)

    def sidebar_suppliers_event(self):
        self.clear_frame(self.main_frame)
        
        
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkComboBox(text="Type in a number:", title="CTkInputDialog")
        
        print("CTkInputDialog:", dialog.get_input())

    def sidebar_transactions_event(self):
        self.clear_frame(self.main_frame)
        self.textboxLabel = customtkinter.CTkLabel(self.main_frame, text = "Current Transactions", font=ctk.CTkFont(size=20, weight="bold")).pack(side = "top")
        self.textbox = customtkinter.CTkTextbox(self.main_frame, width = 500, height =500)
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.textbox.pack(side = "top")

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





