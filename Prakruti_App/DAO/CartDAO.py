from Prakruti_App.Utility.CartData import CartData
from Prakruti_App.models import Cart


def GetSpecificUserCartItem(UserName, ProductID):
    item = Cart.objects.filter(Username=UserName).filter(
        p_id=ProductID)
    return item


def AddNewCartItem(cartData: CartData):
    new_cart = Cart(Username=cartData.UserName,
                    p_id=cartData.ProductID, quantity=cartData.Quantity)
    new_cart.save()


def GetCartItemByID(ProductID):
    item = Cart.objects.get(id=ProductID)
    return item


def GetCartItemByUserName(UserName):
    item = Cart.objects.filter(Username=UserName)
    return item
