from Order_Payment import *

##########################################################################
# GLOBAL FUNCTION FOR USER LOG IN
##########################################################################
def user_log_in():
    print("\n=============================================================================================")
    print("\t\t\t\t\tUSER  LOG-IN")
    print("=============================================================================================")
    lus_id = input("\n\t\t\tEnter Your User Name(User ID):\t")
    l_password = input("\t\t\tEnter Your Password :  \t")

    flag = bool(False)
    for users in User_List:
        if users.user_id == lus_id:
            if l_password == users.user_password:
                flag = True
                print("Logging In!")
                user_menu(users)
                return
    print("\nWrong User Name or Password!!!!!\n")

##########################################################################
# GLOBAL FUNCTION FOR USER MENU
##########################################################################
def user_menu(user):
    while True:
        clear_screen()
        print("\n=============================================================================================")
        print("\t\t\t\t\tUSER MENU")
        print("=============================================================================================")
        print("1. View Products")
        print("2. View Beauty Products")
        print("3. View Clothing Products")
        print("4. View Footwear Products")
        print("5. View Electronic Products")
        print("6. Shopping Cart")
        print("7. View Account Details")
        print("8. Logout")
        print("=============================================================================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_products()
        elif choice == "2":
            display_beauty_products()
        elif choice == "3":
            display_clothing_products()
        elif choice == "4":
            display_footwear_products()
        elif choice == "5":
            display_electronic_products()
        elif choice == "6":
            cart_menu(user)
        elif choice == "7":
            clear_screen()
            print("\n=============================================================================================")
            print("\t\t\t\t\tUSER Details")
            print("=============================================================================================")
            print(user)
            input("Press Enter to  Continue!")
        elif choice == "8":
            print("\nLogging out...")
            break
        else:
            print("\nInvalid choice! Please try again.")


##########################################################################
# GLOBAL FUNCTION FOR CART MENU
##########################################################################
def cart_menu(user):
    while True:
        clear_screen()
        print("\n=============================================================================================")
        print("\t\t\t\t\tSHOPPING CART MENU")
        print("=============================================================================================")
        print("1. View Cart")
        print("2. Add Item to Cart")
        print("3. Update Item Quantity")
        print("4. Remove Item from Cart")
        print("5. Checkout")
        print("6. Back to Main Menu")
        print("=============================================================================================")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            user.shopping_cart.print_cart_details()
        elif choice == "2":
            clear_screen()
            print("\n=============================================================================================")
            print("\t\t\t\tADD PRODUCT IN SHOPPING CART")
            print("=============================================================================================")
            user.shopping_cart.add_to_cart()
        elif choice == "3":
            clear_screen()
            print("\n=============================================================================================")
            print("\t\t\t\tUPDATE PRODUCT IN SHOPPING CART")
            print("=============================================================================================")
            if not user.shopping_cart.cart_items:
                print("\nYour cart is empty!")
                print("Press Enter to Continue!")
            else:
                user.shopping_cart.update_cart()
        elif choice == "4":
            clear_screen()
            print("\n=============================================================================================")
            print("\t\t\t\t\tREMOVE PRODUCT FROM SHOPPING CART")
            print("=============================================================================================")
            if not user.shopping_cart.cart_items:
                print("\nYour Cart is Empty!")
                input("Press Enter to Continue!")
            else:
                user.shopping_cart.remove_from_cart()
        elif choice == "5":
            clear_screen()
            if user.shopping_cart.checkout(user):
                return
        elif choice == "6":
            return
        else:
            print("\nInvalid choice! Please try again.")
##########################################################################
# GLOBAL FUNCTION FOR ADMIN MENU
##########################################################################
def admin_menu(admin):
    while True:
        clear_screen()
        print("\n=============================================================================================")
        print("\t\t\t\t\tADMINISTRATOR MENU")
        print("=============================================================================================")
        print("\t\t\t\t1. Add New Product")
        print("\t\t\t\t2. Delete Existing Product")
        print("\t\t\t\t3. Edit Product Details")
        print("\t\t\t\t4. View All Products")
        print("\t\t\t\t5. View Payment Records")
        print("\t\t\t\t6. Verify Payment")
        print("\t\t\t\t7. Return to Main Menu")
        print("=============================================================================================")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            clear_screen()
            print("\n=============================================================================================")
            print("\t\t\t\t\tADD NEW PRODUCT")
            print("=============================================================================================")
            admin.add_product()
        elif choice == "2":
            clear_screen()
            print("\n=============================================================================================")
            print("\t\t\t\t\tDELETE PRODUCT")
            print("=============================================================================================")
            admin.delete_product()
        elif choice == "3":
            clear_screen()
            print("\n=============================================================================================")
            print("\t\t\t\t\tEDIT PRODUCT")
            print("=============================================================================================")
            admin.edit_product()
        elif choice == "4":
            clear_screen()
            print("\n=============================================================================================")
            print("\t\t\t\t\tPRODUCT CATALOG")
            print("=============================================================================================")
            display_products()
        elif choice == "5":
            clear_screen()
            print("\n=============================================================================================")
            print("\t\t\t\t\tPAYMENT LIST")
            print("=============================================================================================")
            admin.view_payments()
        elif choice == "6":
            clear_screen()
            print("\n=============================================================================================")
            print("\t\t\t\t\tVERIFY PRODUCTS")
            print("=============================================================================================")
            admin.verify_payments()
        elif choice == "7":
            print("\nReturning to Main Menu...")
            break
        else:
            print("\nInvalid Choice! Please Enter a Number Between 1-7")


##########################################################################
# GLOBAL FUNCTION OF MAIN MENU
##########################################################################
def main_menu():

    while True:
        clear_screen()
        print("\n=============================================================================================")
        print("\t\t\t\t\tMAIN MENU")
        print("=============================================================================================")
        print("\n\t\t\t\t1. Admin")
        print("\t\t\t\t2. User (Visitor)")
        print("\t\t\t\t3. Exit")
        print("=============================================================================================")

        choice = input("Enter Your Choice (1-3): ")

        if choice == "1":  # Admin
            if admin_login():
                admin_menu(admin1)

        elif choice == "2":  # User
            while True:
                user_choice = user_sl_menu()

                if user_choice == "1":  # Sign Up
                    clear_screen()
                    sign_up_user()
                    input("\n\t\tPress Enter to continue...")

                elif user_choice == "2":  # Log In
                    clear_screen()
                    if user_log_in():
                        # Get the 'logged in' user object
                        logged_in_user = None
                        user_id = input("\n\t\tEnter your User ID again: ")
                        for user in User_List:
                            if user.user_id == user_id:
                                logged_in_user = user
                                break

                        if logged_in_user:
                            user_menu(logged_in_user)
                    input("\n\t\tPress Enter to continue...")

                elif user_choice == "3":  # Back
                    break

                else:
                    print("\n\t\tInvalid choice! Please try again.")
                    input("\n\t\tPress Enter to continue...")

        elif choice == "3":  # Exit
            print("\n\t\tThank you For Using Our System. Goodbye!")
            break

        else:
            print("\n\t\tInvalid Choice! Please Try Again.")
            input("\n\t\tPress Enter to Continue...")


##########################################################################
# MAIN FUNCTION
##########################################################################
if __name__ == "__main__":
    # Create admin
    admin1 = Admin("admin", "Admin", "admin@store.com", "123 Admin St", "555-0001")

    # Create sample products
    clothing1 = Clothing("CL001", "Men's T-Shirt", "Cotton crew neck", 19.99, 50, "Male", "L", "Cotton")
    clothing2 = Clothing("CL002", "Women's Jeans", "Slim fit denim", 39.99, 30, "Female", "M", "Denim")

    electronics1 = Electronics("EL001", "Wireless Earbuds", "Noise cancelling", 99.99, 30, "Unisex", "Sony", 12)
    electronics2 = Electronics("EL002", "Smartphone", "6.5\" AMOLED display", 699.99, 15, "Unisex", "Samsung", 24)

    footwear1 = Footwear("FW001", "Running Shoes", "Lightweight mesh", 79.99, 40, "Male", "10", "Sneakers")
    footwear2 = Footwear("FW002", "High Heels", "Leather pumps", 59.99, 25, "Female", "7", "Heels")

    beauty1 = Beauty("BT001", "Face Cream", "Hydrating formula", 24.99, 60, "Female", "L'Oreal", "Dry")
    beauty2 = Beauty("BT002", "Shampoo", "For colored hair", 14.99, 45, "Unisex", "Olive", "All")

    # Add to product lists
    Products_List.extend([clothing1, clothing2, electronics1, electronics2, footwear1, footwear2, beauty1, beauty2])
    Clothing_Product_List.extend([clothing1, clothing2])
    Electronics_Product_List.extend([electronics1, electronics2])
    Footwear_Product_List.extend([footwear1, footwear2])
    Beauty_Product_List.extend([beauty1, beauty2])

    # Create sample users
    user1 = User("user1", "William ", "Henry", "william@example.com", "123 Main St", "555-1001", "password1")
    user2 = User("user2", "Bob ", "Smith", "bob@example.com", "456 Oak Ave", "555-1002", "password2")
    User_List.extend([user1, user2])

    # =============================================
    # CREATE SAMPLE ORDERS AND PAYMENTS
    # =============================================

    # User1's Order and Payment
    order1 = Order("ORD001", "user1", 119.98, "123 Main St, Apt 4B")
    payment1 = Payment("PAY001", "ORD001", "user1", 119.98, "Credit Card")
    payment1.verify_payment()  # Mark as verified
    order1.status = "Completed"

    # User2's Order and Payment
    order2 = Order("ORD002", "user2", 159.98, "456 Oak Ave")
    payment2 = Payment("PAY002", "ORD002", "user2", 159.98, "PayPal")

    # Add to global lists
    Orders_List.extend([order1, order2])
    Payments_List.extend([payment1, payment2])

    # =============================================
    # ADD ITEMS TO USER SHOPPING CARTS
    # =============================================

    # User1 has T-Shirt and Earbuds in cart
    user1.shopping_cart.cart_items.append(["CL001", 2, 19.99])  # 2 T-Shirts
    user1.shopping_cart.cart_items.append(["EL001", 1, 99.99])  # 1 Earbuds
    user1.shopping_cart.total_amount = (2 * 19.99) + 99.99
    user1.shopping_cart.total_items = 3

    # User2 has Jeans and Running Shoes in cart
    user2.shopping_cart.cart_items.append(["CL002", 1, 39.99])  # 1 Jeans
    user2.shopping_cart.cart_items.append(["FW001", 2, 79.99])  # 2 Running Shoes
    user2.shopping_cart.total_amount = 39.99 + (2 * 79.99)
    user2.shopping_cart.total_items = 3

    # =============================================
    # UPDATE PRODUCT QUANTITIES FOR CART ITEMS
    # =============================================

    # Reduce quantities for items in carts
    for product in Products_List:
        if product.Product_ID == "CL001":
            product.Product_Quantity -= 2  # User1 took 2 T-Shirts
        elif product.Product_ID == "EL001":
            product.Product_Quantity -= 1  # User1 took 1 Earbuds
        elif product.Product_ID == "CL002":
            product.Product_Quantity -= 1  # User2 took 1 Jeans
        elif product.Product_ID == "FW001":
            product.Product_Quantity -= 2  # User2 took 2 Running Shoes

    # Also update category lists (mirror the changes)
    for clothing in Clothing_Product_List:
        if clothing.Product_ID == "CL001":
            clothing.Product_Quantity -= 2
        elif clothing.Product_ID == "CL002":
            clothing.Product_Quantity -= 1

    for electronics in Electronics_Product_List:
        if electronics.Product_ID == "EL001":
            electronics.Product_Quantity -= 1

    for footwear in Footwear_Product_List:
        if footwear.Product_ID == "FW001":
            footwear.Product_Quantity -= 2

    #################   MAIN CALL #################################################################
    main_menu()


########################### Info For Log In #########################################
#Admin User ID: admin
#_Admin Password: admin123

#Dummy User ID : user1
#Dummy User Password :password1

#Dummy User ID : user2
#Dummy User Password :password2