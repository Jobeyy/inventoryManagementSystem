import customtkinter
from customtkinter import CTkImage
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image
import csv
import datetime

# Themes: "blue" (standard), "green", "dark-blue"




class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.createMainView()
        






        
    def createMainView(self):
        
        #Check if their username and password is already in the system
        # if it isnt, tell them to sign up. 
        # if it is then continue 

        
        
        customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("green") 
        # sidebar Frame
        self.geometry("1100x580")
        self.title("Inventory Management System")
        
        
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
    
    def convert_image_to_photo(self, path : str):
        image = CTkImage(light_image= Image.open(path), dark_image= Image.open(path), size = (200, 100))
        return image

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
        self.items_button = customtkinter.CTkButton(self.main_frame, text = "Items",width = 200, height = 100, command = self.item_products)
        self.items_button.place(x = 650, y = 200)

    def drinks_products(self):
        self.clear_frame(self.main_frame)

        blue_gatorade_image  = self.convert_image_to_photo("static\\blueGatorade.png")
        self.blue_gatorade = customtkinter.CTkButton(self.main_frame,image = blue_gatorade_image, text = "", width = 200, height = 100, command= lambda: self.buy_or_sell("Blue Gatorade")).place(x = 100, y = 100)
        red_gatorade_image = self.convert_image_to_photo("static\\redGatorade.png")
        self.red_gatorade = customtkinter.CTkButton(self.main_frame, text = "", image = red_gatorade_image , width = 200, height = 100,command= lambda: self.buy_or_sell("Red Gatorade")).place(x = 375, y = 100)
        yellow_gatorade_image = self.convert_image_to_photo("static\\limeGatorade.png")
        self.yellow_gatorade = customtkinter.CTkButton(self.main_frame, text = "", image = yellow_gatorade_image, width = 200, height = 100, command= lambda: self.buy_or_sell("Yellow Gatorade")).place(x = 650, y = 100)
        muscle_milk_choc_image = self.convert_image_to_photo("static\\muscleMilk.png")
        self.muscle_milk_chocolate = customtkinter.CTkButton(self.main_frame, text = "",image = muscle_milk_choc_image, width = 200, height = 100, command= lambda: self.buy_or_sell("Muscle Milk Chocolate")).place(x = 100 , y = 250)
        super_shake_choc_image = self.convert_image_to_photo("static\\superShake.png")
        self.super_shake_chocolate = customtkinter.CTkButton(self.main_frame, text = "",image = super_shake_choc_image, width = 200, height = 100, command= lambda: self.buy_or_sell("Super Shake Chocolate")).place(x = 650 , y = 250)
        muscle_milk_vinil_image = self.convert_image_to_photo("static\\muscleVanilla.png")
        self.muscle_milk_vinilla = customtkinter.CTkButton(self.main_frame, text = "",image = muscle_milk_vinil_image, width = 200, height = 100, command= lambda: self.buy_or_sell("Muscle Milk Vanilla")).place(x = 375 , y = 250)
        water_image = self.convert_image_to_photo("static\\water.png")
        self.water = customtkinter.CTkButton(self.main_frame, text = "",image = water_image, width = 200, height = 100, command= lambda: self.buy_or_sell("Aquafina")).place(x = 100 , y = 400)
        rockstar_image = self.convert_image_to_photo("static\\rockstar.png")
        self.rockstar = customtkinter.CTkButton(self.main_frame, text = "", image = rockstar_image, width = 200, height = 100, command= lambda: self.buy_or_sell("Rockstar")).place(x = 375, y = 400)
        redbull_image = self.convert_image_to_photo("static\\redbull.png")
        self.redbull = customtkinter.CTkButton(self.main_frame, text = "",image = redbull_image, width = 200, height = 100, command= lambda: self.buy_or_sell("Redbull")).place(x  = 650, y = 400)


    def snack_products(self):
        self.clear_frame(self.main_frame)
        quest_double_chocolate = self.convert_image_to_photo("static\\questDC.png")
        self.quest_double_chocolate = customtkinter.CTkButton(self.main_frame, text = "", image = quest_double_chocolate , width = 200, height = 100, command= lambda: self.buy_or_sell("Quest Double Chocolate Cookie")).place(x = 100, y = 100)
        quest_cc_image = self.convert_image_to_photo("static\\questCC.png")
        self.quest_chocolate_chip = customtkinter.CTkButton(self.main_frame, text = "" ,image = quest_cc_image, width = 200, height = 100, command= lambda: self.buy_or_sell("Quest Chocolate Chip Cookie")).place(x = 375, y = 100)
        quest_pb_image = self.convert_image_to_photo("static\\questPB.png")
        self.quest_pb = customtkinter.CTkButton(self.main_frame, text = "",image = quest_pb_image, width = 200, height = 100, command= lambda: self.buy_or_sell("Quest Peanut Butter Cookie")).place(x = 650, y = 100)
        gatorade_cc_image = self.convert_image_to_photo("static\\gatoradeCC.png")
        self.gatorade_chocolate_chip = customtkinter.CTkButton(self.main_frame, text = "",image = gatorade_cc_image, width = 200, height = 100,command= lambda: self.buy_or_sell("Gatorade Protein Bar Chocolate Chip")).place(x = 100 , y = 250)
        gatorade_pb_image = self.convert_image_to_photo("static\\gatoradePB.png")
        self.gatorade_pb = customtkinter.CTkButton(self.main_frame, text = "", width = 200, image = gatorade_pb_image, height = 100, command= lambda: self.buy_or_sell("Gatorade Protein Bar Peanut Butter")).place(x = 375 , y = 250)
        gatorade_c_image = self.convert_image_to_photo("static\\gatoradeC.png")
        self.gatorade_caramel = customtkinter.CTkButton(self.main_frame, text = "",image = gatorade_c_image, width = 200, height = 100, command= lambda: self.buy_or_sell("Gatorade Protein Bar Caramel")).place(x = 650 , y = 250)
        loaded_taco = self.convert_image_to_photo("static\\questLoadedTaco.png")
        self.loaded_taco = customtkinter.CTkButton(self.main_frame, text = "", image = loaded_taco, width = 200, height = 100, command= lambda: self.buy_or_sell("Quest Loaded Taco Chips")).place(x = 100 , y = 400)
        chili_lime = self.convert_image_to_photo("static\\questChiliLime.png")
        self.chili_lime = customtkinter.CTkButton(self.main_frame, text = "", image = chili_lime, width = 200, height = 100, command= lambda: self.buy_or_sell("Quest Chili Lime Chips")).place(x = 375, y = 400)
        ranch = self.convert_image_to_photo("static\\questRanch.png")
        self.ranch = customtkinter.CTkButton(self.main_frame, text = "", image = ranch, width = 200, height = 100, command= lambda: self.buy_or_sell("Quest Ranch Chips")).place(x  = 650, y = 400)

    def item_products(self):
        self.clear_frame(self.main_frame)
        smallLock = self.convert_image_to_photo("static\\smallLock.png")
        self.small_combination_lock = customtkinter.CTkButton(self.main_frame, text = "", image = smallLock , width = 200, height = 100, command= lambda: self.buy_or_sell("Small Combination Lock") ).place(x = 100, y = 100)
        masterLock = self.convert_image_to_photo("static\\masterLock.png")
        self.master_combination_lock = customtkinter.CTkButton(self.main_frame, text = "",image = masterLock , width = 200, height = 100, command= lambda: self.buy_or_sell("Master Combination Lock")).place(x = 375, y = 100)
        handWraps = self.convert_image_to_photo("static\\handWrap.png")
        self.hand_wraps = customtkinter.CTkButton(self.main_frame, text = "",image = handWraps, width = 200, height = 100, command= lambda: self.buy_or_sell("Hand Wraps")).place(x = 650, y = 100) 
        shampoo = self.convert_image_to_photo("static\\travelSizeShampoo.png")
        self.travel_size_shampoo = customtkinter.CTkButton(self.main_frame, text = "",image = shampoo, width = 200, height = 100, command= lambda: self.buy_or_sell("Travel Size Shampoo")).place(x = 100 , y = 250)
        conditioner = self.convert_image_to_photo("static\\travelSizeConditioner.png")
        self.travel_size_conditioner = customtkinter.CTkButton(self.main_frame, text = "", image = conditioner, width = 200, height = 100, command= lambda: self.buy_or_sell("Travel Size Conditioner")).place(x = 375 , y = 250)
        racGoggles = self.convert_image_to_photo("static\\raqGoggles.png")
        self.racquetball_goggles =  customtkinter.CTkButton(self.main_frame, text = "",image = racGoggles, width = 200, height = 100, command= lambda: self.buy_or_sell("Racquetball Goggles")).place(x = 650 , y = 250)
        swimGoggles = self.convert_image_to_photo("static\\swimGoggles.png")
        self.swim_goggles = customtkinter.CTkButton(self.main_frame, text = "",image = swimGoggles, width = 200, height = 100,command= lambda: self.buy_or_sell("Swim Goggles")).place(x = 100 , y = 400)
        bottle = self.convert_image_to_photo("static\\gatoradeBottle.png")
        self.gatorade_bottle = customtkinter.CTkButton(self.main_frame, text = "", image = bottle, width = 200, height = 100, command= lambda: self.buy_or_sell("Gatorade Bottle")).place(x = 375, y = 400)
        towel = self.convert_image_to_photo("static\\gatoradeTowel.png")
        self.gatorade_towel = customtkinter.CTkButton(self.main_frame, text = "",image = towel, width = 200, height = 100, command= lambda: self.buy_or_sell("Gatorade Towel")).place(x  = 650, y = 400)
            
    def buy_or_sell(self, name: str):
        self.clear_frame(self.main_frame)
        buyText = "Number you want to buy:"
        sellText = "Number you want to sell:"
        self.buy_button = customtkinter.CTkButton(self.main_frame, width = 200, height = 100, text = "Add To Inventory", command = lambda: self.buy_button_dialog_event(name, buyText)).place(x =150, y = 250)
        self.sell_button = customtkinter.CTkButton(self.main_frame, width = 200, height = 100, text = "Sell To Customer", command = lambda: self.sell_button_dialog_event(name, sellText)).place(x =525, y = 250)
    
    def buy_button_dialog_event(self, nameOfProduct: str, prompt: str):
        dialog = customtkinter.CTkInputDialog(text=prompt, title= nameOfProduct)
        amount = dialog.get_input()
        buyType = "Bought"
        totalAmount = 0
        if amount:
            with open('inventory.csv', 'r') as file:
                reader = csv.reader(file)

                data = []

                for row in reader:
                    if row[0] == nameOfProduct:
                        row[1] = str(int(row[1]) + int(amount))
                        totalAmount = int(row[1])
                    data.append(row)
            file.close()
            # Updating transaction csv        
            transaction_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open("transactions_log.csv", mode = 'a', newline = '') as file:
                writer1 = csv.writer(file)
                writer1.writerow([self.username, nameOfProduct, buyType, amount, transaction_time, totalAmount])
            file.close()
            #update csv
            with open('inventory.csv', "w", newline = '') as file:
                writer2 = csv.writer(file)
                writer2.writerows(data)
            file.close()

    def sell_button_dialog_event(self, nameOfProduct: str, prompt: str):
        dialog = customtkinter.CTkInputDialog(text=prompt, title= nameOfProduct)
        amount = dialog.get_input()
        saleType = "Sold"
        totalAmount = 0
        canAdd = True
        if amount:
            with open('inventory.csv', 'r') as file:
                reader = csv.reader(file)

                data = []
                
                for row in reader:
                    if row[0] == nameOfProduct:
                        if int(row[1]) >= int(amount):
                            row[1] = str(int(row[1]) - int(amount))
                            totalAmount = int(row[1])
                            canAdd = True
                        else:
                            canAdd = False
                            messagebox.showerror(title = "Error", message = "Not enough items to sell")
                    data.append(row)
            file.close()
            # Update Transaction_log
            if canAdd:       
                transaction_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                with open("transactions_log.csv", mode = 'a', newline = '') as file:
                    writer1 = csv.writer(file)
                    writer1.writerow([self.username, nameOfProduct, saleType, amount, transaction_time, totalAmount])
                file.close()
            #update csv
            with open('inventory.csv', "w", newline = '') as file:
                writer2 = csv.writer(file)
                writer2.writerows(data)
            file.close()
        
    def sidebar_transactions_event(self):
        self.clear_frame(self.main_frame)
        self.textboxLabel = customtkinter.CTkLabel(self.main_frame, text = "Current Transactions", font=customtkinter.CTkFont(size=20, weight="bold")).pack(side = "top")
        self.textbox = customtkinter.CTkTextbox(self.main_frame, width = 600, height =500)
        data = []
        
        self.textbox.insert("0.0", "End of Transaction History")
        with open("transactions_log.csv", mode = 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for i, row in enumerate(reader):
                if i > 0:
                #                                   User    Sold    Amount    Product       Time                                 New inventory
                    self.textbox.insert("0.0", f"{row[0]} {row[2]} {row[3]} {row[1]}(s) at {row[4]}. The total inventory is now {row[5]} \n\n")
        self.textbox.pack()
        file.close()


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
        self.tree.heading("#0", text = "", anchor = "w") # annoying unnecessary first thing i cannot change
        self.tree.heading("Product", text = "Product", anchor="w")
        self.tree.heading("Amount", text = "Amount", anchor= "center")

        with open('inventory.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.tree.insert(parent = "", index = 'end', text = '', values = (row['Product'], row['Amount']))

        self.tree.pack(side= "right", fill= "both", expand = True )
        csvfile.close()
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    

if __name__ == "__main__":
    app = App()
    app.mainloop()





