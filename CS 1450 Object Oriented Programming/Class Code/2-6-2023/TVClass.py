#Create a TV class

class TV():

    def __init__(self, brand, location):
        self.isOn = False
        self.isMuted = False
        self.brand = brand
        self.location = location

        #some default list of channels
        self.channelList = [2, 4, 5, 7, 9, 11, 20, 36, 44, 54, 65]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0 #constant
        self.VOLUME_MAXIMUM = 10 #constant
        self.volume = self.VOLUME_MAXIMUM // 2 #integer divide
        
    def power(self):
        self.isOn = not self.isOn #toggle
        
    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False #chaning the volume while muted unmutes the sound
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1
            
    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False #chaning the volume while muted unmutes the sound
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1
            
    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0 #wrap around to the first channel
            
    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1 
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1 #wrap around to the top channel
            
    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted
            
    def setChannel(self, newChannel):
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)    
        # if the newChannel is not in our list of channel, don't do anything
    
    def showInfo(self):
        print()
        print('TV Status:')
        print('The brand name is:', self.brand)
        print('The location is:', self.location)
        if self.isOn:
            print(' TV is on.')
            print(' Channel is: ', self.channelList[self.channelIndex])
            if self.isMuted:
                print(' Volume is:', self.volume, '(sound is muted)')
            else:
                print( 'Volume is:', self.volume, '(sound is on)')
        else:
            print(' TV is off.')             
    


#Main code with testing
oTV_Samsung = TV("Samsung", "Bedroom") #create the TV Samsung object
oTV_Apple = TV("Apple", "Living Room") #create an Apple TV

#Turn on the TV and show the status
oTV_Samsung.power()
oTV_Samsung.showInfo()    
    
#Change the channel up twice, raise the volume twice, show status
oTV_Samsung.channelUp()
oTV_Samsung.channelUp()
oTV_Samsung.volumeUp()
oTV_Samsung.volumeUp()
oTV_Samsung.showInfo()

#Turn the TV off, show status, turn the TV on, show status  
oTV_Samsung.power()
oTV_Samsung.showInfo()
oTV_Samsung.power()
oTV_Samsung.showInfo()  
    
#Lower the volume, mute the sound, show status
oTV_Samsung.volumeDown()
oTV_Samsung.mute()
oTV_Samsung.showInfo()

#Change the channel to 11, mute the sound, show status
oTV_Samsung.setChannel(15)
oTV_Samsung.mute()
oTV_Samsung.showInfo()
    
#Call the Apple TV methods to show, that it is independent from the Samsung TV
oTV_Apple.power()
oTV_Apple.setChannel(11)
oTV_Apple.volumeDown()
oTV_Apple.volumeDown()
oTV_Apple.showInfo()
    
    
    
    
    
    
    
    
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
