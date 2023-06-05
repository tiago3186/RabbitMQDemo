from flask import Flask, render_template
import pika
from datetime import datetime
from threading import Thread

app = Flask(__name__)

received_message = None

def consume_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='messages')

    def callback(ch, method, properties, body):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        global received_message
        received_message = f"{body.decode()}\nReceived: {timestamp}"

    channel.basic_consume(queue='messages', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

@app.route('/')
def index():
    return render_template('index.html', received_message=received_message)

if __name__ == '__main__':
    # Iniciar uma thread para consumir as mensagens em segundo plano
    consumer_thread = Thread(target=consume_messages)
    consumer_thread.start()

    # Executar o servidor Flask
    app.run()
