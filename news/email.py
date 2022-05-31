from django.core.mail import EmailMultiAlternatives #responsible for sending the emails
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
    # Creating message subject and sender
    subject = 'Welcome to the MoringaTribune NewsLetter'
    sender = 'james@moringaschool.com'