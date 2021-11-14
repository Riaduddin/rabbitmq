import pika
import uuid

<<<<<<< HEAD
def on_reply_message_received(ch, method, properties, body):
    print(f"reply recieved: {body}")

=======
>>>>>>> b3416ae (request response)
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

<<<<<<< HEAD
reply_queue = channel.queue_declare(queue='', exclusive=True)

channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True,
    on_message_callback=on_reply_message_received)

channel.queue_declare(queue='request-queue')

cor_id = str(uuid.uuid4())
print(f"Sending Request: {cor_id}")

channel.basic_publish('', routing_key='request-queue', properties=pika.BasicProperties(
    reply_to=reply_queue.method.queue,
    correlation_id=cor_id
), body='Can I request a reply?')

print("Starting Client")

channel.start_consuming()
=======
channel.queue_declare(queue='request_queue')

reply_queue = channel.queue_declare(queue='', exclusive=True)

correlation_id = str(uuid.uuid4())

message = "This Message needs a response"

channel.basic_publish(exchange='', routing_key='request_queue',
            properties=pika.BasicProperties(
                reply_to=reply_queue.method.queue,
                correlation_id=correlation_id,
            ),
            body=message)

print(f"sent : {correlation_id} : {message}")

def on_message_received(ch, method, properties, body):
    print(f"received: {properties.correlation_id} : {body}")

channel.basic_consume(queue=reply_queue.method.queue, auto_ack=True,
    on_message_callback=on_message_received)

print("Client Starting Consuming")

channel.start_consuming()

connection.close()
>>>>>>> b3416ae (request response)
