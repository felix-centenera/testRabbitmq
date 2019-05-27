#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq.rabbitmq.svc'))
channel = connection.channel()

channel.basic_publish(exchange='',
                      routing_key='qa1',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()
