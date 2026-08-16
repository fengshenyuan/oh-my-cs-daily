# -*-coding:utf8 -*-

# This file is a collection to impl singleton pattern in Python
# Reference
# 1).Python 中的单例模式
#    http://python.jobbole.com/87294/
# 2).Python单例模式的4种实现方法
#    http://blog.csdn.net/ghostfromheaven/article/details/7671853
# 3).[python实现设计模式]-1. 单例模式
#    https://www.cnblogs.com/kakaliush/p/5228165.html

# Note: When use singleton pattern with threads and coroutines
#       you should be very careful.
#       Threads and coroutines may change the singleton instance's
#       states without any notifications.
#       Tornado coroutines with a singleton db session controller
#       meet this problem when every coroutine try to release db session
#       when they finished their call, while other coroutines still try to
#       use the released db session when they wake up.


# Method 01
# use __new__
# but not thread safe
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class ThreadSafeSingleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                Lock.acquire()
                # double check for thread safe
                if not cls._instance:
                    orig = super(ThreadSafeSingleton, cls)
                    cls._instance = orig.__new__(cls, *args, **kwargs)
            finally:
                Lock.release()

        return cls._instance


class MyClass(Singleton):
    pass

# Method 02
# share object's inner states dict
# it's magic, not recommend in real world


class Borg(object):
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg, cls).__new__(cls, *args, **kw)
        obj.__dict__ = cls._state
        return obj


class MyClass02(Borg):
    pass

one = MyClass02()
two = MyClass02()

# one and two are different objects, but they share the same inner states dict
print(id(one))
# 28873680
print(id(two))
# 28873712
print(one == two)
# False
print(one is two)
# False

print(id(one.__dict__))
# 30104000
print(id(two.__dict__))
# 30104000


# Method03
# use __metaclass__

class Singleton03(type):
    def __init__(cls, name, bases, dict):
        super(Singleton03, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton03, cls).__call__(*args, **kwargs)
        return cls._instance


# you can also use this to impl Singleton03
class Singleton03_02(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs)
        return cls._instances[cls]


class MyClass03(object):
    # Python2.x style
    __metaclass__ = Singleton2


class MyClass03_02(metaclass=Singleton03):
    # Python3.x style
    pass


# Method04
# Decorator

def singleton04(cls):
    _instances = {}

    @functools.wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return get_instance


@singleton
class MyClass04(object):
    pass
