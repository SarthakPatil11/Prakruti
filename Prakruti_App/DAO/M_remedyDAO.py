from Prakruti_App.models import M_remedy


def GetRemediesByCategory(category):
    remedy = M_remedy.objects.filter(Category=category)
    return remedy


def GetRemediesExcept(exceptionalProducts):
    remedy = M_remedy.objects.all().difference(exceptionalProducts)
    return remedy


def GetAllRemedies():
    remedies = M_remedy.objects.all()
    return remedies


def GetRemedyByProductID(productID):
    remedy = M_remedy.objects.get(pk=productID)
    return remedy
