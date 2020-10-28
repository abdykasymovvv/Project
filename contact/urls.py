from django.urls import path
from .import views


urlpatterns = [
   path('', views.contact_home, name='detail'),
   path('create', views.create, name='create'),
   path('<int:pk>', views.ContactDetailView.as_view(), name='news-detail'),
    path('list', views.list_go, name='list')
   ]