from Prakruti_App.models import Prakruti_Quetions_Ans


def UpdatePrakrutiQuestiosAnsByUserID(UserID, age, request):
    UserQuetionsAns = Prakruti_Quetions_Ans.objects.get(u_id=UserID)
    UserQuetionsAns.age = age
    UserQuetionsAns.ans1 = request.POST['1']
    UserQuetionsAns.ans2 = request.POST['2']
    UserQuetionsAns.ans3 = request.POST['3']
    UserQuetionsAns.ans4 = request.POST['4']
    UserQuetionsAns.ans5 = request.POST['5']
    UserQuetionsAns.ans6 = request.POST['6']
    UserQuetionsAns.ans7 = request.POST['7']
    UserQuetionsAns.ans8 = request.POST['8']
    UserQuetionsAns.ans9 = request.POST['9']
    UserQuetionsAns.ans10 = request.POST['10']
    UserQuetionsAns.ans11 = request.POST['11']
    UserQuetionsAns.ans12 = request.POST['12']
    UserQuetionsAns.ans13 = request.POST['13']
    UserQuetionsAns.ans14 = request.POST['14']
    UserQuetionsAns.ans15 = request.POST['15']
    UserQuetionsAns.ans16 = request.POST['16']
    UserQuetionsAns.ans17 = request.POST['17']
    UserQuetionsAns.ans18 = request.POST['18']
    UserQuetionsAns.ans19 = request.POST['19']
    UserQuetionsAns.ans20 = request.POST['20']
    UserQuetionsAns.ans21 = request.POST['21']
    UserQuetionsAns.ans22 = request.POST['22']
    UserQuetionsAns.ans23 = request.POST['23']
    UserQuetionsAns.save()


def AddPrakrutiQuestiosAns(UserID, age, request):
    Answers = Prakruti_Quetions_Ans(u_id=UserID, age=age, ans1=request.POST['1'], ans2=request.POST['2'],
                                ans3=request.POST['3'], ans4=request.POST['4'], ans5=request.POST['5'],
                                ans6=request.POST['6'], ans7=request.POST['7'], ans8=request.POST['8'],
                                ans9=request.POST['9'], ans10=request.POST['10'], ans11=request.POST['11'],
                                ans12=request.POST['12'], ans13=request.POST['13'], ans14=request.POST['14'],
                                ans15=request.POST['15'], ans16=request.POST['16'], ans17=request.POST['17'],
                                ans18=request.POST['18'], ans19=request.POST['19'], ans20=request.POST['20'],
                                ans21=request.POST['21'], ans22=request.POST['22'], ans23=request.POST['23'])
    Answers.save()
