#class MyError is ectended from super class Exception

class User_Error(Exception):
    # Constructor method
    def __init__(self, value):
        self.value = value
    # __str__display function    
    def __str__(self):
        return(repr(self.value))
try:
    raise(User_Error("User defined error"))
    # Value of Exception is stored in error
except User_Error as error:
    print('A New Exception occured:',error.value)
