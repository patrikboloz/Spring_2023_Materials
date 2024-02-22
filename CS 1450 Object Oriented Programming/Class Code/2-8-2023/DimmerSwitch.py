# Create a DimmerSwitch class

class DimmerSwitch():

    def __init__(self, label):
        self.switchIsOn = False
        self.brightness = 0
        self.labelName = label
        
    def turnOn(self):
        self.switchIsOn = True 
        
    def turnOff(self):
        self.switchIsOn = False
        
    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1
        else:
            print("The maximum brightness has been achieved")
            
    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1
        else:
            print("The minimum brightness has been achieved")
            
    def show(self):
        print("Label:", self.labelName)
        print("Is the Switch on?", self.switchIsOn)
        print("The brightness is:", self.brightness)
        
object_DimmerSwitch = DimmerSwitch('Dimmer Switch 1')
object_DimmerSwitch.show()

object_DimmerSwitch.turnOn()
object_DimmerSwitch.raiseLevel()
object_DimmerSwitch.raiseLevel()
object_DimmerSwitch.raiseLevel()
object_DimmerSwitch.raiseLevel()
object_DimmerSwitch.raiseLevel()
object_DimmerSwitch.show()

object_DimmerSwitch.lowerLevel()
object_DimmerSwitch.lowerLevel()
object_DimmerSwitch.lowerLevel()
object_DimmerSwitch.lowerLevel()
object_DimmerSwitch.lowerLevel()
object_DimmerSwitch.lowerLevel()
object_DimmerSwitch.lowerLevel()
object_DimmerSwitch.lowerLevel()
object_DimmerSwitch.show()

object_DimmerSwitch_2 = DimmerSwitch('Dimmer Switch 2')
object_DimmerSwitch_2.show()

object_DimmerSwitch_3 = DimmerSwitch('Dimmer Switch 3')
object_DimmerSwitch_3.show()
print(object_DimmerSwitch_3)
print(type(object_DimmerSwitch_3))










    
        
    
        
