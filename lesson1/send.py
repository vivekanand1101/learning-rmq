#!/usr/bin/env python
# coding=utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare('hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello world')
print 'Sent'
connection.close()
