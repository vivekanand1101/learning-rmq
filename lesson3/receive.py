#!/usr/bin/env python
# coding=utf-8

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.exchange_declare('logs', type='fanout')

# Queue with arbitrary anem
# Exclusive means, the queue will be ommitted once the consumer disconnect
queue = channel.queue_declare(exclusive=True)
channel.queue_bind(exchange='logs', queue=queue.method.queue)

def print_logs(ch, method, properties, body):
    ''' Receive the logs '''
    print body


# No ack since, everyone will start yelling that they received the msg
channel.basic_consume(print_logs, queue=queue.method.queue, no_ack=True)

channel.start_consuming()
