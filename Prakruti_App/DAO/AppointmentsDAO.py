from Prakruti_App.models import Appointments


def GetAppointmentByUserID(Userid):
    Appointments = Appointments.objects.filter(U_id=Userid)
    return Appointments


def GetAppointmentByDateAndTimeslot(Date, Timeslot):
    Appointments = Appointments.objects.filter(Date=Date, TimeSlot=Timeslot)
    return Appointments
