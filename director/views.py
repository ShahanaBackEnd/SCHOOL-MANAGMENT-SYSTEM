from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import Year_Level
from .serializer import year_levelSerializer


@api_view()
def home(request):
    return Response({"message":"WELCOME"})


@api_view(["GET","POST","PUT","DELETE"])
def Yearlevel(request,pk=None):
    if request.method=='GET':
        if pk is not None:
            rahin = Year_Level.objects.get(id = pk)
            serialize = year_levelSerializer(rahin,many = False)
            return Response(serialize.
                            )
        
        else:
            year = Year_Level.objects.all()      
            serialized = year_levelSerializer(year,many = True)
            return Response(serialized.data)
 ##postind data   
    elif request.method == "POST":
        data = request.data 
        serialize = year_levelSerializer(data= data)
        if serialize.is_valid():
            serialize.save()
            return Response({"Message":"Data Saved Successfully"})
        return Response({"Message":"Insert Valid Data"})

  ##updating data  
    
    elif request.method == "PUT":
        data = Year_Level.objects.get(id = pk)
        serialize = year_levelSerializer(instance=data,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({"Message":"Data Updated Successfully"})
        return Response({"Message":"Insert Valid Data"})
    

##Deleteing data
    elif request.method == "DELETE":
        data = Year_Level.objects.get(id = pk)
        data.delete()
        return Response({"Message":"Data Deleted"})

        

    






