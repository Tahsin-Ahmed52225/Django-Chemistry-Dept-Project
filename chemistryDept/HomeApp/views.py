from django.shortcuts import render
from AdminPanel.models import banner,about,awards
from researchApp.models import research_overview, research_by_direction,research_by_area
from peopleApp.models import faculty,staff,student
from resourceApp.models import labFacility
from eventsApp.models import  seminer,courseAnnouncemets
from resourceApp.models import computing as all_computing
from resourceApp.models import studentService as all_student_service
from newsApp.models import new
#Home page view

def index(request):
    banners = banner.objects.all()
    abouts = about.objects.all()
    award = awards.objects.all()
    return render(request,'HomeApp/index.html',context={'banner':banners,'abouts':abouts,'award':award})


#About page view

def contact(request):
    data = {}
    return render(request,'HomeApp/contact.html',context=data)

def chairletter(request):
    return render(request, 'HomeApp/chairletter.html')

def missionvision(request):
    return render(request, 'HomeApp/missionvision.html')

#Faculty page view

def facultys(request):
    data = faculty.objects.order_by('name')
    return render(request,'HomeApp/faculty.html',context={'faculty':data})

#Staff page view

def staffs(request):
    data = staff.objects.order_by('name')
    return render(request,'HomeApp/staff.html',context={'staff':data})

#Student page view

def students(request):
    undergrad_student = student.objects.filter(student_type="Undergrad").order_by('name')
    grad_student = student.objects.filter(student_type="Graduate").order_by('name')
    return render(request,'HomeApp/student.html',context={'undergrad_student':undergrad_student,'grad_student':grad_student})

#bschemistry page view

def bschemistry(request):
    return render(request, 'HomeApp/bschemistry.html')

#bschemical page view

def bschemical(request):
    return render(request, 'HomeApp/bschemical.html')

#mschemistry page view

def mschemistry(request):
    return render(request, 'HomeApp/mschemistry.html')

#msbiomedical page view

def msbiomedical(request):
    return render(request, 'HomeApp/msbiomedical.html')

#certificateprograms page view

def certificateprograms(request):
    return render(request, 'HomeApp/certificateprograms.html')

#phdprogram page view

def phdprogram(request):
    return render(request, 'HomeApp/phdprogram.html')

#Research by area view page

def researchChemistry(request):
    data = research_by_area.objects.filter(research_fields="Chemistry")
    return render(request, 'HomeApp/research-area.html' , context={'title':"Chemistry",'research': data})
def researchChemical(request):
    data = research_by_area.objects.filter(research_fields="Chemical Engineering")
    return render(request, 'HomeApp/research-area.html' , context={'title':"Chemical Engineering",'research': data})
def researchBiomedical(request):
    data = research_by_area.objects.filter(research_fields="Biomedical Engineering")
    return render(request, 'HomeApp/research-area.html' , context={'title':"Biomedical Engineering",'research': data})


#Research by direction view page
def researchoverview(request):
    data = research_overview.objects.all()
    return render(request, 'HomeApp/researchoverview.html',context={'data':data})
def researchSustainabilityEnergy(request):
    data = research_by_direction.objects.filter(research_fields="Sustainability Energy")
    return render(request, 'HomeApp/research-direction.html',context={'title':"Sustainability Energy",'research': data})
def researchMedical(request):
    data = research_by_direction.objects.filter(research_fields="Medical")
    return render(request, 'HomeApp/research-direction.html',context={'title':"Medical",'research': data})


#Events view Page
def courseAnnouncements(request):
    all_courses = courseAnnouncemets.objects.all()
    return render(request, 'HomeApp/courseAnnouncements.html',context={"all_courses":all_courses})
def seminars(request):
    try:
        featured_seminer = seminer.objects.get(featured=1)
    except seminer.DoesNotExist:
        featured_seminer = None
    all_seminar = seminer.objects.all()
    return render(request, 'HomeApp/seminars.html',context={"featured_seminer":featured_seminer, "all_seminar":all_seminar})

#Resources view page
def labFacilites(request):
    class_rooms = labFacility.objects.filter(lab_sections="Classrooms")
    labs_equipment = labFacility.objects.filter(lab_sections="Labs Equipment")
    instruments = labFacility.objects.filter(lab_sections="Instruments")
    return render(request,'HomeApp/labFacilites.html',context={"class_rooms":class_rooms,"labs_equipment":labs_equipment,"instruments":instruments})

def computing(request):
    image_data = all_computing.objects.filter(computing_type="Image")
    video_data = all_computing.objects.filter(computing_type="Video")
    return render(request, 'HomeApp/computing.html',context={"image_data":image_data,"video_data":video_data})
def studentServices(request):
    data = all_student_service.objects.all()
    return render(request, 'HomeApp/studentServices.html',context={'data':data})

#News view page
def news(request):
    try:
        latest_news = new.objects.get(featured=1)
    except new.DoesNotExist:
        latest_news = None
    all_news = new.objects.all()
    return render(request, 'HomeApp/news.html',context={'latest_news': latest_news , 'all_news':all_news})

#Dummy for test
def dummy(request):
    return render(request, 'HomeApp/dummytest.html')
