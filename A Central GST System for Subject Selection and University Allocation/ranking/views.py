from django.shortcuts import render,HttpResponse
from registration.models import Registration_Model
from registration.models import Registration_Model
from django.contrib.auth.models import User
from user_profile.models import Selected_Subject_Model
from ranking.models import Subject,Email_Model,Subject_and_University_Model,Subject_and_University_Model2
from subjectselection.models import Counter_Model
# Create your views here.
def ranking_value(mail):
    email_model = Registration_Model.objects.filter(student_email = mail)

    print(email_model)
    i = 0
    values = None
    # print('and its the value', values)
    jnu_group = None
    mail_value = None
    ranking_username = None
    ranking_registration_number = None
    ranking_scoore = None
    print("this is on under contorl")
    for new_val in email_model.values():
        jnu_group = new_val
        # print(jnu_group)
    for key, value in jnu_group.items():
        # print(i,value)
        if i == 2:
            ranking_username = value
            # print('mail_value',mail_value)
        if i == 25:
            ranking_registration_number = value
            # print('mail_value',mail_value)
        if i == 28:
            ranking_scoore = value
        i = i + 1
    print('its a mail value', ranking_username,ranking_scoore,ranking_registration_number)
    return ranking_username,ranking_registration_number,ranking_scoore

