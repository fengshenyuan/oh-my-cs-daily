# Data Engineering & Big Data

## Data Architecture
- [常用的几种大数据架构剖析](https://insights.thoughtworks.cn/common-big-data-infrastructure/)
- [数据架构的未来——浅谈流处理架构](https://aijishu.com/a/1060000000007280)
- [Streaming-大数据的未来](https://mp.weixin.qq.com/s/p7PzA9qfDGKKLzmh5qM_Gg)


## Hadoop及其生态
- [Hadoop 十年解读与发展预测](https://www.infoq.cn/article/hadoop-ten-years-interpretation-and-development-forecast)
- [从Hadoop到Spark、Flink，大数据处理框架十年激荡发展史](https://zhuanlan.zhihu.com/p/94302767)
- [解读主流大数据架构](https://zhuanlan.zhihu.com/p/40996525)
- [Azure: Big Data Architectures - 包含大量云大数据处理模式的资料](https://docs.microsoft.com/en-us/azure/architecture/data-guide/big-data/)
- [Hadoop 怎么了，大数据路在何方？](https://greenplum.cn/2019/09/19/hadoop-runs-out-of-gas/)
- [Big Data Telecom](https://www.slideshare.net/TrickConsulting/big-data-telecom)

核心观点
- Hadoop
   - 巅峰已过，正在成为遗留系统
   - Hadoop和分布式数据库在同一个赛道上，Hadoop在这个赛道上目前并无优势
   - 第一代大数据方案的Hadoop巅峰已过，大数据进入第二代：分布式数据库
- 大数据
   - 大数据市场是 SQL市场，是分布式数据库市场
   - 基础分析如BI、交互查询等技术已经成熟
   - 高级分析（机器学习）下沉，向数据库内嵌分析方向发展
   - 高级分析（机器学习）主要问题不在分析而在数据本身
- Could对Hadoop技术的冲击
  - Cloud技术，特别是类S3对象存储提供了比HDFS更廉价、更易用、更可伸缩的存储，撬动了Hadoop的根基HDFS
  - S3 -> HDFS
  - K8S -> Yarn
  - 云计算提供了比独立的Hadoop系统更细粒度、更加灵活、更可运维的分布式伸缩功能，即提供了更好的弹性！
  - 但公有云不能适用于所有企业的应用场景，仍然会需要私有云、混合云场景下的一体化解决方案，但这可能不是再直接适用Hadoop.
- Hadoop自身的复杂性
  - 很快人们发现MapReduce复杂度很高，即使技术实力强大如Facebook都很难写出高效正确的MapReduce程序。
  - 此外除了解决批处理问题，人们需要Hadoop能解决其遇到的交互式查询任务。为此，Facebook 开发了Hive，该项目快速流行起来，到现在还有很多用户。Facebook当时更是高达95%的用户使用Hive而不是裸写MapReduce程序。
  - 由于Hadoop 不是为交互式处理而设计，Hive 效率低，并发度也低。此外Hive不支持标准SQL，使得和其他产品的集成困难重重。

## 趋势&变化
Aigle Data & Data Mesh

- [大数据的问题仍然没有得到完整的解决 Big Data Is Still Hard. Here’s Why](https://www.datanami.com/2019/07/15/big-data-is-still-hard-heres-why/)
   - 云计算解决了一些资源管理上的痛点，但价格、工具链整合、云本身的管理依然是个问题
   - 这些问题不在于cloud自身的缺陷，而是data science中数据管理本身的复杂性 
- [It’s 2019. Can We Drop the Term “Big Data” When We Mean Agile Data?](https://www.infoworks.io/its-2019-and-time-to-drop-the-term-big-data/)
- [How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html)
- [HDFS vs. Cloud Storage: Pros, cons and migration tips - From Google](https://cloud.google.com/blog/products/storage-data-transfer/hdfs-vs-cloud-storage-pros-cons-and-migration-tips)



## My Understanding
- Big Data(Hadoop/Spark/Flink), Cloud, Distributed DB 只是解决同一类问题的不同技术呈现形式，其差别在于暴露出来的细节以及内在组件的组合、部署、运维模式的差别，因而形成了看似不同又雷同的技术栈。
- IT技术三大马车
  - 存储 Storage(HDFS/S3/Parquet/MySQL File/...)
  - 计算 Computing(MapReduce/Spark/Flink/InnoDB/Pandas/...)
  - 通信 Networking(Raft/Paxos/Zookeeper/etc/braft/...)
- 三大挑战
  - 数据同步(Kafka/Logstash/...)
  - 高可用/高性能/一致性(CAP Theory)
  - 资源调度管理
- 三大应用模式
  - OLTP(在线事务型应用)
  - OLAP(离线分析型应用)
  - HATP(新一代应用场景，同时需要在线分析与在线事务的支持才能很好的完成任务，如智慧城市、智慧交通、自动驾驶、智能音箱、虚拟助手等，都大量的分析决策来叠加传统的在线事务业务，最终形成新一代的应用)
 
 ## 组件与系统
- [什么是Kafka？](https://mp.weixin.qq.com/s/NcDNNqH4pebtJQdKvcKi_Q)
- [Apache Flink，流计算？不仅仅是流计算！](https://zhuanlan.zhihu.com/p/53963614)
  - 文中提到了几个非常重要的方向
  - streaming computing 就是我上面说HATP计算类型，同时支持OLTP和OLAP
  - Flink这个话题非常有意思了，值得投入和学习
- [大数据架构如何做到流批一体？](https://www.infoq.cn/article/Uo4pFswlMzBVhq*Y2tB9)
- [官宣！阿里 Blink 和 Flink 合并计划出炉](https://www.infoq.cn/article/GZE4rOr5Y0BssyBR*Rv1)
- [阿里开源全球首个批流一体机器学习平台 Alink，Blink 功能已全部贡献至 Flink](https://www.infoq.cn/article/VNGui2If5fGNcdW7uemA)
- [快速起步 Apache Flink，这远比我们看到的更强大](https://www.infoq.cn/article/AtaBBzQo3GRpm6MkZzhu)
- [如何基于 Kafka 构建一个关系型数据库 - 比较好玩，甚至验证了streaming是否可以作为HATP的基础](https://www.infoq.cn/article/wmB56UkWLg12pWFljaMG?utm_source=related_read&utm_medium=article)
- [为什么我不推荐 Kafka Streams 和 KSQL？](https://www.infoq.cn/article/AFe9vVTyuMlddrArPGwg?utm_source=related_read&utm_medium=article)
- [Flink Forward Asia 2019 - 总结和展望（附PPT下载链接）](https://developer.aliyun.com/article/737762)
- [Flink SQL：使用标准的 ANSI SQL 驱动大数据流计算](https://www.infoq.cn/article/CgxYE69sT3riMxh9X7fc)
- [Flink 从0到1学习—— 分享四本 Flink 国外的书和二十多篇 Paper 论文](https://zhuanlan.zhihu.com/p/70228094)
- [为什么说流处理即未来？](https://zhuanlan.zhihu.com/p/62837715)

## 大数据与AI双生系统
存储、计算、调度、编排、学习、分析、搜索 7大系统

![image](https://user-images.githubusercontent.com/20035835/157274434-0fffc664-71ef-4e76-8ae1-d5a2366f1064.png)

![image](https://user-images.githubusercontent.com/20035835/157274467-23380afb-c38b-480b-aafa-49debf2394b6.png)

**总纲**
* 计算与存储分离设计，数据湖统管一切数据，提供数据统一视角与入口
* 计算下推比数据移动更便宜(计算比存储具有更好的移动性、移植性、适配性)
* 学习无处不在，Machine Learning可以用于大数据处理内部的任何一个地方

### 存储层 Storage
* 数据接入 
  * Filebeats/Apache Flume/Fluentd
  * Kafka
  * Pulsar
* 文件系统 HDFS/OSS/S3/...
* 存储格式 Parquet/Avro/CSV/RelationalEngineFiles/...
* 系统
  * 列式数据库 HBase
  * 行式数据库 Cassandra
  * 数据仓库 Apche Kylin/Apache Druid
  * 关系数据库 MySQL/PostgreSQL/TiDB/...
  * KV Redis
  * 文档型数据库 MongoDB/Elasticsearch/...
  * 数据湖 Apache Hudi

### 计算层 Computing
* Hadoop MapReduce 计算引擎
* Pandas/Dask 列式计算引擎
* Spark 批流一体化处理引擎
* Fink 批流一体化处理引擎
* MySQL/PostgreSQL/SqlAlchemy 关系计算引擎
* Neo4j/TigerGraph等图计算引擎
* MongoDB/Elasticsearch 搜索计算引擎
* Influxdb 时序计算引擎

### 调度层(作业层) Job
* Yarn

### 编排层 Orchestration
* k8s

### AI & Machine Learning
* Spark ML
* Tensorflow Ecosystem
* PyTorch

### OLAP Query & Analytics
* Apache Druid
* Apache Kylin

### Search & Graph Computing
* ElasticSearch
* Neo4j
* TigerGraph

### 交互
* Zeppelin Notebook
* Jupyter Notebook

### 数据可视化
* Matplotlib

### 第三代大数据处理核心架构
![image](https://user-images.githubusercontent.com/20035835/157274566-aebe15a9-ed79-4c51-a069-6412f276a59f.png)

### 问题、观点、博客
- [日志采集系统flume和kafka有什么区别及联系，它们分别在什么时候使用，什么时候又可以结合？](https://www.zhihu.com/question/36688175)
- [Presto、Druid、SparkSQL、Kylin的对比分析，如性能、架构等，有什么异同？](https://www.zhihu.com/question/41541395/answer/666070142)
- [是时候搞一个面向大数据和 AI 的新编程语言了 - SQLFlow ](https://www.infoq.cn/article/KoE2pUuWGEPw8apELeT3)
- [Top 10 Trends for Data Storage with Big Data Analytics](https://www.enterprisestorageforum.com/storage-management/storage-trends/top-10-trends-for-data-storage-with-big-data-analytics.html)
- [独家专访 AI 大神贾扬清：我为什么选择加入阿里巴巴？](https://www.infoq.cn/article/gv7WevhZ*FuvIUxDzu1e)
- [Google推出了Apache Beam以后，spark和flink的路已经要走完了么？](https://www.zhihu.com/question/54673437)
- [6 Trends in Database Management](https://www.mbmsoftware.com/blog/technology/6-trends-in-database-management-2985.html)
- [Database Management Trends in 2020](https://www.dataversity.net/database-management-trends-in-2020/#)
- [Data Gateways in the Cloud Native Era - Sounds good but not interesting](https://www.infoq.com/articles/data-gateways-cloud-native/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=Microservices)

### 公司、网站
- [DATAVERSITY](https://www.dataversity.net/)

### 架构
- [亿级流量系统架构之如何设计每秒十万查询的高并发架构【石杉的架构笔记】](https://juejin.im/post/5bfe771251882509a7681b3a)
- [美图大数据平台架构实践](https://www.infoq.cn/article/QycsTZSz0REAFTgmh_J0)
- [大数据平台 五横一纵](https://www.cnblogs.com/sundy818/p/10382478.html)
- [知名大厂如何搭建大数据平台&架构](https://www.cnblogs.com/xiaodf/p/11611970.html)
- [Enterprise Data Lake Architecture: What to Consider When Designing](https://www.cloudtp.com/doppler/how-to-guide-architecture-patterns-to-consider-when-designing-an-enterprise-data-lake/)
- [TiDB架构与开源之路](https://github.com/thinkpiggy/qcon2018ppt/blob/master/TiDB%E6%9E%B6%E6%9E%84%E4%B8%8E%E5%BC%80%E6%BA%90%E4%B9%8B%E8%B7%AF.pdf)


### Hadoop
- [Hadoop Ecosystem – 15 Must Know Hadoop Components](https://data-flair.training/blogs/hadoop-ecosystem/)
- [Hadoop Ecosystem: Hadoop Tools for Crunching Big Data](https://www.edureka.co/blog/hadoop-ecosystem)
- [2019 年，Hadoop 还是数据处理的可选方案吗？](https://www.infoq.cn/article/zpgr1p*uU6EYoLxSyagb)

### HDFS & HBase
- [Hadoop 之 HDFS 简介](https://www.infoq.cn/article/rudfbPRMb5vwfPyDUS5r)
- [入门Hbase，看这一篇就够了](https://juejin.im/post/5c666cc4f265da2da53eb714#heading-54)
- [HBase问题汇总与解答](https://juejin.im/post/5c6d059af265da2d8c7dc402)
- [【从零单排HBase】全面认识HBase架构](https://juejin.im/post/5e638b41f265da57584db1ee)
- [Apache ORC: the smallest, fastest columnar storage for Hadoop workloads](https://orc.apache.org/)

### Apache Druid
- [快手万亿级实时 OLAP 平台的建设与实践 - Apahce Druid](https://www.infoq.cn/article/IWfHmTig_KNAeEJKF8eS)
- [十分钟了解Apache Druid](https://juejin.im/post/5e6312e76fb9a07cd323e335)
- [Druid 在有赞的使用场景及应用实践](https://www.infoq.cn/article/fXl2QXxCQ-AEx14Ee8X5)

### Apache Hudi
- [Hudi: Uber Engineering的Apache Hadoop增量处理框架](https://www.jianshu.com/p/1ae2db40f43e)
- [深度对比delta、iceberg和hudi三大开源数据湖方案](https://www.infoq.cn/article/FjeBCoNxD2Sz9WLoykFo)

### Apache Kylin
- [Apache Kylin 原理介绍与新架构分享（Kylin On Parquet）| 字节跳动技术沙龙](https://juejin.im/post/5dc54095518825592b20c5f3)


### Flink
- [一文搞懂为什么Flink会称为热门实时流数据处理框架](https://blog.csdn.net/sinat_35667067/java/article/details/105628970)
- [Apache Flink零基础入门到进阶 - 整套教程16篇文章](https://www.infoq.cn/theme/28)

### 流式计算
- [什么是流式计算？](https://juejin.im/post/5d763437f265da03b215605b)
- [什么是流式计算](https://cloud.tencent.com/developer/article/1017092)
- [流式计算和实时计算有什么区别？](https://www.zhihu.com/question/38996005)
- [What is Stream Processing?](https://wso2.com/library/articles/2018/05/what-is-stream-processing/)
- [Stream Processing 101: From SQL to Streaming SQL in 10 Minutes](https://wso2.com/library/articles/2018/02/stream-processing-101-from-sql-to-streaming-sql-in-ten-minutes/)
- [13 Stream Processing Patterns for building Streaming and Realtime Applications](https://iwringer.wordpress.com/2015/08/03/patterns-for-streaming-realtime-analytics/)
- [Streaming Data Integration: The Evolution of ETL](https://wso2.com/library/article/2019/08/streaming-data-integration-the-evolution-of-etl/)
- [谈谈流计算中的『Exactly Once』特性](https://juejin.im/post/5cf0ebe05188251c064813be)

### 图计算 Graph Computing
- [迅速带你入门图计算领域，技术人才趋势产业一应俱全](https://www.jiqizhixin.com/articles/2019-02-27-9)
- [最全技术图谱！一文掌握人工智能各大分支技术](https://cloud.tencent.com/developer/article/1187904)
- [GQL Standard](https://www.gqlstandards.org/)
- [Traversing the Land of Graph Computing and Databases](https://towardsdatascience.com/traversing-the-land-of-graph-computing-and-databases-5cbf8e8ad66b)

### TiDB
- [Gitbook: Deep Dive Tikv](https://tikv.github.io/deep-dive-tikv/overview/introduction.html)

### DHW & Data Lake
- [Data Warehouse Tutorial for Beginners: Learn in 7 Days](https://www.guru99.com/data-warehousing-tutorial.html)
- [What is Data Lake? It's Architecture](https://www.guru99.com/data-lake-architecture.html)
- [Data Lake vs Data Warehouse: What's the Difference?](https://www.guru99.com/data-lake-vs-data-warehouse.html)
- [Building a Platform for Machine Learning and Analytics](https://www.cloudtp.com/doppler/building-platform-machine-learning-analytics/)
- [Enterprise Data Lake Architecture: What to Consider When Designing](https://www.cloudtp.com/doppler/how-to-guide-architecture-patterns-to-consider-when-designing-an-enterprise-data-lake/)
- [Flink + Iceberg 全场景实时数仓的建设实践](https://zhuanlan.zhihu.com/p/347660549)

### AI
- [What is AI? Artificial Intelligence Tutorial for Beginners](https://www.guru99.com/artificial-intelligence-tutorial.html)
- [What is Data Science? Tutorial for Beginners](https://www.guru99.com/data-science-tutorial.html)

### 其他
- [Linkis 数据中间件，打造全面连通融合的金融级大数据平台](https://www.infoq.cn/article/E4jANutN486WrdjPeRWw)
- [大数据及其在物联网中的应用](https://zhuanlan.zhihu.com/p/77779062)
- [Why Is This 30-Year-Old Website Architecture So Popular in 2017?](https://morpheusdata.com/blog/2017-02-28-shared-nothing-architecture)
- [Shared Nothing v.s. Shared Disk Architectures: An Independent View](http://www.benstopford.com/2009/11/24/understanding-the-shared-nothing-architecture/)

### People & Blogsites
- [My views of the World and Systems ~ Hemapani](https://iwringer.wordpress.com/)
- [ben stopford | Gently Flexing the Grid](http://www.benstopford.com/)

### 《Streaming System》学习与总结
- [读 Streaming Systems (一) - By Layne](https://zhuanlan.zhihu.com/p/93522239)
- [读 Streaming Systems (二) - By Layne](https://zhuanlan.zhihu.com/p/96501276)
- [读 Streaming Systems (三) - By Layne](https://zhuanlan.zhihu.com/p/140008612)
- [评:Streaming System(简直炸裂,强势安利) - By 阿莱克西斯](https://zhuanlan.zhihu.com/p/43301661)

### 阿莱克西斯《评:Streaming System》一文中所引出的诸多问题
- 什么是所谓的大数据批处理系统? 一篇非常好的回答 [大数据批量处理系统总结.](https://greeensy.github.io/2014/06/15/Batch-Computing/)
- Apache Hudi的增量计算模型是否欲streaming system的原理一致？ Yes. [增量天然契合流的语义.](https://www.infoq.cn/article/CAgIDpfJBVcJHKJLSbhe)
- CDC(Change Data Capture)的概念: 基于log的数据库自然而然的延伸，且天然符合流式处理的逻辑
  - [CDC（变化数据捕获）同步技术详解](https://blog.csdn.net/qq30211478/article/details/100690948)
  - [浅谈CDC在微服务中的应用](https://zhuanlan.zhihu.com/p/76997736)
  - [Linkedin’s Scalable Consistent Change Data Capture Platform](https://bit.ly/30cUaCh)


### 接下来的两步
- 学习Kafka、Flink、Spark和Apache Hudi
- 学习DDIA和Distributed System两本书

### 学DDIA时想到的问题
- DDIA提到了5中数据处理常用的标准组件(DB，Cache, Search Index, Streaming System, Batching System).问题是这些标准组件到底提供了什么标准语义以及其核心的设计目标是什么(准确性、可靠性、可维护性)
- Fault Torrent: Make it easy to do the right things and discourage the wrong things.
- Declarative Language vs Imperative Language(声明式语言表述的是逻辑，命令式语言表述的是计算，这在一定程度上契合了我常想的分离逻辑与计算的想法，不知是否可以所有启示)

# Hadoop生态组件First Release Time - 进入公众视野(Public Release)的时间

## 核心组件&框架
|Component|Time|
|--|--|
|HDFS|April 1, 2006|
|MapReduce|April 1, 2006|
|HBase|March 28, 2008|
|ZooKeeper|October 27, 2008|
|Hive|October 1, 2010|
|Storm|September 17, 2011|
|Kafka|Jan 6, 2012|
|YARN|August 15, 2012|
|Alluxio|April 8, 2013|
|Mesos|August 11, 2013 v0.12.1|
|Spark|May 26, 2014|
|Flink|August 26, 2014 v0.6| 
|Kylin|June 10, 2015|
|Druid|February 2015 to Apache|
|ClickHouse|June 15, 2016|
|Uber Hoodie|Dec 22, 2016|
|Apache Hudi|Sep 14, 2019|
|Netflix Iceberg|Jul 18, 2018|
|Apache Iceberg|Oct 26, 2019|
|Delta Lake|Apr 24, 2019 |

# 存储格式
|Format|Time|
|--|--|
|CSV|...|
|JSON|...|
|Apache Avro(row based)| November 20, 2009| 
|Apache ORC(列式存储)|February 20, 2013 |
|Apache Parquet(列式存储)|July 2013|
|Apache CarbonData|Huawei in 2013 => May 1, 2017 Apache Top-level project|

>> In February 2013, the Optimized Row Columnar (ORC) file format was announced by Hortonworks in collaboration with Facebook.[3] A month later, the Apache Parquet format was announced, developed by Cloudera and Twitter.[4]

# 未来的大数据发展模式 [“后红海”时代 - 当下大数据架构体系](https://ucc-private-download.oss-cn-beijing.aliyuncs.com/02236c8a8621475e8259898fde2e0518.pdf?Expires=1634459604&OSSAccessKeyId=LTAIvsP3ECkg4Nm9&Signature=o1dzjTYKgw6Sze1a9cXK3qGOmsQ%3D)
关涛，关老板力作
## 重要论断
- 2020年之后Big Data进入后红海时代，技术趋势开始进行收敛，形成比较稳定的主流应用场景和框架
- Shared-Nothing(MPP): Apache Doris, ClickHouse、Presto
- Shared-Data: Snowflake
- Shared-Everything: Apache Spark
![image](https://user-images.githubusercontent.com/20035835/157274785-03c97d23-d95f-486e-abf8-ca410ca548ae.png)

## 计算存储分离 - 两个基本点的分离并各自演进
- 存储 - 数据湖及湖仓一体化
   - HDFS3.0逐渐成熟
   - 业界最牛存储层:S3
      - 超大规模，超高可用性(11个9)
      - 无限带宽，冷热分离，多层一体化存储系统
   - 公有云的对象存储 潜在的存储演化方向(Snowflake基于S3验证了其可行性)
   - 存储格式
      - 存储格式第一代，包含文件格式、压缩和编码技术以及 Index 支持等
      > 存储格式第一代，包含文件格式、压缩和编码技术以及 Index 支持等。目前主流两类的存储格式是 Apache Parquet 和 Apache ORC，分别来自 Spark 和 Hive 生态。两者均为适应大数据的列式存储格式，ORC 在压缩编码上有特长，Parquet 在半结构支持上更优。
此外另有一种内存格式 Apache Arrow，设计体系也属于 format，但主要为内存交换优化。
      - 存储格式第二代，添加ACID特性，以 Apache Hudi/Delta Lake 为代表的近实时化存储格式
      > 存储格式第二代，以 Apache Hudi/Delta Lake 为代表的近实时化存储格式。存储格式早期，是大文件列存储模式，面向吞吐率优化（而非 latency）。随实时化的趋势，上述主流的两个存储模式均向支持实时化演进，Databricks 推出了 Delta Lake，支持Apache Spark 进行近实时的数据 ACID 操作；Uber 推出了 Apache Hudi，支持近实时的数据 Upsert 能力。尽管二者在细节处理上稍有不（例如 Merge on Read or Write），但整体方式都是通过支持增量文件的方式，将数据更新的周期降低到更短（避免传统Parquet/ORC 上的针对更新的无差别 FullMerge 操作），进而实现近实时化存储。因为近实时方向，通常涉及更频繁的文件 Merge 以及细粒度元数据支持，接口也更复杂，Delta/Hudi 均不是单纯的 format、而是一套服务。存储格式再向实时更新支持方向演进，会与实时索引结合，不再单单作为文件存储格式，而是与内存结构融合形成整体方案。主流的是实时更新实现是基于 LogStructuredMergeTree（几乎所有的实时数仓）或者 LuceneIndex（Elastic Search 的格式）的方式。

- 计算 - 批流一体、OLAP分析任务SQL成为标配
  > 计算资源管理是分布式计算的核心能力，本质是解决不同种类的负载与资源最优匹配的问题
   - AI逐渐成为主流，形成 BI+AI(大数据平台除了支持传统的查询分析类BI服务，大部分算力也用来支持越来越大的AI模型计算)
   - 调度器：Yarn、K8S(仍在发展中，如KubeBatch)
   - 调度算法多元化和智能化：随各种资源的解耦（例如，存储计算分离），调度算法可以在单一维度做更深度的优化，AI优化是关键方向
   - 上云 - 充分利用云计算提供的弹性扩容特性，实现多租户隔离，Serverless化 
- 元数据服务
  - 第一代 Hive MetaStore
  - 第二代元数据系统的开源代表: Apache IceBerg
    > IceBerg 是开源大数据平台最近两年出现的独立于引擎和存储的“元数据系统”，其要解决的核心问题是大数据处理的 ACID，以及表和分区的元数据的规模化之后性能瓶颈。在实现方法上 IceBerg 的 ACID 依托了文件系统 POSIX 的语义，分区的元数据采用了文件方式存储，同时，IceBerg 的 Table Format 独立于 Hive MetaStore 的元数据接口，因此在引擎的 adoption 上成本很高，需要各个引擎改造。
  - 云厂商托管的DataCatalog服务
    > 基于未来的热点和趋势的分析，开放的，托管的统一元数据服务越来越重要，多家云厂商，都开始提供了 DataCatalog 服务，支持多引擎对湖和仓数据存储层的访问。

- 多模引擎与计算模式
  - 批处理计算 Hadoop(Hive为代表，Map-Reduce驱动) -> Spark(DAG驱动)
  - 交互式计算(查询分析类BI计算，OLAP场景，Apache Doris, ClickHouse, Presto, Snowflake)
    > 批处理和交互分析，有天然的统一需求，因此很多自研的分析引擎也包括一定的批处理能力，形成一体化，例如当前如日中天的 snowflake。而 Google BigQuery 采用附加交互引擎（内置一个更快的 BI Engine）的方式形成一体化。从细节看，交互分析的引擎优化
更偏数据库类优化方向，更强调用好 Memory 和 Index，Plan 相对简单对 QueryOptimizer要求低，不需要支持丰富的 UDF，也不需要做 Query 中间的 failover。批处理引擎更面向throughput 优化，核心是更优化的 Plan 以及尽量降低 IO，同时对 failover 要求高（因此部分数据要落盘）。这也是为什么 BigQuery 选择双引擎的原因。
  - 流式计算(实时性好)
    > 采用 Continuous Processing 的计算模式，通过本地状态保存（State）和CheckPoint（CP，用来做 failover），形成分布式增量计算引擎。这种计算模式与BSP 架构不同。主打的场景是实时大屏，监控报警以及最近流行的实时机器学习。系统面向低延迟优化，处理的是流式写入的数据，一致性模型（Exact-Once VS Atleast-Once）、LateEvent 处理方式、以及 Window 函数支持是不同流计算引擎设计的取舍。开源领域 Spark Streaming、Apex、Heron 和 Flink 经过竞争，Flink 因具备完整 Exact-Once 语义保证和完善的 LateEvent 处理能力，最终获得社区广泛的关注。
  - AI类计算 MachineLearning(ML)/DeepLearning(DL)
    - 随着AlphaGo引爆深度学习领域，TensorFlow和Pytorch成为业界标杆
    - Spark集成Pandas API用于连接大数据与AI开发，Python有取代Java成为命令式编程类（Imperitive）大数据开发语言的潜力（Decleritive 类编程标准一直是 SQL）
  - 图计算模式与文本检索(快速发展ing)
    > 图领域细分成三个子场景：图计算、图分析和图学习。分布式图分析场景目前仍未有完善的方案，图语言也在发展期，未形成统一标准。文本检索领域，主要基于倒排索引技术，开源生态Elastic Search成为主流
  - 引擎优化技术
    - 基于 LLVM 优化代码生产，支持列式处理与丰富的关系算符；基于CPP的运行时具有更高效率
    - 基于HBO、CBO、LBO的优化
    > Learned based 优化 - 机器学习技术会充分融入大数据系统（甚至任何系统）的设计，优化器、调度系统、存储格式、Index/MV 设计等多个领域均会大量使用 AI 的技术来做优化。例如 Cost based Optimization 中的基于 Statistics 的 Cost 推导，会大量被Learn based Statistics 取代

- 数据开发平台趋势
  - 低代码开发与分析
  - 智能编程(AI辅助)
  - 开发即治理
    > 过去我们大多习惯于先开发后治理，最终则让数据治理成为了负担。随着数据规模的不断增长、数据安全与隐私保护越来越受关注、数据业务化的持续发展，将不再允许数据治理仅仅是事后行为，数据治理将会融合到覆盖事前、事中和事后的大数据生产与应用的全链路中，数据开发与治理将协同并进。

- 一些观察
  - 10PB 到 EB 级数据和百万级别作业规模，已经成为主流，海量数据和作业靠人很难管理和。传统的DBA模式或数据中台团队不再胜任。
  - 多种数据融在一起，人无法在海量规模上理解数据的所有价值。
  - 大数据系统经过多年发展，如果需要实现“跃迁”式的进步，需要体系结构层面的改造。

- AI for System与自动数仓
  > 基于 AI 的能力做系统的优化，在数仓领域我们可以称之为自动数仓（Auto Data Warehouse）
![image](https://user-images.githubusercontent.com/20035835/157275066-7f283973-82da-46a2-b0c6-56a4b36f84a0.png)
  - 自动数仓分级 L1 ~ L5
     - L1: 运维能力白屏化和工具化
     - L2: 更好的系统托管化，底层系统对用户透明。例如小文件 Merge 自动化、软硬件升级透明、自动 loadbalance 等。很多全托管系统都可以做到这个层次（例如Snowflake、MaxCompute）。
     - L3 级：中台能力的自动化，辅助数据关联与理解，建模与调优。包括数据血缘，相似度，冗余度，使用情况与自动评分。辅助标签系统，辅助中台建设。市面上的很多数据中台产品聚焦在这一层。
     - L4: 系统具备自学习能力。基于历史信息的性能调优（自动 Parallelism，自动冷热数据分层等等），资源与优先级的动态调配，自适应的监控和报警能力，自动数据异常识别。目前大多数系统的能力边界在此，有巨大的发挥空间。
     - L5: 自动化建模。包含更高阶的数据理解，能够自动发现数据的内在关联与冗余度，根据数据访问情况，自动维护数仓体系。

![image](https://user-images.githubusercontent.com/20035835/157275113-1b93a545-a14a-4f2b-be72-d21258b5927c.png)

## 博客与文章
- [Snowflake官方论文: The Snowflake Elastic Data Warehouse](http://pages.cs.wisc.edu/~remzi/Classes/739/Fall2018/Papers/p215-dageville-snowflake.pdf)
- [从Snowflake看数据仓库未来演进方向：计算存储分离、弹性计算、统一存储和Serverless化](https://www.infoq.cn/article/Afr0uCxfAXsRBzLQQ24N), =>
  [PPT](https://static001.geekbang.org/con/76/pdf/1687552530/file/%E6%B2%99%E9%BE%991-%E9%99%88%E9%BE%99-1206%E4%B8%8B%E5%8D%88.pdf)
- [让数据存得起 看得见，云原生多模数据库Lindorm技术解析](http://blog.itpub.net/69972138/viewspace-2729597/)
- [Pulsar：如何打造可以无限扩展的分布式消息队列?](https://www.infoq.cn/article/IKqw6FSiDfCMQk2uqmwo)
- [Flink集成Iceberg简介](https://www.cnblogs.com/swordfall/p/14548574.html)
- [大数据架构变革进行时：为什么腾讯看好 Apache Iceberg?](https://www.infoq.cn/article/59lbBUvCrZluSmDOWJBB?utm_source=related_read_bottom&utm_medium=article)
- [融合趋势下基于 Flink Kylin Hudi 湖仓一体的大数据生态体系](https://mp.weixin.qq.com/s/gT44WTA49TdisJLZGdVHNw)

## 数据仓库 vs 数据湖 + 湖仓一体化
- [数据仓库介绍与实时数仓案例](https://www.huaweicloud.com/articles/683d6a69e1492b246363728cf823d0e5.html)

# Streaming SQL
## What has been created?
- [StreamSQL](https://docs.streamsql.io/): for machine learning
- [ksqlDB](https://ksqldb.io/overview.html): Kafka for stream processing
  - Kafka is like a file system for your events
- [Fink SQL](https://flink.apache.org/2020/07/28/flink-sql-demo-building-e2e-streaming-application.html)

## Blogs
- [Stream Processing 101: From SQL to Streaming SQL in 10 Minutes](https://wso2.com/library/articles/2018/02/stream-processing-101-from-sql-to-streaming-sql-in-ten-minutes/)
- [Streaming SQL in the Real World](https://wso2.com/library/conference/streaming-sql-in-the-real-world/)
- [Streaming Key Concepts](https://apim.docs.wso2.com/en/latest/streaming/streaming-key-concepts/)
- [Introducing KSQL: Streaming SQL for Apache Kafka](https://www.confluent.io/blog/ksql-streaming-sql-for-apache-kafka/)
- [Stream SQL 的执行原理与 Flink 的实现](https://zhuanlan.zhihu.com/p/59643962)
- [分布式数据系统小菜](https://zhuanlan.zhihu.com/io-meter)
- [Apache Flink零基础入门到进阶](https://www.infoq.cn/theme/28)
- [Flink 和 Pulsar 的批流融合](https://mp.weixin.qq.com/s/reFTJ-eqNptkSILzck94uA)

# OLAP的未来
- [The Rise and Fall of the OLAP Cube](https://www.holistics.io/blog/the-rise-and-fall-of-the-olap-cube/)
- [OLAP, what’s coming next?](https://www.sspaeti.com/blog/olap-whats-coming-next/)
- [Building a Data Engineering Project in 20 Minutes](https://www.sspaeti.com/blog/data-engineering-project-in-twenty-minutes/)

![image](https://user-images.githubusercontent.com/20035835/163666155-5b207328-8cf2-4b96-a790-792c1f322fb7.png)


# Sisence vs Tableau
- [Sisense vs. Tableau: A Scalable Business Intelligence Comparison](https://technologyadvice.com/blog/information-technology/sisense-vs-tableau-comparison/)

# Blogs
- [ClickHouse 在有赞的实践之路](https://tech.youzan.com/clickhouse-zai-you-zan-de-shi-jian-zhi-lu/)
- [Picking A Kubernetes Orchestrator: Airflow, Argo, and Prefect](https://medium.com/arthur-engineering/picking-a-kubernetes-orchestrator-airflow-argo-and-prefect-83539ecc69b)
- [Building a Real-time Data Vault in Snowflake](https://datavaultalliance.com/news/building-a-real-time-data-vault-in-snowflake/)
- [Streams and Tables in Apache Kafka: A Primer](https://www.confluent.io/blog/kafka-streams-tables-part-1-event-streaming/)
- [Streaming Pipeline in Snowflake](https://infinitelambda.com/post/streaming-pipeline-in-snowflake/)
- [耗时 18 个月，我们构建了一个真正可扩展的无服务器 SQL 数据库](https://www.infoq.cn/article/4cCk2dbTFXP3k6pNvNhe)
- [Flink 执行引擎：流批一体的融合之路](https://developer.aliyun.com/article/783112)


# Data Engineer & Data Engineering
- [The Rise of the Data Engineer](https://medium.com/free-code-camp/the-rise-of-the-data-engineer-91be18f1e603)
- [The Future of the Data Engineer](https://towardsdatascience.com/the-future-of-the-data-engineer-4dcfa53800ab)
- [The Future of Data Engineering](https://www.infoq.com/articles/future-data-engineering-riccomini/)

# Stream Storage
- [Pravega, the Answer of Storage Layer in Flink Ecosystem](https://www.alibabacloud.com/blog/pravega-the-answer-of-storage-layer-in-flink-ecosystem_596430)
- [如何将索引大小减少 99.5%？解读流式存储 Pravega 的段属性](https://www.infoq.cn/article/mcaVdWZHrxufuYPrjxGu)
- [专为流式数据设计的另一种缓存：流式缓存技术解读](https://www.infoq.cn/article/xVmAffiuL0kmO1wXaJBH?utm_source=related_read_bottom&utm_medium=article)

# Modern Data Stack
- [Building a Scalable Analytics Architecture with Airflow and dbt](https://www.astronomer.io/blog/airflow-dbt-1)
- [Great Expectations is a shared, open standard for data quality](https://greatexpectations.io/)

**A brief introduction of the Modern Data Stack(MDS)**

> The modern data stack is a collection of cloud-native tools that are centered around a cloud data warehouse and together comprise a data platform. The benefits of adopting a modern data stack are many: 
> - Ease of Use: SaaS technologies allow your team to not worry about installing and maintaining technology. Everything is built for the data warehouse so this minimizes integration pains and siloed data platforms that require lots of effort spent shifting data around. 
> - Wide Adoption: The modern data stack is constructed with the intention of upskilling data workers and removing the barriers between workflows; anyone can be a data engineer, data analyst, or machine learning engineer with the right tooling. SQL is the lingua franca that creates a common foundation to work with data across disciplines. A common theme we’ve noticed among modern data stack adopters is that people no longer focus on just one discipline and are now hybrid “data engineer/data analyst/data scientist”. 
> - Automation: Tools that don’t focus on automation place a huge technology burden on users when it comes time to operationalize data workflows. We often refer to these strewn together systems as “pipeline jungles”, where, over time, it can become almost impossible to detangle the complex web of logic. Automation needs to be a core feature of data tools.  
> - Cost: Say goodbye to predatory vendors with high entry fees. In the cloud, you pay for what you use, and nothing more. A side effect of tools having wide adoption and a focus on automation means your data workers can get more done, in less time, with fewer resources. This has benefits in terms of the cost to staff up a data team as well.

From The Modern Data Stack Ecosystem - Fall 2021 Edition

**Blogs**
- The Beginner’s Guide to the Modern Data Stack
- The Modern Data Stack: Past, Present, and Future(from Tristan Handy, the creator of dbt)
- Future Data 2020 - Tristan Handy - The Modern Data Stack: Past, Present, and Future (Youtube Video Version)
- The Modern Data Stack (updated for 2021)
- The Modern Data Stack Ecosystem - Fall 2021 Edition

**Available  Toolsets**
- Rivery:  all-in-one solution for Ingestion, Transformation, Orchestration, Reverse ETL, and Data Operations
- Fivetran( begin with 2013): The 5 Billion Dollar Data Transport Company You’ve Never Heard Of 
- airbyte: open source data ingestion tool
- dbt: open source data transformation tool
- datahub: open source metadata & data catalog tool
- Databricks: All in one data processing & management platform developed the company behind Spark
- Snowflake: Cloud data warehouse & data management platform

**Personal Thinkings**
- The trend is clear: the world is moving from ETL to ELT
- All these platforms(dbt, Fivetran, Rivery, Snowflake, Databricks) try to become a unified data management & data ops platform based on modern data stack trends but from different ways
   - Some begins from data loader, such as Fivetran, Rivery
   - Some begins transformation, such as dbt
   - Some begins with computing engines, such as Snowflake, Databricks
       - Databricks introduced a built-in feature name Delta Live Tables, which is very similar dbt
       - Databricks introduced a built-in Auto Loader feature, which seems similar to airbyte
       - Seems Databricks try to build a unified data management & ops platform - all the things load, transformation, data lineage, data governance, data share can be done in one place.
       - Snowflake already has features like Pipeline + Task help developer easily do the transformation
- UI is the one of the most import things - data engineers liberate themselves by deliver data dev & ops tools which can be easily used by end-users 
- Our BDP platform & Auto Pipeline framework is somehow following the trends of industry but needs to spend more time to improve the documentation & dev-efficiency
- Orchestration seems still a hard part: all these platforms somehow need to integrate with schedulers whether built-in or other open-source projects such as Airflow, Argo, Prefect

[The key building blocks of a modern data platform](https://towardsdatascience.com/the-building-blocks-of-a-modern-data-platform-92e46061165)

![image](https://user-images.githubusercontent.com/20035835/157275329-f4eadd2b-e26b-4f17-a3b2-c9f0d759715c.png)

[Modern Data Stack Tools](https://untitledfirm.com/modern-data-stack-tools/)
![image](https://user-images.githubusercontent.com/20035835/157275362-b2cbe693-1c28-4712-975b-0e39fbbb7d7d.png)

[Emerging Architectures for Modern Data Infrastructure](https://future.a16z.com/emerging-architectures-modern-data-infrastructure/)
![image](https://user-images.githubusercontent.com/20035835/160046764-805c8830-c464-489a-9986-54472861662f.png)


# Data Mesh
- [Data Mesh From an Engineering Perspective](https://www.datamesh-architecture.com/)
