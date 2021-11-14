import pika

<<<<<<< HEAD
def on_request_message_received(ch, method, properties, body):
    print(f"Received Request: {properties.correlation_id}")
    ch.basic_publish('', routing_key=properties.reply_to, body=f'Hey its your reply to {properties.correlation_id}')

=======
>>>>>>> b3416ae (request response)
connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

<<<<<<< HEAD
channel.queue_declare(queue='request-queue')

channel.basic_consume(queue='request-queue', auto_ack=True,
    on_message_callback=on_request_message_received)

print("Starting Server")

channel.start_consuming()
=======
channel.queue_declare(queue='request_queue')

def on_message_received(ch, method, properties, body):

    print(f"recieved : {properties.correlation_id} : {body}")

    response_message = "This is the response message"

    channel.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id=properties.correlation_id),
                     body=response_message)

    print(f"sent : {properties.correlation_id} : {response_message}")

channel.basic_consume(queue='request_queue', auto_ack=True,
    on_message_callback=on_message_received)

print("Server Starting Consuming")

channel.start_consuming()

connection.close()
>>>>>>> b3416ae (request response)
