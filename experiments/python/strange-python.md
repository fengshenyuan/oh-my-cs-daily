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
