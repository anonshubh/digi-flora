"""
Developed By Group 11 (M2M)
"""
import requests,random,time

def sensor1():
    try:
        name = "Sunflower"
        device_id = "SRD02"
        temperature = random.randint(1,50)
        humidity = random.randint(10,30)
        light = random.randint(1,10)
        moisture = random.randint(1,100)

        response = requests.get(
            "http://digiflora.herokuapp.com/api/plant-data/",
            params={
                'name':name,
                'device_id':device_id,
                'temperature':temperature,
                'humidity':humidity,
                'light':light,
                'moisture':moisture
            }
        )
        print(f"Status {response.status_code}")
    except:
        print("\nExiting due to Error...")


def sensor2():
    try:
        name = "Tulip"
        device_id = "SRD03"
        temperature = random.randint(1,50)
        humidity = random.randint(10,50)
        light = random.randint(5,60)
        moisture = random.randint(20,300)

        response = requests.get(
            "http://digiflora.herokuapp.com/api/plant-data/",
            params={
                'name':name,
                'device_id':device_id,
                'temperature':temperature,
                'humidity':humidity,
                'light':light,
                'moisture':moisture
            }
        )
        print(f"Status {response.status_code}")
    except:
        print("\nExiting due to Error...")
    

if __name__ == '__main__':
    while True:
        sensor1()
        sensor2()
        time.sleep(60)
    







