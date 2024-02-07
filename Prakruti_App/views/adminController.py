# from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from ..models import Users, Appointments, M_remedy, H_remedy, Blogs, Orders, Med_per_ord
from django.contrib.auth.models import User, auth
from django.contrib import messages

from django.utils.datastructures import MultiValueDictKeyError
from sqlalchemy import null
import random
from datetime import date, datetime, timedelta

from .sharedController import jinja, getGender, getPrakruti, getNextAvailableSlot, getAvailableSlot


def dashboard(request):
    if request.user.is_superuser:
        Pts = Users.objects.all()
        MRs = M_remedy.objects.all()
        HRs = H_remedy.objects.all()
        Bls = Blogs.objects.all()

        Apts = Appointments.objects.all()
        CApts = Appointments.objects.filter(Status_A=True)
        Ords = Orders.objects.all()
        COrds = Orders.objects.filter(Status=True)

        all_data = {}
        all_data['pts_ct'] = len(Pts)
        all_data['mrs_ct'] = len(MRs)
        all_data['hrs_ct'] = len(HRs)
        all_data['bls_ct'] = len(Bls)
        try:
            all_data['apts_ct'] = round((len(CApts) / len(Apts))*100, 2)
        except:
            all_data['apts_ct'] = 0
        try:
            all_data['ords_ct'] = round((len(COrds) / len(Ords))*100, 2)
        except:
            all_data['ords_ct'] = 0

        print(all_data)
        return render(request, 'admin/Dashboard.html', {'data': all_data})
    else:
        return redirect('/')


