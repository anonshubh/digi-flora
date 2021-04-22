"""
Developed By Group 11 (M2M)
"""
import requests,random,time,json

def sensor1():
    try:
        name = "Sunflower"
        device_id = "SRD02"
        temperature = random.randint(1,50)
        humidity = random.randint(10,30)
        light = random.randint(1,10)
        moisture = random.randint(1,100)

        headers = {'Content-Type':'application/json'}

        data_moisture = {'value1':moisture}

        try:
            if(moisture<30 and moisture>10):
                response_gmail = requests.post(
                    'https://maker.ifttt.com/trigger/moisture_plant/with/key/fQ4f1iZlmNheWnwWPPnNW73iaHDrt_RaXxoxlNxlOeE',
                    data = data_moisture
                )
        except:
            pass

        data={
            'name':name,
            'device_id':device_id,
            'temperature':temperature,
            'humidity':humidity,
            'light':light,
            'moisture':moisture
        }

        json_data = json.dumps(data)

        response = requests.post("http://digiflora.herokuapp.com/api/plant-data/",data=json_data,headers=headers)
        print(f"Status {response.status_code}")
    except:
        print("\nExiting due to Error...")


def sensor2():
    try:
        name = "Rose"
        device_id = "SRD03"
        temperature = random.randint(5,50)
        humidity = random.randint(15,40)
        light = random.randint(2,10)
        moisture = random.randint(50,100)

        data_moisture = {'value1':moisture}

        try:
            if(moisture<30 and moisture>10):
                response_gmail = requests.post(
                    'https://maker.ifttt.com/trigger/moisture_plant/with/key/fQ4f1iZlmNheWnwWPPnNW73iaHDrt_RaXxoxlNxlOeE',
                    data = data_moisture
                )
        except:
            pass

        headers = {'Content-Type':'application/json'}

        data={
            'name':name,
            'device_id':device_id,
            'temperature':temperature,
            'humidity':humidity,
            'light':light,
            'moisture':moisture
        }

        json_data = json.dumps(data)

        response = requests.post("http://digiflora.herokuapp.com/api/plant-data/",data=json_data,headers=headers)
        print(f"Status {response.status_code}")
    except:
        print("\nExiting due to Error...")


    

if __name__ == '__main__':
    while True:
        sensor1()
        sensor2()
        time.sleep(900)
    







