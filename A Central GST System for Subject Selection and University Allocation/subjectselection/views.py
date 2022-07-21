from django.shortcuts import render,HttpResponse
from subjectselection.models import JNU_Model,IU_Model,KU_Model,COU_Model,JKKNIU_Model,BRUR_Model,BU_Model,RUB_Model,BDU_Model,SHU_Model,SUST_Model,HSTU_Model,MBSTU_Model,NSTU_Model,JUST_Model,PUST_Model,BSMRSTU_Model,RMSTU_Model,BSFMSTU_Model,PSTU_Model
from registration.models import Registration_Model
from django.contrib.auth.models import User
import random
# Create your views here.
def subjectselection(request):
    a = User.email
    # print(a.value())
    registration = Registration_Model.objects.all()
    print(registration)


    # JNU = JNU_Model.objects.filter(group='science')

    # instance = User.values_list('email', 'username')
    current_user = request.user
    print(current_user.email)
    user_email = current_user.email
    regist = Registration_Model.objects.filter(student_email = user_email)
    print(regist)

    # for item in instance:
    #     print(item)
    # for new_value in a.value():
    #     print(new_value)

    # JNU_group = Registration_Model.objects.values("hsc_group")
    a = regist
    i = 0
    values = None
    print('and its the value',values)
    jnu_group = None
    for new_val in a.values():
        jnu_group = new_val
        print(jnu_group)
    for  key, value in jnu_group.items():
        if i == 27:
           values = value
           print('the fucking value is',value)
        i = i + 1
    print('this is the value',value)
    if values == 'Scinece':
        JNU = JNU_Model.objects.filter(group='science')
        PSTU = PSTU_Model.objects.filter(group='science')
        BSFMSTU = BSFMSTU_Model.objects.filter(group='science')
        RMSTU = RMSTU_Model.objects.filter(group='science')
        BSMRSTU = BSMRSTU_Model.objects.filter(group='science')
        PUST = PUST_Model.objects.filter(group='science')
        JUST = JUST_Model.objects.filter(group='science')
        NSTU = NSTU_Model.objects.filter(group='science')
        MBSTU = MBSTU_Model.objects.filter(group='science')
        HSTU = HSTU_Model.objects.filter(group='science')
        SUST = SUST_Model.objects.filter(group='science')
        SHU = SHU_Model.objects.filter(group='science')
        BDU = BDU_Model.objects.filter(group='science')
        RUB = RUB_Model.objects.filter(group='science')
        BU = BU_Model.objects.filter(group='science')
        BRUR = BRUR_Model.objects.filter(group='science')
        JKKNIU = JKKNIU_Model.objects.filter(group='science')
        COU = COU_Model.objects.filter(group='science')
        JNU = JNU_Model.objects.filter(group='scinece')
        IU = IU_Model.objects.filter(group='science')
        KU = KU_Model.objects.filter(group='science')
    if values == 'Commerce':

        IU = IU_Model.objects.filter(group='commerce')
        JNU = JNU_Model.objects.filter(group='commerce')
        KU = KU_Model.objects.filter(group='commerce')
        COU = COU_Model.objects.filter(group='commerce')
        JKKNIU = JKKNIU_Model.objects.filter(group='commerce')
        BRUR = BRUR_Model.objects.filter(group = 'commerce')
        BU = BU_Model.objects.filter(group='commerce')
        RUB = RUB_Model.objects.filter(group='commerce')
        BDU = BDU_Model.objects.filter(group='commerce')
        SHU = SHU_Model.objects.filter(group='commerce')
        SUST = SUST_Model.objects.filter(group='commerce')
        HSTU = HSTU_Model.objects.filter(group='commerce')
        MBSTU = MBSTU_Model.objects.filter(group='commerce')
        NSTU = NSTU_Model.objects.filter(group='commerce')
        JUST = JUST_Model.objects.filter(group='commerce')
        PUST = PUST_Model.objects.filter(group='commerce')
        BSMRSTU = BSMRSTU_Model.objects.filter(group='commerce')
        RMSTU = RMSTU_Model.objects.filter(group='commerce')
        BSFMSTU = BSFMSTU_Model.objects.filter(group='commerce')
        PSTU = PSTU_Model.objects.filter(group='commerce')

    if values =='Humanities':
        JNU = JNU_Model.objects.filter(group = 'humanities')
        IU = IU_Model.objects.filter(group='humanities')
        KU = KU_Model.objects.filter(group='humanities')
        COU = COU_Model.objects.filter(group='humanities')
        JKKNIU = JKKNIU_Model.objects.filter(group='humanities')
        BRUR = BRUR_Model.objects.filter(group='humanities')
        BU = BU_Model.objects.filter(group='humanities')
        RUB = RUB_Model.objects.filter(group='humanintes')
        BDU = BDU_Model.objects.filter(group='humanities')
        SHU = SHU_Model.objects.filter(group='humanities')
        SUST = SUST_Model.objects.filter(group='humanities')
        HSTU = HSTU_Model.objects.filter(group='humanities')
        MBSTU = MBSTU_Model.objects.filter(group='humanities')
        NSTU = NSTU_Model.objects.filter(group='humanities')
        JUST = JUST_Model.objects.filter(group='humanities')
        PUST = PUST_Model.objects.filter(group='humanities')
        BSMRSTU = BSMRSTU_Model.objects.filter(group='humanities')
        RMSTU = RMSTU_Model.objects.filter(group='humanities')
        BSFMSTU = BSFMSTU_Model.objects.filter(group='humanities')
        PSTU = PSTU_Model.objects.filter(group='humanities')
    if values == 'Engineering':
        JNU = JNU_Model.objects.filter(group='engineering')
        IU = IU_Model.objects.filter(group='engineering')
        KU = KU_Model.objects.filter(group='engineering')
        COU = COU_Model.objects.filter(group='engineering')
        JKKNIU = JKKNIU_Model.objects.filter(group='engineering')
        BRUR = BRUR_Model.objects.filter(group='engineering')
        BU = BU_Model.objects.filter(group='engineering')
        RUB = RUB_Model.objects.filter(group='engineering')
        BDU = BDU_Model.objects.filter(group='engineering')
        SHU = SHU_Model.objects.filter(group='engineering')
        SUST = SUST_Model.objects.filter(group='engineering')
        HSTU = HSTU_Model.objects.filter(group='engineering')
        MBSTU = MBSTU_Model.objects.filter(group='engineering')
        NSTU = NSTU_Model.objects.filter(group='engineering')
        JUST = JUST_Model.objects.filter(group='engineering')
        PUST = PUST_Model.objects.filter(group='engineering')
        BSMRSTU = BSMRSTU_Model.objects.filter(group='engineering')
        RMSTU = RMSTU_Model.objects.filter(group='engineering')
        BSFMSTU = BSFMSTU_Model.objects.filter(group='engineering')
        PSTU = PSTU_Model.objects.filter(group='engineering')


    # else:
    #     JNU = JNU_Model.objects.filter(group='humanities')

    context = {'JNU':JNU,'IU':IU,'KU':KU,'COU':COU,'JKKNIU':JKKNIU,'BRUR':BRUR,'BU':BU,'RUB':RUB,'BDU':BDU,'SHU':SHU,'SUST':SUST,'HSTU':HSTU,'MBSTU':MBSTU,'NSTU':NSTU,'JUST':JUST,'PUST':PUST,'BSMRSTU':BSMRSTU,'RMSTU':RMSTU,'BSFMSTU':BSFMSTU,'PSTU':PSTU}
    return render(request, 'subjectselection/subjectselection.html',context)
