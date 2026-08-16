# Queue & Asynchronous Task Orchestration System
This document is used to record the asynchronous task orchestration system learning notes.

Target Systems
* ABC ATQ System
* Airbnb Airflow
* AWS StepFunction
* ...

# Task Queue

[Task Queues - Full Stack Python](https://www.fullstackpython.com/task-queues.html)

This blog collects a lot of network resources about Task Queue in Python.

Generally speaking, task queue is in language or in framework solution. The unit dispatched into the queue is `task`, not a general message.

## Pull Model
*  A while True loop to fetch message from Broker if u are developing long-running consumer.


## Background Tasks
In most cases when we mentioned background tasks, it's usually not the Messaging Queue System we general talking about. These background tasks usually implemented with built-in infrastructure in the same framework. They are just background tasks. Sometimes, they cannot even be called asynchronous tasks, because they just execute in the background. We don't even need their asynchronous responses.

  ![image](https://user-images.githubusercontent.com/20035835/157273344-42baff79-e759-46f7-b233-172a696a3c20.png)

## Asynchronous Tasks
In this kind of tasks, there is a broker to pass messages between producers and consumers, more precisely, in this context, the caller will create and push the tasks into the broker, and the worker will get the task info in the broker after restoring the task into an executable object in the environment.

[Developing an Asynchronous Task Queue in Python](https://testdriven.io/blog/developing-an-asynchronous-task-queue-in-python/)

In this blog, a Redis Demo shows that it will serialize the python task definition with parameters together. Although it's not a good practice, it's here. I am worrying that this pattern used in more places.

```python
# redis_queue.py

import uuid
import pickle


class SimpleQueue(object):
    def __init__(self, conn, name):
        self.conn = conn
        self.name = name

    def enqueue(self, func, *args):
        task = SimpleTask(func, *args)
        serialized_task = pickle.dumps(task, protocol=pickle.HIGHEST_PROTOCOL)
        self.conn.lpush(self.name, serialized_task)
        return task.id

    def dequeue(self):
        _, serialized_task = self.conn.brpop(self.name)
        task = pickle.loads(serialized_task)
        task.process_task()
        return task

    def get_length(self):
        return self.conn.llen(self.name)


class SimpleTask(object):
    def __init__(self, func, *args):
        self.id = str(uuid.uuid4())
        self.func = func
        self.args = args

    def process_task(self):
        self.func(*self.args)

```

[rq - Simple job queues for Python]( https://python-rq.org)

This is typically the implementation of this kind of async task system. 

The rq system has 3 basic components, the Job object, the worker and the queue.
The producer will push the job-related info including the func reference and params as meta info to the queue. Then you need to launch a worker instance to fetch meta info from the queue, restore a new Job object with the meta info, and finally perform the computing task.

To implement a system like rq, you need to design an internal job status and job meta info exchange protocol between the producer and the worker. 

**Disadvantages**

It's obvious to see that these systems are hard to corporate with other frameworks and languages. They are suitable tools to solve small scale async tasks limited to only one language and one framework.

**Related Frameworks**
 - [resque - a Redis-backed Ruby library for creating background jobs, placing them on multiple queues, and processing them later.](https://github.com/resque/resque)
- [tasq - A simple brokerless task queue implementation leveraging zmq and a naive implementation of the actor model...](https://github.com/codepr/tasq)


# General Messaging Queue

- [beanstalk - a simple, fast work queue](https://github.com/beanstalkd/beanstalkd)
- [ZMQ - An open-source universal messaging library](https://zeromq.org/) This is a very important topic. Lots of solutions can be based on ZMQ.

# [Celery](https://github.com/celery/celery)
Celery is special enough to have a separate topic here!

* Learn Celery architecture and basic usage
* Learn the core concepts in Message Queue
* Compare the Task Queue Solution and the Spark Solution for Bulk Delivery
