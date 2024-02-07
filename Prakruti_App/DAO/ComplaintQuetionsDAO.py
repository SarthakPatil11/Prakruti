from Prakruti_App.models import Complaint_Quetions


def GetComplaintQuetionsByPrakruti(prakruti):
    Questions = Complaint_Quetions.objects.filter(prakruti=prakruti)
    return Questions

