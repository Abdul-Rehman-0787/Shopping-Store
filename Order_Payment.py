from datetime import datetime
# this is also result of internet research, importing this just to copy date and time
from  Admin import *

##########################################################################
# CLASS OF ORDERS MADE BY USER
##########################################################################
class Order:
    def __init__(self, order_id, user_id, amount, shipping_address, status="Pending"):
        self.order_id = order_id
        self.user_id = user_id
        self.amount = amount
        self.shipping_address = shipping_address
        self.status = status
        #STORES CURRENT TIME WITH THE HELP OF BUILTIN FUNCTION
        self.datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #IT WAS CRUCIAL TO ADD AS ORDER AND PAYMENT MUST HAVE RECORD OF TIME

    ###################################  CLASS FUNCTION ##########################################
    def create_payment(self, payment_method):
        payment_id = "PAY" + str(len(Payments_List) + 1)
        new_payment = Payment(payment_id, self.order_id, self.user_id,self.amount, payment_method)
        Payments_List.append(new_payment)
        return new_payment

    ###################################  CLASS FUNCTION ##########################################
    def __str__(self):
        return ("Order ID: "+ str(self.order_id) +
                "\nUser ID:" + str(self.user_id) +
                "\nAmount: $" +str(self.amount) +
                "\nShipping Address:" + str(self.shipping_address) +
                "\nStatus: " + str(self.status) +
                "\nDate & Time:"+ str(self.datetime) )

##########################################################################
# CLASS OF PAYMENT FOR ORDER
##########################################################################
class Payment:
    def __init__(self, payment_id, order_id, user_id, amount, payment_method, status="Pending"):
        self.payment_id = payment_id
        self.order_id = order_id
        self.user_id = user_id
        self.amount = amount
        self.payment_method = payment_method
        self.status = status
        #STORES CURRENT TIME WITH THE HELP OF BUILTIN FUNCTION
        self.payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # IT WAS CRUCIAL TO ADD AS ORDER AND PAYMENT MUST HAVE RECORD OF TIME
        self.verification = False

    ###################################  CLASS FUNCTION ##########################################
    def verify_payment(self):
        self.verification = True
        self.status = "Verified"

    ###################################  CLASS FUNCTION ##########################################
    def __str__(self):
        return ("\nPayment ID:" + str(self.payment_id) +
                "\nOrder ID: " + str(self.order_id) +
                "\nUser ID:" + str(self.user_id) +
                "\nAmount: $" + str(self.amount) +
                "\nPayment Method: " + str(self.payment_method) +
                "\nStatus: " + str(self.status) +
                "\nVerification: " + str('Verified' if self.verification else 'Not Verified') +
                "\nPayment Date: " + str(self.payment_date))