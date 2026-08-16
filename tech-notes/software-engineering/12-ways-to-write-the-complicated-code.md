# 12 Ways to Write the Complicated Code! 简单代码复杂化的艺术

如何做到自然而然地将简单代码复杂化，还不被发现，实乃一件艺术！

—— *The Code Review Note*

## 01 > 万不可将代码写成一行。
如律所行，我必绞尽脑汁、生拉硬扯，使此代码轻则折叠换行、格式不齐，重则分崩离析，多段组合。
```python
# 如是我闻: 组合target_key的相关代码居然分割的如此厉害
# 完成这件事情依次出现了original_name, processed_dir,gened_item_gz, target_key等4个几乎只用一次的变量!
original_name = "{country_code}.json".format(country_code=country_code)
processed_dir = AppDiscoveryConst.REGULAR_PATH.format(
    data_type=folder_type, granularity=granularity, date=date_file)

gened_item_gz = original_name + '.gz'
target_key = processed_dir + gened_item_gz

# 改造后
COUNTRY_LEVEL_RESULT_PTN = "xx_bucket/{s3_tmp_root}/{data_type}/" \
                            "{granularity}/{date}/app_list/ranking_records/{country_code}.json.gz"

target_key = AppDiscoveryConst.COUNTRY_LEVEL_RESULT_PTN.format(
        s3_tmp_root=self.s3_tmp_root,
        data_type=self.data_source,
        granularity=self.granularity,
        date=self.target_date,
        country_code=country_code)
```



## 02 > 善用全局变量改变代码并不混沌的局面。
```python
# 哪怕USAGE_DB_INFO这个变量只会使用一次，我们也要在函数开头进行全局性定义！
def process_data(self, date_group):
    USAGE_DB_INFO = DATABASES['int_cohorts']
    total_run_time = 0.0
    for start_date, end_date in date_group:
        print("{}: start {}|{} job at {}".format(
            self.usage_cross, self.granularity, start_date, datetime.now()))
        begin = time()
        with ThreadPoolExecutor(4) as e:
            for country_code in self.country_codes:
                e.submit(self._process_data_by_country_code, country_code, USAGE_DB_INFO, start_date, end_date)
        one_date_run_time = time() - begin
        total_run_time += one_date_run_time
        print('{}: Finished {}|{} job at {} -- use {:.2f} seconds'.format(
            self.usage_cross, self.granularity, start_date, datetime.now(), one_date_run_time))
    return total_run_time
```

## 03 > 将一个简单函数拆成3个或者更多，直接或间接破坏代码亲和性
```python
# 改造前
def _get_unified_category_id_from_permission_table(self, app_id, country_code):
    perm_key = (app_id, country_code)
    category_ids = self.permission_data_dict[perm_key] if self.permission_data_dict[perm_key] else {0}
    all_country_perm_key = (app_id, "-1")
    all_country_category_ids = self.permission_data_dict[all_country_perm_key]
    unified_category_ids = self._category_game_mapping(category_ids)
    all_country_unified_category_id = self._category_game_mapping(all_country_category_ids)
    unified_category_ids.update(all_country_unified_category_id)
    return unified_category_ids

def _category_game_mapping(self, category_ids):
    unified_category_id = set()
    for category_id in category_ids:
        unified_category_id.add(category_id)
        if category_id in AppDiscoveryConst.ALL_GAMES_CATEGORY_IDS:
            unified_category_id.update({0, 1})
        elif category_id in AppDiscoveryConst.ALL_NON_GAMES_CATEGORY_IDS:
            unified_category_id.update({0, 2})
        elif category_id in AppDiscoveryConst.OVERALL_CATEGORY_ID:
            unified_category_id.add(0)
        else:
            unified_category_id.add(0)
    return unified_category_id

# 改造后
def _get_unified_category_id_from_permission_table(self, app_id, country_code):

    unified_category_ids = self.permission_data_dict.get((app_id, country_code), set()) | \
                            self.permission_data_dict.get((app_id, "-1"), set()) | {0}

    if unified_category_ids & AppDiscoveryConst.ALL_GAMES_CATEGORY_IDS:
        unified_category_ids.add(1)

    if unified_category_ids & AppDiscoveryConst.ALL_NON_GAMES_CATEGORY_IDS:
        unified_category_ids.add(2)

    return unified_category_ids
```

