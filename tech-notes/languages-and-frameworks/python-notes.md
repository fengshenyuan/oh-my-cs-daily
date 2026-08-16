
# A little Experience about Python
Author G.Yuan 2018/07/12

## Python Class Hierarchy constant definitions have very strange actions

I suppose the B.D should be [4, 5], but actually not.
```Python
>>> class A:
...     C = [1, 2, 3]
...     D  = C[-2:]
...
>>> class B(A):
...     C = [2, 3, 4, 5]
...
>>> A.D
[2, 3]
>>> B.D
[2, 3]

```

## Python `__getattr__` vs `__getattribute__`
* `__getattribute__` will be called before you look up attribute in normal place, such as `__dict__`, super(), etc.
* `__getattr__ `will be called after you looked up in normal place.
* `__getattribute__`  AttribureError Exception will be ignored and continue to look up in normal place and `__getattr__` . A good sample:

```python
class Sample(object):

	def __init__(self, a, b):
		self.a = a
		self.b = b
		self._x = None

	def __getattr__(self, item):
		return str(item)

	def __getattribute__(self, item):
		if item.startswith('_'):
			raise AttributeError
		return super().__getattribute__(item)


s = Sample('a', 'b')
print(s.a)
print(s.b)
print(s._x)
# result
# a
# b
# _x
```

## python super

 * super() is just a normal function. You can call super() anywhere if u can pass it the right parameters.(You can call it outside a class)
 *  Call `super().__init__` not means the interpreter will init all the parent classes right for u. It just says that I will find the next `parent` in the chain, then call `__init__`.(No promise about further parents). If u want init all parent classes, u need design carefully and call super() in almost every level of inheritance.
 * When u want something implemented in parent classes, try super.
 * When u want to understand the behavior of super, print A.mro or `A.__class__.__mro__`.
```python
# a simple demo to understand how super works
def my_super(clazz, inst):
	mro_list = inst.__class__.__mro__
	for i, parent_clazz in enumerate(mro_list):
		if parent_clazz == clazz:
			return mro_list[i+1]()
	raise Exception("super error")
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg5ODYyNTE4NywxODAzOTc5NTQwLC03ND
AyNzQ2NTIsLTc3NjgzNTQ4MSwxOTAzNTAyNjM5XX0=
-->

## Run Pylint With Scripts
```python
if __name__ == '__main__':
    from pylint.lint import Run
    try:
        Run(['/path/to/your/code/repo/'])
    except Exception as ex:
        print ex
    finally:
        end = True
```


## Pandas
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
