from Products_Classes import *

##########################################################################
# INITIALIZING LISTS FOR PRODUCTS MANAGEMENT
##########################################################################
Products_List = []            #STORES ALL PRODUCTS
Clothing_Product_List = []    #STORES ONLY CLOTHING PRODUCTS
Electronics_Product_List =[]  #STORES ONLY ELECTRONICS PRODUCTS
Beauty_Product_List=[]        #STORES ONLY BEAUTY PRODUCTS
Footwear_Product_List =[]     #STORES ONLY FOOTWEAR PRODUCTS
User_List = []                #STORES ALL THE USERS
Orders_List = []              #STORES ALL THE ORDERS
Payments_List = []            #STORES ALL THE PAYMENTS


##########################################################################
# GLOBAL FUNCTION FOR DISPLAYING PRODUCTS
##########################################################################
def display_products():
    clear_screen()
    print("=============================================================================================")
    print("\t\t\t\t--- Available All Products ---")
    print("=============================================================================================")
    if not Products_List:
        print("No Products Available.")
    else:
        num = 1
        for product in Products_List:
            print("---------------------(Product-" + str(num) + ")----------------------")
            print(product)
            num += 1

    input("Press Enter to Continue!")

##########################################################################
# GLOBAL FUNCTION FOR DISPLAYING CLOTHING PRODUCTS
##########################################################################
def display_clothing_products():
    clear_screen()
    print("=============================================================================================")
    print("\t\t\t\t--- Available Clothing Products ---")
    print("=============================================================================================")
    if not Clothing_Product_List:
        print("No Products Available.")
    else:
        num = 1
        for product in Clothing_Product_List:
            print("---------------------(Product-" + str(num) + ")----------------------")
            print(product)
            num +=1

    input("Press Enter to Continue!")

##########################################################################
# GLOBAL FUNCTION FOR DISPLAYING ELECTRONIC PRODUCTS
##########################################################################
def display_electronic_products():
    clear_screen()
    print("=============================================================================================")
    print("\t\t\t\t--- Available Electronic Products ---")
    print("=============================================================================================")
    num = 1
    if not Electronics_Product_List:
        print("No Products Available.")
    else:
        for product in Electronics_Product_List:
            print("---------------------(Product-" + str(num) + ")----------------------")
            print(product)
            num+=1

    input("Press Enter to Continue!")

##########################################################################
# GLOBAL FUNCTION FOR DISPLAYING FOOTWEAR PRODUCTS
##########################################################################
def display_footwear_products():
    clear_screen()
    print("=============================================================================================")
    print("\t\t\t\t--- Available Footwear Products ---")
    print("=============================================================================================")
    if not Footwear_Product_List:
        print("No Products Available.")
    else:
        num =1
        for product in Footwear_Product_List:
            print("---------------------(Product-" + str(num) + ")----------------------")
            print(product)
            num+=1
    input("Press Enter to Continue!")

##########################################################################
# GLOBAL FUNCTION FOR DISPLAYING Beauty PRODUCTS
##########################################################################
def display_beauty_products():
    clear_screen()
    print("=============================================================================================")
    print("\t\t\t\t--- Available Beauty Products ---")
    print("=============================================================================================")
    if not Beauty_Product_List:
        print("No Products Available.")
    else:
        num = 1
        for product in Beauty_Product_List:
            print("---------------------(Product-" + str(num) + ")----------------------")
            print(product)
            num +=1

    input("Press Enter to Continue!")


##########################################################################
# GLOBAL FUNCTION TO CLEAR THE OUTPUT SCREEN (TERMINAL)
##########################################################################

import os #importing os just for clearing the screen

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    #This Function is the result of internet research
    #If your output is not getting clear before printing next page than you should change your terminal setting and enable
    #{Emulate terminal in output console}
    # If you are still facing the issue than you can also google it
    print("\n\t\t\t\t***********************************")
    print("\t\t\t\t*           WELCOME TO            *")
    print("\t\t\t\t*       OUR SHOPPING STORE        *")
    print("\t\t\t\t***********************************\n")