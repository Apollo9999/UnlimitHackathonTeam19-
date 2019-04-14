import random
import socket
#gas Sensor
class Sensor:
    def PressureSensor():
        return(str(random.uniform(0,40)))

    def Carbonmonoxide():
        return(str(random.uniform(0,2)))

    def Oxygen():
        return(str(random.randint(30,60)))

    def Carbondioxide():
        return(str(random.randint(10,25)))

    def Nitrogen():
        return(str(random.randint(50,80)))

    def Smoke():
        return(str(random.uniform(0,35)))

    def HeatSensor():
        return(str(random.randint(16,45)))

        
    
