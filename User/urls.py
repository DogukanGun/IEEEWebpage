from django.urls import path
from django.contrib import admin
from . import views
app_name="User"
urlpatterns = [
    path('register/<int:id>/',views.register,name="register"),
    path('login/<int:id>/',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('about/', views.about, name="about"),
    path('members/', views.members, name="members"),
    path('Ieee/', views.Ieee, name="Ieee"),
    path('releatedClubs/', views.ReleatedClubs, name="releatedclubs"),
    path('projects/', views.Projects, name="projects"),
    path('mainPage/',views.mainPage,name="mainPageBridge"),
    path('forgot/',views.forgotPassword,name="passwordReset"),
    path('', views.welcomePage, name="welcomePage"),
    path('reset/',views.resetPassword,name='resetPassword'),
    path('courses',views.courses,name="courses")
]
