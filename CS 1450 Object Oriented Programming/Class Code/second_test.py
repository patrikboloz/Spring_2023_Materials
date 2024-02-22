def say_hi(name):
    if name == '':
        print("You didnt enter your name!")
    else:
        print("Hi there....")
        for letter in name:
            print(letter)
            
            
            
name = input("your name: ")
say_hi(name)
