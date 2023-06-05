from django.shortcuts import render
import pika
from datetime import datetime

def index(request):
    received_message = None

    if request.method == 'POST':
        message = request.POST.get('message', '')
        send_message_to_rabbitmq(message)

    return render(request, 'index.html', {'received_message': received_message})

def send_message_to_rabbitmq(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='messages')

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    body = f"{message}\nSent: {timestamp}"
    channel.basic_publish(exchange='', routing_key='messages', body=body)

    connection.close()