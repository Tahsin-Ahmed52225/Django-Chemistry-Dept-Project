from django.shortcuts import render
from researchApp.models import research_by_area
from peopleApp.models import faculty,staff
#Home page view

def index(request):
    data = {}
    return render(request,'HomeApp/index.html',context=data)


#About page view

def contact(request):
    data = {}
    return render(request,'HomeApp/contact.html',context=data)

#Faculty page view

def facultys(request):
    data = faculty.objects.order_by('name')
    return render(request,'HomeApp/faculty.html',context={'faculty':data})

#Staff page view

def staffs(request):
    data = staff.objects.order_by('name')
    return render(request,'HomeApp/staff.html',context={'staff':data})

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

#Research by area view page

def researchChemistry(request):
    data = research_by_area.objects.filter(research_fields="Chemistry")
    return render(request, 'HomeApp/research-area.html' , context={'title':"Chemistry Research",'research': data})
def researchChemical(request):
    data = research_by_area.objects.filter(research_fields="Chemical Engineering")
    return render(request, 'HomeApp/research-area.html' , context={'title':"Chemical Engineering Research",'research': data})
def researchBiomedical(request):
    data = research_by_area.objects.filter(research_fields="Biomedical Engineering")
    return render(request, 'HomeApp/research-area.html' , context={'title':"Biomedical Engineering Research",'research': data})
