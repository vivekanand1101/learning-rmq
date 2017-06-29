#!/usr/bin/env python
# coding=utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare('logs', type='fanout')

msg = 'hello there'
channel.basic_publish(exchange='logs', routing_key='', body=msg)
print 'Sent: ', msg
connection.close()
