# Python
## 为什么Python 3.6以后字典有序并且效率更高？- Python3中的字典是如何实现的？
> entries数组之外，添加了额外的indices数组作为entries的存储索引，使得entries数组从稀疏变得更加紧密，从而节省了空间，提升了遍历的速度，且保证了读取时可以按照插入顺序！

link: https://www.kingname.info/2019/07/13/python-dict/

# SQL 
## SQL之行转列Pivot函数
> Rotates a table by turning the unique values from one column in the input expression into multiple columns and aggregating results where required on any remaining column values. In a query, it is specified in the FROM clause after the table name or subquery.

link:
- https://zhuanlan.zhihu.com/p/76965711 (用case语句实现pivot函数)
- https://docs.snowflake.com/en/sql-reference/constructs/pivot.html

## 数据分析SQL面试题目9套汇总
https://zhuanlan.zhihu.com/p/88942950

## Redis持久化机制：RDB和AOF
> Redis作为一个内存数据库，数据是以内存为载体存储的，那么一旦Redis服务器进程退出，服务器中的数据也会消失。为了解决这个问题，Redis提供了持久化机制，也就是把内存中的数据保存到磁盘当中，避免数据意外丢失
Redis提供了两种持久化方案：RDB持久化和AOF持久化，一个是快照的方式，一个是类似日志追加的方式

作者：TurboSnail
链接：https://juejin.cn/post/6844903939339452430
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## Apache Kafka内核深度剖析
https://insights.thoughtworks.cn/apache-kafka/
> Kafka该怎么用
虽然Kafka整体看起来非常优秀，但是Kafka也不是全能的银弹，必然有其对应的短板，那么对于Kafka如何，或者如何能用的更好，则需要经过实际的实践才能得感悟的出。经过归纳和总结，能够发现以下不同的使用场景和特点。

- Kafka 并不合适高频交易系统：Kafka虽然具有非常高的吞吐量和性能，但是不可否认，Kafka在单条消息的低延迟方面依旧不如传统MQ，毕竟依托推模型的MQ能够在实时消息发送的场景下取得先天的优势。
- Kafka并不具备完善的事务机制：0.11之后Kafka新增了事务机制，可以保障Producer的批量提交，为了保障不会读取到脏数据，Consumer可以通过对消息状态的过滤过滤掉不合适的数据，但是依旧保留了读取所有数据的操作，即便如此Kafka的事务机制依旧不完备，背后主要的原因是Kafka对client并不感冒，所以不会统一所有的通用协议，因此在类似仅且被消费一次等场景下，效果非常依赖于客户端的实现。
- Kafka的异地容灾方案非常复杂：对于Kafka来说，如果要实现跨机房的无感知切换，就需要支持跨集群的代理，因为Kafka特殊的append log的设计机制，导致同样的offset在不同的broker和不同的内容上无法复用，也就是文件一旦被拷贝到另外一台服务器上，将不可读取，相比类似基于数据库的MQ，很难实现数据的跨集群同步，同时对于offset的复现也非常难，曾经帮助客户实现了一套跨机房的Kafka 集群Proxy，投入了非常大的成本。
- Kafka Controller架构无法充分利用集群资源：Kafka Controller类似于Es的去中心化思想，按照竞选规则从集群中选择一台服务器作为Controller，意味着改服务器即承担着Controller的职责，同时又承担着Broker的职责，导致在海量消息的压迫下，该服务器的资源很容易成为集群的瓶颈，导致集群资源无法最大化。Controller虽然支持HA但是并不支持分布式，也就意味着如果要想Kafka的性能最优，每一台服务器至少都需要达到最高配置。
- Kafka不具备非常智能的分区均衡能力：通常在设计落地存储的时候，对于热点或者要求性能足够高的场景下，会是SSD和HD的结合，同时如果集群存在磁盘容量大小不均等的情况，对于Kafka来说会有非常严重的问题，Kafka的分区产生是按照paratition的个数进行统计，将新的分区创建在个数最少的磁盘上
