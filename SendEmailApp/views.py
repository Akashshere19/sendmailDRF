from django.shortcuts import render
import datetime
from .models import *
import smtplib
from django.core.mail import EmailMessage
# Create your views here.
def send_email(employee):
    EMAIL_SERVER = "smtp.gmail.com"
    EMAIL_PORT = 587
    EMAIL_USER = "akashshere19@gmail.com"
    EMAIL_PASS = "cukp ghny zlkn pwbf"
    server =smtplib.SMTP(EMAIL_SERVER,EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_USER,EMAIL_PASS)
    
    subject = "Upcoming Event Reminder"
    message = f"Hello {employee.name}, you have an event '{employee.event_name}' on {employee.imp_date}."
    from_email = "akash@servicenet.in"
    recipient_list = ["akashshere19@gmail.com"]  # Add the recipient's email address here

    email = EmailMessage(subject, message, from_email, recipient_list)
    server.sendmail('',recipient_list,'subject:{}\n\n{}'.format(subject,subject)) 
    print('mail Sent')
    server.close()

# Get the current date
current_date = datetime.date.today()
print('today date:',current_date)
# Get employees with upcoming events
up = Employee.objects.all()
print(up)
upcoming_employees = Employee.objects.filter(imp_date__gte=current_date)
print('upcome event:',upcoming_employees)
# Loop through upcoming employees and send email reminders
for employee in upcoming_employees:
    send_email(employee)