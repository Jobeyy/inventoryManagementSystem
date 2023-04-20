import customtkinter
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import csv

# Themes: "blue" (standard), "green", "dark-blue"




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.createMainView()
        
    def createMainView(self):
        '''Dont change'''
        #Check if their username and password is already in the system
        # if it isnt, tell them to sign up. 
        # if it is then continue 

        
        
        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("green") 
        # sidebar Frame
        self.geometry("1100x580")
        self.title("Inventory Management System")
        '''Dont Change'''
        
        self.user_var = tk.StringVar()
        self.pass_var = tk.StringVar()
        # Main Frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.pack(side= "right", fill= "both", expand = True )
            
        self.login_frame = customtkinter.CTkFrame(self.main_frame, width = 320, height = 560, corner_radius = 15)
        self.login_frame.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)

        self.login_label = customtkinter.CTkLabel(self.login_frame, text = "Create Your account", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.place(x = 50, y = 45)

        self.username_entry = customtkinter.CTkEntry(self.login_frame, textvariable = self.user_var ,width = 220, placeholder_text = "Username")
        self.username_entry.place(x = 50, y = 110)

        self.password_entry = customtkinter.CTkEntry(self.login_frame, textvariable = self.pass_var, width = 220, placeholder_text="Password", show = "*")
        self.password_entry.place(x= 50, y= 165)

        self.login_button = customtkinter.CTkButton(self.login_frame, width = 220, text  = "Login", corner_radius= 6, command = self.Login)
        self.login_button.place(x = 50, y =290)

        self.sign_up_button = customtkinter.CTkButton(self.login_frame, width = 220,  text = "Sign Up", corner_radius= 6, command = self.Signup)
        self.sign_up_button.place(x = 50, y = 240)
        

    def clear_frame(self, frame):
        for widgets in frame.winfo_children():
            widgets.destroy()
    
    def Login(self):
        self.userData = {}                      #empty dictionary
        with open('userData.csv') as f:         #open file userData.csv
            reader = csv.reader(f)              #cs.reader reads row, f is the file as stated
            for row in reader:                  #for each row in that file (read in rows)
                if len(row) >= 2:                              
                    self.userData[row[0]] = row[1]
        self.username = str(self.user_var.get())
        self.password = str(self.pass_var.get())

        if self.username in self.userData and self.userData[self.username] == self.password:
            self.sidebar_frame()
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    def Signup(self):
         #READ USER DATA
        self.userData = {}                      #empty dictionary
        with open('userData.csv') as f:         #open file userData.csv
            reader = csv.reader(f)              #cs.reader reads row, f is the file as stated
            for row in reader:                  #for each row in that file (read in rows)
                if len(row) >= 2:                              
                    self.userData[row[0]] = row[1]  #CREATES the dictionary based off what it's reading
            #f.close()
        self.username = str(self.user_var.get())
        self.password = str(self.pass_var.get())
        print("The name is : " + self.username)
        print("The password is : " + self.password)
        if self.username not in self.userData:
            
            self.userData[self.username] = self.password  # add the new user data to the dictionary

            # list of fieldnames for the CSV file
            fieldnames = ['username', 'password']

            # write the new user data to the CSV file
            with open('userData.csv', 'a', newline='') as csvfile:
                csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # write the new row to the CSV file
                csvwriter.writerow({'username': self.username, 'password': self.password})

            messagebox.showinfo("Success!", "You can now login!")

        else:
            messagebox.showerror("Error", "Username Has Been Taken")

        self.user_var.set("")
        self.pass_var.set("")

    def sidebar_frame(self):

        self.clear_frame(self.main_frame)

        customtkinter.set_default_color_theme("blue")
        self.sidebar_frame = customtkinter.CTkFrame(self, width = 150, corner_radius=0, border_color = "gray30", border_width = 1)
        self.sidebar_frame.pack(side = 'left', fill = 'y')

        # Sidebar stuff
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Inventory \n Managment \n System", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(padx = 20, pady = 20)

        #Sidebar Buttons
        self.product_button = customtkinter.CTkButton(self.sidebar_frame, text= "Products", command = self.sidebar_products_event).pack(pady = 10)
        #self.supplier_button = customtkinter.CTkButton(self.sidebar_frame, text= "Suppliers", command = self.sidebar_suppliers_event).pack(pady = 10)
        self.transaction_button = customtkinter.CTkButton(self.sidebar_frame, text = "Transactions",command = self.sidebar_transactions_event).pack(pady = 10)
        self.inventory_button = customtkinter.CTkButton(self.sidebar_frame, text = "Inventory", command = self.sidebar_inventory_event).pack(pady = 10)
        
        # Sidebar Appearance and Scaling
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w").pack(pady = 30)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"],command=self.change_appearance_mode_event).pack()
    
    

    def sidebar_products_event(self):
        self.clear_frame(self.main_frame)
        self.drinks_label = customtkinter.CTkLabel(self.main_frame, text = "Drinks",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.drinks_label.place(x = 170, y = 150)
        self.drinks_button = customtkinter.CTkButton(self.main_frame, text = "Drinks", width = 200, height =100, command = self.drinks_products)
        self.drinks_button.place(x = 100, y = 200) 
        self.snacks_label = customtkinter.CTkLabel(self.main_frame, text = "Snacks",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.snacks_label.place(x = 442, y = 150)
        self.snacks_button = customtkinter.CTkButton(self.main_frame, text = "Snacks", width = 200, height = 100, command = self.snack_products)
        self.snacks_button.place(x = 375, y = 200)
        self.items_label = customtkinter.CTkLabel(self.main_frame, text = "Items",font=customtkinter.CTkFont(size=20, weight="bold"))
        self.items_label.place(x= 725, y = 150)
        self.items_button = customtkinter.CTkButton(self.main_frame, text = "Items",width = 200, height = 100 )
        self.items_button.place(x = 650, y = 200)

    def drinks_products(self):
        self.clear_frame(self.main_frame)
        self.blue_gatorade = customtkinter.CTkButton(self.main_frame, text = "Blue Gatorade" , width = 200, height = 100)
        self.blue_gatorade.place(x = 100, y = 100)
        self.red_gatorade = customtkinter.CTkButton(self.main_frame, text = "Red Gatorade" , width = 200, height = 100)
        self.red_gatorade.place(x = 375, y = 100)
        self.yellow_gatorade = customtkinter.CTkButton(self.main_frame, text = "Yellow Gatorade", width = 200, height = 100)
        self.yellow_gatorade.place(x = 650, y = 100)

        self.muscle_milk = customtkinter.CTkButton(self.main_frame, text = "Muscle Milk", width = 200, height = 100)
        self.muscle_milk.place(x = 100 , y = 250)
        self.super_shake_chocolate = customtkinter.CTkButton(self.main_frame, text = "Super Shake Chocolate", width = 200, height = 100)
        self.super_shake_chocolate.place(x = 375 , y = 250)
        self.super_shake_vinilla = customtkinter.CTkButton(self.main_frame, text = "Muscle Milk", width = 200, height = 100)
        self.super_shake_vinilla.place(x = 650 , y = 250)

        self.water = customtkinter.CTkButton(self.main_frame, text = "Water", width = 200, height = 100).place(x = 100 , y = 400)
        self.rockstar = customtkinter.CTkButton(self.main_frame, text = "Rockstar", width = 200, height = 100).place(x = 375, y = 400)
        self.redbull = customtkinter.CTkButton(self.main_frame, text = "Redbull", width = 200, height = 100).place(x  = 650, y = 400)


    def snack_products(self):
        self.clear_frame(self.main_frame)
        self.quest_double_chocolate = customtkinter.CTkButton(self.main_frame, text = "Quest Double Chocolate" , width = 200, height = 100).place(x = 100, y = 100)
        self.quest_chocolate_chip = customtkinter.CTkButton(self.main_frame, text = "Quest Chocolate Chip" , width = 200, height = 100).place(x = 375, y = 100)
        self.quest_pb = customtkinter.CTkButton(self.main_frame, text = "Quest PB", width = 200, height = 100).place(x = 650, y = 100)
    
        self.gatorade_chocolate_chip = customtkinter.CTkButton(self.main_frame, text = "Protein Bar Chocolate Chip", width = 200, height = 100).place(x = 100 , y = 250)
        self.gatorade_pb = customtkinter.CTkButton(self.main_frame, text = "Protein Bar Peanut Butter", width = 200, height = 100).place(x = 375 , y = 250)
        self.gatorade_caramel = customtkinter.CTkButton(self.main_frame, text = "Protein Bar Caramel", width = 200, height = 100).place(x = 650 , y = 250)
    
        self.loaded_taco = customtkinter.CTkButton(self.main_frame, text = "Quest Loaded Taco", width = 200, height = 100).place(x = 100 , y = 400)
        self.chili_lime = customtkinter.CTkButton(self.main_frame, text = "Quest Chili Lime", width = 200, height = 100).place(x = 375, y = 400)
        self.ranch = customtkinter.CTkButton(self.main_frame, text = "Quest Ranch", width = 200, height = 100).place(x  = 650, y = 400)

    def item_products(self):
        self.clear_frame(self.main_frame)
        
    def inventory_button(self):
        self.clear_frame(self.main_frame)

        
        
        
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkComboBox(text="Type in a number:", title="CTkInputDialog")
        
        print("CTkInputDialog:", dialog.get_input())

    def sidebar_transactions_event(self):
        self.clear_frame(self.main_frame)
        self.textboxLabel = customtkinter.CTkLabel(self.main_frame, text = "Current Transactions", font=customtkinter.CTkFont(size=20, weight="bold")).pack(side = "top")
        self.textbox = customtkinter.CTkTextbox(self.main_frame, width = 500, height =500)
        self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.textbox.pack(side = "top")

    def sidebar_inventory_event(self):
        self.clear_frame(self.main_frame)
        
        self.tree = ttk.Treeview(self.main_frame)
        # Defining columns
        self.tree['columns'] = ("Product","Amount")

        #Formating columns
        self.tree.column("#0", width = 0, stretch = "NO")
        self.tree.column("Product", anchor = "w", width = 300)
        self.tree.column("Amount", anchor = "center", width = 300)

        # Creating Headings
        self.tree.heading("#0", text = "", anchor = "w")
        self.tree.heading("Product", text = "Product", anchor="w")
        self.tree.heading("Amount", text = "Amount", anchor= "center")

        #adding data
        with open('inventory.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            for i, row in enumerate(reader, start=1):
                self.tree.insert(parent='', index='end', iid=i, text='',
                                  values=(row[0], row[1]))

        self.tree.place(x = 150, y = 200)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    

if __name__ == "__main__":
    app = App()
    app.mainloop()





