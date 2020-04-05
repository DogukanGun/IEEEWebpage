from django.urls import path
from . import views
app_name="Article"
urlpatterns = [
    path("news",views.news,name="news")
]
