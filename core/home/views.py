from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .models import Person
from .serializers import PeopleSerializer



# api views
@api_view(['GET','POST', 'PUT'])
def index(request):
    courses = {
        'course_name' : 'python',
        'learn' : ['flask', 'django', 'tornado'],
        'course_provider' : 'scaler'
    }

    if request.method=='POST':
        newcourses=request.data
        return Response(newcourses)
    
    if request.method=='GET':
        print(request.GET.get("search"))  #query set ?search='xyz' ex; to search anything from database
        return Response(courses)

    if request.method == 'PUT':
        courses=request.data
        return Response(courses)
    
@api_view(['GET', 'POST'])
def person(request):
    if request.method == 'GET':
        objs=Person.objects.all()
        serializer = PeopleSerializer(objs, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

