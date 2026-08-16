# MicroOLAP - Thinking on AQL
- First, revisit the architecture of AQL, its design goal, and the problems of the current implementation.
- Second, improvements to the current implementation & the right way to do things correctly
- Third, new solutions with open source technology.

## Reading Summary of [How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh](https://martinfowler.com/articles/data-monolith-to-mesh.html) 
I have read the How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh article one year ago. Glad to see experts from the industry try to summary the thinkings & trends to a theory. 
- The name Data Mesh actually is very interesting. It is obvious that it borrows some idea from the Micro-service and Kubernetes. My understanding is that this new conception or paradigm tries to decentralize the traditional data warehouse & data lake into the so called Distributed Domain Driven Architecture. 
- A simple version of this is do what micro-service movement has done with a monolithic application in data side. 
- If you treat the traditional data warehouse & data lake just as the monolithic application and each table in the data warehouse & data lake as a migrated micro-service, you may find something very interesting. That means in a higher abstract level application & data actually can be managed in the same pattern. 
- And one thing I think ABC have done ahead of the industry is we already put the data mesh ideas into practice - the AQL.  Just as in micro-service world, after you split the application into lots of micro-services in dev side, you need an API Gateway to gather all the things back to provide a unified end-user experience of your original monolithic application. This is also true in data mesh - so we need Data Gateway. 
- AQL can be viewed as a kind of Data Gateway but actually is higher level ‘Gateway’ than a traditional ‘Gateway’ - because it is a language - more flexible, easier to extend, easier to learn and maintenance.
- So comes back the data mesh paradigm, the great series released in Martin Fowler’s website actually no more than theories but the whole industry lacks of practice and prototypes.  
- From my perspective, AQL hasn’t reach all the goals mentioned in the articles but it does follow the principles and patterns and actually works very well in our cases. If you have more interesting in this topic, you can read one of notes on AQL wrote last year. It gives more details of my thinking of the AQL and the Data Mesh pattern.

# Chapter 1: The Original of AQL
AQL is a query language used in ABC. Just as other query languages, there is a data structure called ADM designed to work with AQL to form the complete scope of AQL based DB or OLAP functionalities.

