# ABC Data Ecosystem & Governance
This document is trying to describe the ABC from the very beginning to the final delivered data materials such as AQL, Bulk CSV files, Snowflake Secure Share, and the way we choose to manage and govern such a complex data ecosystem in ABC.

## Chapter 0: The Data Warehouse
Generally, a data warehouse is a database that stores a large amount of data with super complex dimensional attributions. It's built for Analysis or the OLAP. 

### The Data Warehouse Theory
The most popular data warehouse theory is the multiple-dimensional data modeling theory(MDDM). Ralph Kimball and Margy Ross have written the fantastic Book The ***[Data Warehouse Toolkit: The Definitive Guide to Dimensional Modeling](https://www.amazon.com/Data-Warehouse-Toolkit-Definitive-Dimensional/dp/1118530802/)*** to introduce this theory to data warehouse developers and tech leaders. ABC also follows up the basic modeling tools and theory introduced in this book to construct the ABC Data Ecosystem while in some cases we made trade-offs according to our own business.

### Snowflake: The Real World DW Used by ABC
The [Snowflake](https://www.snowflake.com/) is the physical database chosen by ABC to leverage The Data Warehouse Theory and build the one source of the truth of ABC Data Ecosystem.

## Chapter 1: The Raw Data
The raw data of AA comes from several data sources. What we call raw data is the data does not use to build any layer of the modeling directly. They are fundamental datasets such as data collected from Scrappers, inputs from upstreams.


## Chapter 2: The Business Data Layer(BDL ==> DWD + DWB)
TBD

## Chapter 3: The Application Data Layer(ADL ==> DWS: Data Warehouse Service)
TBD

## Chapter 4: The Customized Data Layer(CDL ==> ADS：Application Data Service)
TBD

## Chapter 5: The ETL & Data Pipeline
TBD

## Chapter 6: The Unified Interface of ABC Data Ecosystem
TBD

## Chapter 7: Pricing Model: How the data is consumed by customers?
TBD

## Chapter 8: Data QA
TBD

## Chapter 9: Data Delivery 
### 9.1 Snowflake Data Share
TBD

### 9.2 Clould Data File Exchange
TBD

### 9.3 AQL
TBD

### 9.4 API
TBD

## Chapter 10: A/B Test, Changes, Restatements, and Notifications
### 10.1 A/B Test
TBD

### 10.2 Non-breaking Changes
TBD

### 10.3 Breaking Changes
TBD

### 10.4 How to send notifications to customers?
TBD

## Chapter 11: Access Permission Management
TDB

## Chapter 12: Performance & Cost
TBD

## Chapter 13: Issues 
TBD

## Chapter 14: Todolist
TBD

## Chapter 15: Q & A
TBD