def patients(request):
    new_pts = []
    if request.method == 'POST':
        print(request.POST)
        try:
            if request.POST['sort']:
                jinja['pt_sort'] = request.POST['sort']
        except:
            pass
        try:
            if request.POST['search']:
                if request.POST['srch'] == '1':
                    if (jinja['pt_sort'] == 'first_name' or jinja['pt_sort'] == 'email'):
                        Pts = User.objects.all().order_by(jinja['pt_sort'])
                    else:
                        Pts = Users.objects.all().order_by(jinja['pt_sort'])
                    string = request.POST['search'].lower()
                    for Pt in Pts:
                        if (jinja['pt_sort'] == 'first_name' or jinja['pt_sort'] == 'email'):
                            Pt_ext = Users.objects.get(UserName=Pt.username)
                            strs = (Pt.first_name+" " +
                                    Pt_ext.Middle_name+" " + Pt.last_name)
                        else:
                            Pt_ext = User.objects.get(username=Pt.UserName)
                            strs = (Pt_ext.first_name+" " +
                                    Pt.Middle_name+" " + Pt_ext.last_name)
                        strs = strs.lower()
                        print(string, strs)
                        if string in strs:
                            new_pt = vars(Pt)
                            new_pt.update(vars(Pt_ext))
                            new_pt.pop('_state')
                            new_pt.pop('password')
                            new_pt.pop('last_login')
                            new_pt.pop('is_superuser')
                            new_pt.pop('is_staff')
                            new_pt.pop('is_active')
                            new_pt.pop('date_joined')
                            new_pt.pop('UserName')
                            new_pts.append(new_pt)
                    return render(request, 'admin/patients.html', {'patients': new_pts})
                if request.POST['srch'] == '2':
                    try:
                        Pt = Users.objects.get(pk=request.POST['search'])
                        Pt_ext = User.objects.get(username=Pt.UserName)
                        new_pt = vars(Pt)
                        new_pt.update(vars(Pt_ext))
                        new_pt.pop('_state')
                        new_pt.pop('password')
                        new_pt.pop('last_login')
                        new_pt.pop('is_superuser')
                        new_pt.pop('is_staff')
                        new_pt.pop('is_active')
                        new_pt.pop('date_joined')
                        new_pt.pop('UserName')
                        new_pts.append(new_pt)
                        return render(request, 'admin/patients.html', {'patients': new_pts})
                    except:
                        return render(request, 'admin/patients.html', {'patients': new_pts})
                if request.POST['srch'] == '3':
                    Pts = User.objects.filter(
                        email__icontains=request.POST['search'])
                    for Pt in Pts:
                        Pt_ext = Users.objects.filter(UserName=Pt.username)
                        if Pt_ext:
                            new_pt = vars(Pt)
                            for vr in Pt_ext:
                                new_pt.update(vars(vr))
                            new_pt.pop('_state')
                            new_pt.pop('password')
                            new_pt.pop('last_login')
                            new_pt.pop('is_superuser')
                            new_pt.pop('is_staff')
                            new_pt.pop('is_active')
                            new_pt.pop('date_joined')
                            new_pt.pop('UserName')
                            new_pts.append(new_pt)
                    return render(request, 'admin/patients.html', {'patients': new_pts})
                if request.POST['srch'] == '4':
                    Pts = Users.objects.filter(
                        Phone_No__icontains=request.POST['search'])
                    for Pt in Pts:
                        Pt_ext = User.objects.filter(username=Pt.UserName)
                        if Pt_ext:
                            new_pt = vars(Pt)
                            for vr in Pt_ext:
                                new_pt.update(vars(vr))
                            new_pt.pop('_state')
                            new_pt.pop('password')
                            new_pt.pop('last_login')
                            new_pt.pop('is_superuser')
                            new_pt.pop('is_staff')
                            new_pt.pop('is_active')
                            new_pt.pop('date_joined')
                            new_pt.pop('UserName')
                            new_pts.append(new_pt)
                    return render(request, 'admin/patients.html', {'patients': new_pts})
        except MultiValueDictKeyError:
            print("Search User: ", MultiValueDictKeyError)

        try:
            if request.POST['submit']:
                fname = request.POST['fname']
                mname = request.POST['mname']
                lname = request.POST['lname']
                email = request.POST['email']
                phone = request.POST['phone']
                age = request.POST['age']
                gender = getGender(request.POST['gender'])
                P_prakruti, S_prakruti = getPrakruti(request.POST['prakruti'])

                # Generate Username
                urname = fname+str(random.randint(00, 99))
                while User.objects.filter(username=urname):
                    urname = fname+str(random.randint(00, 99))

                # Generate Passward
                splChar = ['^', '%', '$', '#', '!', '@', '&']
                pwd = fname+random.choice(splChar)+str(random.randint(00, 99))

                # create User
                user = User.objects.create_user(
                    username=urname, password=pwd, email=email, first_name=fname, last_name=lname)
                user.save()
                new_user = Users(UserName=urname, Middle_name=mname,
                                 Phone_No=phone, Age=age, Gender=gender, P_Prakruti=P_prakruti, S_Prakruti=S_prakruti)
                new_user.save()
                messages.success(request, 'User is created.')
            else:
                messages.error(request, 'User is not created.')
        except MultiValueDictKeyError:
            print("Add User: ", MultiValueDictKeyError)

        # remove patient code
        try:
            if request.POST['remove']:
                Ur = Users.objects.get(UserName=request.POST['remove'])
                User.objects.get(username=request.POST['remove']).delete()
                Apts = Appointments.objects.filter(U_id=Ur.pk)
                for Apt in Apts:
                    Apt.delete()
                Ords = Orders.objects.filter(UserName=request.POST['remove'])
                for ord in Ords:
                    mds = Med_per_ord.objects.filter(o_id=ord.o_id)
                    for md in mds:
                        md.delete()
                    ord.delete()
                Ur.delete()
                messages.error(request, 'User is removed.')
            else:
                messages.error(request, 'User is not removed.')
        except MultiValueDictKeyError:
            print("Remove User: ", MultiValueDictKeyError)

        # appintment booking
        try:
            if request.POST['book']:
                print(request.POST['book'])
                dt, slot = getNextAvailableSlot()
                print(dt, slot)
                if dt != null and slot != null:
                    new_apt = Appointments(
                        U_id=request.POST['book'], Date=dt, TimeSlot=slot)
                    new_apt.save()
                    pass
                else:
                    messages.warning(
                        request, 'Slot is not available for next 5 days.')
                    pass
                messages.success(request, 'Appintment is Booked.')
                pass
            else:
                messages.error(request, 'Appintment is not Booked.')
        except MultiValueDictKeyError:
            print("Book Appointment: ", MultiValueDictKeyError)

    if (jinja['pt_sort'] == 'first_name' or jinja['pt_sort'] == 'email'):
        Pts = User.objects.all().order_by(jinja['pt_sort'])
    else:
        Pts = Users.objects.all().order_by(jinja['pt_sort'])
    for Pt in Pts:
        id = Pt.pk
        if (jinja['pt_sort'] == 'first_name' or jinja['pt_sort'] == 'email'):
            Pt_ext = Users.objects.get(UserName=Pt.username)
        else:
            Pt_ext = User.objects.get(username=Pt.UserName)
        if Pt_ext:
            new_pt = vars(Pt)
            new_pt.update(vars(Pt_ext))
            new_pt.pop('_state')
            new_pt.pop('password')
            new_pt.pop('last_login')
            new_pt.pop('is_superuser')
            new_pt.pop('is_staff')
            new_pt.pop('is_active')
            new_pt.pop('date_joined')
            new_pt.pop('UserName')
            new_pt['id'] = id
            new_pts.append(new_pt)
    print("sorting by ", jinja['pt_sort'], new_pts)
    print(new_pts)
    return render(request, 'admin/patients.html', {'patients': new_pts})


