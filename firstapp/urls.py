from . import views
from django.urls import path

urlpatterns = [
    path('main/', views.mainpage,name="mainpage"),
    path('welcome/', views.helloworld,name="welcome"),
    path('hello/', views.sayhi,name="hello"),
    path('mypages/', views.displayhtml,name="mypages"),
    path('mypages2/', views.displayhtml2,name="mypages2"),
    path('allmembers/', views.getAllMembers,name="allmembers"),
    path('allmembers/details/<int:rid>', views.details,name="details"),
    path('allmembers/addmember', views.memberadd,name="addmember"),
    path('allmembers/editmember/<int:rid>', views.memberedit,name="editmember"),
    path('allmembers/deletemember/<int:rid>', views.memberdelete,name="deletemember"),
    
]
