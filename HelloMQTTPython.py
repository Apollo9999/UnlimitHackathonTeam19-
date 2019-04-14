import paho.mqtt.client as mqtt
from Sensors import Sensor

import time, threading, ssl
device_id = ["0000000055f2461a",
             "0000000055f2461b",
             "0000000055f2461c",
             "0000000055f2461d",
             "0000000055f2461e",
             "0000000055f2461f",
             "0000000055f2461g"]
publish1 = ["100,Temperature,c8y_MQTTDevice",
            "100,Pressure Sensor,c8y_MQTTDevice",
            "100,CO Sensor,c8y_MQTTDevice",
            "100,O2 Sensor,c8y_MQTTDevice",
            "100,CO2 Sensor,c8y_MQTTDevice",
            "100,N Sensor,c8y_MQTTDevice",
            "100,Smoke Sensor,c8y_MQTTDevice",]
publish2 = ["110,S123456789,Temperature test model,Rev0.1",
            "110,S234567890,Pressure Test Model,Rev0.1",
            "110,S234567891,CO Test Model,Rev0.1",
            "110,S234567892,O2 Test Model,Rev0.1",
            "110,S234567893,CO2 Test Model,Rev0.1",
            "110,S234567894,N Test Model,Rev0.1",
            "110,S234567895,Smoke Test Model,Rev0.1",]
val = [["211,","",""],
       ["200,Pressure,PASCAL,","",",PSI"],
       ["200,Carbon_monoxide,Parts_per_million,","",",PPM"],
       ["200,Oxygen,Parts_per_million,","",",PPM"],
       ["200,Carbon_dioxide,Parts_per_million,","",",PPM"],
       ["200,Nitrogen,Parts_per_million,","",",PPM"],
       ["200,Smoke,Parts_per_million,","",",PPM"]]


receivedMessages = []
class Senderdata1():
    x = 0   
    class Senderdata():
        def on_message(client, userdata, message) :
            print("Received operation " + str(message.payload))
            if (message.payload.startswith ("510")) :
                print("Simulating device restart...")
                publish("s/us", "501,c8y_Restart");
                print("...restarting...")
                time.sleep(1)
                publish("s/us", "501,c8y_Restart");
                print("...done...")

        def sendMeasurements (Senderdata,y) :
            try:
                print("Sending metrics")
                if y == 0:
                    val[y][1] = Sensor.HeatSensor()
                elif y == 1:
                    val[y][1] = Sensor.PressureSensor()
                elif y == 2:
                    val[y][1]= Sensor.Carbonmonoxide()
                elif y == 3:
                    val[y][1] = Sensor.Oxygen()
                elif y == 4:
                    val[y][1] = Sensor.Carbondioxide()
                elif y == 5:
                    val[y][1] = Sensor.Nitrogen()
                elif y == 6:
                    val[y][1] = Sensor.Smoke()
                
                    
                Senderdata.publish(Senderdata.client,"s/us",val[y][0]+val[y][1]+val[y][2])
            except Exception as e :
                print(e)

            
             
        def publish(client,topic, message, waitForAck = False):
            mid = client.publish(topic, message, 2)[1]
            if (waitForAck):
                while mid not in receivedMessages:
                    time.sleep(0.30)
                    
        def on_publish(client, userdata, mid):
            receivedMessages.append(mid)

    while True:
        value = device_id[x]
        client = mqtt.Client(client_id=value)
        client.username_pw_set("team19/team19","Test@1234")
        client.on_message = Senderdata.on_message
        client.on_publish = Senderdata.on_publish
        client.connect("management.unlimitenablement.co.in", 1883)
        client.loop_start()
        Senderdata.publish(client,"s/us", publish1[x], True)
        Senderdata.publish(client,"s/us", publish2[x])
        client.subscribe("s/ds")
        Senderdata.client = client
        Senderdata.sendMeasurements(Senderdata,x)
        client.loop_stop()
        time.sleep(0.2)
        if x == 0:
            x = 1
        elif x == 1:
            x = 2
        elif x == 2:
            x = 3
        elif x == 3:
            x = 4
        elif x == 4:
            x = 5
        elif x == 5:
            x = 6
        elif x == 6:
            x = 0
        
        


    
    
 
 
  
 
 
 
 
      
    
  
 
 
 
 
