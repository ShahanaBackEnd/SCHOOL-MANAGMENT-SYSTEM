from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Year_Level,classroom_type
from .serializer import year_levelSerializer,classroom_typeSerializer
from rest_framework import status



@api_view()
def home(request):
    return Response({"message":"WELCOME"})


@api_view(["GET","POST","PUT","DELETE"])
def Yearlevel(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            try:
               Update_data = Year_Level.objects.get(id = pk)
               serialize = year_levelSerializer(Update_data,many = False)
               return Response(serialize.data,status.HTTP_200_OK)


            except Year_Level.DoesNotExist:
                return Response({"Message":"Data not found"},status.HTTP_404_NOT_FOUND)
        else:
            year = Year_Level.objects.all()      
            serialized = year_levelSerializer(year,many = True)
            return Response(serialized.data,status.HTTP_200_OK)
 ##posting data   
    elif request.method == "POST":
        data = request.data 
        serialize = year_levelSerializer(data= data)
        if serialize.is_valid():
            serialize.save()
            return Response({"Message":"Data Saved Successfully"},status.HTTP_200_OK)
        return Response({"Message":"Insert Valid Data"},status.HTTP_201_CREATED)

  ##updating data  
    
    elif request.method == "PUT":
        try:
            data = Year_Level.objects.get(id = pk)
            serialize = year_levelSerializer(instance=data,data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response({"Message":"Data Updated Successfully"},status.HTTP_200_OK)
            return Response({"Message":"Insert Valid Data"},status.HTTP_400_BAD_REQUEST)
        
        except Year_Level.DoesNotExist:
                return Response({"Message":"Data not found"},status.HTTP_404_NOT_FOUND)
        

##Deleteing data
    elif request.method == "DELETE":
        try:
            data = Year_Level.objects.get(id = pk)
            data.delete()
            return Response({"Message":"Data Deleted"},status.HTTP_204_NO_CONTENT)
        
        except Year_Level.DoesNotExist:
                return Response({"Message":"Data not found"},status.HTTP_404_NOT_FOUND)


##CRUD FOR CLASSROOM_TYPE

@api_view(["GET","POST","PUT","DELETE"])
def classroomtype(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            try:
               data = classroom_type.objects.get(id = pk)
               serialize = classroom_typeSerializer(data,many = False)
               return Response(serialize.data,status.HTTP_200_OK)
                

            except classroom_type.DoesNotExist:
                return Response({"Message":"Data not found"},status.HTTP_404_NOT_FOUND)
        else:
            classroom = classroom_type.objects.all()      
            serialized = classroom_typeSerializer(classroom,many = True)
            return Response(serialized.data,status.HTTP_200_OK)
        
 ##posting data   
    elif request.method == "POST":
        data = request.data 
        serialize = classroom_typeSerializer(data= data)
        if serialize.is_valid():
            serialize.save()
            return Response({"Message":"Data Saved Successfully"},status.HTTP_200_OK)
        return Response({"Message":"Insert Valid Data"},status.HTTP_201_CREATED)

  ##updating data  
    
    elif request.method == "PUT":
        try:
            data = classroom_type.objects.get(id = pk)
            serialize = classroom_typeSerializer(instance=data,data=request.data)
            if serialize.is_valid():
                serialize.save()
                return Response({"Message":"Data Updated Successfully"},status.HTTP_200_OK)
            return Response({"Message":"Insert Valid Data"},status.HTTP_400_BAD_REQUEST)
        
        except Year_Level.DoesNotExist:
                return Response({"Message":"Data not found"},status.HTTP_404_NOT_FOUND)
        

##Deleteing data
    elif request.method == "DELETE":
        try:
            data = classroom_type.objects.get(id = pk)
            data.delete()
            return Response({"Message":"Data Deleted"},status.HTTP_204_NO_CONTENT)
        
        except Year_Level.DoesNotExist:
                return Response({"Message":"Data not found"},status.HTTP_404_NOT_FOUND)


        

    






