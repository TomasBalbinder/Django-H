
from django.urls import path
from cosmonauts_app import views
from .views import CosmonautListView

urlpatterns = [
    #CRUD
    path('home/',CosmonautListView.as_view(), name='shows_all_cosmonauts'),
    path('create/', views.create_cosmonaut, name='create_cosmonaut'),
    path('edit/<int:pk>/', views.edit_cosmonaut, name='edit_cosmonaut'),
    path('delete/<int:pk>/', views.delete_cosmonaut, name='delete_cosmonaut'),

    #upload file
    path('upload-xml/', views.upload_cosmonauts, name='upload_cosmonauts'),
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),

]