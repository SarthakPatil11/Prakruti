from django.contrib.auth.models import User

from Prakruti_App.Utility.UserData import UserData


def GetUserByEmail(email):
    user = User.objects.filter(email=email)
    return user


def GetUserByUserNameFromUser(Username):
    user = User.objects.filter(username=Username)
    return user


def GetUsersFromUserTable(UserName):
    users = User.objects.filter(username__contains=UserName)
    return users


def ChangePassword(user, Password):
    user.set_password(Password)
    user.save()


def CreateUserInUser(data: UserData):
    new_User = User.objects.create_user(
        username=data.UserName, password=data.Password, email=data.Email, first_name=data.FirstName, last_name=data.LastName)
    new_User.save()
