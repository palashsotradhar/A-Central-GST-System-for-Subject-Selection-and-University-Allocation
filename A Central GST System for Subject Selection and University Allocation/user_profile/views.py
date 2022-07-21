from django.shortcuts import render,HttpResponse
from registration.models import Registration_Model
from .models import Selected_Subject_Model
from ranking.models import  Subject_and_University_Model2

# Create your views here.
def user_profile(request):
    if request.method == "POST":
        current_user = request.user
        print(current_user.email)
        user_email = current_user.email
        regist = Registration_Model.objects.filter(student_email=user_email)
        # regist = regist.split(") ")
        # print(regist)
        a = regist
        i = 0
        name = None
        jnu_group = None
        for new_val in a.values():
            jnu_group = new_val
            # print(jnu_group)
        for key, value in jnu_group.items():
            if i == 2:
                name = value
            i = i + 1
        subject_name = request.POST.get('subjects')
        # print(subject_name)

        all_subject = subject_name.split(")")
        print(all_subject)
        del all_subject[-1]
        for one_subject in all_subject:
            # print(one_subject,end='')
            subject_and_university = one_subject.split('(')
            student_subject_name = None
            student_university_name = None
            choosen_number = None
            # list = ['a','b']
            # print(list[1])
            # print(subject_and_university)
            # print(subject_and_university[0])
            # print(subject_and_university[1])
            i = 0
            for subject_or_university in subject_and_university:

                if i == 0:
                    subject_name = subject_or_university.split('.')
                    choosen_number = int(subject_name[0])
                    student_subject_name = subject_name[1]
                    # context = Selected_Subject_Model(subject_name = subject_name[1],email = user_email)
                    # context.save()
                    print("its subject name",subject_name[1])
                    print("its choosen number",choosen_number)
                if i ==1:
                    print("its uni name",subject_or_university)
                    # context = Selected_Subject_Model( = subject_or_university)
                    student_university_name = subject_or_university
                    # context.save()
                # university_name
                i = i + 1
            context = Selected_Subject_Model(subject_name=student_subject_name, university_name=student_university_name,
                                             email=user_email,choosen_number = choosen_number)
            context.save()



        # print(x)
        # subject_name = subject_name.split(")")
        # print(subject_name)
        # yourList = subject_name
        # butFirst = yourList[1:]
        # subject_name = "\n".join(butFirst)
        # print(subject_name)
        context = {'subject_name':subject_name,'name':name}
    else:
        profile_data = Subject_and_University_Model2.objects.filter(student_email = request.user.email)
        choise_list = Selected_Subject_Model.objects.filter(email = request.user.email).order_by('choosen_number')
        print('fdfdfdf',choise_list)
        context = {'profile_data':profile_data,'choise_list':choise_list}

    return render(request, 'user_profile/user_profile.html',context)