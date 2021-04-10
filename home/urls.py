from django.urls import path
from home import views

urlpatterns = [
    path('', views.home),
    path('show', views.show),
    path('send', views.send),
    path('delete', views.delete),
    path('edit', views.edit),
    path('RecordEdited', views.RecordEdited)

]