def appointments(request):
    new_apts = []
    if request.method == 'POST':
        print(request.POST)
        try:
            if request.POST['search']:
                if request.POST['srch'] == '1':
                    Apts = Appointments.objects.all()
                    for Apt in Apts:
                        string = request.POST['search'].lower()
                        Pt = Users.objects.get(id=Apt.U_id)
                        Pt_exts = User.objects.filter(username=Pt.UserName)
                        for Pt_ext in Pt_exts:
                            strs = (Pt_ext.first_name+" " +
                                    Pt.Middle_name+" " + Pt_ext.last_name)
                            strs = strs.lower()
                            print(string, strs)
                            if string in strs:
                                new_apt = vars(Apt)
                                new_apt['full_name'] = Pt_ext.first_name+' ' + \
                                    Pt.Middle_name+' '+Pt_ext.last_name
                                new_apt['email'] = Pt_ext.email
                                new_apt['phno'] = Pt.Phone_No
                                new_apt['age'] = Pt.Age
                                new_apt['gender'] = Pt.Gender
                                new_apt.pop('_state')
                                new_apts.append(new_apt)
                    return render(request, 'admin/appointments.html', {'Apts': new_apts})
                if request.POST['srch'] == '2':
                    try:
                        Apt = Appointments.objects.get(
                            pk=request.POST['search'])
                        Pt = Users.objects.get(pk=Apt.U_id)
                        Pt_ext = User.objects.get(username=Pt.UserName)
                        new_apt = vars(Apt)
                        new_apt['full_name'] = Pt.first_name+' ' + \
                            Pt_ext.Middle_name+' '+Pt.last_name
                        new_apt['email'] = Pt.email
                        new_apt['phno'] = Pt_ext.Phone_No
                        new_apt['age'] = Pt_ext.Age
                        new_apt['gender'] = Pt_ext.Gender
                        new_apt.pop('_state')
                        new_apts.append(new_apt)
                        return render(request, 'admin/appointments.html', {'Apts': new_apts})
                    except:
                        return render(request, 'admin/appointments.html', {'Apts': new_apts})
                if request.POST['srch'] == '3':
                    mail = str(request.POST['search'])
                    Pts = User.objects.filter(email__icontains=mail.lower())
                    for Pt in Pts:
                        Pt_ext = Users.objects.get(UserName=Pt.username)
                        Apts = Appointments.objects.filter(U_id=Pt_ext.pk)
                        for Apt in Apts:
                            new_apt = vars(Apt)
                            new_apt['full_name'] = Pt.first_name+' ' + \
                                Pt_ext.Middle_name+' '+Pt.last_name
                            new_apt['email'] = Pt.email
                            new_apt['phno'] = Pt_ext.Phone_No
                            new_apt['age'] = Pt_ext.Age
                            new_apt['gender'] = Pt_ext.Gender
                            new_apt.pop('_state')
                            new_apts.append(new_apt)
                    return render(request, 'admin/appointments.html', {'Apts': new_apts})
                if request.POST['srch'] == '4':
                    Pts = Users.objects.filter(
                        Phone_No__icontains=request.POST['search'])
                    for Pt in Pts:
                        Pt_ext = User.objects.get(username=Pt.UserName)
                        Apts = Appointments.objects.filter(U_id=Pt.pk)
                        for Apt in Apts:
                            new_apt = vars(Apt)
                            new_apt['full_name'] = Pt_ext.first_name+' ' + \
                                Pt.Middle_name+' '+Pt_ext.last_name
                            new_apt['email'] = Pt_ext.email
                            new_apt['phno'] = Pt.Phone_No
                            new_apt['age'] = Pt.Age
                            new_apt['gender'] = Pt.Gender
                            new_apt.pop('_state')
                            new_apts.append(new_apt)
                    return render(request, 'admin/appointments.html', {'Apts': new_apts})
                if request.POST['srch'] == '5':
                    Pts = Users.objects.filter(Age__gte=request.POST['search'])
                    for Pt in Pts:
                        Pt_ext = User.objects.get(username=Pt.UserName)
                        Apts = Appointments.objects.filter(U_id=Pt.pk)
                        for Apt in Apts:
                            new_apt = vars(Apt)
                            new_apt['full_name'] = Pt_ext.first_name+' ' + \
                                Pt.Middle_name+' '+Pt_ext.last_name
                            new_apt['email'] = Pt_ext.email
                            new_apt['phno'] = Pt.Phone_No
                            new_apt['age'] = Pt.Age
                            new_apt['gender'] = Pt.Gender
                            new_apt.pop('_state')
                            new_apts.append(new_apt)
                        print(new_apts)
                    return render(request, 'admin/appointments.html', {'Apts': new_apts})
        except MultiValueDictKeyError:
            print('searching', MultiValueDictKeyError)
        # reschedule
        try:
            if request.POST['reschedule']:
                Aid = request.POST['apptID']
                Appnt = request.POST['appnt']
                Day = int(request.POST['day'])-1
                print(request.POST, "\n", Day)
                # appintment reschedule code
                if Day == 2:
                    Date = request.POST['date']
                    if getAvailableSlot(Date, Appnt):
                        new_apt = Appointments.objects.get(id=Aid)
                        new_apt.Date = Date
                        new_apt.TimeSlot = Appnt
                        new_apt.Status_R = True
                        new_apt.save()
                        messages.success(
                            request, 'Appointment slot is booked.')
                    else:
                        messages.warning(
                            request, 'Appointment slot is not available.')
                else:
                    if Day == 1:
                        Date = datetime.now() + timedelta(1)
                    else:
                        Date = datetime.now()
                    Date = Date.strftime('%Y-%m-%d')
                    print(Date)
                    if getAvailableSlot(Date, Appnt):
                        new_apt = Appointments.objects.get(id=Aid)
                        new_apt.Date = Date
                        new_apt.TimeSlot = Appnt
                        new_apt.Status_R = True
                        new_apt.save()
                        messages.success(
                            request, 'Appointment slot is booked.')
                    else:
                        messages.error(
                            request, 'Appointment slot is not available.')
            else:
                messages.error(request, 'Appointment slot is not resheduled.')
        except MultiValueDictKeyError:
            print("Appointment Reschedule: ", MultiValueDictKeyError)

        # prescribe
        try:
            if request.POST['prescribe']:
                Pid = request.POST['P_apptID']
                Presc = request.POST['Description']
                # add prescription code
                new_apt = Appointments.objects.get(id=Pid)
                new_apt.P_med = Presc
                new_apt.Status_A = True
                new_apt.save()
                messages.success(
                    request, 'Remedies are prescribed and Appointment is attended.')
            else:
                messages.error(request, 'Remedies are not prescribed.')
        except MultiValueDictKeyError:
            print("Appointment Prescribe: ", MultiValueDictKeyError)

        # remove
        try:
            if request.POST['remove']:
                # remove appintment code
                # print(request.POST['remove'])
                Appointments.objects.get(id=request.POST['remove']).delete()
                messages.error(request, 'Appointment is deleted.')
            else:
                messages.error(request, 'Appointment is not deleted.')
        except MultiValueDictKeyError:
            print("Appointment Remove: ", MultiValueDictKeyError)

    # view
    Apts = Appointments.objects.all().order_by(jinja['apt_sort'])
    for Apt in Apts:
        patient_ext = Users.objects.get(id=Apt.U_id)
        patient = User.objects.get(username=patient_ext.UserName)
        new_apt = vars(Apt)
        new_apt['full_name'] = patient.first_name+' ' + \
            patient_ext.Middle_name+' '+patient.last_name
        new_apt['email'] = patient.email
        new_apt['phno'] = patient_ext.Phone_No
        new_apt['age'] = patient_ext.Age
        new_apt['gender'] = patient_ext.Gender
        new_apt.pop('_state')
        new_apts.append(new_apt)
    # print(new_apts)
    # print(Apts)
    return render(request, 'admin/appointments.html', {'Apts': new_apts})


