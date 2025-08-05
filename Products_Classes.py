##########################################################################
# BASE CLASS OF PRODUCTS (PRODUCT)
##########################################################################
class Product:
    def __init__(self, pd_id, name, description, price, quantity, category, gender):
        self.Product_ID = pd_id
        self.Product_Name = name
        self.Product_Description = description
        self.Product_Price = price
        self.Product_Quantity = quantity
        self.Product_Category = category
        self.Product_Gender = gender

    ###################################### FUNCTION #########################################
    def __str__(self):
            return ("ID: " + str(self.Product_ID) + "\n" +
                    "Name: " + str(self.Product_Name) + "\n" +
                    "Price: $" + str(self.Product_Price) + "\n" +
                    "Quantity: " + str(self.Product_Quantity) + "\n" +
                    "Category: " + str(self.Product_Category) + "\n" +
                    "Gender: " + str(self.Product_Gender) + "\n" +
                    "Description: " + str(self.Product_Description) + "\n")



##########################################################################
# DERIVED CLASS OF PRODUCT (CLOTHING)
##########################################################################
class Clothing(Product):
    def __init__(self, pd_id, name, description, price, quantity, gender, size, material):
        super().__init__(pd_id, name, description, price, quantity, "Clothing", gender)
        self.Size = size
        self.Material = material

    def __str__(self):
        return super().__str__() + "Size: " + str(self.Size) + "\n" + "Material: " + str(self.Material) + "\n"


##########################################################################
# DERIVED CLASS OF PRODUCT (ELECTRONICS)
##########################################################################
class Electronics(Product):
    def __init__(self, pd_id, name, description, price, quantity, gender, brand, warranty):
        super().__init__(pd_id, name, description, price, quantity, "Electronics", gender)
        self.Brand = brand
        self.Warranty = warranty

    def __str__(self):
        return super().__str__() + "Brand: " + str(self.Brand) + "\n" + "Warranty: " + str(self.Warranty) + " months\n"


##########################################################################
# DERIVED CLASS OF PRODUCT (FOOTWEAR)
##########################################################################
class Footwear(Product):
    def __init__(self, pd_id, name, description, price, quantity, gender, size, shoe_type):
        super().__init__(pd_id, name, description, price, quantity, "Footwear", gender)
        self.Size = size
        self.Type = shoe_type

    def __str__(self):
        return super().__str__() + "Size: " + str(self.Size) + "\n" + "Type: " + str(self.Type) + "\n"



##########################################################################
# DERIVED CLASS OF PRODUCT (BEAUTY)
##########################################################################
class Beauty(Product):
    def __init__(self, pd_id, name, description, price, quantity, gender, brand, skin_type):
        super().__init__(pd_id, name, description, price, quantity, "Beauty", gender)
        self.Brand = brand
        self.SkinType = skin_type

    def __str__(self):
        return super().__str__() + "Brand: " + str(self.Brand) + "\n" + "Skin Type: " + str(self.SkinType) + "\n"
