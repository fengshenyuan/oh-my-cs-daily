# Data & Data Engineering
* Data Grabbing
* Data 清洗
* Data 转储
* Database
  * Data Model
  * Data Query Language
  * Data Manipulation Language
  * Data Definition Language
  * Data Transaction Language 
  * Data Control Language
* Data Mining
* Data Visualization

"世界是普遍关联的"的客观反映在于数据是普遍关联的。绝没有一份数据是独立产生的。一份数据必然产生于另一份数据。一份数据必然描述或者记述了另一份数据。

抽象的本质是递归？
逻辑的本质也是递归？

没有递归，一个概念就不可能深层嵌套。

## Storage Type

- Object Storage(AWS S3)
- Block Storage(Disk/Data Volume)
- File Storage(File System > Combine many raw block storages as a pure system, such as Windows File System)

# Data Model & Data Structure

## Data Models
- Relational Model
- Graph Model
- Document Model
- Multidimensional Model

From the historical development review and the data modeling and management perspective, the relational model is the most general and productive model for programmers. Other models, such as the hierarchical model, networks model, ER-model, object model, graph model, k-v model, document model all can be viewed as a certain extension or equal things of the relational model. The core difference between the relational model and k-v model, object-model, graph model, document model is the normalization depth. And based on the core difference, each model builds different theory to store and manage the relations between the data sets they managed and expose different usability and productivity for the end-users.

(Can be wrong)
- Object Model = Relation Model + ORM Frameworks
- K-V Model = Relation Model + Relations Coded in programmings
- Wider Column Model = Relation Model + JSON Column
- Document Model = No Normarlization Relation Model

From wikipedia
> A data model (or datamodel[1][2][3][4][5]) is an abstract model that organizes elements of data and standardizes how they relate to one another and to the properties of real-world entities. For instance, a data model may specify that the data element representing a car be composed of a number of other elements which, in turn, represent the color and size of the car and define its owner.


# Data Language

## Data Query Language

- SQL(Structure data query language, MySQL)
- AQL(Multidimensional data query language, AA Microservice AQL Architecture)
- DQL(Document-oriented, semi-structured data query language => ES, MongoDB)
- LINQ(This is very awesome things. Worth to learn it! => Spreadsheet, Array, Iterator, simple tables, common data structures in general programming language)
- SQLAlchemy(ORM = Object + Relational Model, combine the SQL and Python together, perfect things.)
- Cypher(Graph data query language, Neo4j)


# The Management of Data
## Database Theory
> Database theory encapsulates a broad range of topics related to the study and research of the theoretical realm of databases and database management systems.

> Theoretical aspects of data management include, among other areas, the foundations of query languages, computational complexity and expressive power of queries, finite model theory, database design theory, dependency theory, foundations of concurrency control and database recovery, deductive databases, temporal and spatial databases, real time databases, managing uncertain data and probabilistic databases, and Web data.

> Most research work has traditionally been based on the relational model, since this model is usually considered the simplest and most foundational model of interest. Corresponding results for other data models, such as object-oriented or semi-structured models, or, more recently, graph data models and XML, are often derivable from those for the relational model.[1]