def M_remedies(request):

    if request.method == 'POST':
        print(request.POST)
        try:
            if request.POST['sort']:
                jinja['mr_sort'] = request.POST['sort']
                print('hello', jinja['mr_sort'])
        except:
            pass
        try:
            if request.POST['search']:
                if request.POST['srch'] == '1':
                    MRs = M_remedy.objects.filter(
                        Name__icontains=request.POST['search'])
                    return render(request, 'admin/M_remedies.html', {'MRs': MRs})
                if request.POST['srch'] == '2':
                    try:
                        MRs = M_remedy.objects.filter(
                            id=request.POST['search'])
                        return render(request, 'admin/M_remedies.html', {'MRs': MRs})
                    except:
                        MRs = []
                        return render(request, 'admin/M_remedies.html', {'MRs': MRs})
                if request.POST['srch'] == '3':
                    MRs = M_remedy.objects.filter(
                        Price__gte=int(request.POST['search']))
                    return render(request, 'admin/M_remedies.html', {'MRs': MRs})
        except MultiValueDictKeyError:
            print(MultiValueDictKeyError)
        try:
            m_id = request.POST['m_id']
            name = request.POST['name']
            category = request.POST['category']
            description = request.POST['description']
            contents = request.POST['contents']
            quantity = request.POST['quantity']
            price = request.POST['price']
            try:
                picture = request.FILES['inFile']
            except:
                picture = request.POST['ImgURL']

            if request.POST['submit'] == 'Modify':
                # update medicine code
                update_med = M_remedy.objects.get(id=m_id)
                update_med.Name = name
                update_med.Category = category
                update_med.Desc = description
                update_med.Content = contents
                update_med.Quantity = quantity
                update_med.Price = price
                update_med.Img = picture
                update_med.save()
                messages.success(request, 'Medicine Remedy is updated.')
                pass
            else:
                messages.error(request, 'Medicine Remedy is not updated.')

            if request.POST['submit'] == 'Create':
                # add medicine code
                new_med = M_remedy(Name=name, Desc=description, Content=contents,
                                   Quantity=quantity, Price=price, Img=picture, Category=category)
                new_med.save()
                messages.success(request, 'Medicine Remedy is inserted.')
            else:
                messages.error(request, 'Medicine Remedy is not inserted.')
        except MultiValueDictKeyError:
            print("Update and Add medicine: ", MultiValueDictKeyError)

        try:
            if request.POST['remove']:
                # remove medicine code
                mr = M_remedy.objects.get(id=request.POST['remove'])
                mds = Med_per_ord.objects.filter(m_id=mr.pk)
                for md in mds:
                    md.m_id = -1
                    md.save()
                mr.delete()
                messages.error(request, 'Medicine Remedy is deleted.')
            else:
                messages.error(request, 'Medicine Remedy is not deleted.')
        except MultiValueDictKeyError:
            print("Remove medicine: ", MultiValueDictKeyError)

    # view
    MRs = M_remedy.objects.all().order_by(jinja['mr_sort'])
    print('order by :', jinja['mr_sort'], MRs)
    # print(MRs)
    return render(request, 'admin/M_remedies.html', {'MRs': MRs})