def subject_selet(valueee,mail):


    # print("its under in the funtion")
    email_model = Email_Model.objects.all()
    print(email_model)
    i = 0
    values = None
    # print('and its the value', values)
    jnu_group = None
    mail_value = None
    print("this is on under contorl")
    for new_val in email_model.values():
        jnu_group = new_val
        # print(jnu_group)
    for key, value in jnu_group.items():
        # print(value)
        if i == 1:
            mail_value = value
            # print('mail_value',mail_value)
        i = i + 1
    print('its a mail value',mail_value)
    print('its a mail',mail)
    if mail_value == mail:
        print("its not a joke")



    # print('this is the values resdfbdbfdfdfnfndjbfdfjdnf')
    # print('this is the valuefdfdfdfdff', mail_value)


    else:
        print("its under else and itsa good point")
        a = Subject.objects.filter(subject_name = valueee)
        count = Subject.objects.filter(subject_name = valueee).count()
        print(count)
        # print('fdfdfdf',a)
        if count > 0:

            # dfdfdfdsfdsfdsfdsfdsf
            i = 0
            values = None
            print('and its the value', values)
            jnu_group = None
            no_of_seat = None
            university_and_subject = None
            subject_id = None
            for new_val in a.values():
                jnu_group = new_val
                # print(jnu_group)
            for key, value in jnu_group.items():
                if i == 2:
                    no_of_seat = value - 1
                    # print("no_of_seat",no_of_seat)

                if i == 1:
                    university_and_subject = value
                    # print('university and subject name',university_and_subject)
                if i == 0:
                    subject_id = value
                    # print('the fucking value is', subject_id)
                i = i + 1
                # print(value)

            # print('this is the value', values)
            print('what is the fucking value',valueee)

            print('this is the value', valueee, 'this is the no of seat', no_of_seat)
            if valueee == 'GeoInformationScienceandEarthObservationPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='GeoInformation Scienceand Earth Observation',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnvironmentalSciencePSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='Environmental Science',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'GeoInformationScienceandEarthObservationPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='GeoInformation Scienceand Earth Observation',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Mathematics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Statistics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnvironmentalScienceandGeographyIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='EnvironmentalScienceandGeography',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AppliedNutritionandFoodTechnologyIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='AppliedNutrition and FoodTechnology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiotechnologyandGeneticEngineeringIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Biotechnology and GeneticEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PharmacyIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Pharmacy',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsDeciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='MathematicsDecipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsDeciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Physics Decipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemistryDeciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='ChemistryDecipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsDeciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Statistics Decipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ForestryAndWoodTechnologyDeciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Forestry And WoodTechnology Decipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FesheiesAndMarineTechnologyDeciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Fesheies And MarineTechnologyDecipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiotechnologyandGeneticEngineeringDeciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='BiotechnologyandGeneticEngineeringDecipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AgrotechnologyDeciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='AgrotechnologyDecipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnvironmentalScienceDeciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Environmental ScienceDecipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PharmacyDeciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='PharmacyDecipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SoilWaterAndEnvironmentalDiciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='SoilWater And EnvironmentalDicipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Mathematics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Physics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Statistics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemistryCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Chemistry',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PharmacyCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Pharmacy',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='Statistics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Mathematics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Statistics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='PhysicsBRUR',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemistryBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Chemistry',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'GeographyandEnvironmentalScienceBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Geography and EnvironmentalScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'DisasterManagementBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Disaster Management',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Electrical & Electronic Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Mathematics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemistryBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Chemistry',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Physics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'GeologyandMiningBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Geology and Mining',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Statistics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SoilandEnvironmentalSciencesBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Soil and Environmental Sciences',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BotanyBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Botany',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'CoastalStudiesandDisasterManagementBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='CoastalStudiesandDisasterManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiochemistryandBiotechnologyBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Biochemistry and Biotechnology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EducationBDU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BDU',
                                                                            student_subject='Education',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemistrySUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Chemistry',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'GeographyandEnvironmentSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Geography and Environment',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Mathematics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Statistics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Physics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'OceanographySUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Oceanography',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Forestry&EnvironmentalScienceSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Forestry & EnvironmentalScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiochemistryandMolecularBiologySUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Biochemistry and MolecularBiology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'GeneticEngineering&BiotechnologySUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='GeneticEngineering & Biotechnology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AgricultureHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='Agriculture',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FisheriesHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='FisheriesHSTU',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'VeterinaryandAnimalScienceHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='Veterinary and AnimalScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemistryHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='Chemistry',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemistryHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='ChemistryHSTU',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='Mathematics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='Statistics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnvironmentalScienceandResourceManagementMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='EnvironmentalScience and ResourceManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'CriminologyandPoliceScienceMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='Criminology and PoliceScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FoodTechnologyandNutritionalScienceMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='FoodTechnology and NutritionalScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiotechnologyandGeneticEngineeringMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='Biotechnology and GeneticEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PharmacyMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='Pharmacy',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiochemistryandMolecularBiologyMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='BiochemistryandMolecularBiology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemistryMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='Chemistry',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='Mathematics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='Physics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='StatisticsMBSTU',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FisheriesandMarineScienceNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='FisheriesandMarineScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PharmacyNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Pharmacy',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MicrobiologyNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Microbiology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AppliedMathematicsNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='AppliedMathematics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FoodTechnologyandNutritionScienceNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='FoodTechnologyandNutritionScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnvironmentalScienceandDisasterManagementNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='EnvironmentalScienceandDisasterManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiotechnologyandGeneticEngineeringNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='BiotechnologyandGeneticEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AgricultureNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Agriculture',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Statistics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'OceanographyNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Oceanography',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiochemistryandMolecularBiologyNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Biochemistry and MolecularBiology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ZoologyNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Zoology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AgroProductProcessingTechnologyJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='AgroProduct ProcessingTechnology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ClimateandDisasterManagementJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='ClimateandDisasterManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnvironmentalScienceandTechnologyJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='EnvironmentalScience and TechnologyJUST',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'NutritionandFoodTechnologyJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='Nutrition and FoodTechnology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FisheriesandMarineBioscienceJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='Fisheries and MarineBioscience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'GeneticEngineeringandBiotechnologyJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='GeneticEngineeringandBiotechnology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MicrobiologyJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='Microbiology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PharmacyJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='PharmacyJUST',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'NursingandHealthScienceJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='NursingandHealthScienceJUS',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicalEducationandSportsScienceJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='PhysicalEducation and SportsScienceJUSTGeoInformation Scienceand Earth Observation',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysiotherapyandRehabilitationJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='Physiotherapy and Rehabilitation',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemistryJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='Chemistry',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='MathematicsJUST',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='Physics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='Mathematics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='Physics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='Physics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PharmacyPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='Pharmacy',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='Statistics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'GeographyandEnvironmentPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='GeographyandEnvironment',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PharmacyBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='Pharmacy',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiotechnologyandGeneticEngineeringBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='BiotechnologyandGeneticEngineeringBSMRSTU',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PsychologyBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='PsychologyBSMRSTU',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BotanyBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='BotanyBSMRSTU',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BotanyBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='BotanyBSMRSTU',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='MathematicsBSMRSTU',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'StatisticsBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='Statistics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemistryBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='Chemistry',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='Physics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhysicsBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='Physics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ForestryandEnvironmentalScienceRMSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='RMSTU',
                                                                            student_subject='ForestryandEnvironmentalScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MathematicsBSFMSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSFMSTU',
                                                                            student_subject='Mathematics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiochemistryandFoodAnalysisPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='Biochemistry and FoodAnalysis',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiochemistryandFoodAnalysisPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='BiochemistryandFoodAnalysis',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnvironmentalSanitationPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='EnvironmentalSanitation',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FoodMicrobiologyPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='FoodMicrobiology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'HumanNutritionandDieteticsPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='HumanNutritionandDieteticsPSTU',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PostHarvestTechnologyandMarketingPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='PostHarvestTechnologyandMarketing',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'DisasterResilienceandEngineeringPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='DisasterResilience and Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True

            if valueee == 'DisasterRiskManagementPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='DisasterRiskManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EmergencyManagementPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='EmergencyManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[
                                                                                1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Science')
                subject_and_university_save.save()
                sucsess = True





            if valueee == 'BiomedicalEngineeringIU' and no_of_seat >= 0:
                print('its the bidirectiona')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail )
                print('its the bidirectiona')
                ranking_val = ranking_value(mail)
                regis = Email_Model(id = 1,email_name = mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email = mail,student_university = 'IU',student_subject = 'BiomedicalEngineering',ranking_score = ranking_val[2],
                                                                            ranking_registration_number = ranking_val[1],ranking_username = ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True

                # BiomedicalEngineeringIU -= 1
                # selected_subject = ['Biomedical Engineering','IU']
                # return selected_subject
            if valueee == 'AppliedChemistry&ChemicalEngineeringIU' and no_of_seat >= 0:
                print('its the bidirectiona')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectiona')
                ranking_val = ranking_value(mail)
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='IU',
                                                                            student_subject='AppliedChemistry & Chemical Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringIU' and no_of_seat >= 0:
                print('its the bidirectiona')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectiona')
                ranking_val = ranking_value(mail)
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='IU',
                                                                            student_subject='Electrical & Electronic Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Information&CommunicationTechnologyIU' and no_of_seat >= 0:
                print('its the bidirectiona')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectiona')
                ranking_val = ranking_value(mail)
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='IU',
                                                                            student_subject='Information & CommunicationTechnology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True

            if valueee == 'Computerscience&EngineeringIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='IU',
                                                                           student_subject='Computerscience&Engineering',ranking_score = ranking_val[2],
                                                                            ranking_registration_number = ranking_val[1],ranking_username = ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electronics&CommunicationEngineeringDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='KU',
                                                                            student_subject='Electronics & Communication Engineering Discipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Urban&RuralPlanningDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='KU',
                                                                            student_subject='Urban & RuralPlanning Discipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ComputerScience&EngineeringDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='KU',
                                                                            student_subject='Computer Science & Engineering Discipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ArchitectureDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='KU',
                                                                            student_subject='ArchitectureDiscipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='COU',
                                                                            student_subject='Computer science & Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Information&CommunicationTechnologyCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='COU',
                                                                            student_subject='Information & Communication Technology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='JKKNIU',
                                                                            student_subject='Computerscience & Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='JKKNIU',
                                                                            student_subject='Electrical & Electronic Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnviornmentalScience&EngineeringJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='JKKNIU',
                                                                            student_subject='EnviornmentalScience&Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BRUR',
                                                                            student_subject='Computer science & Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ComputerScience&EngineeringBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BU',
                                                                            student_subject='ComputerScience&Engineeringe',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Information&CommunicationTechnologyBDU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BDU',
                                                                            student_subject='Information & Communication Technology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringSHU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='SHU',
                                                                            student_subject='Computerscience&Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ArchitectureSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='SUST',
                                                                            student_subject='Architecture',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemicalEngineering&PolimerScienceSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='SUST',
                                                                            student_subject='Chemical Engineering & PolimerScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Civil&EmviornmentEngineeringSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='SUST',
                                                                            student_subject='Civil & Emviornment Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='SUST',
                                                                            student_subject='Computer science & Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='SUST',
                                                                            student_subject='Electrical & Electronic Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FoodEngineering&TeaTechnologySUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='SUST',
                                                                            student_subject='FoodEngineering & TeaTechnology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Industrial&ProductionEngineeringSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='SUST',
                                                                            student_subject='Industrial & Production Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Petroleum&MiningEngineeringSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='SUST',
                                                                            student_subject='Petroleum & Mining Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MechanicalEngineeringSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='SUST',
                                                                            student_subject='Mechanical Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='HSTU',
                                                                            student_subject='Computerscience & Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='HSTU',
                                                                            student_subject='Electrical & Electronic Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electronics&CommunicationEngineeringHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='HSTU',
                                                                            student_subject='Electronics & Communication Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='MBSTU',
                                                                            student_subject='Computerscience & Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Information&CommunicationTechnologyMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='MBSTU',
                                                                            student_subject='Information&CommunicationTechnology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'TextileMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='MBSTU',
                                                                            student_subject='Textile',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MechanicalEngineeringMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='MBSTU',
                                                                            student_subject='MechanicalEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ComputerScience&TelecomunicationEngineeringNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='NSTU',
                                                                            student_subject='ComputerScience & Telecomunication Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Information&ComunicationEngineeringNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='NSTU',
                                                                            student_subject='Information & Comunication Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AppliedChemistry&ChemicalEngineeringNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='NSTU',
                                                                            student_subject='AppliedChemistry & Chemical Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='NSTU',

                                                                            student_subject='Electrical & Electronic Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SoftwareEngineeringNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='NSTU',
                                                                            student_subject='Software Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ChemicalEngineeringJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='JUST',
                                                                            student_subject='ChemicalEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BiomedicalEngineeringJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='JUST',
                                                                            student_subject='Biomedical Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='JUST',
                                                                            student_subject='Computerscience&Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='JUST',
                                                                            student_subject='Electrical & Electronic Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Industrial&ProductionEngineeringJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='JUST',
                                                                            student_subject='Industrial & ProductionEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Petroleum&MiningEngineeringJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='JUST',
                                                                            student_subject='Petroleum & MiningEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='PUST',
                                                                            student_subject='Computerscience & Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='PUST',
                                                                            student_subject='Electrical & Electronic Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical,Electronic&ComunicationEngineeringPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='PUST',
                                                                            student_subject='Electrical,Electronic & ComunicationEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Information&ComunicationEngineeringPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='PUST',
                                                                            student_subject='Information&ComunicationEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'CivilEngineeringPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='PUST',
                                                                            student_subject='CivilEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Urban&RuralPlanningPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='PUST',
                                                                            student_subject='Urban&RuralPlanning',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ArchitecturePUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='PUST',
                                                                            student_subject='Architecture',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BSMRSTU',
                                                                            student_subject='Computerscience & Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BSMRSTU',
                                                                            student_subject='Electrical & ElectronicEngineering ArchitectureDiscipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AppliedChemistry&ChemicalEngineeringBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BSMRSTU',
                                                                            student_subject='AppliedChemistry&ChemicalEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'CivilEngineeringBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BSMRSTU',
                                                                            student_subject='CivilEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ArchitectureBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BSMRSTU',
                                                                            student_subject='Architecture',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Food&AgroProcessingTechnologyBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BSMRSTU',
                                                                            student_subject='Food & Agro Processing Technology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ComputerSceince&engineeringRMSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='RMSTU',
                                                                            student_subject='Computer Sceince & engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computerscience&EngineeringBSFMSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BSFMSTU',
                                                                            student_subject='Computerscience & Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringBSFMSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='BSFMSTU',
                                                                            student_subject='Electrical&ElectronicEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Computer&ComunicationEngineeringPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='PSTU',
                                                                            student_subject='Computerv&vComunication Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ComputerScience&InformationEngineeringPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='PSTU',
                                                                            student_subject='ComputerScience&InformationEngineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Electrical&ElectronicEngineeringPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail, student_university='PSTU',
                                                                            student_subject='Electrical & Electronic Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Physics&MechanicalEngineeringPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='Physics & Mechanical Engineering',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Engineering')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Economics Discipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SociologyDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Sociology Discipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'DevelopmentStudiesDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Development Studies Discipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MassCommunication&JournalismDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='MassCommunication & JournalismDiscipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='English Discipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            # if valueee == 'EnglishDisciplineKU' and no_of_seat >= 0:
            #     print('its the bidirectionacomputer')
            #     print("no_of_seatededdd", no_of_seat)
            #     reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
            #     reg.save()
            #     print('############################')
            #     print(mail)
            #     print('its the bidirectionacomputer')
            #     ranking_val = ranking_value(mail)
            #     # print('rank_value',ranking_val[1])
            #     # print('rank_value', ranking_val[0])
            #     # print('rank_value', ranking_val[2])
            #     regis = Email_Model(id=1, email_name=mail)
            #     regis.save()
            #     subject_and_university_save = Subject_and_University_Model2(student_email=mail,
            #                                                                 student_university='KU',
            #                                                                 student_subject='English Discipline',
            #                                                                 ranking_score=ranking_val[2],
            #                                                                 ranking_registration_number=ranking_val[1],
            #                                                                 ranking_username=ranking_val[0],ranking_group = 'Humanities')
            #     subject_and_university_save.save()
            #     sucsess = True
            if valueee == 'BanglaDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='BanglaDiscipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'HistoryandCivilizationDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Historyand Civilization Discipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'LawDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Law Discipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'InstituteofEducationandResearchKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='Institute of EducationandResearch',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Al-QuranandIslamicStudiesIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Al-QuranandIslamicStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Da’wah&IslamicStudiesIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Da’wah&IslamicStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Al-Hadith&IslamicStudiesIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Al-Hadith&IslamicStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BengaliIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Bengali',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ArabicLanguageandLiteratureiIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='ArabicLanguageandLiteraturei',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'IslamicHistoryandCultureIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='IslamicHistory and Culture',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FineArtsIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='FineArts',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PublicAdministrationIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='PublicAdministration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PoliticalScienceIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Political Science',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FolkloreStudiesIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Folklore Studies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'DevelopmentStudiesIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='DevelopmentStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SocialWelfareIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='SocialWelfare',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'LawIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Law',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Al-FiqhandLegalStudiesIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Al-FiqhandLegalStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'LawandLandManagementIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='LawandLandManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BanglaCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Bangla',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ArchaeologyCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Archaeology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PublicAdministrationCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='PublicAdministration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AnthropologyCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Anthropology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MassCommunicationandJournalismCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='MassCommunicationandJournalism',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'LawCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Law',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'LanguageandLiteratureJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='LanguageandLiterature',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishLanguageandLiteratureJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='EnglishLanguageandLiterature',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MusicJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='Music',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'TheatreandPerformanceStudiesJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='TheatreandPerformanceStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FilmandMediaJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='FilmandMedia',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhilosophyJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='Philosophy',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PublicAdministrationandGovernanceStudiesJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='PublicAdministrationandGovernanceStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FolkloreJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='Folklore',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AnthropologyJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='Anthropology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PopulationScienceJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='Population Science',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'LocalGovernmentandUrbanDevelopmentJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='LocalGovernmentandUrbanDevelopment',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SociologyJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='Sociology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'LawandJusticeJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='LawandJustice',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FineArtsJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='FineArts',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BanglaBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='RUR',
                                                                            student_subject='Bangla',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'History&ArchaeologyBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='History&Archaeology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PoliticalScienceBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Political Science',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SociologyBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Sociology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'GenderStudiesandDevelopmentStudiesBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Gender Studies and DevelopmentStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MassCommunicationandJournalismBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='MassCommunication and Journalism',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PublicAdministrationBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='PublicAdministration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PoliticalScienceBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Political Science',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SociologyBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Sociology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PublicAdministrationBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='PublicAdministration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'banglaBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='bangla',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhilosophyBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Philosophy',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MassCommunication&JournalismBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='MassCommunication&Journalism',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'HistoryandCivilizationBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='HistoryandCivilization',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'LawBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Law',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishSHU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SHU',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BanglaSHU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SHU',
                                                                            student_subject='Bangla',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsSHU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SHU',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AnthropologySUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Anthropology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BanglaSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Bangla',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PoliticalStudiesSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='PoliticalStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PublicAdministrationSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='PublicAdministration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SocialWorkSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='SocialWork',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SociologySUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Sociology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SociologyHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='Sociology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'DevelopmentStudiesHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='DevelopmentStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBTU',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBTU',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'InformationSciencesandLibraryManagementNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='InformationSciencesandLibraryManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BangladeshandLiberationWarStudiesNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='BangladeshandLiberationWarStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SociologyNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Sociology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BanglaNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Bangla',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SocialWorkNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='SocialWork',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EducationNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Education',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EducationalAdministrationNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='EducationalAdministration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'LawNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='Law',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishJUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JUST',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BanglaPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='Bangla',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SocialWorkPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='SocialWork',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PublicAdministrationPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='PublicAdministration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'HistoryandBangladeshStudiesPUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PUST',
                                                                            student_subject='HistoryandBangladeshStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BanglaBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='Bangla',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'HistoryBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='History',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SociologyBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='Sociology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PublicAdministrationBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='PublicAdministration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'InternationalRelationsBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='International Relations',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PoliticalScienceBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='PoliticalScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'LawBSMRSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSMRSTU',
                                                                            student_subject='Law',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SocialWorkBSFMSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSFMSTU',
                                                                            student_subject='SocialWork',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FisheriesBSFMSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BSFMSTU',
                                                                            student_subject='Fisheries',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Science')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SocialWorkPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='SocialWork',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EnglishJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='English',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'HistoryJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='History',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PhilosophyJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='Philosophy',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'IslamicStudiesJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='IslamicStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'EconomicsJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='Economics',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PoliticalScienceJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='PoliticalScience',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SociologyJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='Sociology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AnthropologyJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='Anthropology',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'SocialWorkJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='SocialWork',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MassCommunicationandJournalismJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='MassCommunicationandJournalism',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'PublicAdministrationJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='PublicAdministration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Humanities')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'TourismandHospitalityManagementPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='Tourism and Hospitality Management',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BusinessAdministrationPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='PSTU',
                                                                            student_subject='Business Administration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],ranking_group = 'Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'Accounting&InformationSystemJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='Accounting&InformationSystem',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementStudiesJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='ManagementStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FinanceJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='Finance',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MarketingJNU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JNU',
                                                                            student_subject='Marketing',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AccountingandInformationSystemsIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Accounting and InformationSystems',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Management',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FinanceandBankingIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Finance and Banking',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MarketingIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='Marketing',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'HumanResourceManagementIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='HumanResourceManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'TourismandHospitalityManagementIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='IU',
                                                                            student_subject='TourismandHospitalityManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BusinessAdministrationDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='BusinessAdministrationDiscipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'HumanResourceManagementDisciplineKU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='KU',
                                                                            student_subject='HumanResourceManagementDiscipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementStudiesCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='ManagementStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementStudiesCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='ManagementStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AccountingandInformationSystemsCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='AccountingandInformationSystems',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MarketingCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='Marketing',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FinanceandBankingCOU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='COU',
                                                                            student_subject='FinanceandBankin',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AccountingandInformationSystemsJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='AccountingandInformationSystems',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BusinessAdministrationPSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='BusinessAdministrationPSTU',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'HumanResourceManagementJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='HumanResourceManagement',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='Management',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MarketingJKKNIU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='JKKNIU',
                                                                            student_subject='Marketing',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ACCOUNTINGANDINFORMATIONSYSTEMBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='ACCOUNTINGANDINFORMATIONSYSTEM',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FinanceandBankingBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='FinanceandBanking',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementStudiesBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='ManagementStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MarketingBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='Marketing',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementInformationSystemsBRUR' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BRUR',
                                                                            student_subject='ManagementInformationSystems',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementStudiesBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='ManagementStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AccountingandInformationSystemsBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='AccountingandInformationSystems',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MarketingBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='Marketing',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FinanceandBankingBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='FinanceandBanking',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FinanceandBankingBU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='FinanceandBanking',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementStudiesRUB' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='BU',
                                                                            student_subject='ManagementStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementStudiesRUB' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='RUB',
                                                                            student_subject='ManagementStudies',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BusinessAdministrationSUST' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='SUST',
                                                                            student_subject='Business Administration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AccountingHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='Accounting',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'FinanceandBankingHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='FinanceandBanking',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='Management',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'MarketingHSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='HSTU',
                                                                            student_subject='Marketing',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'BusinessAdministrationDisciplineMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='BusinessAdministrationDiscipline',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'ManagementMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='Management',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'AccountingMBSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='MBSTU',
                                                                            student_subject='Accounting',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'DepartmentofBusinessAdministrationNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='DepartmentofBusinessAdministration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'DepartmentofTourismandHospitalityManagementNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='DepartmentofTourismandHospitalityManagementBusiness Administration',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True
            if valueee == 'DepartmentofManagementInformationSystemsNSTU' and no_of_seat >= 0:
                print('its the bidirectionacomputer')
                print("no_of_seatededdd", no_of_seat)
                reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                reg.save()
                print('############################')
                print(mail)
                print('its the bidirectionacomputer')
                ranking_val = ranking_value(mail)
                # print('rank_value',ranking_val[1])
                # print('rank_value', ranking_val[0])
                # print('rank_value', ranking_val[2])
                regis = Email_Model(id=1, email_name=mail)
                regis.save()
                subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                            student_university='NSTU',
                                                                            student_subject='DepartmentofManagementInformationSystems',
                                                                            ranking_score=ranking_val[2],
                                                                            ranking_registration_number=ranking_val[1],
                                                                            ranking_username=ranking_val[0],
                                                                            ranking_group='Commerce')
                subject_and_university_save.save()
                sucsess = True

                if valueee == 'AccountingandInformationSystemsJUST' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='JUST',
                                                                                student_subject='AccountingandInformationSystems',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'FinanceandBankingJUST' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='JUST',
                                                                                student_subject='FinanceandBanking',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'ManagementJUST' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='JUST',
                                                                                student_subject='Management',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'MarketingJUST' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='JUST',
                                                                                student_subject='Marketing',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'BusinessAdministrationPUST' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='PUST',
                                                                                student_subject='BusinessAdministration',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'ManagementStudiesBSMRSTU' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='BSMRSTU',
                                                                                student_subject='ManagementStudies',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'MarketingBSMRSTU' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='BSMRSTU',
                                                                                student_subject='Marketing',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'AccountingandInformationSystemsBSMRSTU' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='BSMRSTU',
                                                                                student_subject='AccountingandInformationSystems',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'FinanceandBankingBSMRSTU' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='BSMRSTU',
                                                                                student_subject='FinanceandBanking',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'TourismandHospitalityManagementBSMRSTU' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='BSMRSTU',
                                                                                student_subject='TourismandHospitalityManagement',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'TourismandHospitalityManagementRMSTU' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='RMSTU',
                                                                                student_subject='Tourism and HospitalityManagement',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                if valueee == 'ManagementRMSTU' and no_of_seat >= 0:
                    print('its the bidirectionacomputer')
                    print("no_of_seatededdd", no_of_seat)
                    reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                    reg.save()
                    print('############################')
                    print(mail)
                    print('its the bidirectionacomputer')
                    ranking_val = ranking_value(mail)
                    # print('rank_value',ranking_val[1])
                    # print('rank_value', ranking_val[0])
                    # print('rank_value', ranking_val[2])
                    regis = Email_Model(id=1, email_name=mail)
                    regis.save()
                    subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                                                                                student_university='RMSTU',
                                                                                student_subject='Management',
                                                                                ranking_score=ranking_val[2],
                                                                                ranking_registration_number=ranking_val[
                                                                                    1],
                                                                                ranking_username=ranking_val[0],
                                                                                ranking_group='Commerce')
                    subject_and_university_save.save()
                    sucsess = True
                # if valueee == 'BSFMSTU' and no_of_seat >= 0:
                #     print('its the bidirectionacomputer')
                #     print("no_of_seatededdd", no_of_seat)
                #     reg = Subject(id=subject_id, subject_name=university_and_subject, subject_seat_number=no_of_seat)
                #     reg.save()
                #     print('############################')
                #     print(mail)
                #     print('its the bidirectionacomManagementputer')
                #     ranking_val = ranking_value(mail)
                #     # print('rank_value',ranking_val[1])
                #     # print('rank_value', ranking_val[0])
                #     # print('rank_value', ranking_val[2])
                #     regis = Email_Model(id=1, email_name=mail)
                #     regis.save()
                #     subject_and_university_save = Subject_and_University_Model2(student_email=mail,
                #                                                                 student_university='BSFMSTU',
                #                                                                 student_subject='Management',
                #                                                                 ranking_score=ranking_val[2],
                #                                                                 ranking_registration_number=ranking_val[
                #                                                                     1],
                #                                                                 ranking_username=ranking_val[0],
                #                                                                 ranking_group='Commerce')
                #     subject_and_university_save.save()
                #     sucsess = True



        # if value == 'Computerscience&EngineeringIU' and ComputerscienceEngineeringIU != 0:
        #     print('its the cumdirection',ComputerscienceEngineeringIU)
        #     ComputerscienceEngineeringIU -=1
        #     selected_subject = ['Computerscience & Engineering','IU']
        #     return selected_subject





