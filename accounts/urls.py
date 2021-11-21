from django.urls import path , include
from . import views


app_name = 'accounts' 

urlpatterns = [
    
    path('signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
     path('author/<int:id>', views.visit_profile, name='visit_profile'),
    
]