def H_remedies(request):
    if request.method == 'POST':
        print(request.POST)
        try:
            if request.POST['sort']:
                jinja['hr_sort'] = request.POST['sort']
                print('hello', jinja['hr_sort'])
        except:
            pass
        try:
            if request.POST['search']:
                if request.POST['srch'] == '1':
                    HRs = H_remedy.objects.filter(
                        Name__icontains=request.POST['search'])
                    return render(request, 'admin/H_remedies.html', {'HRs': HRs})
                if request.POST['srch'] == '2':
                    try:
                        HRs = H_remedy.objects.filter(
                            id=request.POST['search'])
                        return render(request, 'admin/H_remedies.html', {'HRs': HRs})
                    except:
                        HRs = []
                        return render(request, 'admin/H_remedies.html', {'HRs': HRs})
        except MultiValueDictKeyError:
            print(MultiValueDictKeyError)
        try:
            title = request.POST['title']
            desc = request.POST['description']
            acce = request.POST['accessaries']
            try:
                picture = request.FILES['inFile']
            except:
                picture = request.POST['ImgURL']
            if request.POST['submit'] == 'Modify':
                # update remedy code
                h_id = request.POST['hid']
                update_hmed = H_remedy.objects.get(id=h_id)
                update_hmed.Name = title
                update_hmed.Desc = desc
                update_hmed.Accessories = acce
                update_hmed.Img = picture
                update_hmed.save()
                messages.success(request, 'Home Remedy is updated.')
                pass
            else:
                messages.error(request, 'Home Remedy is not updated.')
            if request.POST['submit'] == 'Create':
                # add remedy code
                new_hmed = H_remedy(Name=title, Desc=desc,
                                    Accessories=acce, Img=picture)
                new_hmed.save()
                messages.success(request, 'Home Remedy is inserted.')
            else:
                messages.error(request, 'Home Remedy is not inserted.')
        except MultiValueDictKeyError:
            print("update and add home med: ", MultiValueDictKeyError)

        try:
            if request.POST['remove']:
                # remove remedy code
                H_remedy.objects.filter(id=request.POST['remove']).delete()
                messages.success(request, 'Home Remedy not deleted.')
                pass
            else:
                messages.error(request, 'Home Remedy is not deleted.')
        except MultiValueDictKeyError:
            print("remove home med: ", MultiValueDictKeyError)

    # view
    HRs = H_remedy.objects.all().order_by(jinja['hr_sort'])
    print('order by :', jinja['hr_sort'], HRs)

    return render(request, 'admin/H_remedies.html', {'HRs': HRs})


