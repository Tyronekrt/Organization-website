from django.contrib import admin
from django.urls import path

from FoundationApp import views
from .views import logout

urlpatterns = [
    path('',views.index, name='index'),
    path('starter/',views.starter, name='starter'),
    path('about/',views.about, name='about'),
    path('causes/',views.causes, name='causes'),
    path('events/',views.show_events, name='events'),
    path('donate_for_love/', views.donate_for_love, name='donate_for_love'),
    path('love_for_humanity/', views.love_for_humanity, name='love_for_humanity'),
    path('love_for_future_generations/', views.love_for_future_generations, name='love_for_future_generations'),
    path('love_for_environment/', views.love_for_environment, name='love_for_environment'),
    path('teams/',views.show_image, name='teams'),
    path('contact/',views.contact, name='contact'),
    path('submit/',views.submit, name='submit'),
    path('pay/',views.pay, name='pay'),
    # path('uploadimage/', views.upload_image, name='uploadimage'),
    # path('uploadevent/', views.upload_events, name='uploadevent'),
    path('uploadview/', views.upload_view, name='uploadview'),
    path('administrator/', views.administrator, name='administrator'),
    path('login/', views.login, name='login'),
    path('adminmember/', views.adminMember, name='adminmember'),
    path('adminevents/', views.adminEvents, name='adminevents'),
    path('editmembers/<int:id>', views.editmembers, name='editmembers'),
    path('updatemembers/<int:id>', views.updatemembers, name='updatemembers'),
    path('deletemembers/<int:id>', views.deletemembers),
    path('editevents/<int:id>', views.editevents, name='editevents'),
    path('updatevents/<int:id>', views.updatevents, name='updatevents'),
    path('deleteevents/<int:id>', views.deleteevents),

    path('logout/', logout, name='logout'),




]