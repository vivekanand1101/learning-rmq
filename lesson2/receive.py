#!/usr/bin/env python
# coding=utf-8

import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare('task_queue', durable=True)

def print_recieved_msg(ch, method, properties, body):
    """ Wait and print this time to demo a long running process """

    print 'Received: ', body
    length = body.count('.')
    time.sleep(length)
    print 'Done: ', body

    # Tell the Broker to free the memory as the task is done
    # Only needed with ACK is on (which is the default setting
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(print_recieved_msg, queue='task_queue')

channel.start_consuming()