def blogs(request):
    type = ["BLOG", "IMAGE", "VIDEO"]
    if request.method == 'POST':
        type = ["BLOG", "IMAGE", "VIDEO"]
        print(request.POST)
        print(request.FILES)
        try:
            if request.POST['sort']:
                jinja['bl_sort'] = request.POST['sort']
                print('hello', jinja['bl_sort'])
        except:
            pass
        try:
            if request.POST['search']:
                # if request.POST['srch'] == '1':
                Bls = Blogs.objects.filter(
                    Title__icontains=request.POST['search'])
                return render(request, 'admin/blogs.html', {'Bls': Bls})
                # if request.POST['srch'] == '2':
                #     try:
                #         Bls = Blogs.objects.filter(id = request.POST['search'])
                #         return render(request, 'admin/blogs.html', {'Bls': Bls})
                #     except:
                #         Bls = []
                #         return render(request, 'admin/blogs.html', {'Bls': Bls})
        except MultiValueDictKeyError:
            print(MultiValueDictKeyError)
        try:
            title = request.POST['Title']
            Btype = type[int(request.POST['Btype'])-1]
            File = " "
            content = ' '
            dt = date.today()
            if Btype == 'BLOG':
                content = request.POST['content']
            else:
                try:
                    File = request.FILES['inFile']
                except:
                    File = request.POST['ImgURL']
            if request.POST['submit'] == 'Modify':
                # update blog code
                b_id = request.POST['bid']
                update_blog = Blogs.objects.get(id=b_id)
                update_blog.Title = title
                update_blog.Type = Btype
                update_blog.Content = content
                update_blog.Date = dt
                update_blog.file = File
                update_blog.save()
                messages.success(request, 'Blog is edited.')
                pass
            else:
                messages.error(request, 'Blog is not edited.')
            if request.POST['submit'] == 'Create':
                # add blog code
                new_blog = Blogs(Title=title, Type=Btype,
                                 Content=content, Date=dt, file=File)
                new_blog.save()
                messages.success(request, 'Blog is posted.')
            else:
                messages.error(request, 'Blog is not posted.')
        except MultiValueDictKeyError:
            print("update and add blog: ", MultiValueDictKeyError)

        try:
            if request.POST['remove']:
                # remove blog code
                Blogs.objects.get(id=request.POST['remove']).delete()
                messages.error(request, 'Blog is deleted.')
                pass
            else:
                messages.error(request, 'Blog is not deleted.')
        except MultiValueDictKeyError:
            print("remove blog: ", MultiValueDictKeyError)

    # view
    Bls = Blogs.objects.all().order_by(jinja['bl_sort'])
    print('order by :', jinja['bl_sort'], Bls)
    return render(request, 'admin/blogs.html', {'Bls': Bls})