## 1.1 ADM - ABC Data Model
The AQL & ADM OLAP system is based on the [multidimensional data model](https://docs.oracle.com/cd/B13789_01/olap.101/b10333/multimodel.htm) theory. Usually, the MOLAP is a way to implement the Data Warehouse, besides other solutions like the ROLAP system.

### Structure of ADM
In the data model of a multidimensional data set or the data cube, we basically need to give two kinds of info to describe the cube. That's the metrics and dimensions.

**Metrics** are the facts that represent the quantity of real-world business.

**Dimensions** are the primary keys of the facts which represent how these quantities are determined.

Additionally, we can add aggregations info for each data model to indicate what kind of aggregations are supported for the given data sets. But from the perspective of generally data engineering or data warehouse, that seems not a good idea since how to explore and use the data actually should be made by the end-user. A nice and general target of a data model should only care about things in the `storage` level. Things like **aggregations** should be considered at the computing level. With this responsibility architecture, we can keep each part of the system pure and simple and build super complex but also super powerful toolsets with these basic wheels.

## 1.2 AQL - The ABC Query Language
The AQL actually is language expose to end-users of the ABC OLAP system. With AQL and ADM, clients could express the data sets they want to and interact with the system.

Like the ADM, the AQL is also based on multidimensional data model theory. Generally speaking, each result of an AQL is multidimensional data sets or a data cube. AQL is a description language like SQL. You just need to describe what the data cube looks like. The system will give the right response to you.

# Chapter 2: AQL v1(The Original Impl)
The online impl of AQL which is called AQL v1 is based on microservice architecture.

![Architecuture of AQL v1](https://user-images.githubusercontent.com/20035835/157422060-1faf2c84-c804-47a6-ac59-1a2988928606.png)


## 2.1 Overview of The Original Impl
As the overview architecture shows, the real data is stored in different databases. In the above layer the storage level, there are microservices which is implemented to fetch data from the underlying database. Generally speaking, all the data belongs to one business domain will be governed by one microservice.

### 2.1.1 Meta Info Management
And there are meta info management services that implement the permission and user authentication control of the system. Also, all the data model info is governed by the Data Model Service, where you can find all the available data models in the system and which service is responsible for low-level data fetch for the corresponding data model.  

### 2.1.2 BAPI - The Computing Engine
Maybe you are curious what's the BAPI? Why is it here?

As the diagram shows, the BAPI is the computing engine of the AQL. From a high-level perspective, all the data models in the system form a large data set net. AQL allows you to query data from different domains in one query if they can be expressed in the same query descriptions. Besides this, when clients want to get metrics with dimensional entities info like product details, publisher details, company details, etc. There should be one engine to fetch them from different dimensional data model governance services and merge them together as a full & correct response to clients.

### 2.1.3 Essential of AQL v1
In AQL v1's architecture, you can think 
- Each service as a [schema namespace](https://dataedo.com/kb/data-glossary/what-is-database-schema#:~:text=3.-,Namespace%20(element%20of%20SQL),can%20duplicate%20across%20different%20schemas.) of the SQL world. That's to say each service serves as the namespace to hold one or more data models(tables, views in the world of SQL).
- The BAPI is just an engine like InnoDB in MySQL. All the things like parse the input AQL, generate the execution plan, join cube from different services, apply the grouping and aggregations should happen in the layer.

Summary in one sentence is that AQL is just an implementation of query language under microserver architecture. Nothing really changes from the familiar SQL world.

In traditional SQL implementation, all functionalities are ususally implemented in one codebase and functionality like language parser, executor, data scanner is implemented as a library or a model. In AQL, we just replace these pieces of implementations with one or more microservices.

### 2.1.3 Benefits of Microservice Arch
With the Microservice Impl Pattern used by AQL, we can leverage the benefits from microservice as possible as we can such as
- **Storage Free** 
  > the low-level data can be stored in any available storage format and engine like CSV, txt, MySQL/PostgreSQL, ElasticSearch, S3, etc. Familiar? Yes. The core idea is very close to what we called **Data Lake**!
- **Upgrade online** 
 > With a traditional DB, usually you need to stop or do a backup switch-over to upgrade the DB engines - which means there is business unavailable time. In microservice arch, it's so common we replace or upgrade online services or functionalities with technologies to traffic channels, traffic redirections, A/B tests.
- **Scale Free** 
  > Microservice can be easily scaled out or scaled up with features provided by the cloud platform like **AWS ECS, EKS, or K8S**. 
- **Resource Isolation** 
 > With the microservice arch, you can add resources to accelerate the application if works. You don't need to worry about the increased resource for one model is actually occupied by another model in a traditional DB like PG.
- **Tech Stack Free**  
  > Each microservice actually could choose a different tech stack to do the implementation. The only thing each microservice should obey is to impl the protocol between the AQL Computing Engine and itself - that's what called simple AQL in the current design. If python is too slow, replace it with go, rust, c/c++, and no one would blame you. If the PL/Proxy is too complex, replace it with Citus, Snowflake, S3, and the upper level wouldn't blame you.

### 2.1.4 Cons of Microservice Arch
The complexity comes from the data itself won't disappear automatically. They only transfer to other places corresponding with your system architecture.

The Microservice Impl Pattern has lots of benefits. That's true. But the cons are also obvious.
- **Need Query Translator**
  > To fetch the raw data from low-level storage, the system needs to translate the query from AQL into something the low-level storage engine could understand. For example, for PG or other relational DB, we need an AQL-SQL translator and for ES, we need an AQL-ESQL translator, etc. Sometimes, you even need to translate the AQL into S3 APIs. To fully match the low-level storage engine languages or APIs requires careful design and very strong engineering skills & management. Sometimes, the translator could be very complex to match the high-level AQL's requirements.

- **Need Protocol Between ACE(AQL Computing Engine) and MS**
  > The lightest solution is the clients, ACE and MS receiver use one same language.

- **ACE Hot Points**
  > Usually, the OLAP system queries lots of data to do the meet the analysis requirements from clients. That means the ACE part will receive lots of data sets from each involved MS. And to get the final results, the ACE needs to apply operations such as join, group, filter, aggregation which will generate lots of temporary middle results. This may cost a huge amount of CPU, memory, and I/O. That's to say the ACE layer usually becomes the bottleneck and cost lots of resources.

- **Performance**
  > To translate the data from the low-level storage engine to final clients, there are too many network layers like PG -> MS -> ACE -> API Gateway -> Clients. In each layer, serialization and anti-serialization could really be a waste and performance slow point. And the data translation in-network adds more delay of the final performance. **But since we are in an OLAP world, this hasn't become a serious issue yet.** 

## 2.2 ABC's Impl - AQL
ABC actually follows our discussion about the MircoOLAP to build an OLAP system to serve the business. At least, it pretends to be the standard MicroOLAP system at the very beginning. But it almost failed in reality. We are going to discuss the difference between ABC's impl & standard impl principles.

### 2.2.1 Overview
ABC has been working on the implementation of AQL for several years with more than 50 full-time developers. But actually, it is a mess. Engineers are not working on the framework but stuffing business logic into the system with a wrong impl pattern.

What ABC gets are
- 40+ microservice 
  > each of them corresponded with data sets of one or two domains.
- Redundant and duplicated fill-up logic in 40+ microservice.
- Several general-purpose libraries for MS build responses, AQL syntax checking, and call each other.
- High effort to upgrade the DM 
- Limited abilities to query the data  
... 


### 2.2.2 The Problems

### 2.2.2.1 AQL Doesn't Wrap the Low-level Storage Engines by Design
Following the original MicroOLAP Principle, the microservice layer should
- expose the basic functionalities of the low-level storage engine loyally 
  > loyally means does not add anything and does not hide anything - only to be a good translator
- reject the query that includes data models that the service doesn't know
- join, group, aggregation should happen in the ACE layer not in microservice

The real AQL used in ABC is a pure multidimensional data query language - the available filters, aggregations, breakdowns are defined by the ADM. The limitations are
- Usually, you can query metrics with dimensions as filters and you can never naturally get dimensions by metric filters. Say find the products whose est_download_rank of yesterday is higher than 10K! It's very simple in SQL. But in the current AQL design, you can never do it.
- Another example, since the filter operation supported are only `in` and `equal` for most dimensions, you can never express the `!=` logic easily! Sometimes, it's not possible because of the size of data sets! But the underlying storage engine, like PG, ES has supported this already.

The most important reason why I think ABC's implementation is a failure following the truth that lots of computing are implemented in the Microservice layer. That makes the microservice never pure - translate the AQL and fetch the raw data from the low-level storage engine. These include
- Fill up progress happens in the microservice layer!
 > This means a very strange phenomenon - almost all the ms implement a fill-up logic!

- cascading filter like `product_id.has_iap` is implemented microservice!
  > This could be general filter implementation in the ACE. To do this, the microservice needs to know other data models and fetch data into its env then apply the filter.

### 2.2.2.2 Fill NA Issue
One problem that should be motioned first is the FE Render Framework - the data visualization layer of our Web UI.
![Copy_of_Review_of_AQL_s_Impl_Architecture_Bak__1_](https://user-images.githubusercontent.com/20035835/157422318-85d4f607-7222-40c6-8090-5754267d8d90.png)


To build a general render layer for customers, a very special requirement emerged from FE - the response data should be filled up even if there is actually no valid data in low-level DB. That's we called Fill NA process.
For example, in the query to the system
```python
query = {
    'facets': [
        {'name': 'store_product_rank_free', 'aggregations': ['aggr']},
        {'name': 'store_product_rank_grossing', 'aggregations': ['aggr']}
    ],
    'filters': {
        'product_id': {
            'equal': 1016323413
            },
        'category_id': {
            'in': [100000, 100022]
            },
        'country_code': {
            'in': ['US', 'CN']
            },
        'device_code': {
            'equal': 'ios-phone'
            },
        'date': {
            'between': ['2019-04-26', '2019-04-27']
            },
        'granularity': {
            'equal': 'daily'
            }
        },
    'order_by': [
        {
            'name': 'date', 
            'order': 'desc'
        }
    ]
}

response = [
    {'category_id': 100000, 'country_code': 'US', 'date': datetime.date(2019, 4, 26),
    'store_product_rank_free': None, 'store_product_rank_grossing': None},
    {'category_id': 100000, 'country_code': 'US', 'date': datetime.date(2019, 4, 27),
        'store_product_rank_free': None, 'store_product_rank_grossing': None},
    {'category_id': 100000, 'country_code': 'CN', 'date': datetime.date(2019, 4, 26),
        'store_product_rank_free': None, 'store_product_rank_grossing': None},
    {'category_id': 100000, 'country_code': 'CN', 'date': datetime.date(2019, 4, 27),
        'store_product_rank_free': None, 'store_product_rank_grossing': None},
    {'category_id': 100022, 'country_code': 'US', 'date': datetime.date(2019, 4, 26),
        'store_product_rank_free': None, 'store_product_rank_grossing': None},
    {'category_id': 100022, 'country_code': 'US', 'date': datetime.date(2019, 4, 27),
        'store_product_rank_free': None, 'store_product_rank_grossing': None},
    {'category_id': 100022, 'country_code': 'CN', 'date': datetime.date(2019, 4, 26),
        'store_product_rank_free': None, 'store_product_rank_grossing': None},
    {'category_id': 100022, 'country_code': 'CN', 'date': datetime.date(2019, 4, 27),
        'store_product_rank_free': None, 'store_product_rank_grossing': None}
]
```
Although there are no records that meet the condition, you still need to return 8 filled-up records as a response.

The reason why we need to do the fill-up is that from FE render's perspective, there should be 8 data points displayed in the chart. If the backend doesn't return them, then FE must generate them by itself! 

Sounds reasonable & acceptable, right?

Yes. It's reasonable and acceptable. 
- Usually, FE has fewer computing resources to fill up missed data in a browser.
- To fill up the missed data need lots of meta info, especially when the query doesn't give `country_code` in the filters but requires the results breakdown by `country_code`. That means we need to fill up missed data for all the countries. Different metrics in different domain has different supported countries. This meta info should be statemented in the associated ADM. As a Front-end framework, it's really reasonable to refuse to fill up the missed data by itself. It's too heavy for FE to get all the required meta info and compose the missed data by themself and sometimes the meta info can even be unavailable for FE because of business/tech security strategy or some other reasons.

### 2.2.3 The Experience of ABC's Impl
All these issues make the AQL development get harder and harder. Especially when 
- more and more cascading filters like `product_id.publisher_id.company_id` and `product_id.has_iap` are required by businesss.
- user-defined aggregations requirements emerged like get `annually` results of est_download_free__sum.

If someway we can avoid the limitation of ABC's impl, we can get a very powerful OLAP system. Lessons learned from ABC's impl are
- KISS
 > Keep it simple and stupid! The microservice layer should be very simple and stupid.  
   Do one thing and do it well. The microservice layer should only care about data fetching!

- ADM Should Only Be About Schema 
 > From the end-user perspective of ADM, only 2 things are required for using each ADM  
   metrics + dimensions.  
    
   ```javascript
    // example of est_download_and_revenue metric bundles
    {
        "vendor": "ABC",
        "domain": "est_download_and_revenue",
        "metrics": [
            "est_free_app_download",
            "est_paid_app_download",
            "est_free_app_revenue",
            "est_paid_app_revenue"  
        ], 
        "dimensions": [
            "product_id",
            "device_code",
            "country_code",
            "granularity",
            "date"
        ]
    }
   ```
> For visualization, we can consider adding more fields like `description`.  
  And only the ACE layer need more meta info like where the raw data is stored and what the storage engine is.  
  ```json
    {
        "vendor": "ABC",
        "domain": "est_download_and_revenue",
        "metrics": [
            "est_free_app_download",
            "est_paid_app_download",
            "est_free_app_revenue",
            "est_paid_app_revenue"  
        ], 
        "dimensions": [
            "product_id",
            "device_code",
            "country_code",
            "granularity",
            "date"
        ],
        "engine": {
            "type": "pg",
            "connection_params": {
                "connection_str": "postgres://someuser:somepassword@somehost:381/somedatabase",
                "host": "", 
                "port": ""
            }
            
        }
    }
  ```

- ACE
  > ACE should be the only center of computing. Use the low-level storage engine's functionalities like `group` and `aggregations` or not is determined by ACE's optimization strategy. MS layer should focus on query translation and data fetching.

- AQL
 > The language exposed to the end-users should be a general query language based on the data model and simply enough to learning. From the experience of ABC, two points worth to raise up  
  (1). The language should be a superset of the underlying storage engines, not a subset.  
  (2). Could interact or integrate with the most popular query language - SQL.
> ABC does not implement these two points very well. The way ABC choose makes the AQL a bad data analysis and development experience, especially born without the support for the cascading filter (`product_id.publisher_id.company_id`) and other common operators!

- The Fill-Up Issue
  > The fill-up requirement is reasonable and acceptable. But the right way to do it is to put it in the right place. Implement in MS layer is absolutely a wrong decision. ACE should take the responsibility and provide it as an optional feature for the clients. Anyway, not every client needs the missed data to be filled-up.

# Chapter 3: MicroOLAP Impl Pattern

![MicroOLAP_Impl_Pattern](https://user-images.githubusercontent.com/20035835/157422419-caae6064-4850-43c6-9988-2429860ae372.png)


The MicroOLAP Impl Pattern includes 4 important parts. They are
- **AQL - The language of end-users**
- **AQL Core - The implementation of MicroOLAP Computing Engine**
- **Protocol used by AQL Core and USE**
- **USE - The unified storage engine**

The whole architecture is based on containerized microservice. So the AQL Core and USE layer could be a group of containers. Combined with the traffic channel and load balancer technologies, we can achieve a multi-user, resource isolated OLAP system just like what Snowflake provides.

# Chapter 4: Compared with Other Solutions
Candidates may include Spark Based Architecture, ClickHouse, Snowflake.
- Spark is a general computing engine
- ClickHouse is a data warehouse 
- Snowflake is a cloud warehouse very similar
- Presto is a data warehouse with the same arch but not impl with MS-Arch

# Reference
- [Data Mesh From an Engineering Perspective](https://www.datamesh-architecture.com/)

**My Comment**
> Summary In one word: Database/Warehouse ReImplementation Within the Microservice Theory. The problem with this architecture is when analyzing Cross-domain Data or joinings in the SQL world. MPP analytical engines like Presto and Snowflake already proved to handle it you need a powerful SQL engine so do the Data Mesh. If not, you probably will get a ClickHouse within Microservices.

