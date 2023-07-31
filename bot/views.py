from django.http.response import HttpResponse
from whatsappBot.settings import client
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def bot(request):
    message = request.POST['Body']
    sender_name = request.POST['ProfileName']
    sender_number = request.POST['From']

    if message == 'Hi':
        client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"Hi {sender_name}, how are you??",
            to=sender_number,
        )
        
    return HttpResponse('Hello')