def orders(request):

    new_ords = []
    if request.POST:
        print(request.POST)
        try:
            if request.POST['sort']:
                jinja['ord_sort'] = request.POST['sort']
                print('hello', jinja['ord_sort'])
        except:
            pass
        # search
        try:
            if request.POST['search']:
                if request.POST['srch'] == '1':
                    string = request.POST['search'].lower()
                    Pts = Users.objects.all()
                    for Pt in Pts:
                        Pt_ext = User.objects.get(username=Pt.UserName)
                        strs = (Pt_ext.first_name+" "+Pt.Middle_name +
                                " " + Pt_ext.last_name).lower()
                        print(string, strs)
                        if string in strs:
                            Ords = Orders.objects.filter(UserName=Pt.UserName)
                            for Ord in Ords:
                                new_ord = vars(Ord)
                                new_ord.pop('_state')
                                new_ord['full_name'] = Pt_ext.first_name + \
                                    " "+Pt.Middle_name+" " + Pt_ext.last_name
                                new_ord['email'] = Pt_ext.email
                                new_ord['phno'] = Pt.Phone_No
                                Pids = Med_per_ord.objects.filter(
                                    o_id=Ord.o_id)
                                print(Pids)
                                Prds = []
                                for Pid in Pids:
                                    temp = {}
                                    Prd = M_remedy.objects.get(id=Pid.m_id)
                                    temp['name'] = Prd.Name
                                    temp['price'] = Prd.Price
                                    temp['quantity'] = Pid.m_qt
                                    temp['m_id'] = Pid.m_id
                                    temp['U_name'] = Pid.U_name
                                    Prds.append(temp)
                                new_ord['products'] = Prds
                                new_ord['amount'] = Ord.Price
                                new_ords.append(new_ord)
                        print(new_ords)
                    return render(request, 'admin/Orders.html', {'orders': new_ords})
                if request.POST['srch'] == '2':
                    try:
                        Ord = Orders.objects.get(o_id=request.POST['search'])
                        Pt = Users.objects.get(UserName=Ord.UserName)
                        Pt_ext = User.objects.get(username=Pt.UserName)
                        new_ord = vars(Ord)
                        new_ord.pop('_state')
                        new_ord['full_name'] = Pt_ext.first_name + \
                            ' '+Pt.Middle_name+' '+Pt_ext.last_name
                        new_ord['email'] = Pt_ext.email
                        new_ord['phno'] = Pt.Phone_No
                        Pids = Med_per_ord.objects.filter(o_id=Ord.o_id)
                        Prds = []
                        for Pid in Pids:
                            temp = {}
                            Prd = M_remedy.objects.get(id=Pid.m_id)
                            temp['name'] = Prd.Name
                            temp['price'] = Prd.Price
                            temp['quantity'] = Pid.m_qt
                            temp['m_id'] = Pid.m_id
                            temp['U_name'] = Pid.U_name
                            Prds.append(temp)
                        new_ord['products'] = Prds
                        new_ord['amount'] = Ord.Price
                        new_ords.append(new_ord)
                        return render(request, 'admin/Orders.html', {'orders': new_ords})
                    except:
                        return render(request, 'admin/Orders.html', {'orders': new_ords})
                if request.POST['srch'] == '3':
                    Pts = User.objects.filter(
                        email__icontains=request.POST['search'])
                    for Pt in Pts:
                        Pt_ext = Users.objects.get(UserName=Pt.username)
                        Ords = Orders.objects.filter(UserName=Pt_ext.UserName)
                        for Ord in Ords:
                            new_ord = vars(Ord)
                            new_ord.pop('_state')
                            new_ord['full_name'] = Pt.first_name+' ' + \
                                Pt_ext.Middle_name+' '+Pt.last_name
                            new_ord['email'] = Pt.email
                            new_ord['phno'] = Pt_ext.Phone_No
                            Pids = Med_per_ord.objects.filter(o_id=Ord.o_id)
                            Prds = []
                            for Pid in Pids:
                                temp = {}
                                Prd = M_remedy.objects.get(id=Pid.m_id)
                                temp['name'] = Prd.Name
                                temp['price'] = Prd.Price
                                temp['quantity'] = Pid.m_qt
                                temp['m_id'] = Pid.m_id
                                temp['U_name'] = Pid.U_name
                                Prds.append(temp)
                            new_ord['products'] = Prds
                            new_ord['amount'] = Ord.Price
                            new_ords.append(new_ord)
                    return render(request, 'admin/Orders.html', {'orders': new_ords})
                if request.POST['srch'] == '4':
                    Pts = Users.objects.filter(
                        email__icontains=request.POST['search'])
                    for Pt in Pts:
                        Pt_ext = User.objects.get(username=Pt.UserName)
                        Ords = Users.objects.filter(UserName=Pt_ext.username)
                        for Ord in Ords:
                            new_ord = vars(Ord)
                            new_ord.pop('_state')
                            new_ord['full_name'] = Pt_ext.first_name + \
                                ' ' + Pt.Middle_name+' '+Pt_ext.last_name
                            new_ord['email'] = Pt_ext.email
                            new_ord['phno'] = Pt.Phone_No
                            Pids = Med_per_ord.objects.filter(o_id=Ord.o_id)
                            Prds = []
                            for Pid in Pids:
                                temp = {}
                                Prd = M_remedy.objects.get(id=Pid.m_id)
                                temp['name'] = Prd.Name
                                temp['price'] = Prd.Price
                                temp['quantity'] = Pid.m_qt
                                temp['m_id'] = Pid.m_id
                                temp['U_name'] = Pid.U_name
                                Prds.append(temp)
                            new_ord['products'] = Prds
                            new_ord['amount'] = Ord.Price
                            new_ords.append(new_ord)
                    return render(request, 'admin/Orders.html', {'orders': new_ords})
                # if request.POST['srch'] == '5':
                #     Ords = Orders.objects.all()
                #     for Ord in Ords:
                #         new_ord = vars(Ord)
                #         new_ord.pop('_state')
                #         patient = User.objects.get(username=Ord.UserName)
                #         patient_ext = Users.objects.get(
                #             UserName=patient.username)
                #         new_ord['full_name'] = patient.first_name+' ' + \
                #             patient_ext.Middle_name+' '+patient.last_name
                #         new_ord['email'] = patient.email
                #         new_ord['phno'] = patient_ext.Phone_No
                #         Pids = Med_per_ord.objects.filter(o_id = Ord.o_id)
                #         Prds = []
                #         for Pid in Pids:
                #             temp = {}
                #             try:
                #                 Prd = M_remedy.objects.filter(id = Pid.m_id).filter(Name__icontains=request.POST['search'])
                #                 for Pr in Prd:
                #                     print(Prd)
                #                     temp['name'] = Pr.Name
                #                     temp['price'] = Pr.Price
                #                     temp['quantity'] = Pid.m_qt
                #                     temp['m_id'] = Pr.id
                #                     temp['U_name'] = Pid.U_name
                #                 Prds.append(temp)
                #             except Exception as e:
                #                 print(e.args)
                #         new_ord['products'] = Prds
                #         new_ord['amount'] = Ord.Price
                #         new_ords.append(new_ord)
                #     return render(request, 'admin/Orders.html', {'orders': new_ords})
        except MultiValueDictKeyError:
            print('Searching', MultiValueDictKeyError)
        # remove
        try:
            if request.POST['remove']:
                # remove order code
                ord = Orders.objects.get(id=request.POST['remove'])
                mds = Med_per_ord.objects.filter(o_id=ord.o_id)
                for md in mds:
                    md.delete()
                ord.delete()
                messages.error(request, 'Oreder is deleted.')
            else:
                messages.error(request, 'Order is not deleted.')
        except MultiValueDictKeyError:
            print('remove', MultiValueDictKeyError)

    # view
    Ords = Orders.objects.all().order_by(jinja['ord_sort'])
    for Ord in Ords:
        new_ord = vars(Ord)
        new_ord.pop('_state')
        patient = User.objects.get(username=Ord.UserName)
        patient_ext = Users.objects.get(UserName=patient.username)
        new_ord['full_name'] = patient.first_name+' ' + \
            patient_ext.Middle_name+' '+patient.last_name
        new_ord['email'] = patient.email
        new_ord['phno'] = patient_ext.Phone_No
        Pids = Med_per_ord.objects.filter(o_id=Ord.o_id)
        Prds = []
        for Pid in Pids:
            temp = {}
            Prd = M_remedy.objects.get(id=Pid.m_id)
            temp['name'] = Prd.Name
            temp['price'] = Prd.Price
            temp['quantity'] = Pid.m_qt
            temp['m_id'] = Pid.m_id
            temp['U_name'] = Pid.U_name
            Prds.append(temp)
        new_ord['products'] = Prds
        new_ord['amount'] = Ord.Price
        new_ords.append(new_ord)
    return render(request, 'admin/Orders.html', {'orders': new_ords})


