from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('nuevo-articulo/', views.create_post, name='create_post'),
    path('articulo/<int:pk>/', views.post_detail, name='post_detail'),
    path('articulo/<int:pk>/editar/', views.update_post, name='update_post'),
    path('articulo/<int:pk>/eliminar/', views.delete_post, name='delete_post'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile_detail, name='profile-detail'),
    path('profile/edit/', views.profile_edit, name='profile-edit'),
]
