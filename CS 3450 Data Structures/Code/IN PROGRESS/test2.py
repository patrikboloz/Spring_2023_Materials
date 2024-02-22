prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
print(prime_list)
print(prime_list[0])

prime_list.append(37)
print(prime_list)

prime_tuple = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
print(prime_tuple)

one_element_tuple = (18,)
print(type(one_element_tuple))

a_string = "I'm here"

a_string2 = 'I\'m\n here \tand there'
euro_symbol = "20\u20AC"
dollar_symbol = "50\u0024" 

'''unicode for the dollar sign
and the next line is here '''

print(a_string)
print(a_string2)
print(euro_symbol)
print(dollar_symbol)

custom_dict = {'A':100, 'B':90, 'C':80}

a = 50
b = 5

if a <= 20:
    a = a + 5
    print(a)
elif b > 10:
    b = b - 5
    print(b)
else:
    print("There is nothing else to do")
    
while True:
    print("a is smaller than 100. a is ", a)
    #a = a + 10
    break
    
a_string2 = "Hello"
for i in a_string2:
    print(i)
    
def greeting(name, location): 
    print("Hello", name, "welcome to", location)
    
greeting("Mark", "NMHU")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














