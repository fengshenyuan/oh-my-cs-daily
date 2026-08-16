# Snowflake
Snowflake是一个计算引擎与存储引擎分开scale的架构：
 - 凡属于静态数据分片、存储、索引功能的都属于存储引擎范畴
 - 凡属于动态fetch、计算、转移功能的都属于计算引擎范畴

## Snowflake 10问
- How to use Snowflake with the best ROI?
> Materialized view is auto-updated. But if we use materialized views so much for performance concerns, I doubt that the backstage updating progress will cost much than we expected if there are so many materialized views waiting for updating.

> My understanding that the materialized view is something that can be called partial-replication, which only replication the target data from the MV definitions. But as we know, we need a balance on the number of replications in a distributed env.

> Reference: https://docs.snowflake.com/en/user-guide/views-materialized.html#general-usage-notes

- Materialized View supports clustering. What does this mean?
> ???

- Is share views to customers a good idea?
   - security concerns
   - performance concerns
   - maintenance concerns
   - product concerns:
     - what kind of views are used to share with customers?
     - how many views will be created to satisfy our customers?
     - how to create & maintain these views?
     - what are the [limitations](https://docs.snowflake.com/en/user-guide/views-materialized.html#limitations-on-creating-materialized-views) of these views? Will these limitations become a blocker of product SRD?
     - what if we need to update a shared view definition?(customers may build apps relay on the views.)

- How to understanding the materialized views?
> Basically, it's a storage engine feature. So almost everything involves the computing engine with the 
 MV definition SQL will not be supported or certainly have some limitations.

> First impression, avoid MR as possible as we can! It's an unknown-box and cost lots of resources.

> It's a very weak guarantee in distributed computing env and this is not product env ready feature for real big data progressing company like AppAnnie.(限制太多；没有快速一致性更新方案-cost还可能非常高；不易维护 - 关联的dependency太多；对于开发人员缺乏可见性)

- The transaction of Snowflake?
> READ COMMITTED is the only isolation level currently supported for tables! It means SF can not even guarantee repeatable read!

- How the Snowflake can be used to support the data restatement projects like Diamond?
> TBD

- The [Task](https://docs.snowflake.com/en/user-guide/tasks-intro.html#task-scheduling) feature of Snowflake?
   - Need to consider cross regions & platform sharing issues(will trigger replications)
   - Need to consider development management(sharing management requires a admin role)
   - Databases created from shares cannot be replicated.
   - What's the replication sync up strategy?
> There is no event source that can trigger a task; instead, a task runs on a schedule, which can be defined when creating a task (using CREATE TASK) or later (using ALTER TASK).

- How does the Snowflake support the ASL?

## Snowflake Performance Tuning
- How the Snowflake SQL Engine works? It seems the internal mechanism is very different from the traditional, index-based DB system.
> TBD

- How to use view in Snowflake?
> If to materialize a view is a small cost, why not put it into the ETL/Data pipeline? If computing a view on the fly is slow and a large cost, why still use view and compute the view every time when used? 

> Maybe a view query would be parsed into the underlying table query and only fetch the required underlying data partitions and then only compute with a small dataset in memory.

- [Data Warehouse Architecture, Concepts and Components](https://www.guru99.com/data-warehouse-architecture.html)
- [Four Stages that Revolutionized Database Architecture](https://dzone.com/articles/understand-the-incredible-database-revolution-unde)
- [UNDERSTANDING MICRO-PARTITIONS AND DATA CLUSTERING](https://community.snowflake.com/s/article/understanding-micro-partitions-and-data-clustering)
- 为什么用combined keys，而不是multi-columns clustering?
- What's the problem with Automatic Clustering? Why disabled it?
- 
