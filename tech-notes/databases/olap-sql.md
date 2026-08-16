# OLAP-SQL
This SQL extension for OLAP applications, which tries to reduce the query complexity of multidimensional modeled data by avoid joining in the SQL.

The basic idea of OLAP-SQL is that we need to abandon the 2-dimensional, relational model language expression in a multidimensional analytics environment. The data itself is multidimensional. There is no reason why we need to express the relation and analytics processing in a low-level 2-dimensional way. That totally a mess, especially when you more than 100 dimensions. You cannot imagine how big and how complex the SQL you would write. You would join B from A, join  C with B, and so on. The industry has developed some methodology to avoid the dimensional explosion disaster such as star model or just store duplication data in each metric table. But that does solve the problem. It just makes it not so obvious and painful. My thinking is that if we cannot avoid this, then let's face it. We need a new design that admits and accepts the complexity born with multidimensional data itself. 

That's what I call OLAP-SQL. I try to build a model not directly based on the 2-dimensional tabular theory and in a higher level - the domain modeling level.

What we want to achieve is to avoid express the relationships among data in every query dynamically and instead we want to build the relationship of the datasets into a static, predefined model.[避免在每次查询中动态的构建join关系，转而采用模型预先定义好的逻辑关系 - Join静态化建模方法论]

这将带来以下好处
- 模型是标准化、公理化的，这将大大减轻模型维护者和使用者的学习和理解成本，好的建模规范将使得所有的事情都以最简单的方式呈现出来，而不是关系型模型那样充斥着冗余和庞杂。
- 不用写大量join来描述如何产生数据，只需要简单且必要的所想要的数据即可

## Domain, Catalog, Model
```sql
domain.catelog.model 
vendor.catelog.model 

SELECT 
    product_id.*
FROM 
   VENDER ABC
WHERE
    product_id.country_code = 'CN'
```

## Models, Dimension, Properties
```json
{
    "vendor": "ABC",
    "domain": "est_download_and_revenue",
    "metrics": [
        "est_download",
        "est_revenue",
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


```json
{
    "vendor": "ABC",
    "domain": "est_usage_base",
    "metrics": [
        "est_activer_user",
        "est_install_base",
    ], 
    "dimensions": [
        "product_id",
        "device_code",
        "category_id",
        "country_code",
        "granularity",
        "date"
    ],
    "engine": {
        "type": "pg",
        "connection_params": {
            "connection_str": "postgres://someuser:somepassword@somehost:3600/somedatabase",
            "host": "", 
            "port": ""
        }
        
    }
}
```

# OLAP-SQL 
## Metric Select SQL
What's top 100 download apps date 2021-07-01 which have download in CN and at the same time have installs in US?
```sql
SELECT FACT
    sum(est_download) as est_download__sum,
    sum(est_revenue) as est_revenue__sum,
    sum(est_active_user) as est_active_user__sum,
    sum(est_install_base) as est_install_base__sum
FROM 
    VENDER ABC 
WHERE
    est_download.country_code = 'CN' AND 
    est_install_base.country_code = 'US' AND
    date = '2021-07-01' AND 
    granularity = 'daily' AND 
    product_id.company_id.name = 'Netflix'
GROUP BY  
    product_id,
    country_code,
    granularity,
    date
HAVING 
    est_download__sum >= 100 AND 
    est_install_base__sum >= 100 
ORDER BY 
    est_download__sum DESC
LIMIT 
   100
WITH 
    (
        CARD 
            est_download left JOIN ON est_install_base
        DIMENSION
            product_id.*, 
            product_id.release_time,
            product_id.company_id.*,
            product_id.company_id.name,
            product_id.publisher_id,
            product_id.publisher_id.name
    ) 

RESPONSE_FORMAT = '{CUBE or TABLE}';
```


## Dimension Select SQL 
Show me the top 100 apps(and their company names) which have most downloads from 2021-07-01 and at least have more than 10000 downloads?
```sql
SELECT DIMENSION 
    product_id.product_id,
    product_id.name,
    product_id.company_id,
    product_id.company_id.name
FROM 
    VENDER ABC 
WHERE
    date >= '2021-07-01' AND 
    granularity = 'daily' AND 
    country_code = 'CN' AND
    product_id.company_id.name = 'Netflix'
GROUP BY  
    product_id
HAVING 
    (sum(est_download) AS est_download__sum) >= 10000 AND
    (sum(est_install_base) AS est_install_base__SUM) >= 1000
ORDER BY 
   est_download__sum DESC
LIMIT 100;
```

