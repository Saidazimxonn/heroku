
from .models import Email, Patient, Message


def create_patient(post_request):
    name = post_request.get('name', '')
    phone = post_request.get('phone', '')
    email = post_request.get('email', '')
    message = post_request.get('message', '')
    day = post_request.get('day', '')
    time = post_request.get('time', '')
    doctor = post_request.get('doctor', '')
    Patient.objects.create(
                            name=name,
                            phone=phone,
                            email=email,
                            message=message,
                            day=day,
                            time=time,
                            doctor_id=doctor
    )


def create_message(post_request):
    name = post_request.get('name', '')
    email = post_request.get('email', '')
    phone = post_request.get('phone', '')
    subject = post_request.get('subject', '')
    message = post_request.get('message', '')
    Message.objects.create(
        name=name,
        email=email,
        phone=phone,
        subject=subject,
        message=message, 
    )
    
def create_email(post_request):
    email = post_request.get('email', '')
    Email.objects.create(
        email=email,
    )

