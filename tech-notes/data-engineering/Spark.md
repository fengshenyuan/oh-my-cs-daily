## Spark底层最值得一读的论文
- [Resilient Distributed Datasets: A fault-tolerant abstraction for in-Memory cluster computing 原版论文](https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf)
- [RDD论文中文翻译版：弹性分布式数据集：基于内存的集群计算的容错性抽象](https://fangmiao97.github.io/2019/04/13/tanslate-Resilient-Distributed-Datasets-A-Fault-Tolerant-Abstraction%E2%80%93for-In-Memory-Cluster-Computing/)
- [入门必读 | Spark 论文导读 - 《Resilient Distributed Datasets: A fault-tolerant abstraction for in-Memory cluster computing》](https://zhuanlan.zhihu.com/p/102572842)
- [Large-Scale Intelligent Microservices](https://arxiv.org/pdf/2009.08044.pdf) - Microsoft paper that presents an Apache Spark-based micro-service orchestration framework that extends database operations to include web service primitives.(跟我说的分布式数据库是一个更好的微服务体系相一致 - 分布式计算的核心范式转换经历了从数据库层不适用 -> 改造服务计算层(to Mircoservice Arch) -> 数据库层适应了分布式与云原生环境(Microservice为核心的架构转换回到以数据库为核心的架构上来) )

## Spark Broadcast Join
Spark Broadcast Join是一种分布式的多计算核心计算方案，这可以在一定程度上扩展spark所能处理的数据规模。shuffle时可以尽可能保证单个节点可以完成运算。这感觉和Snowflake的计算模型不太一样：Snowflake更可能是把数据拉到集群里，然后单个核心直接计算(需要验证？但是怎么验证呢？Snowflake又没有开源 :cry: )

## Spark基础：Parquet
- [Parquet文件存储格式详细解析](https://zhuanlan.zhihu.com/p/363509988)
  - Striping/Assembly算法
    - Repetition Levels
    - Definition Levels
  - Parquet的优势
    - 映射下推(Project PushDown)
    - 谓词下推(Predicate PushDown)
- [一文讲透大数据列存标准格式 - Parquet](https://zhuanlan.zhihu.com/p/341572070)
- [原版论文：Dremel: Interactive Analysis of Web-Scale Datasets](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/36632.pdf)

## Delta Lake
数砖大佬们给 VLDB 投了一篇名为《Delta Lake: High-Performance ACID Table Storage overCloud Object Stores》的论文，并且被 VLDB 收录了，这是第一篇比较系统介绍数砖开发 Delta Lake 的论文
- [全面介绍数砖开发 Delta Lake 的第一篇论文](https://www.sohu.com/a/431026284_315839)
- [Snowflake、Delta Lake 两大新型数仓对比分析](https://zhuanlan.zhihu.com/p/350958074)

## Spark学习路径
- [RDD](https://www.cnblogs.com/qingyunzong/p/8899715.html)
```
1.2　RDD的属性
（1）一组分片（Partition），即数据集的基本组成单位。对于RDD来说，每个分片都会被一个计算任务处理，并决定并行计算的粒度。用户可以在创建RDD时指定RDD的分片个数，如果没有指定，那么就会采用默认值。默认值就是程序所分配到的CPU Core的数目。

（2）一个计算每个分区的函数。Spark中RDD的计算是以分片为单位的，每个RDD都会实现compute函数以达到这个目的。compute函数会对迭代器进行复合，不需要保存每次计算的结果。

（3）RDD之间的依赖关系。RDD的每次转换都会生成一个新的RDD，所以RDD之间就会形成类似于流水线一样的前后依赖关系。在部分分区数据丢失时，Spark可以通过这个依赖关系重新计算丢失的分区数据，而不是对RDD的所有分区进行重新计算。

（4）一个Partitioner，即RDD的分片函数。当前Spark中实现了两种类型的分片函数，一个是基于哈希的HashPartitioner，另外一个是基于范围的RangePartitioner。只有对于于key-value的RDD，才会有Partitioner，非key-value的RDD的Parititioner的值是None。Partitioner函数不但决定了RDD本身的分片数量，也决定了parent RDD Shuffle输出时的分片数量。

（5）一个列表，存储存取每个Partition的优先位置（preferred location）。对于一个HDFS文件来说，这个列表保存的就是每个Partition所在的块的位置。按照“移动数据不如移动计算”的理念，Spark在进行任务调度的时候，会尽可能地将计算任务分配到其所要处理数据块的存储位置。
```
- RDD各种算子
```
map(func)
flatMap(func)
mapPartitions(func)
mapPartitionsWithIndex(func)
...
groupByKey([numTasks])
reduceByKey(func, [numTasks])
aggregateByKey(zeroValue)(seqOp, combOp, [numTasks])
sortByKey([ascending], [numTasks])
sortBy(func,[ascending], [numTasks])
cogroup(otherDataset, [numTasks])
coalesce(numPartitions)  ---> CoalescedRDD这个是什么？
```
- [RDD之Partition](https://blog.csdn.net/qq_22473611/article/details/107822168)
```
Spark学习之路 （十七）Spark分区
https://www.cnblogs.com/qingyunzong/p/8987065.html
....
2. 为什么要进行分区
　　数据分区，在分布式集群里，网络通信的代价很大，减少网络传输可以极大提升性能。mapreduce框架的性能开支主要在io和网络传输，io因为要大量读写文件，它是不可避免的，但是网络传输是可以避免的，把大文件压缩变小文件，   从而减少网络传输，但是增加了cpu的计算负载。

　　Spark里面io也是不可避免的，但是网络传输spark里面进行了优化：

　　Spark把rdd进行分区（分片），放在集群上并行计算。同一个rdd分片100个，10个节点，平均一个节点10个分区，当进行sum型的计算的时候，先进行每个分区的sum，然后把sum值shuffle传输到主程序进行全局sum，所以进行sum型计算对网络传输非常小。但对于进行join型的计算的时候，需要把数据本身进行shuffle，网络开销很大。

spark是如何优化这个问题的呢？

　　Spark把key－value rdd通过key的hashcode进行分区，而且保证相同的key存储在同一个节点上，这样对改rdd进行key聚合时，就不需要shuffle过程，我们进行mapreduce计算的时候为什么要进行shuffle？，就是说mapreduce里面网络传输主要在shuffle阶段，shuffle的根本原因是相同的key存在不同的节点上，按key进行聚合的时候不得不进行shuffle。shuffle是非常影响网络的，它要把所有的数据混在一起走网络，然后它才能把相同的key走到一起。要进行shuffle是存储决定的。

　　Spark从这个教训中得到启发，spark会把key进行分区，也就是key的hashcode进行分区，相同的key，hashcode肯定是一样的，所以它进行分区的时候100t的数据分成10分，每部分10个t，它能确保相同的key肯定在一个分区里面，而且它能保证存储的时候相同的key能够存在同一个节点上。比如一个rdd分成了100份，集群有10个节点，所以每个节点存10份，每一分称为每个分区，spark能保证相同的key存在同一个节点上，实际上相同的key存在同一个分区。

　　key的分布不均决定了有的分区大有的分区小。没法分区保证完全相等，但它会保证在一个接近的范围。所以mapreduce里面做的某些工作里边，spark就不需要shuffle了，spark解决网络传输这块的根本原理就是这个。

　　进行join的时候是两个表，不可能把两个表都分区好，通常情况下是把用的频繁的大表事先进行分区，小表进行关联它的时候小表进行shuffle过程。

　　大表不需要shuffle。
　　

　　需要在工作节点间进行数据混洗的转换极大地受益于分区。这样的转换是  cogroup，groupWith，join，leftOuterJoin，rightOuterJoin，groupByKey，reduceByKey，combineByKey 和lookup。

　　分区是可配置的，只要RDD是基于键值对的即可。
```

- Spark RangerPartition
  - [水塘抽样（Reservoir sampling）](https://juejin.cn/post/6844904045845413895)
  - [Spark源码解读2之水塘抽样算法（Reservoir Sampling）](https://www.shangmayuan.com/a/86dd18a781a04d319ff28907.html)
  - [Spark分区器HashPartitioner和RangePartitioner代码详解](https://www.iteblog.com/archives/1522.html)

- [Spark广播变量&累加器](https://www.cnblogs.com/frankdeng/p/9301653.html)
```
# 广播变量注意事项
1、能不能将一个RDD使用广播变量广播出去？不能，因为RDD是不存储数据的。可以将RDD的结果广播出去。
2、 广播变量只能在Driver端定义，不能在Executor端定义。
3、 在Driver端可以修改广播变量的值，在Executor端无法修改广播变量的值。
4、如果executor端用到了Driver的变量，如果不使用广播变量在Executor有多少task就有多少Driver端的变量副本。
5、如果Executor端用到了Driver的变量，如果使用广播变量在每个Executor中只有一份Driver端的变量副本。
```
![image](https://user-images.githubusercontent.com/20035835/165106168-bf3f2eb8-4dcd-4f36-95a6-2e21968673dd.png)

```
# 累加器注意事项
1、 累加器在Driver端定义赋初始值，累加器只能在Driver端读取最后的值，在Excutor端更新。
2、累加器不是一个调优的操作，因为如果不这样做，结果是错的
```
![image](https://user-images.githubusercontent.com/20035835/165106343-012ff696-d9b2-4029-8889-c9f74dec4503.png)


- [Yarn集群运行环境详解](https://blog.csdn.net/qq_22473611/article/details/88640495)
```
YARN的出现，使得多个计算框架可以运行在一个集群当中。

  1）每个应用程序对应一个ApplicationMaster。

  2）目前可以支持多种计算框架运行在YARN上面比如MapReduce、Storm、Spark、Flink等。

YARN作为一个资源调度平台。三个组件-ResourceManager, NodeManager以及ApplicationMaster，它们各自的职责。

严格来说，YARN只包含两个组件，ResourceManager以及NodeManager。而ApplicationMaster只是一个YARN的客户端
————————————————
版权声明：本文为CSDN博主「四月天03」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_22473611/article/details/88640495
```
- [Spark任务的提交与运行 - 源码级解释](https://www.cnblogs.com/frankdeng/p/9301485.html)
```
一、Spark中的基本概念
（1）Application：表示你的应用程序

（2）Driver：表示main()函数，创建SparkContext。由SparkContext负责与ClusterManager通信，进行资源的申请，任务的分配和监控等。程序执行完毕后关闭SparkContext

（3）Executor：某个Application运行在Worker节点上的一个进程，该进程负责运行某些task，并且负责将数据存在内存或者磁盘上。在Spark on Yarn模式下，其进程名称为 CoarseGrainedExecutor Backend，一个CoarseGrainedExecutor Backend进程有且仅有一个executor对象，它负责将Task包装成taskRunner，并从线程池中抽取出一个空闲线程运行Task，这样，每个CoarseGrainedExecutorBackend能并行运行Task的数据就取决于分配给它的CPU的个数。

（4）Worker：集群中可以运行Application代码的节点。在Standalone模式中指的是通过slave文件配置的worker节点，在Spark on Yarn模式中指的就是NodeManager节点。

（5）Task：在Executor进程中执行任务的工作单元，多个Task组成一个Stage

（6）Job：包含多个Task组成的并行计算，是由Action行为触发的

（7）Stage：每个Job会被拆分很多组Task，作为一个TaskSet，其名称为Stage

（8）DAGScheduler：根据Job构建基于Stage的DAG，并提交Stage给TaskScheduler，其划分Stage的依据是RDD之间的依赖关系

（9）TaskScheduler：将TaskSet提交给Worker（集群）运行，每个Executor运行什么Task就是在此处分配的。
```

```
2.1　Spark的基本运行流程
1、说明
(1)构建Spark Application的运行环境（启动SparkContext），SparkContext向资源管理器（可以是Standalone、Mesos或YARN）注册并申请运行Executor资源；

(2)资源管理器分配Executor资源并启动StandaloneExecutorBackend，Executor运行情况将随着心跳发送到资源管理器上；

(3)SparkContext构建成DAG图，将DAG图分解成Stage，并把Taskset发送给Task Scheduler。Executor向SparkContext申请Task

(4)Task Scheduler将Task发放给Executor运行同时SparkContext将应用程序代码发放给Executor。

(5)Task在Executor上运行，运行完毕释放所有资源。
```

- [Spark Shuffle详解1](https://www.cnblogs.com/itlz/p/15148079.html)
```
Spark Shuffle 分为两种：一种是基于 Hash 的 Shuffle；另一种是基于 Sort 的 Shuffle。先介绍下它们的发展历程，有助于我们更好的理解 Shuffle：

在 Spark 1.1 之前， Spark 中只实现了一种 Shuffle 方式，即基于 Hash 的 Shuffle 。在 Spark 1.1 版本中引入了基于 Sort 的 Shuffle 实现方式，并且 Spark 1.2 版本之后，默认的实现方式从基于 Hash 的 Shuffle 修改为基于 Sort 的 Shuffle 实现方式，即使用的 ShuffleManager 从默认的 hash 修改为 sort。在 Spark 2.0 版本中， Hash Shuffle 方式己经不再使用。

Spark 之所以一开始就提供基于 Hash 的 Shuffle 实现机制，其主要目的之一就是为了避免不需要的排序，大家想下 Hadoop 中的 MapReduce，是将 sort 作为固定步骤，有许多并不需要排序的任务，MapReduce 也会对其进行排序，造成了许多不必要的开销
...
```
- [Spark Shuffle详解2](https://www.cnblogs.com/xueqiuqiu/articles/12979864.html)
```
Shuffle描述着数据从map task输出到reduce task输入的这段过程。shuffle是连接Map和Reduce之间的桥梁，Map的输出要用到Reduce中必须经过shuffle这个环节，shuffle的性能高低直接影响了整个程序的性能和吞吐量。因为在分布式情况下，reduce task需要跨节点去拉取其它节点上的map task结果。这一过程将会产生网络资源消耗和内存，磁盘IO的消耗。通常shuffle分为两部分：Map阶段的数据准备和Reduce阶段的数据拷贝处理。一般将在map端的Shuffle称之为Shuffle Write，在Reduce端的Shuffle称之为Shuffle Read.
...
```
- [Spark内存管理与调优](https://www.cnblogs.com/frankdeng/p/9301783.html)
![image](https://user-images.githubusercontent.com/20035835/164983943-d8bb3f70-d35d-49a5-a8f0-2ad3200aa8ad.png)

- [Spark之开发调优以及资源调优](https://www.cnblogs.com/frankdeng/p/9301780.html)
```
Spark调优主要分为开发调优、资源调优、数据倾斜调优、shuffle调优几个部分。开发调优和资源调优是所有Spark作业都需要注意和遵循的一些基本原则，是高性能Spark作业的基础；数据倾斜调优，主要讲解了一套完整的用来解决Spark作业数据倾斜的解决方案；shuffle调优，面向的是对Spark的原理有较深层次掌握和研究的同学，主要讲解了如何对Spark作业的shuffle运行过程以及细节进行调优。

本文作为Spark性能优化指南的基础篇，主要讲解开发调优以及资源调优。
...
```

- [SparkSQL内核剖析](https://xie.infoq.cn/article/2a70e9fb993bed9bc9ed02c46)
```
SparkSQL提供了一个叫做 DataFrames 的可编程抽象数据模型，并且可被视为一个分布式的 SQL 查询引擎。对外提供 SQL 的操作方式主要为 JDBC 数据源，CLI shell 和 Programs 三种；而 SQL 解析，优化以及运行都是由 SparkSQL Catalyst 模块完成，最终转化为相应的 Spark Rdd 执行计算任务。
```
![image](https://user-images.githubusercontent.com/20035835/164983918-6c2e7507-e72b-4430-8c05-4912cf162375.png)

- [别再人云亦云了！！！你真的搞懂了RDD、DF、DS的区别吗？](https://www.cnblogs.com/mr-bigdata/p/14426049.html)
```
写得真的好！
```
- [Spark中RDD、DataFrame和DataSet的区别 ？](https://codeantenna.com/a/lVaWJDkEFJ)
```
因为DataFrame和DataSet的API是建立在Spark SQL引擎之上的，无论是java、scala还是python，所有涉及到关系型查询的语句，都会经历相同的逻辑优化和执行计划。不同的是， Dataset[T]类的API更适合数据工程任务，Dataset[Row]（即DataFrame）类的API则更适合交互式分析。而且，spark作为一种编译器可以理解DataSet中的JVM对象，可以通过Tungsten编码，将这些对象进行快速的序列化和反序列化。
```
- [Spark SQL知识点大全与实战](https://www.ikeguang.com/?p=1946)
```
Spark SQL是Spark用于结构化数据(structured data)处理的Spark模块。
与基本的Spark RDD API不同，Spark SQL的抽象数据类型为Spark提供了关于数据结构和正在执行的计算的更多信息。
在内部，Spark SQL使用这些额外的信息去做一些额外的优化，有多种方式与Spark SQL进行交互，比如: SQL和DatasetAPI。
当计算结果的时候，使用的是相同的执行引擎，不依赖你正在使用哪种API或者语言。这种统一也就意味着开发者可以很容易在不同的API之间进行切换，这些API提供了最自然的方式来表达给定的转换。
Hive是将Hive SQL转换成 MapReduce然后提交到集群上执行，大大简化了编写MapReduce的程序的复杂性，由于MapReduce这种计算模型执行效率比较慢。所以Spark SQL的应运而生，它是将Spark SQL转换成RDD，然后提交到集群执行，执行效率非常快！
Spark SQL它提供了2个编程抽象，类似Spark Core中的RDD
（1）DataFrame
（2）Dataset
...
```

- [Spark数据倾斜处理](https://blog.csdn.net/kaede1209/article/details/81145560)
```
什么是数据倾斜
数据倾斜是指我们在并行进行数据处理的时候，由于数据Spark的单个Partition)的分布不均，导致大量的数据集中分不到一台或者某几台计算节点上，导致处理速度远低于平均计算速度，从而拖延导致整个计算过程过慢，影响整个计算性能

数据倾斜的危害
单个或者某几个task拖延整个任务运行时间,导致整体耗时过大
单个task处理数据过多，很容易导致oom
Executor Kill lost,Shuffle error 
数据倾斜的产生
 数据倾斜容易产生在两个过程，本身数据源读的倾斜，这个主要由于本身文件的分布不均，主要是不能切分的文件isSplitable=false 例如gz 另外的在shuffle阶段，key的分布不均，导致大量的数据集中到单个或者某几个task上导致数据整个stage，执行慢，影响整个job作业，总结主要有以下两个过程

数据源数据文件不均匀
计算过程中key的分布不均
单个rdd中进行groupby 的时候key分布不均
多个rdd进行join过程中key的不均匀

————————————————
版权声明：本文为CSDN博主「彩笔程序猿zxxxx」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/kaede1209/article/details/81145560
```

- [Spark性能优化之道——解决Spark数据倾斜（Data Skew）的N种姿势](http://www.jasongj.com/spark/skew/)
```
什么是数据倾斜
对Spark/Hadoop这样的大数据系统来讲，数据量大并不可怕，可怕的是数据倾斜。

何谓数据倾斜？数据倾斜指的是，并行处理的数据集中，某一部分（如Spark或Kafka的一个Partition）的数据显著多于其它部分，从而使得该部分的处理速度成为整个数据集处理的瓶颈。

对于分布式系统而言，理想情况下，随着系统规模（节点数量）的增加，应用整体耗时线性下降。如果一台机器处理一批大量数据需要120分钟，当机器数量增加到三时，理想的耗时为120 / 3 = 40分钟，如下图所示
```
![image](https://user-images.githubusercontent.com/20035835/165014869-8047d0bb-2e2d-4aaf-890c-994fe5b275f3.png)

- [Spark面试题整理](https://github.com/MoRan1607/BigDataGuide/tree/master/%E9%9D%A2%E8%AF%95/Spark%E9%9D%A2%E8%AF%95%E9%A2%98%E6%95%B4%E7%90%86)

