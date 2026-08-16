# Pandas
## Summary
* pandas can be viewed as column-based, in-memory relational DB
* pd['column_A'] = True will set all the value of column_A to be True
* index in pandas is just labels of data rows
* so pandas basically have 3 key conceptions: index, columns, values

```Python

By default, columns get inserted at the end. The insert function is available to insert at a particular location in the columns:

In [72]: df.insert(1, 'bar', df['one'])
In [73]: df
Out[73]: 
   one  bar   flag  foo  one_trunc
a  1.0  1.0  False  bar        1.0
b  2.0  2.0  False  bar        2.0
c  3.0  3.0   True  bar        NaN
d  NaN  NaN  False  bar        NaN
```
* axis 表示数据的聚合等操作发生在哪个轴上(axis=0, index轴; axis=1, column轴) 即把对应轴上的一串数据抽取出来，然后apply对应的操作
```
In [77]: df
Out[77]: 
        one       two     three
a  1.394981  1.772517       NaN
b  0.343054  1.912123 -0.050390
c  0.695246  1.478369  1.227435
d       NaN  0.279344 -0.613172

In [78]: df.mean(0)
Out[78]: 
one      0.811094
two      1.360588
three    0.187958
dtype: float64

In [79]: df.mean(1)
Out[79]: 
a    1.583749
b    0.734929
c    1.133683
d   -0.166914
dtype: float64
```
