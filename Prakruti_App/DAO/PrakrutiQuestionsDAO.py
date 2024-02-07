from Prakruti_App.models import Prakruti_Quetions


def GetAllPrakrutiQuestions():
    Questions = Prakruti_Quetions.objects.all()
    return Questions