def ranking(request):

    Count_model = Counter_Model.objects.all()
    i = 0
    count_values = None
    # print('and its the value',values)
    jnu_group = None
    for new_val in Count_model.values():
        jnu_group = new_val
        print(jnu_group)
    for  key, value in jnu_group.items():
        if i == 0:
           count_values = value
           print('the fucking value is')
        i = i + 1
    print('this is the value',value)
    # print(Count_model)
    c_value = value


    #fdddddddddddddddddddddd
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
            print('the fucking value is',values)
        i = i + 1
    print('this is the value',values)
    ranking_group_value = values
    if c_value == 1:
        new_count = Counter_Model(id = 1,count = 0)
        new_count.save()
        if values == 'Scinece':
            rank = Registration_Model.objects.filter(hsc_group ='Scinece').order_by('exam_score').reverse()
            print(rank)
            i = 0
            values = None
            # print('and its the value', values)
            jnu_group = None
            for new_val in rank.values():
                i = 0
                jnu_group = new_val
                # print('whatsabig dig')
                # print('fucing jnu group',jnu_group)
                for key, value in jnu_group.items():
                    # i = 0
                    # print('my dick is a big thdfdfdfdfdfdffdfdf')
                    # print('secondary_value',i,value)
                    if i == 7:
                        values = value
                        # print(values)
                        selected_subject = Selected_Subject_Model.objects.filter(email=values)
                        # print(selected_subject)
                        # print(rank)
                        i = 0
                        values = None
                        # print('and its the value', values)
                        jnu_group = None
                        for new_val in selected_subject.values():
                            i = 0
                            values1 = None
                            values2 = None
                            mail = None
                            jnu_group = new_val
                            # print('whatsabig dig')
                            # print('fucing jnu group',jnu_group)
                            for key, value in jnu_group.items():
                                # i = 0
                                # print('my dick is a big thdfdfdfdfdfdffdfdf')
                                # print('secondary_value',i,value)
                                if i == 2 or i == 3:
                                    if i == 2:
                                        values1 = str(value)
                                        # print(values1)
                                        # selected_subject = Selected_Subject_Model.objects.filter(email=values)
                                        # print(selected_subject)
                                    if i == 3:
                                        values2 = str(value)
                                        print(values2)
                                if i == 4:
                                    mail = value
                                    # print('its is the fucking mail',value)
                                    values = str(values1) + str(values2)
                                    values = str(values)
                                    print(str(values).replace(" ", ""))

                                    s_select = subject_selet(str(values).replace(" ", ""), mail)
                                    # a = "my name is"
                                    # print(a.replace(" ",""))
                                    #
                                    # print(values)

                                i = i + 1

                    i = i + 1
        if values == 'Commerce':
            rank = Registration_Model.objects.filter(hsc_group='Commerce').order_by('exam_score').reverse()
            print(rank)
            i = 0
            values = None
            # print('and its the value', values)
            jnu_group = None
            for new_val in rank.values():
                i = 0
                jnu_group = new_val
                # print('whatsabig dig')
                # print('fucing jnu group',jnu_group)
                for key, value in jnu_group.items():
                    # i = 0
                    # print('my dick is a big thdfdfdfdfdfdffdfdf')
                    # print('secondary_value',i,value)
                    if i == 7:
                        values = value
                        # print(values)
                        selected_subject = Selected_Subject_Model.objects.filter(email=values)
                        # print(selected_subject)
                        # print(rank)
                        i = 0
                        values = None
                        # print('and its the value', values)
                        jnu_group = None
                        for new_val in selected_subject.values():
                            i = 0
                            values1 = None
                            values2 = None
                            mail = None
                            jnu_group = new_val
                            # print('whatsabig dig')
                            # print('fucing jnu group',jnu_group)
                            for key, value in jnu_group.items():
                                # i = 0
                                # print('my dick is a big thdfdfdfdfdfdffdfdf')
                                # print('secondary_value',i,value)
                                if i == 2 or i == 3:
                                    if i == 2:
                                        values1 = str(value)
                                        # print(values1)
                                        # selected_subject = Selected_Subject_Model.objects.filter(email=values)
                                        # print(selected_subject)
                                    if i == 3:
                                        values2 = str(value)
                                        print(values2)
                                if i == 4:
                                    mail = value
                                    # print('its is the fucking mail',value)
                                    values = str(values1) + str(values2)
                                    values = str(values)
                                    print(str(values).replace(" ", ""))

                                    s_select = subject_selet(str(values).replace(" ", ""), mail)
                                    # a = "my name is"
                                    # print(a.replace(" ",""))
                                    #
                                    # print(values)

                                i = i + 1

                    i = i + 1

        if values =='Humanities':
            rank = Registration_Model.objects.filter(hsc_group='Humanities').order_by('exam_score').reverse()
            print(rank)
            i = 0
            values = None
            # print('and its the value', values)
            jnu_group = None
            for new_val in rank.values():
                i = 0
                jnu_group = new_val
                # print('whatsabig dig')
                # print('fucing jnu group',jnu_group)
                for key, value in jnu_group.items():
                    # i = 0
                    # print('my dick is a big thdfdfdfdfdfdffdfdf')
                    # print('secondary_value',i,value)
                    if i == 7:
                        values = value
                        # print(values)
                        selected_subject = Selected_Subject_Model.objects.filter(email=values)
                        # print(selected_subject)
                        # print(rank)
                        i = 0
                        values = None
                        # print('and its the value', values)
                        jnu_group = None
                        for new_val in selected_subject.values():
                            i = 0
                            values1 = None
                            values2 = None
                            mail = None
                            jnu_group = new_val
                            # print('whatsabig dig')
                            # print('fucing jnu group',jnu_group)
                            for key, value in jnu_group.items():
                                # i = 0
                                # print('my dick is a big thdfdfdfdfdfdffdfdf')
                                # print('secondary_value',i,value)
                                if i == 2 or i == 3:
                                    if i == 2:
                                        values1 = str(value)
                                        # print(values1)
                                        # selected_subject = Selected_Subject_Model.objects.filter(email=values)
                                        # print(selected_subject)
                                    if i == 3:
                                        values2 = str(value)
                                        print(values2)
                                if i == 4:
                                    mail = value
                                    # print('its is the fucking mail',value)
                                    values = str(values1) + str(values2)
                                    values = str(values)
                                    print(str(values).replace(" ", ""))

                                    s_select = subject_selet(str(values).replace(" ", ""), mail)
                                    # a = "my name is"
                                    # print(a.replace(" ",""))
                                    #
                                    # print(values)

                                i = i + 1

                    i = i + 1
        if values == 'Engineering':
            rank = Registration_Model.objects.filter(hsc_group='Engineering').order_by('exam_score').reverse()
            print(rank)
            i = 0
            values = None
            # print('and its the value', values)
            jnu_group = None
            for new_val in rank.values():
                i = 0
                jnu_group = new_val
                # print('whatsabig dig')
                # print('fucing jnu group',jnu_group)
                for key, value in jnu_group.items():
                    # i = 0
                    # print('my dick is a big thdfdfdfdfdfdffdfdf')
                    # print('secondary_value',i,value)
                    if i == 7:
                        values = value
                        # print(values)
                        selected_subject = Selected_Subject_Model.objects.filter(email = values)
                        # print(selected_subject)
                        # print(rank)
                        i = 0
                        values = None
                        # print('and its the value', values)
                        jnu_group = None
                        for new_val in selected_subject.values():
                            i = 0
                            values1 = None
                            values2 = None
                            mail = None
                            jnu_group = new_val
                            # print('whatsabig dig')
                            # print('fucing jnu group',jnu_group)
                            for key, value in jnu_group.items():
                                # i = 0
                                # print('my dick is a big thdfdfdfdfdfdffdfdf')
                                # print('secondary_value',i,value)
                                if i == 2 or i ==3:
                                    if i == 2 :
                                        values1 = str(value)
                                        # print(values1)
                                        # selected_subject = Selected_Subject_Model.objects.filter(email=values)
                                        # print(selected_subject)
                                    if i == 3:
                                        values2 = str(value)
                                        print(values2)
                                if i == 4:
                                    mail = value
                                    # print('its is the fucking mail',value)
                                    values = str(values1) + str(values2)
                                    values = str(values)
                                    print(str(values).replace(" ",""))

                                    s_select = subject_selet(str(values).replace(" ",""),mail)
                                    # a = "my name is"
                                    # print(a.replace(" ",""))
                                    #
                                    # print(values)

                                i = i + 1


                    i = i + 1
        if ranking_group_value == 'Engineering':

            defined_university = Subject_and_University_Model2.objects.filter(ranking_group = 'Engineering')
            print('the defined uni',defined_university)
            context = {'rank':rank,'defined_university':defined_university}
            return render(request,'ranking/ranking.html',context)


        if ranking_group_value == 'Humanities':
            defined_university = Subject_and_University_Model2.objects.filter(ranking_group='Humanities')
            print('the defined uni', defined_university)
            context = {'rank': rank, 'defined_university': defined_university}
            return render(request, 'ranking/ranking.html', context)

        if ranking_group_value == 'Commerce':
            defined_university = Subject_and_University_Model2.objects.filter(ranking_group='Commerce')
            print('the defined uni', defined_university)
            context = {'rank': rank, 'defined_university': defined_university}
            return render(request, 'ranking/ranking.html', context)
        if ranking_group_value == 'Scinece':
            defined_university = Subject_and_University_Model2.objects.filter(ranking_group='Science')
            print('the defined uni', defined_university)
            context = { 'defined_university': defined_university}
            return render(request, 'ranking/ranking.html', context)
    else:
        if ranking_group_value == 'Humanities':
            defined_university = Subject_and_University_Model2.objects.filter(ranking_group='Humanities')
            print('the defined uni', defined_university)
            context = { 'defined_university': defined_university}
            return render(request, 'ranking/ranking.html', context)

        if ranking_group_value == 'Commerce':
            defined_university = Subject_and_University_Model2.objects.filter(ranking_group='Commerce')
            print('the defined uni', defined_university)
            context = { 'defined_university': defined_university}
            return render(request, 'ranking/ranking.html', context)
        if ranking_group_value == 'Scinece':
            defined_university = Subject_and_University_Model2.objects.filter(ranking_group='Science')
            print('the defined uni', defined_university)
            context = { 'defined_university': defined_university}
            return render(request, 'ranking/ranking.html', context)

        if ranking_group_value == 'Engineering':
            defined_university = Subject_and_University_Model2.objects.filter(ranking_group='Engineering')
            print('the defined uni', defined_university)
            context = { 'defined_university': defined_university}
            return render(request, 'ranking/ranking.html', context)