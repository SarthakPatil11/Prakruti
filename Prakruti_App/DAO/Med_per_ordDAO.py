from Prakruti_App.Utility.Med_per_ordData import Med_per_ordData
from Prakruti_App.models import Med_per_ord


def AddMed_per_order(medPerOrder: Med_per_ordData):
    new_MedPerOrder = Med_per_ord(
        o_id=medPerOrder.OrderID, m_id=medPerOrder.MedicineID, m_qt=medPerOrder.MedicineQuatity, U_name=medPerOrder.UserName)
    new_MedPerOrder.save()