def A_profile(request):
    if request.POST:
        print(request.POST)
        print(request.FILES)
        try:
            if request.POST['submit']:
                usr = User.objects.get(id=request.POST['patient_id'])
                usr_ext = Users.objects.get(UserName=usr.username)
                usr.first_name = request.POST['Fname']
                usr_ext.Middle_name = request.POST['Mname']
                usr.last_name = request.POST['Lname']
                usr.email = request.POST['Email']
                usr_ext.Phone_No = request.POST['Phone']
                usr_ext.Gender = getGender(request.POST['Gender'])
                usr_ext.Age = request.POST['Age']
                try:
                    usr_ext.P_Prakruti, usr_ext.S_Prakruti = getPrakruti(
                        request.POST['Prakruti'])
                except:
                    pass
                try:
                    print('file', request.FILES['inFile'])
                    usr_ext.Img = request.FILES['inFile']
                except:
                    pass
                usr.save()
                usr_ext.save()
                print("____________________________________")
                print('user updated successfully')
        except:
            pass

        usr = User.objects.get(id=request.POST['patient_id'])
        usr_ext = Users.objects.get(UserName=usr.username)
        Usrs = vars(usr)
        Usrs.update(vars(usr_ext))
        Usrs['admin'] = 0
        Usrs['appnts'] = Appointments.objects.filter(U_id=usr_ext.pk)
        try:
            if request.POST['search']:
                Usrs['appnts'] = Appointments.objects.filter(
                    id=request.POST['search'])
        except:
            Usrs['appnts'] = Appointments.objects.filter(U_id=usr_ext.pk)
        # print(Usrs)
        return render(request, 'admin/A_profile.html', {'users': Usrs})
    usr = User.objects.get(username=request.user.username)
    usr_ext = Users.objects.get(UserName=usr.username)
    Usrs = vars(usr)
    Usrs.update(vars(usr_ext))
    Usrs['admin'] = 1
    return render(request, 'admin/A_profile.html', {'users': Usrs})