## 04 > 针对同一个问题采取不同的实现路径或方案，并交叉使用以成功迷惑读者
```python
# Solution 1
@staticmethod
def device_code_mapping(device_id, feed_id):
    if feed_id is None:
        if device_id == 1001:
            return "android-phone"
        elif device_id == 1002:
            return "android-tablet"
        elif device_id == 2001:
            return "ios-phone"
        else:
            return "ios-tablet"
    else:
        if device_id == 0:
            return "android-phone"
        else:
            if feed_id in (0, 1, 2):
                return "ios-phone"
            return "ios-tablet"


# Solution 2
DEVICE_ID_CODE_MAPPING = {
    1001: "android-phone",
    1002: "android-tablet",
    2001: "ios-phone",
    2002: "ios-tablet"
}            
device_code = AppDiscoveryConst.DEVICE_ID_CODE_MAPPING.get(device_id)
```
 

## 05 > 不相信和使用基础数据结构提供的特性，而是自己添加ensure logic
```python
# why we need a deepcopy? Just to make sure start_date will not be affected by the split function!
_date = deepcopy(start_date)
_date_pattern = _date.split("-")
date_str = _date_pattern[0] + _date_pattern[1]

# 改造后
date_str = ''.join(end_date.split('-')[:2])
```


## 06 > 使用for循环而不是其他更高级的operators将代码复杂化
```python
# 改造前
def _category_game_mapping(self, category_ids):
    unified_category_id = set()
    for category_id in category_ids:
        unified_category_id.add(category_id)
        if category_id in AppDiscoveryConst.ALL_GAMES_CATEGORY_IDS:
            unified_category_id.update({0, 1})
        elif category_id in AppDiscoveryConst.ALL_NON_GAMES_CATEGORY_IDS:
            unified_category_id.update({0, 2})
        elif category_id in AppDiscoveryConst.OVERALL_CATEGORY_ID:
            unified_category_id.add(0)
        else:
            unified_category_id.add(0)
    return unified_category_id

# 改造后
unified_category_ids = {0}
if unified_category_ids & AppDiscoveryConst.ALL_GAMES_CATEGORY_IDS:
    unified_category_ids.add(1)
if unified_category_ids & AppDiscoveryConst.ALL_NON_GAMES_CATEGORY_IDS:
    unified_category_ids.add(2)
```

## 07 > 将永远都不可能出现的逻辑合法地包装在一段复杂代码中，以保证只有我自己才能读懂
```python
# 你永远都想不明白generate_begin_date_and_end_date_for_granularity为什么被调用了2次以及后续的for循环处理逻辑
rt_all_res = []
if device_id < 2000:
    rt_store_id = store_id

    retention_sql = RETENTION_SINGLE_QUERY.format(
        rt_schema=self.rt_schema,
        store_id=rt_store_id,
    )
    rt_param = {"rt_kpi": tuple(UsageConst.RETENTION_KPI)}
    runner = LocalSqlRunner(usage_db_info)
    rt_start_start_date, rt_start_end_date = \
        self.generate_begin_date_and_end_date_for_granularity(
            start_date, granularity="monthly")
    rt_end_start_date, rt_end_end_date = \
        self.generate_begin_date_and_end_date_for_granularity(
            start_date, granularity="monthly")
    rt_dates = [rt_start_end_date]
    if rt_start_start_date != rt_end_start_date:
        rt_dates = [rt_start_end_date, rt_end_end_date]
    retention_res = []
    try:
        rt_all_res = []
        for rt_date in rt_dates:
            rt_param['end_date'] = rt_date
            retention_res = runner.select(retention_sql, rt_param)[0]
        rt_all_res.extend(retention_res)
    except Exception as err:
        rt_all_res = []
        logger.warning('Fail to run get udb pro retention sql Error: %s', err)
```

