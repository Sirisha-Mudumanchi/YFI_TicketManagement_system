from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import TicketData
from .serializers import TicketSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

@api_view(['GET','POST','PATCH'])
def home(request):
    if (request.method=='GET'):
        Items=TicketData.objects.all()
        seialized_data=TicketSerializer(Items,many=True)
        return Response(seialized_data.data)
    elif (request.method=='POST'):
        user_data=TicketSerializer(data=request.data,many=True)
        if user_data.is_valid():
            user_data.save()
            return Response(user_data.data)
        else:
            return Response(user_data.errors)
        
@api_view(['GET','PATCH','DELETE','PUT'])
def single_Ticket(request,id):
    if(request.method=='GET'):
        single_ticket_data=get_object_or_404(TicketData,id=id)
        serialized_data=TicketSerializer(single_ticket_data)
        return Response(serialized_data.data)
    elif (request.method=='PATCH'):
        single_ticket_data=get_object_or_404(TicketData,id=id)
        serialized_data=TicketSerializer(single_ticket_data,data=request.data,partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
    elif request.method=='PUT':
        single_ticket_data=get_object_or_404(TicketData,id=id)
        serialized_data=TicketSerializer(single_ticket_data,data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
    elif(request.method=='DELETE'):
        single_ticket_data=get_object_or_404(TicketData,id=id)
        single_ticket_data.delete()
        return Response(({"data":{"deleted":id}}))

@api_view(['GET'])
def ticketByName(request, customer_name):
    if (request.method == 'GET'):
        single_ticket_data = get_object_or_404(TicketData,customer_name=customer_name)
        serialized_data = TicketSerializer(single_ticket_data)
        return Response(serialized_data.data)
    

