from django.urls import path , include
from . import views , api


app_name = 'job' 

urlpatterns = [
    
    path('', views.job_list, name='job_list'),
    path('add', views.add_job, name = 'add_job' ),
    path('<str:slug>', views.job_details, name = 'job_detail' ),

    ## Rest Api  joblist
    path('api/job/list', api.job_list, name='job_list'),
    path('api/job/<int:id>', api.job_detail, name = 'job_detail' ),
    

    ## Class Based Views
     path('api/job/li', api.JobApiList.as_view(), name='JobApiList'),

]