## 08 > 添加并混用大量print/logger.info/time()等调试相关代码，成功淹没主代码逻辑
```python
# 改造前
def process_data(self, date_group):
    USAGE_DB_INFO = DATABASES['int_cohorts']
    total_run_time = 0.0
    for start_date, end_date in date_group:
        print("{}: start {}|{} job at {}".format(
            self.usage_cross, self.granularity, start_date, datetime.now()))
        begin = time()
        with ThreadPoolExecutor(4) as e:
            for country_code in self.country_codes:
                e.submit(self._process_data_by_country_code, country_code, USAGE_DB_INFO, start_date, end_date)
        one_date_run_time = time() - begin
        total_run_time += one_date_run_time
        print('{}: Finished {}|{} job at {} -- use {:.2f} seconds'.format(
            self.usage_cross, self.granularity, start_date, datetime.now(), one_date_run_time))
    return total_run_time

# 改造后
def process_data(self):
    with ThreadPoolExecutor(self.thread_pool_size) as e:
        for country_code in self.data_source_conf.COUNTRY_LEVELS['all']:
            e.submit(self._process_data_by_country_code, country_code)
```

## 09 > 在函数签名中添加不少于3个以上的额外参数，即使这些参数可以通过this/self指针获取，那又有什么关系？
```python
# 改造前
def upload_data_to_s3(self, granularity, country_code, date_file, folder_type, res_data):
    original_name = "{country_code}.json".format(country_code=country_code)
    processed_dir = AppDiscoveryConst.REGULAR_PATH.format(
        data_type=folder_type, granularity=granularity, date=date_file)

    gened_item_gz = original_name + '.gz'
    key = processed_dir + gened_item_gz
    logger.info("bulk_data: start to upload file to S3: {}/{}".format(AppDiscoveryConst.BUCKET_NAME, key))
    gzip_and_upload_cnt_to_s3(cnt=json.dumps(res_data), target_key=key)

# 改造后
def _upload_country_code_level_result(self, country_code, result_data):
    key = AppDiscoveryConst.COUNTRY_LEVEL_RESULT_PTN.format(
        self.data_source, granularity=self.granularity, date=self.target_date, country_code=country_code
    )
    gzip_and_upload_cnt_to_s3(cnt=json.dumps(result_data), target_key=key)
```

## 11 > 在父类中定义只有某个特殊子类才能用到的变量，而且该变量与子类一一绑定。绝对没有人会想到OOP还可以这么玩，我一定是个天才！
```python
# 其中usage_base/usage_professional/usage_store/...都是DataToS3的特定子类关系变量
class DataToS3(object):
    is_regular = False
    rt_schema = "rt"
    ca_schema = "ca"
    usage_base = "usage_base"
    usage_professional = "usage_professional"
    usage_store = "store"
    usage_cross = "cross_app_usage"
    rating_level = "app_store_ratings"

    def __init__(self, granularity, country_codes, permission_data_dict):
        self.granularity = granularity
        self.country_codes = country_codes
        self.permission_data_dict = permission_data_dict

```

## 12 > 定义一些事关重大的bool变量，但从来不使用它们，也不写任何注释，保证每个看到的人都会迷糊好一阵并对着屏幕发呆...
```python
# is_regular标记显示可能有重大的处理逻辑分支，但是改变量并没有使用过，查看所有代码也没有任何迹象有针对regular或非regular不同逻辑
class DataToS3(object):
    is_regular = False
    rt_schema = "rt"
    ca_schema = "ca"
    usage_base = "usage_base"
    usage_professional = "usage_professional"
    usage_store = "store"
    usage_cross = "cross_app_usage"
    rating_level = "app_store_ratings"
```
