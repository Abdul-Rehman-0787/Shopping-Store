from Shopping_Cart import *

##########################################################################
# CLASS OF USER (VISITOR)
##########################################################################
class User:
    def __init__(self,us_id,first_name,last_name,e_mail,address,number,password):
        self.user_id = us_id
        self.user_first_name = first_name
        self.user_last_name = last_name
        self.user_e_mail = e_mail
        self.user_number = number
        self.user_address = address
        self.user_password = password
        self.shopping_cart = ShoppingCart(us_id)

    ###################################  CLASS FUNCTION ##########################################
    def __str__(self):
        return(
            "\nUser ID    :\t" +str(self.user_id) +
            "\nFirst Name :\t" +str(self.user_first_name)+
            "\nLast Name  :\t" +str(self.user_last_name)+
            "\nE-Mail     :\t" +str(self.user_e_mail)+
            "\nNumber     :\t" +str(self.user_number)+
            "\nAddress    :\t" +str(self.user_address) + "\n"
        )



##########################################################################
# GLOBAL FUNCTION FOR USER LOG IN MENU
##########################################################################
def user_sl_menu():
    clear_screen()
    print("\n=============================================================================================")
    print("\t\t\t\t\tUSER - PAGE")
    print("=============================================================================================")
    print("\n\t\t1. Sign Up")
    print("\t\t2. Log In")
    print("\t\t3. Back to Main Menu")
    print("=============================================================================================")
    choice = input("\n\t\tEnter your choice (1-3): ")
    return choice

##########################################################################
# GLOBAL FUNCTION FOR ADDING USER
##########################################################################
def sign_up_user():
    clear_screen()
    print("\n=============================================================================================")
    print("\t\t\t\t\tUSER - SIGN UP")
    print("=============================================================================================")
    us_id = input("Enter User ID:\t")
    f_name = input("Enter Your First Name:\t")
    l_name = input("Enter Your Last Name:\t")
    email = input("Enter Your E-Mail:\t")
    number = input("Enter Your Number:\t")
    address = input("Enter Your Address:\t")
    u_password = input("Enter Your Password:\t")

    flag = bool(True)
    for users in User_List:
        if users.user_id == us_id:
            flag = False
            print("\n\t\t\t\tError: User With This Id Already Exists!\n")
            break
        elif users.user_e_mail == email:
            flag = False
            print("\n\t\t\t\tError: User With This E-Mail Already Exists!\n")
            break
        elif users.user_number == number:
            flag = False
            print("\n\t\t\t\tError: User With This Contact Number Already Exists!\n")
            break

    if not flag:
        print("\t\t\t\t\t\tUnable To Sign Up\n")
    else:
        new_user = User(us_id, f_name, l_name, email, address, number,u_password)
        User_List.append(new_user)
        print("\n" + f_name + " with User ID: " + us_id + " has Successfully Signed Up!\n")
