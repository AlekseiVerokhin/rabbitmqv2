# Import the 'pika' library for RabbitMQ communication.
import pika

# Parse the AMQP URL to extract connection parameters.
url_params = pika.URLParameters('amqp://rabbit_mq?connection_attempts=10&retry_delay=10')

# Establish a blocking connection to the RabbitMQ server.
connection = pika.BlockingConnection(url_params)

channel = connection.channel()

# Объявляем exchange с типом 'headers'
exchange_name = 'topic_logs'
channel.exchange_declare(exchange=exchange_name, exchange_type='topic')

# Объявляем очередь
queue_name = 'my_topic_queue'
channel.queue_declare(queue=queue_name)

# Создаем привязку (binding) с заданными аргументами заголовков


# Привязываем очередь к exchange с определенными аргументами заголовков
channel.queue_bind(exchange=exchange_name, queue=queue_name,  routing_key='*.iam.#')

# Текст сообщения для отправки
message = 'This is a message with topic.'

# Публикуем сообщение в exchange с указанными заголовками
channel.basic_publish(exchange=exchange_name, routing_key='new.iam.new.new', body=message)

print(f"Sent: '{message}' with ")

# Close the channel.
channel.close()

# Close the connection to RabbitMQ.
connection.close()
