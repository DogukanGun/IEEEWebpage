from django.urls import path
from . import views
app_name="Contact"
urlpatterns = [
    path('send/',views.contact,name="contactSend")
]
