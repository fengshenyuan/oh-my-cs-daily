# Computer System

# Language&Compiler

# Network

# Python
- 函数执行时间的装饰器
    ```Python
    def runtime_cost(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()

            try:
                result = func(*args, **kwargs)
            except Exception as Ex:
                result = None

                logging.info(traceback.format_exc())

            end_time = time.time()

            logging.info(func.__module__ + "." + func.__name__ + " call takes " + str(end_time - start_time) + " seconds")

            return result

        return wrapper
    ```

- map函数的实现
    ```Python
    def map_impl(func, iterable):
        result = []
        try:
            for x in iterable:
                if func(x):
                    result.append(x)

        except Exception as ex:
            logging.info(traceback.format_exc())

        return result

    ```

# DataBase

# Redis

# NewStack

# LinuxCmds

# RealWorldProblems

* URL Quick Match
    ```
    问题：现有1亿条URL访问记录，sample如下
    GET /v1.3/intelligence/apps/app/986905979/history 200
    ...

    所有的URL访问记录都来自于下面1000个RESTful风格的URL Pattern。
    所有的URL Pattern都是结构良好的，即API Name中的各个部分对应着RESTful中对应的名字或正则表达式，即不存在一个正则表达式包含多个部分的情况。
    /v1.3/%(vertical)s/unified_search /v1.3/(?P<vertical>apps)/unified_search$
    /v1.3/intelligence/sdk/%(sdk_id)s/details /v1.3/intelligence/sdk/(?P<sdk_id>[0-9]+)/details
    /v1.3/intelligence/%(vertical)s/%(market)s/ad-platforms /v1.3/intelligence/(?P<vertical>apps)/(?P<market>[0-9a-zA-Z_\-.]+)/ad-platforms$
    /v1.3/%(vertical)s/%(market)s/ranking /v1.3/(?P<vertical>apps)/(?P<market>[0-9a-zA-Z_\-.]+)/ranking


    现在想统计这1000个URL Pattern各自的访问量是多少，请问应该如何做？


    注：1000个URL Pattern中不含相互交叉的部分，即每个URL必然且只能匹配到唯一一个URL Pattern.

    ==>
    1.顺序匹配太慢；
    2.优化的方向是：
    (1).尽可能缩小需要匹配的URL Pattern的数量。
        这可以从URL Pattern的前缀、后缀、长度等各个维度与URL本身进行匹配，然后再进行正则校验。
    (2).在第一步的基础上如何获得一个最佳的匹配顺序？
        搜索引擎原理就是干这个事情的。
        构建一个倒排索引和一个简单的计分系统即可。


    ```
