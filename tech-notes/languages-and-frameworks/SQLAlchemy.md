# SQLAlchemy

## When to Expire or Refresh 
The Session uses the expiration feature automatically whenever the transaction referred to by the session ends. Meaning, whenever Session.commit() or Session.rollback() is called, all objects within the Session are expired, using a feature equivalent to that of the Session.expire_all() method. The rationale is that the end of a transaction is a demarcating point at which there is no more context available in order to know what the current state of the database is, as any number of other transactions may be affecting it. Only when a new transaction starts can we again have access to the current state of the database, at which point any number of changes may have occurred.

>  That means we should avoid keeping lots of objects in one session. Otherwise, every time you commit or rollback your DB will receive a group of queries to refresh these objects in this session.

## Expunging
Expunge removes an object from the Session, sending persistent instances to the detached state, and pending instances to the transient state:

`session.expunge(obj1)`

To remove all items, call expunge_all() (this method was formerly known as clear()).

> This makes the objects out of the session's control so that you use them as return results from DB, without worrying you will change anything.

## Session Reusage
When the transactional state is completed after a rollback or commit, the Session releases all Transaction and Connection resources, and goes back to the “begin” state, which will again invoke new Connection and Transaction objects as new requests to emit SQL statements are received.

> This means a session is reusable on multiple transactions.

## Using Thread-Local Scope with Web Applications
As discussed in the section When do I construct a Session, when do I commit it, and when do I close it?, a web application is architected around the concept of a web request, and integrating such an application with the Session usually implies that the Session will be associated with that request. As it turns out, most Python web frameworks, **with notable exceptions such as the asynchronous frameworks Twisted and Tornado**, use threads in a simple way, such that a particular web request is received, processed, and completed within the scope of a single worker thread. When the request ends, the worker thread is released to a pool of workers where it is available to handle another request.

This simple correspondence of web request and thread means that to associate a Session with a thread implies it is also associated with the web request running within that thread, and vice versa, provided that the Session is created only after the web request begins and torn down just before the web request ends. So it is a common practice to use scoped_session as a quick way to integrate the Session with a web application. The sequence diagram below illustrates this flow:
```

Web Server          Web Framework        SQLAlchemy ORM Code
--------------      --------------       ------------------------------
startup        ->   Web framework        # Session registry is established
                    initializes          Session = scoped_session(sessionmaker())

incoming
web request    ->   web request     ->   # The registry is *optionally*
                    starts               # called upon explicitly to create
                                         # a Session local to the thread and/or request
                                         Session()

                                         # the Session registry can otherwise
                                         # be used at any time, creating the
                                         # request-local Session() if not present,
                                         # or returning the existing one
                                         Session.query(MyClass) # ...

                                         Session.add(some_object) # ...

                                         # if data was modified, commit the
                                         # transaction
                                         Session.commit()

                    web request ends  -> # the registry is instructed to
                                         # remove the Session
                                         Session.remove()

                    sends output      <-
outgoing web    <-
response

```

Using the above flow, the process of integrating the Session with the web application has exactly two requirements:

Create a single scoped_session registry when the web application first starts, ensuring that this object is accessible by the rest of the application.

Ensure that scoped_session.remove() is called when the web request ends, usually by integrating with the web framework’s event system to establish an “on request end” event.

As noted earlier, the above pattern is just one potential way to integrate a Session with a web framework, one which in particular makes the significant assumption that the web framework associates web requests with application threads. It is however strongly recommended that the integration tools provided with the web framework itself be used, if available, instead of scoped_session.

In particular, while using a thread local can be convenient, it is preferable that the Session be associated directly with the request, rather than with the current thread. The next section on custom scopes details a more advanced configuration which can combine the usage of scoped_session with direct request based scope, or any kind of scope.

> This means we cannot use scoped_session directly with Tornado. We need to find a way of managing the DB session of each request separately.

> The above flow is a way to integrate the scoped_session with thread-based frameworks, such as flask under gunicorn thread or gthread model.

> The scoped_session by default is thread local storage, which means, a special object is used that will maintain a distinct object per each application thread. 

> Most better way is that the Session be associated directly with the request, rather than with the current thread.

# Tornado + Sqlalchemy
> Tornado is designed to be used by passing the request around explicitly to wherever it's needed; there is no implicit global magic. If you really want to use scoped_session you might be able to build something with contextvars.

[From the author of Tornado](https://github.com/tornadoweb/tornado/issues/2705)


### SQLAlchemy Session Execute Raw SQL
https://docs.sqlalchemy.org/en/13/orm/session_api.html#sqlalchemy.orm.session.Session.execute

```shell
>>> from application.services.model.db_sessions import get_session
>>> session = get_session()
>>>
>>> insert_qa_task = """INSERT INTO aa_bulk_qa_tasks ("id", "task_status", "s3_keys", "create_time", "bundle", "granularity", "target_date", "change_id") VALUES ('f2ee55c638084ebfb35a00c003670ad9', '101', '{}', '2020-03-01', 'store', 'daily', '2020-04-01', '3');"""
>>> session.execute(insert_qa_task)
<sqlalchemy.engine.result.ResultProxy object at 0x7f3a302f5860>
>>> results = session.execute("""SELECT * FROM aa_bulk_qa_tasks LIMIT 1; """)
>>> for rcd in results:
...     print(rcd)
...
('f2ee55c638084ebfb35a00c003670ad9', 101, {}, datetime.datetime(2020, 3, 1, 0, 0), datetime.datetime(2020, 6, 3, 10, 45, 0, 287701), 'store', 'daily', datetime.date(2020, 4, 1), 3, None, None, None)
>>>
>>> session.execute("""UPDATE aa_bulk_qa_tasks SET task_status = 99 WHERE id = 'f2ee55c638084ebfb35a00c003670ad9'; """)
<sqlalchemy.engine.result.ResultProxy object at 0x7f3a302f5630>
>>> results = session.execute("""SELECT * FROM aa_bulk_qa_tasks LIMIT 1; """)
>>> for rcd in results:
...     print(rcd)
...
('f2ee55c638084ebfb35a00c003670ad9', 99, {}, datetime.datetime(2020, 3, 1, 0, 0), datetime.datetime(2020, 6, 3, 10, 45, 0, 287701), 'store', 'daily', datetime.date(2020, 4, 1), 3, None, None, None)
>>>
>>>
>>> session.execute("""DELETE FROM aa_bulk_qa_tasks;""")
<sqlalchemy.engine.result.ResultProxy object at 0x7f3a302f5898>
>>> results = session.execute("""SELECT * FROM aa_bulk_qa_tasks LIMIT 1; """)
>>> for rcd in results:
...     print(rcd)
...
>>>
```
