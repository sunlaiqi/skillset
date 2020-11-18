

## Defining Your Own Exception Classes 

```python
class NameTooShortError(ValueError): 
	pass 
def validate(name):
    if len(name) < 10: 
		raise NameTooShortError(name) 

>>> validate('jane')
Traceback (most recent call last): 
	File "<input>", line 1, in <module> 
		validate('jane') 
	File "<input>", line 3, in validate 
		raise NameTooShortError(name) 
NameTooShortError: jane
```