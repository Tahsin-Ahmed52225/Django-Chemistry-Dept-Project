from django.contrib import admin
from .models import Userinfo
from peopleApp.models import faculty,staff
from researchApp.models import research_by_area

# Register your models here.
admin.site.register(faculty)
admin.site.register(staff)
admin.site.register(research_by_area)
admin.site.register(Userinfo)
admin.site.site_header = 'Admin Dashboard'
