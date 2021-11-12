from .models import Job 
from .serializers import JobSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics



class JobApiList(generics.ListAPIView):
    # model = Job
    queryset =Job.objects.all()
    serializer_class = JobSerializers



@api_view(['GET'])
def job_list(request):
    all_job = Job.objects.all()
    showdata = JobSerializers(all_job, many=True).data

    return Response({'data':showdata})

@api_view(['GET'])
def job_detail(request, id):
    job_detail = Job.objects.get(id = id)
    data = JobSerializers(job_detail).data

    return Response({'data' : data})

