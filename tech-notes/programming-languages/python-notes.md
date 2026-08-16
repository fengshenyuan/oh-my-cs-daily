
# <center>A little Experience about Python</center>
<center>Author G.Yuan 2018/07/12</center>

## `__getattr__ vs __getattribute__`
* `__getattribute__` will be called before you look up attribute in normal place, such as `__dict__`, super(), etc.
* `__getattr__ `will be called after you looked up in normal place.
* `__getattribute__`  AttribureError Exception will be ignored and continue to look up in normal place and `__getattr__` . A good sample:
	```
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
	```
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
