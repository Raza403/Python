
def decorator_function(origional_function):
    def wrapper_function(*args,**kwargs):
        return origional_function(*args,**kwargs)
    return wrapper_function
@decorator_function
def display():
    print ("display function ran")
display()

@decorator_function

def display_info( name, age):
    print ("display_info ran with format {}, {}".format(name,age))
display_info ('ahmed', 30)
