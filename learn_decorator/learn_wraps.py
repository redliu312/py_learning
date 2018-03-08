from functools import wraps
'''
https://www.thecodeship.com/patterns/guide-to-python-function-decorators/
'''

def tags(tag_name):
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(name):
            return "<0>{1}</0>".format(tag_name,func(name))
        return func_wrapper 
    return tags_decorator

@tags("p")
def get_text(name):
    return name

print(get_text.__name__)
print(get_text.__doc__)
print(get_text.__module__)

