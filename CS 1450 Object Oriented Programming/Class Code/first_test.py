#print("Hello world")

def say_hi(name, location): #this is a custom function that will print out a custom message
    print('hi', name, "welcome to", location)
    
#say_hi('Mark', 'NMHU') 

def add(a, b):
    return a + b
    
#result = add(10, 20)

#if add(1,1) == 2:
#    print("That is what you'd expect!")

def welcome(name='Mark', location='NMHU'):
    print("Hello", name, "welcome to", location)
    
welcome('Peter', 'NMSU')
