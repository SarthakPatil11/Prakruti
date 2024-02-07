from datetime import date
import datetime
from Prakruti_App.Utility.OrderData import OrderData
from Prakruti_App.models import Orders


def GetOrderByID(orderID):
    order = Orders.objects.get(o_id=orderID)
    return order

def AddOrder(order : OrderData):
    new_Order = Orders(o_id=order.OrderID, UserName=order.UserName, Date=date.today(),
                    Time=datetime.now().strftime("%H:%M:%S"), Address=order.Address, Price=order.Price)
    new_Order.save()
