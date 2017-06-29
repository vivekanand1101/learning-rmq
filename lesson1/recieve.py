#!/usr/bin/env python
# coding=utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare('hello')

def print_recieved_msg(ch, method, properties, body):
    ''' Print the recieved msg '''
    print 'Received: ', body

channel.basic_consume(print_recieved_msg, queue='hello', no_ack=True)
channel.start_consuming()