> A central focus of database theory is on understanding the complexity and power of query languages and their connection to logic. Starting from relational algebra and first-order logic (which are equivalent by Codd's theorem) and the insight that important queries such as graph reachability are not expressible in this language, more powerful language based on logic programming and fixpoint logic such as datalog were studied. Another focus was on the foundations of query optimization and data integration. Here most work studied conjunctive queries, which admit query optimization even under constraints using the chase algorithm.

The main research conferences in the area are the ACM Symposium on Principles of Database Systems (PODS) and the International Conference on Database Theory (ICDT).

## Data Warehouses
> where the speed of data retrieval is more important than the efficiency of data manipulations. As such, the tables in these schemas are not normalized much and are frequently designed at a level of normalization short of third normal form.

From: Wikipedia

> A data warehouse is an organized collection of large amounts of structured data. It is a database designed and intended to support decision making in organizations. It is usually batch updated and structured for rapid online queries and managerial summaries of its contents. According to Bill Inmon (1993), who is often called the "father" of data warehousing, "a data warehouse is a subject-oriented, integrated, time-variant, nonvolatile collection of data". Ralph Kimball (1996), another data warehousing pioneer, notes, "A data warehouse is a copy of transaction data specifically structured for query and analysis." So, the data warehouse or the single subject data mart stores data for a data-driven DSS. 

Reference: [Data Warehouses, Schemas and Decision Support Basics](http://www.b-eye-network.com/view/8451)




## Data normalization and storage
> Normalization splits up data to avoid redundancy (duplication) by moving commonly repeating groups of data into new tables. Normalization therefore tends to increase the number of tables that need to be joined in order to perform a given query, but reduces the space required to hold the data and the number of places where it needs to be updated if the data changes.

## Comments

不是只有MySQL, Oracle, Elasticsearch, MongoDB这样大型的数据库才叫数据库。数据库本质是一套对特定范围的数据进行收集，处理，格式化校验，建模，入库，支持查询，删除，更新，修改的数据管理系统。本质上这是所有程序的通用逻辑。所有的程序都是在某种程度上处理数据而已。所以，在各种地方都能使用到构建数据库的所使用的技术、概念和经验。像DOM， Redis, iTerms2 search history, git，AA AQL, XML都可以视为数据库系统。


# Multidimensional Data Theory

## Data Models
- [Snowflake Model(雪花模型)](https://en.wikipedia.org/wiki/Snowflake_schema)
- Star Model
> In computing, a snowflake schema is a logical arrangement of tables in a multidimensional database such that the entity-relationship diagram resembles a snowflake shape. The snowflake schema is represented by centralized fact tables which are connected to multiple dimensions.[citation needed]. "Snowflaking" is a method of normalizing the dimension tables in a star schema. When it is completely normalized along all the dimension tables, the resultant structure resembles a snowflake with the fact table in the middle. The principle behind snowflaking is normalization of the dimension tables by removing low cardinality attributes and forming separate tables.[1]

> The snowflake schema is similar to the star schema. However, in the snowflake schema, dimensions are normalized into multiple related tables, whereas the star schema's dimensions are denormalized with each dimension represented by a single table. A complex snowflake shape emerges when the dimensions of a snowflake schema are elaborate, having multiple levels of relationships, and the child tables have multiple parent tables ("forks in the road").

# [Graph Database Theory](https://en.wikipedia.org/wiki/Graph_database)

## Cypher Query Language
> Cypher is a declarative graph query language that allows for expressive and efficient querying and updating of a property graph.

# [OLAP](https://en.wikipedia.org/wiki/Online_analytical_processing)

Implementation Pattern of OLAP
- MOLAP: Multidimensional OLAP, based on multidimensional data cube structure
- ROLAP: Relational OLAP, based on general relational database.
- MS-OLAP: Based on Mircoservice implementation to provide OLAP functionalities.
- HTAP: Hybrid transactional/analytical processing (HTAP)


# Real World Data Engineering

## Data Architecture

From wikipedia
> Data architecture is the design of data for use in defining the target state and the subsequent planning needed to hit the target state. It is usually one of several architecture domains that form the pillars of an enterprise architecture or solution architecture.

> A data architecture describes the data structures used by a business and/or its applications. There are descriptions of data in storage and data in motion; descriptions of data stores, data groups and data items; and mappings of those data artifacts to data qualities, applications, locations etc.

> Essential to realizing the target state, Data architecture describes how data is processed, stored, and utilized in a given system. It provides criteria for data processing operations that make it possible to design data flows and also control the flow of data in the system.

## Data Modeling

> Data modeling in software engineering is the process of creating a data model by applying formal data model descriptions using data modeling techniques. Data modeling is a technique for defining business requirements for a database. It is sometimes called database modeling because a data model is eventually implemented in a database.[19]

> The figure illustrates the way data models are developed and used today. A conceptual data model is developed based on the data requirements for the application that is being developed, perhaps in the context of an activity model. The data model will normally consist of entity types, attributes, relationships, integrity rules, and the definitions of those objects. This is then used as the start point for interface or database design.

## Data Organization(如何组织数据)

> Another kind of data model describes how to organize data using a database management system or other data management technology. It describes, for example, relational tables and columns or object-oriented classes and attributes. Such a data model is sometimes referred to as the physical data model, but in the original ANSI three schema architecture, it is called "logical". In that architecture, the physical model describes the storage media (cylinders, tracks, and tablespaces). Ideally, this model is derived from the more conceptual data model described above. It may differ, however, to account for constraints like processing capacity and usage patterns.

> While data analysis is a common term for data modeling, the activity actually has more in common with the ideas and methods of synthesis (inferring general concepts from particular instances) than it does with analysis (identifying component concepts from more general ones). {Presumably we call ourselves systems analysts because no one can say systems synthesists.} Data modeling strives to bring the data structures of interest together into a cohesive, inseparable, whole by eliminating unnecessary data redundancies and by relating data structures with relationships.

> A different approach is to use adaptive systems such as artificial neural networks that can autonomously create implicit models of data.

## The Properties of a Fine Dataset

Some important properties of data for which requirements need to be met are

**definition-related properties**
 - relevance: the usefulness of the data in the context of your business.
 - clarity: the availability of a clear and shared definition for the data.
 - consistency: the compatibility of the same type of data from different sources.

**content-related properties**
 - timeliness: the availability of data at the time required and how up to date that data is.
 - accuracy: how close to the truth the data is.

**properties related to both definition and content**
 - completeness: how much of the required data is available.
 - accessibility: where, how, and to whom the data is available or not available (e.g. security).
 - cost: the cost incurred in obtaining the data, and making it available for use

![Some important properties of data](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/3-2_Properties_of_data.svg/640px-3-2_Properties_of_data.svg.png)


## Tools & Methodologies

### Data Flow Diagram

> A data-flow diagram (DFD) is a graphical representation of the "flow" of data through an information system. It differs from the flowchart as it shows the data flow instead of the control flow of the program. A data-flow diagram can also be used for the visualization of data processing (structured design). 

![image](https://user-images.githubusercontent.com/20035835/157264066-41b896bc-dd3c-47f3-be77-209c222ef9c3.png)


### Data Architecture Practice
Certain elements must be defined during the design phase of the data architecture schema. For example, administrative structure that will be established in order to manage the data resources must be described. Also, the methodologies that will be employed to store the data must be defined. In addition, a description of the database technology to be employed must be generated, as well as a description of the processes that will manipulate the data. It is also important to design interfaces to the data by other systems, as well as a design for the infrastructure that will support common data operations (i.e. emergency procedures, data imports, data backups, external transfers of data).

Without the guidance of a properly implemented data architecture design, common data operations might be implemented in different ways, rendering it difficult to understand and control the flow of data within such systems. This sort of fragmentation is highly undesirable due to the potential increased cost, and the data disconnects involved. These sorts of difficulties may be encountered with rapidly growing enterprises and also enterprises that service different lines of business (e.g. insurance products).

Properly executed, the data architecture phase of information system planning forces an organization to precisely specify and describe both internal and external information flows. These are patterns that the organization may not have previously taken the time to conceptualize. It is therefore possible at this stage to identify costly information shortfalls, disconnects between departments, and disconnects between organizational systems that may not have been evident before the data architecture analysis.[4]

## Data Manipulation Pattern

This most important pattern of data manipulation is making the data source iterable. 
Once the data source is iterable, we can process the data like a stream and apply all the standard SQL operation to the data elements. It's the most basic but powerful pattern for data retrieving and transforming.

When some data is not in the iterable pattern(like multidimensional data set), just write an iterable interface transform for this data source.

This pattern can be called data stream, table operation language, and other things. The core of the conception is iterate and transform the data element one by one, from one iterable data source to another iterable data source.

Like the zip, map, filter, stop, head, tail...

# What's the goal of the database system?
> One of the goals of the database system is to represent history correctly.

> So to make this possible, it would require we rethink how the SQL language should be - i.e, how to represent the abstract conception - history and how to query with the history.

## Is that possible to for any information system to get a quick and accurate answer from a very long historical period with a super large amount of facts and details? 
> 问：想要从一段非常的复杂、包含了各种各样事件和关系的历史时期中快速获得一个正确且准确的回答是可能的么？这其中肯定有什么不可能三角或悖论。从常识来说，如果一个数据仓库准确反映了所有的历史事实和变化细节，其内部数据关系和数据组织方法将无可避免的变得如同历史自身一样复杂，而想要从相当长的一段历史时期中还原或推演某个事件的发生过程，得出其中的正确且准确的统计结果或因果事实，有些痴人说梦。历史学家的苦心孤诣早已证明在面对浩如烟海的历史文献面前，想要理清或挖掘出有意义的事实，要么直接不可能，要么就要耗费大量人力物力。历史信息自身的组织结构决定了该系统回答一个外部问题时的最短路径或最小信息量。在此种情况下，要么改变我们提问的方式(即问正确的问题)，或者去改变信息自身的组织方式使之方便回答我们的问题。

## Data Governance & DataOps

数据架构是实现数据治理的必要手段！

### 数据中台
[数据中台VS数据仓库，究竟谁优谁劣](https://zhuanlan.zhihu.com/p/80317504)

数据中台与技术中台是类似的概念，所有的数据使用将在数据中台统一赋能！

> 数据中台通常会对来自多方面的的基础数据进行清洗，按照主题域概念建立多个以事物为主的主题域。比如用户主题域，商品主题域，渠道主题域，门店主题域等等。

> 数据中台遵循三个One的概念：One Data, One ID, One Service，就是说数据中台不仅仅是汇聚企业各种数据，而且让这些数据遵循相同的标准和口径，对事物的标识能统一或者相互关联，并且提供统一的数据服务接口。就像做菜一样，按照标准化的菜名，先把所有可能用到的材料都准备好。

> 而传统的数仓主要用来做BI的报表，目的性很单一，只抽取和清洗相关需要使用到的基础数据，进行建仓，然后再用来做领域分析，有的时候可能因为新增一张报表，就要从底层到上层再做一次加工和处理。

[想要读懂大数据，你得先了解这些技术](https://zhuanlan.zhihu.com/p/77038376)

### 企业级实例

[美团酒旅起源数据治理平台的建设与实践](https://tech.meituan.com/2018/12/27/onedata-origin.html)

### IT三大技术类别(数据、计算和语言| Data, Computing, and Languages)

- 分布式计算基础设施构建类技术(Computing)
- 数据治理相关技术(Data Governance)
- 业务表达相关技术(Language/Framework/DevOps toolkit/...)
