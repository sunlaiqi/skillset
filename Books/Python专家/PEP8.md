- [代码规范](#代码规范)
	- [推荐命名规范](#推荐命名规范)
		- [变量命名 - 'Public'和'Private'](#变量命名---public和private)

# 代码规范

## 推荐命名规范

Module names − all_lower_case
Class names and exception names − CamelCase
Global and local names − all_lower_case
Functions and method names − all_lower_case
Constants − ALL_UPPER_CASE

### 变量命名 - 'Public'和'Private'
Python中没有所谓的'私有'属性，理论上任何属性都是'共有'的。Python只是通过命名规范来来约定哪些属性是公开的，哪些属性是内部使用的。

- Public attributes or variables (intended to be used by the importer of this module or user of this class) − `regular_lower_case`
- Private attributes or variables (internal use by the module or class) − `_single_leading_underscore`
- Private attributes that shouldn’t be subclassed − `__double_leading_underscore`
- Magic attributes − `__double_underscores__`（use them, don’t create them）

name mangling
`__double_leading_underscore`也叫naming mangling。不知道怎么翻译。结果就是，`__double_leading_underscore`变成了`_ClassName__double_leading_underscore`
```python
class ManglingTest:	
    def __init__(self): 
		self.__mangled = 'hello' 
	def get_mangled(self): 
		return self.__mangled 

>>> ManglingTest().get_mangled() 
'hello'
>>> ManglingTest().__mangled 
AttributeError: 'ManglingTest' object has no attribute '__mangled'
>>> ManglingTest()._ManglingTest__mangled
'hello' 
```
在这里`__mangled`实际上变成了`_ManglingTest__mangled`，可以直接访问。
注意到，对于实例的函数是没有影响的。
