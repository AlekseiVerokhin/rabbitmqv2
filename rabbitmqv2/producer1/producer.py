# Import the 'pika' library for RabbitMQ communication.
import pika

# Parse the AMQP URL to extract connection parameters.
url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

# Establish a blocking connection to the RabbitMQ server.
connection = pika.BlockingConnection(url_params)

channel = connection.channel()

# Объявляем exchange с типом 'headers'
exchange_name = 'notifier_logs'
channel.exchange_declare(exchange=exchange_name, exchange_type='fanout')

# Объявляем очередь
queue_name = 'my_fanout_queue'
#queue_name1 = 'my_fanout_queue'
#queue_name2 = 'my_fanout_queue'
channel.queue_declare(queue=queue_name)
#channel.queue_declare(queue=queue_name1)
#channel.queue_declare(queue=queue_name2)


# Привязываем очередь к exchange с определенными аргументами заголовков
channel.queue_bind(exchange=exchange_name, queue=queue_name)
#channel.queue_bind(exchange=exchange_name, queue=queue_name1)
#channel.queue_bind(exchange=exchange_name, queue=queue_name2)



# Текст сообщения для отправки
message = 'This is a message with fanout.'

# Публикуем сообщение в exchange с указанными заголовками
channel.basic_publish(exchange=exchange_name, body=message)

print(f"Sent: '{message}' with ")

# Close the channel.
channel.close()

# Close the connection to RabbitMQ.
connection.close()