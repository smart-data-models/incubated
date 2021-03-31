import requests
import time
url = r'http://localhost:1026/v2/subscriptions/'
headers = {
    'Content-Type': 'application/json',
    'fiware-service': 'openiot',
    'fiware-servicepath': r'/'}
data = {
  "description": "plc_id",
  "subject": {
    "entities": [
      {
        "idPattern": "plc_1"
      }
    ],
    "condition": {
      "attrs": [
        "busy"
      ]
    }
  },
  "notification": {
    "http": {
      "url": r"http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "busy"
    ],
    "metadata": ["dateCreated", "dateModified"]
  },
  "throttling": 1
}
print('test')
r = requests.post(url, data=data, headers=headers)
print(data)
l = ['main', 'Gripper_active', 'Assembly_speed', "running_hours", "busy", "servos_active", "partsOK", "partsNOK"]
#l = ['main']
for x in l:
    data['subject']['condition']['attrs'] = x
    data['notification']['attrs'] = [x]
    r = requests.post(url, data=data, headers=headers)
    print(f'{x}:{r}')
    print(data)
    time.sleep(3)
