from Products_Functions import *


##########################################################################
# CLASS OF SHOPPING CART FOR USER
##########################################################################
class ShoppingCart:
    def __init__(self, us_id):
        self.user_id = us_id
        self.total_amount = 0.0
        self.total_items = 0
        self.cart_items = []  # Will store [product_id, quantity, unit_price]

    ###################################  CLASS FUNCTION ##########################################
    def verify_product(self, product_id):
        for product in Products_List:
            if product.Product_ID == product_id:
                return product
        return None

    ###################################  CLASS FUNCTION ##########################################
    def update_category_lists(self, product_id, quantity_change):
        for category_list in [Clothing_Product_List, Electronics_Product_List,
                              Beauty_Product_List, Footwear_Product_List]:
            for product in category_list:
                if product.Product_ID == product_id:
                    product.Product_Quantity += quantity_change
                    break

    ###################################  CLASS FUNCTION ##########################################
    def add_to_cart(self):
        product_id = input("Enter Product ID to Add in Your Shopping Cart: ")
        product = self.verify_product(product_id)

        if not product:
            print("\nProduct Not Found!")
            input("Press Enter to Continue!")
            return


        qty_input = input("Enter Quantity: ")


        if not qty_input.isdigit():
            print("\nPlease Enter a Natural Number for Quantity!")
            input("Press Enter to Continue!")
            return

        qty = int(qty_input)

        if qty <= 0:
            print("\nQuantity Must be Greater than 0!")
            input("Press Enter to Continue!")
            return

        if qty > product.Product_Quantity:
            print("\nNot Enough Stock! Only " + str(product.Product_Quantity) + " Available.")
            return

        product.Product_Quantity -= qty
        self.update_category_lists(product_id, -qty)

        # Add to cart
        self.cart_items.append([product_id, qty, product.Product_Price])
        self.total_amount += qty * product.Product_Price
        self.total_items += qty

        print("\n" + str(product.Product_Name) + "x" + str(qty) + "Added to Cart!")
        input("Press Enter to Continue!")

    ###################################  CLASS FUNCTION ##########################################
    def update_cart(self):
        product_id = input("Enter Product ID to Update: ")
        found = False

        for item in self.cart_items:
            if item[0] == product_id:
                product = self.verify_product(product_id)
                if not product:
                    print("\nProduct No Longer Available!")
                    input("Press Enter to Continue!")
                    return

                new_qty_input = input("Enter New Quantity: ")

                if not new_qty_input.isdigit():
                    print("\nPlease Enter a Whole Number (e.g., 1, 2, 3)")
                    input("Press Enter to Continue!")
                    return

                new_qty = int(new_qty_input)

                if new_qty <= 0:
                    print("\nQuantity Must be At Least 1!")
                    input("Press Enter to Continue!")
                    return

                qty_diff = new_qty - item[1]

                if qty_diff > product.Product_Quantity:
                    print(f"\nNot Enough Stock! Only " + str(product.Product_Quantity) + " Available.")
                    input("Press Enter to Continue!")
                    return

                product.Product_Quantity -= qty_diff
                self.update_category_lists(product_id, -qty_diff)

                item[1] = new_qty
                self.total_amount += qty_diff * item[2]
                self.total_items += qty_diff

                print("\nCart Updated Successfully!")
                input("Press Enter to Continue!")
                found = True

        if not found:
            print("\nProduct Not Found in Cart!")
            input("Press Enter to Continue!")

    ###################################  CLASS FUNCTION ##########################################
    def remove_from_cart(self):
        product_id = input("Enter Product ID to Remove: ")
        found = False

        for item in self.cart_items:
            if item[0] == product_id:
                product = self.verify_product(product_id)
                if product:
                    product.Product_Quantity += item[1]
                    self.update_category_lists(product_id, item[1])

                    self.total_amount -= item[1] * item[2]
                    self.total_items -= item[1]

                    self.cart_items.remove(item)
                    print("\nItem Removed From Cart!")
                found = True
                break

        if not found:
            print("\nProduct is Not in Your Cart!")

    ###################################  CLASS FUNCTION ##########################################
    def print_cart_details(self):
        if not self.cart_items:
            print("\nYour Cart is Empty!")
            input("Press Enter to Continue!")
            return
        clear_screen()
        print("\n=====================================================================================================")
        print("\t\t\t\t\tSHOPPING CART")
        print("=====================================================================================================")
        print("Item#\t\tProduct ID\t\tUnit Price\t\tQuantity\t\tSubtotal")
        print("-----------------------------------------------------------------------------------------------------")

        item_number = 1
        for item in self.cart_items:
            print(str(item_number) + "\t\t" + item[0] + "\t\t\t$" + str(item[2]) + "\t\t\t" +
                  str(item[1]) + "\t\t\t$" + str(item[1] * item[2]))
            item_number += 1

        print("======================================================================================================")
        print("TOTAL ITEMS: " + str(self.total_items))
        print("TOTAL AMOUNT: $" + str(self.total_amount))
        print("======================================================================================================")
        input("Press Enter to Continue!")

    ###################################  CLASS FUNCTION ##########################################
    def checkout(self, user):
        if not self.cart_items:
            print("\nYour Cart is Empty!")
            input("Press Enter to Continue!")
            return False

        print("\n=============================================================================================")
        print("\t\t\t\t\tCHECKOUT")
        print("=============================================================================================")

        # Display cart summary
        self.print_cart_details()

        # Get shipping address
        shipping_address = input("\nEnter Shipping Address: ")
        if not shipping_address.strip():
            print("\nShipping Address is Required!")
            input("Press Enter to Continue")
            return False

        # GENERATES ORDER ID
        order_id = "ORD" + str(len(Orders_List) + 1)

        # CREATES ORDER
        from Order_Payment import Order
        new_order = Order(order_id, self.user_id, self.total_amount, shipping_address)
        Orders_List.append(new_order)

        # PAYMENT PROCESS
        print("\n=============================================================================================")
        print("\t\t\t\t\tPAYMENT PROCESS")
        print("=============================================================================================")
        print("\nPlease select payment method:")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. PayPal")
        print("4. Cash on Delivery")
        print("=============================================================================================")
        payment_choice = input("Enter Your Choice (1-4): ")
        payment_methods = {
            "1": "Credit Card",
            "2": "Debit Card",
            "3": "PayPal",
            "4": "Cash on Delivery"
        }

        if payment_choice not in payment_methods:
            print("\nInvalid Payment Method!")
            input("Press Enter to Continue!")
            return False

        payment_method = payment_methods[payment_choice]
        payment = new_order.create_payment(payment_method)

        clear_screen()
        print("\n=============================================================================================")
        print("\t\t\t\t\tORDER CONFIRMATION")
        print("=============================================================================================")
        print(new_order)
        print("\nPayment Details:")
        print(payment)

        # Clear the cart after successful checkout
        self.cart_items = []
        self.total_amount = 0.0
        self.total_items = 0
        input("Press Enter to Continue!")
        return True

    ###################################  CLASS FUNCTION ##########################################
    def __str__(self):
        return ("User ID: " + self.user_id +
                "\nTotal Items: " + str(self.total_items) +
                "\nTotal Amount: $" + str(self.total_amount))

