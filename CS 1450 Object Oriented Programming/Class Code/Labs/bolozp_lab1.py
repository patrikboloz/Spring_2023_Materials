#CS 1450 Lab 1 - worth 100 points
#Your task will be to create a class called StandingFan(), which by using methods will be able to turn on/off rotation, increase/decrease the speed of the fan (0 - fan turned off, 5 - maximum speed), and show the state of the fan (what speed the fan is on currently and if the rotation is on/off.
 
#HINT:Use attributes self.fan_speed = 0 and self.rotation = False as a starting point.

#Extra credit: If self.fan_speed would go to negative numbers, reset the self.fan_speed to 0, and if the self.fan_speed would go above 5, reset it back to 5. Also add a print statement saying that the minimum or maximum speed has been achieved


class StandingFan():

    def __init__(self):
        self.fan_speed = 0
        self.rotation = False











        
    def speed_up(self):
        self.fan_speed = self.fan_speed + 1
        return self.fan_speed
        
    def speed_down(self):
        self.fan_speed = self.fan_speed - 1
        return self.fan_speed
        
    def rotate(self):
    
        if self.rotation == True:
            self.rotation = False
            return self.rotation
            
        elif self.rotation == False: 
            self.rotation = True
            return self.rotation
    
    def show(self):
        print("The Fan's speed is: ", self.fan_speed, "and the rotation is: ", self.rotation)
        
        
#Main code

#Creating the object           
fan_1 = StandingFan()

#Using methods
fan_1.show() #show the starting state
fan_1.speed_up() #speed up the fan by 1
fan_1.speed_up() #speed up the fan by 1
fan_1.speed_up() #speed up the fan by 1
fan_1.show() #show the fan state after using methods
fan_1.rotate() #turn on/off the rotation
fan_1.show() #show the fan state after using methods
fan_1.speed_down() #slow down the fan by 1
fan_1.speed_down() #slow down the fan by 1
fan_1.show() #show the fan state after using methods

















    
   
        
