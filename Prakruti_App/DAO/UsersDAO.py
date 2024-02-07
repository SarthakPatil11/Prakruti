from Prakruti_App.Utility.UserData import UserData
from Prakruti_App.models import Users


def GetUserByUserNameFromUsers(userName):
    users = Users.objects.get(UserName=userName)
    return users


def CreateUserInUsers(data: UserData):
    new_User = Users(UserName=data.UserName, Middle_name=data.MiddleName,
                    Phone_No=data.PhoneNumber, Age=data.Age, Gender=data.Gender, Img=data.ProfilePicture)
    new_User.save()
