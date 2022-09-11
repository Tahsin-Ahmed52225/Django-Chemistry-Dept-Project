from django.urls import path,include
from . import views
urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('user-login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('people/', include('peopleApp.url')),
    path('research/', include('researchApp.url')),
    path('resource/', include('resourceApp.url')),
    path('events/', include('eventsApp.url')),
    path('news/', include('newsApp.url')),
    #Settings
    path('settings/', views.settings, name='settings'),
    #Home banner url
    path('settings/homebanner', views.homebanner, name='homebanner'),
    path('settings/add-homebanner', views.addHomeBanner, name='add_homebanner'),
    path('settings/homebanner/getData/<int:id>', views.getHomeBanner, name='get_homebanner_data'),
    path('settings/homebanner/edit-data/<int:id>', views.editHomeBanner, name='edit_homebanner_data'),
    path('settings/homebanner/<int:id>/delete', views.deleteHomeBanner, name='delete_banner'),
    #Home about url
    path('settings/homeabout', views.homeabout, name='homeabout'),
    #Home award section
    path('settings/homeaward', views.homeaward, name='homeaward'),
    path('settings/add-homeaward', views.addHomeaward, name='add_homeaward'),
    path('settings/homeaward/<int:id>/delete', views.deleteHomeAward, name='delete_award'),
    path('settings/homeaward/getData/<int:id>', views.getHomeAward, name='get_homeaward_data'),
    path('settings/homeaward/edit-data/<int:id>', views.editHomeAward, name='edit_homeaward_data'),

]
