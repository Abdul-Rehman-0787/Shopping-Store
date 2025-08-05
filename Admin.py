from User import *

##########################################################################
#  CLASS OF ADMIN (OWNER)
##########################################################################
class Admin:
    def __init__(self, ad_id, name, e_mail, address, number):
        self.Admin_id = ad_id
        self.Admin_Name = name
        self.Admin_E_mail = e_mail
        self.Admin_Address = address
        self.Admin_Number = number

    ###################################  CLASS FUNCTION ##########################################
#CLASS FUNCTION TO ADD NEW PRODUCT IN EVERY LIST
    def add_product(self):
        print("\n\t\t\t\t--- Add New Product ---")
        category = input("Enter Category (Clothing/Electronics/Footwear/Beauty): ").lower()
        pd_id = input("Enter Product ID: ")
        for prod in Products_List:
            if prod.Product_ID == pd_id:
                print("This Product ID Already Exists!")
                input("Press Enter to Continue!")
                return
        name = input("Enter Product Name: ")
        description = input("Enter Product Description: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Product Quantity: "))
        gender = input("Enter Gender (Male/Female/Unisex): ")




        if category == "clothing":
            size = input("Enter Size: ")
            material = input("Enter Material: ")
            new_product = Clothing(pd_id, name, description, price, quantity, gender, size, material)
            Clothing_Product_List.append(new_product)
        elif category == "electronics":
            brand = input("Enter Brand: ")
            warranty = int(input("Enter Warranty (months): "))
            new_product = Electronics(pd_id, name, description, price, quantity, gender, brand, warranty)
            Electronics_Product_List.append(new_product)
        elif category == "footwear":
            size = input("Enter Size: ")
            shoe_type = input("Enter Type (Sneakers/Boots/etc): ")
            new_product = Footwear(pd_id, name, description, price, quantity, gender, size, shoe_type)
            Footwear_Product_List.append(new_product)
        elif category == "beauty":
            brand = input("Enter Brand: ")
            skin_type = input("Enter Skin Type: ")
            new_product = Beauty(pd_id, name, description, price, quantity, gender, brand, skin_type)
            Beauty_Product_List.append(new_product)
        else:
            new_product = Product(pd_id, name, description, price, quantity, category, gender)

        Products_List.append(new_product)
        print("\nProduct '" + name + "' Added Successfully!")
        input("Press Enter to Continue!")

    ###################################  CLASS FUNCTION ##########################################
#CLASS FUNCTION TO DELETE SPECIFIC EXISTING PRODUCT FROM EVERY LIST
    def delete_product(self):
        product_id = input("Enter Product ID to delete: ")
        deleted = False

        # Check and delete from main list
        for product in Products_List[:]:
            if product.Product_ID == product_id:
                Products_List.remove(product)
                deleted = True
                break

        # Check and delete from category lists
        if deleted:
            for category_list in [Clothing_Product_List, Electronics_Product_List,
                                  Beauty_Product_List, Footwear_Product_List]:
                for product in category_list[:]:
                    if product.Product_ID == product_id:
                        category_list.remove(product)

            print("Product Deleted Successfully!")
        else:
            print("Product Not Found!")
        input("Press Enter to Continue!")

    ###################################  CLASS FUNCTION ##########################################
#CLASS FUNCTION TO EDIT SPECIFIC EXISTING PRODUCT IN PRODUCTS_LIST
    def edit_product(self):
        product_id = input("Enter Product ID to edit: ")
        found = False

        #Search and edit in main Products_List
        for product in Products_List:
            if product.Product_ID == product_id:
                print("\n\t\t\t\tCurrent Product Details:")
                print(product)

                print("\nLeave Empty if You Do Not Want to Make any Changes in a Option")
                # Get new values
                new_name = input("Enter New Name Inplace of (" + product.Product_Name + ") :\t") or product.Product_Name
                new_desc = input("Enter New Description Inplace of (" + product.Product_Description + ") :\t") or product.Product_Description
                new_price = float(input("Enter New Price Inplace of (" + str(product.Product_Price) + ") :\t") or product.Product_Price)
                new_qty = int(input("Enter New Quantity Inplace of (" + str(product.Product_Quantity) + ") :\t") or product.Product_Quantity)

                # Update main list product
                product.Product_Name = new_name
                product.Product_Description = new_desc
                product.Product_Price = new_price
                product.Product_Quantity = new_qty
                found = True

                # Update in category lists
                category_lists = [Clothing_Product_List, Electronics_Product_List,
                                  Beauty_Product_List, Footwear_Product_List]

                for cat_list in category_lists:
                    for cat_product in cat_list:
                        if cat_product.Product_ID == product_id:
                            cat_product.Product_Name = new_name
                            cat_product.Product_Description = new_desc
                            cat_product.Product_Price = new_price
                            cat_product.Product_Quantity = new_qty
                            break  # Found in this category, move to next

                print("Product Updated in All Lists!")
                input("Press Enter to Continue!")
                return

        if not found:
            print("Product Not Found!")
            input("Press Enter to Continue!")
            return

    ###################################  CLASS FUNCTION ##########################################
# CLASS FUNCTION TO VIEW PAYMENT
    def view_payments(self):

        if not Payments_List:
            print("No Payments Found.")
            input("Press Enter to Continue!")
            return
        num = 1
        for payment in Payments_List:
            print("------------------------------------("+str(num)+")-----------------------------------------")
            print(payment)
            num+=1
        input("Press Enter to Continue!")

    ###################################  CLASS FUNCTION ##########################################
# CLASS FUNCTION TO VERIFY PAYMENT
    def verify_payments(self):
        payment_id = input("Enter Payment ID to Verify: ")
        amount = float(input("Enter Payment Amount to Confirm: "))

        for payment in Payments_List:
            if payment.payment_id == payment_id:
                if payment.amount == amount:
                    payment.verify_payment()
                    print("\nPayment Verified Successfully!")
                    input("Press Enter to Continue!")
                    # Update corresponding order status
                    for order in Orders_List:
                        if order.order_id == payment.order_id:
                            order.status = "DONE"
                            break
                    return
                else:
                    print("\nAmount Doesn't Match!")
                    input("Press Enter to Continue!")
                    return

        print("\nPayment Not Found!")
        input("Press Enter to Continue!")


##########################################################################
#  GLOBAL FUNCTION FOR ADMIN LOG IN
##########################################################################
def admin_login():
    clear_screen()
    print("\n=============================================================================================")
    print("\t\t\t\t\tADMIN LOG-IN")
    print("=============================================================================================")
    admin_id = input("\n\t\t\tEnter Admin ID: ")
    password = input("\t\t\tEnter Password: ")

    # Hardcoded admin credentials
    if admin_id == "admin" and password == "admin123":
        return True
    print("\n\t\t\tInvalid Credentials! Access Denied!!!!")
    input("\n\t\t\tPress Enter to continue...")
    return False