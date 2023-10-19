from django.shortcuts import render
import datetime
from .models import *
import smtplib
from django.core.mail import EmailMessage
# from .serializers import EmployeeNameSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def send_email(employee,template):
    EMAIL_SERVER = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_USER = "akashshere19@gmail.com"
    EMAIL_PASS = "cukp ghny zlkn pwbf"
    server =smtplib.SMTP(EMAIL_SERVER,EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_USER,EMAIL_PASS)
    
    subject = "Upcoming Event "
    
    message = template # template from table
   
    recipient_list = [employee.email]  #  recipient's email address here

    # server.sendmail('',recipient_list,'subject:{}\n\n{}'.format(subject,message)) 
    print('mail Sent')
    server.close()


current_date = datetime.date.today() # Get the current date
print('today date:',current_date)

# up = Employee.objects.all()
# print(up)
upcoming_employees = Employee.objects.filter(imp_date__gte=current_date)

print('upcome event:',upcoming_employees)

for employee in upcoming_employees:
        event_name = employee.event_name
        print('event_name:',event_name)
        template_query = EventTemplate.objects.filter(event_namefor=event_name).first()
       
        template  =template_query.template
        print('template :',template)
        send_email(employee, template)


class EmployeeEventDetails(APIView):
    def post(self, request):
        print('request:',request.data)
        serializer = EmployeeNameSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            name = serializer.validated_data['name']

            # checkout employee by name
            try:
                employee = Employee.objects.get(name=name)
            except Employee.DoesNotExist:
                return Response({"error": "Employee not found"}, status=404)

            # Retrieve the event details
            event_name = employee.event_name
            template_query = EventTemplate.objects.filter(event_namefor=event_name).first()
            template = template_query.template

            return Response({"event_name": event_name, "event_date": employee.imp_date, "event_details": template})

        return Response(serializer.errors, status=400)