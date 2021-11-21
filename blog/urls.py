from django.urls import path 
from . import views


app_name = 'blog' 

urlpatterns = [
    
    path('', views.post_list, name='posts_list'),
    path('<str:slug>', views.post_details, name = 'post_details' ),
     path('add_post/', views.add_post, name = 'add_post' ),
    
    
]
