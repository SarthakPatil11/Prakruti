# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from Prakruti_App.DAO.AppointmentsDAO import GetAppointmentByDateAndTimeslot
from Prakruti_App.DAO.M_remedyDAO import GetAllRemedies
from Prakruti_App.DAO.UserDAO import *
from Prakruti_App.DAO.UsersDAO import *
from Prakruti_App.Utility.UserData import UserData
from django.contrib.auth.models import auth
from django.contrib import messages

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

from sqlalchemy import null
import calendar
from datetime import date, datetime, timedelta

jinja = {'pt_sort': 'id', 'bl_sort': 'id', 'apt_sort': 'id',
         'mr_sort': 'id', 'hr_sort': 'id', 'ord_sort': 'o_id', 'rcmd': ''}

# -----------------------------Getters and setters---------------------------


def rcmd(ip):
    out = {
        '1': ['Vata', 'Pitta'],
        '1': ['Vata', 'Kapha'],
        '1': ['Pitta', 'Vata'],
        '1': ['Pitta', 'Kapha'],
        '1': ['Kapha', 'Pitta'],
        '1': ['Kapha', 'Vata'],
        '1': ['Sama', 'Sama'],
    }
    ds = pd.read_csv('dataset.csv')
    ds.pop('vata')
    ds.pop('pitta')
    ds.pop('kapha')
    ds['prakruti'] = ds['primary']+' - '+ds['secondary']
    ds.pop('primary')
    ds.pop('secondary')
    print('Dataset Imported...')
    Enc = LabelEncoder()
    for col in ds.columns[0:24]:
        ds[col] = Enc.fit_transform(ds[col])
    ip = ds.iloc[:, 0:24]
    op = ds.prakruti.fillna('Sama')
    clf = DecisionTreeClassifier()
    clf.fit(ip, op)
    Y_pred = clf.predict(ip)
    return out[str(Y_pred)]


def getPrakruti(val):
    if val == '1':
        return ("Vata", "Kapha")
    elif val == '2':
        return ("Vata", "Pitta")
    elif val == '3':
        return ("Kapha", "Vata")
    elif val == '4':
        return ("Kapha", "Pitta")
    elif val == '5':
        return ("Pitta", "Vata")
    else:
        return ("Pitta", "Kapha")


def getGender(gender):
    if (gender == "1"):
        return "male"
    elif (gender == "2"):
        return "female"
    elif (gender == "3"):
        return "other"


def getAvailableSlot(date, appointment):
    Apts = GetAppointmentByDateAndTimeslot(date, appointment)
    if len(Apts) < 11:
        return 1
    else:
        return 0


def getNextAvailableSlot():
    i = 0
    while i < 5:
        dt = date.today() + timedelta(i)
        day = calendar.day_name[dt.weekday()]
        if day != "Sunday":
            slots = ["Morning", "Afternoon", "Evening"]
            if i == 0:
                currentTime = datetime.now()
                if currentTime.hour < 12:
                    j = 0
                elif 12 <= currentTime.hour < 18:
                    j = 1
                elif 18 <= currentTime.hour < 20:
                    j = 2
                else:
                    i += 1
                    continue
            else:
                j = 0
            while j < 3:
                Apts = GetAppointmentByDateAndTimeslot(dt, slots[j])
                if len(Apts) < 10:
                    return dt, slots[j]
                j += 1
        i += 1
    return null, null

# -----------------------------Main functions---------------------------


def index(request):
    prds = GetAllRemedies().order_by('?')[:4]
    abc = ""
    try:
        abc = GetUserByUserNameFromUsers(request.user)
    except:
        pass
    return render(request, 'index.html', {'prds': prds, 'usr': abc})


def signup(request):
    return render(request, 'signup.html')


def mailVerify(request):
    print("in email", request.GET)
    if GetUserByEmail(request.GET['email']):
        print('Email exists')
        return HttpResponse(True)
    else:
        print('Email does not exist')
        return HttpResponse(False)


def unameVerify(request):
    print("in uname", request.GET)
    if GetUserByUserNameFromUser(request.GET['uname']):
        print('username exists')
        return HttpResponse(True)
    else:
        print('username does not exist')
        return HttpResponse(False)


def handleSignUp(request):
    if request.method == 'POST':
        userData = UserData()
        userData.UserName = request.POST['input_UserName']
        userData.FirstName = request.POST['input_FirstName']
        userData.MiddleName = request.POST['input_MiddleName']
        userData.LastName = request.POST['input_LastName']
        userData.Email = request.POST['input_SignupEmail']
        userData.PhoneNumber = request.POST['input_Phone']
        userData.Password = request.POST['input_Password']
        userData.Age = request.POST['input_Age']
        userData.Gender = getGender(request.POST['input_Gender'])
        userData.ProfilePicture = request.FILES['input_File']

        CreateUserInUser(userData)

        try:
            CreateUserInUsers(userData)
        except Exception:
            print(Exception)

        messages.success(
            request, "Your account has been successfully created.")
        return redirect('/')
    else:
        return render(request, 'signup.html')


def handleLogin(request):
    if request.method == 'POST':
        # print(request.POST)
        log_usr = request.POST['log_username']
        log_pwd = request.POST['log_pwd']
        print(request.POST)
        user = auth.authenticate(username=log_usr, password=log_pwd)
        if user is not None:
            Whos = GetUserByUserNameFromUser(user)
            auth.login(request, user)
            messages.success(request, 'Successfully Logged In.')
            for Who in Whos:
                if Who.is_superuser:
                    # jinja["Who"] = Who.username
                    return redirect('/dashboard/')
                else:
                    jinja["Who"] = ""
                    return index(request)
        else:
            messages.error(request, 'Invalid Credentials, Please try again.')
            return redirect('/')
    return HttpResponse('404 - Not Found')


def handleLogout(request):
    jinja["Who"] = ""
    auth.logout(request)
    messages.success(request, 'Successfully Logged Out')
    return redirect('/')


def chPass(request):
    if request.POST:
        chPassMail = request.POST['chPassMail']
        conf_pass = request.POST['confPass']
        print(request.POST)

        try:
            user = GetUserByEmail(chPassMail)
            ChangePassword(user, conf_pass)
            messages.success(request, 'Password changed successfully.')
            return redirect('/')
        except Exception as e:
            messages.error(request, 'Invalid Credentials, Please try again.')
            print('somthing wrong', e)

    return redirect('/')
