Leverage the LAG/LEAD window function can be much easier!

```sql
with
  a as (
    select
      *
    from
      fact_download_v1
    where
      date >= '2022-06-01'
      and device_code = 'ios-phone'
      and country_code = 'US'
  ),
  b as (
    select
      product_key,
      country_code,
      device_code,
      date,
      granularity_code,
      lag(date, 60) over (
        partition by product_key,
        country_code,
        device_code,
        granularity_code
        order by
          date asc
      ) start_date
    from
      a qualify dateadd(day, 60, start_date) = date
  )
select
  *
from
  b
order by
  product_key,
  country_code,
  device_code,
  date,
  granularity_code;
  ```
