from django.shortcuts import render,HttpResponse
from .models import Registration_Model
from django.shortcuts import redirect
from django.contrib.auth.models import User
import random

# Create your views here.
def registration(request):
    if request.method == "POST":
        a = User.email
        # name  = request.POST.get('name')
        # email = request.POST.get('email')
        # phone = request.POST.get('phone')
        # desc = request.POST.get('desc')
        student_name = request.POST.get('student_name')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        student_contact = request.POST.get('student_contact')
        parent_contact = request.POST.get('parent_contact')
        student_email = request.POST.get('student_email')
        relation = request.POST.get('relation')
        present_address = request.POST.get('present_address')
        permanant_address = request.POST.get('permanant_address')
        district = request.POST.get('district')
        upazila = request.POST.get('upazila')
        postal_zip = request.POST.get('postal_zip')
        sscexam_name = request.POST.get('sscexam_name')
        sscpassing_year = request.POST.get('sscpassing_year')
        sscgpa = request.POST.get('sscgpa')
        ssc_roll = request.POST.get('ssc_roll')
        ssc_registration = request.POST.get('ssc_registration')
        sscboard = request.POST.get('sscboard')
        sscgroup = request.POST.get('sscgroup')
        hscexam_name = request.POST.get('hscexam_name')
        hscpassing_year = request.POST.get('hscpassing_year')
        hscgpa = request.POST.get('hscgpa')
        hsc_roll = request.POST.get('hsc_roll')
        hsc_registration = request.POST.get('hsc_registration')
        hscboard = request.POST.get('hscboard')
        hsc_group = request.POST.get('hsc_group')
        # myuser = User.objects.create_user(hsc_roll,hscboard,hscpassing_year)
        # myuser.save()
        myuser = User.objects.create_user(student_name, student_email, hsc_registration)

        myuser.save()
        score = random.randint(100, 200)
        print(score)

        contact = Registration_Model(user = myuser, student_name = student_name,father_name=father_name, mother_name= mother_name,
                                     student_contact_no=student_contact,parent_contact=parent_contact,student_email=student_email,
                                     relationship=relation,present_adress=present_address,parmanent_adress=permanant_address,District= district,
                                     upazila=upazila, postal_zip=postal_zip,exam_namessc= sscexam_name, passing_yearssc=sscpassing_year,
                                     gpassc=sscgpa, ssc_roll_number=ssc_roll,   ssc_registration_number=ssc_registration,boardssc = sscboard,
                                     sscgroup=sscgroup,exam_namehsc=hscexam_name, passing_yearhsc= hscpassing_year,  gpahsc=hscgpa,
                                     hsc_roll_number=hsc_roll, hsc_registration_number=hsc_registration, boardhsc=  hscboard,
                                     hsc_group=  hsc_group,exam_score = score)
        # contact.user = request.user.username
        contact.save()

        # myuser = User.objects.create_user(student_name, student_email, hsc_registration)
        # myuser.save()
    #     return redirect('/registration/registration1/')
    return render(request, 'registration/registration.html')

def registration1(request):
    i = 0
    for i in range(1,150):
        student_name = 'eee'+str(i)
        print(student_name)
        student_email = 'eee'+ str(i)+'@gmail.com'
        print(student_email)
        hsc_registration = str(i)
        print(hsc_registration)
        father_name = 'f'
        print(father_name)
        mother_name = 'f2'
        student_contact = 2323
        parent_contact = 3434
        relation = 'father'
        present_address = 'fdfddf'
        permanant_address = 'dffdf'
        district = 'dfdf'
        upazila ='dfdf'
        postal_zip = '14'
        sscexam_name = 'ssc'
        sscpassing_year = '2014'
        sscgpa = '5'
        ssc_roll = 12
        ssc_registration = 123
        sscboard = 'dhaka'
        sscgroup = 'Scinece'
        hscexam_name = 'HSC'
        hscpassing_year = '2016'
        hscgpa = '5'
        hsc_roll = 343
        hscboard = 'dfdf'
        hsc_group = 'Engineering'

        myuser = User.objects.create_user(student_name, student_email, hsc_registration)

        myuser.save()
        score = random.randint(100, 200)
        print(score)

        contact = Registration_Model(user=myuser, student_name=student_name, father_name=father_name,
                                     mother_name=mother_name,
                                     student_contact_no=student_contact, parent_contact=parent_contact,
                                     student_email=student_email,
                                     relationship=relation, present_adress=present_address,
                                     parmanent_adress=permanant_address, District=district,
                                     upazila=upazila, postal_zip=postal_zip, exam_namessc=sscexam_name,
                                     passing_yearssc=sscpassing_year,
                                     gpassc=sscgpa, ssc_roll_number=ssc_roll, ssc_registration_number=ssc_registration,
                                     boardssc=sscboard,
                                     sscgroup=sscgroup, exam_namehsc=hscexam_name, passing_yearhsc=hscpassing_year,
                                     gpahsc=hscgpa,
                                     hsc_roll_number=hsc_roll, hsc_registration_number=hsc_registration, boardhsc=hscboard,
                                     hsc_group=hsc_group, exam_score=score)
        # contact.user = request.user.username
        contact.save()

    return HttpResponse('my name is palash')
