docker-compose -f docker-compose.yml up -d
docker cp conf/config.json opc_iot_iotage_1:usr/src/app/conf/config.json
docker cp conf/config.properties opc_iot_iotage_1:usr/src/app/conf/config.properties
docker cp certificates/client_certificate2.pem opc_iot_iotage_1:usr/src/app/certificates/client_certificate.pem 
docker cp certificates/client_private_key2.pem opc_iot_iotage_1:usr/src/app/certificates/client_private_key.pem 



docker exec iotagent-opcua_iotage_1 node index.js > /dev/null 2>&1 &
sleep 2
curl http://localhost:4001/iot/devices \
     -H "fiware-service: openiot" \
     -H "fiware-servicepath: /" \
     -H "Content-Type: application/json" \
     -d @add_device.json \
      > /dev/null 2>&1 &
sleep 2
curl -iX POST \
  'http://localhost:1026/v2/subscriptions/' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
  "description": "plc_id",
  "subject": {
    "entities": [
      {
        "idPattern": "plc_1"
      }
    ],
    "condition": {
      "attrs": [
        "partsOK"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "partsOK"
    ],
    "metadata": ["dateCreated", "dateModified"]
  },
  "throttling": 1
}'
sleep 0.5

curl -iX POST \
  'http://localhost:1026/v2/subscriptions/' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
  "description": "plc_id",
  "subject": {
    "entities": [
      {
        "idPattern": "plc_1"
      }
    ],
    "condition": {
      "attrs": [
        "main"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "main"
    ],
    "metadata": ["dateCreated", "dateModified"]
  },
  "throttling": 1
}'


curl -iX POST \
  'http://localhost:1026/v2/subscriptions/' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
  "description": "plc_id",
  "subject": {
    "entities": [
      {
        "idPattern": "plc_1"
      }
    ],
    "condition": {
      "attrs": [
        "partsNOK"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "partsNOK"
    ],
    "metadata": ["dateCreated", "dateModified"]
  },
  "throttling": 1
}'
sleep 0.5


curl -iX POST \
  'http://localhost:1026/v2/subscriptions/' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
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
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "busy"
    ],
    "metadata": ["dateCreated", "dateModified"]
  },
  "throttling": 1
}'

sleep 0.5

curl -iX POST \
  'http://localhost:1026/v2/subscriptions/' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
  "description": "plc_id",
  "subject": {
    "entities": [
      {
        "idPattern": "plc_1"
      }
    ],
    "condition": {
      "attrs": [
        "servos_active"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "servos_active"
    ],
    "metadata": ["dateCreated", "dateModified"]
  },
  "throttling": 1
}'

sleep 0.5

curl -iX POST \
  'http://localhost:1026/v2/subscriptions/' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
  "description": "plc_id",
  "subject": {
    "entities": [
      {
        "idPattern": "plc_1"
      }
    ],
    "condition": {
      "attrs": [
        "Gripper_active"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "Gripper_active"
    ],
    "metadata": ["dateCreated", "dateModified"]
  },
  "throttling": 1
}'

sleep 0.5

curl -iX POST \
  'http://localhost:1026/v2/subscriptions/' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
  "description": "plc_id",
  "subject": {
    "entities": [
      {
        "idPattern": "plc_1"
      }
    ],
    "condition": {
      "attrs": [
        "running_hours"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "running_hours"
    ],
    "metadata": ["dateCreated", "dateModified"]
  },
  "throttling": 1
}'

sleep 0.5

curl -iX POST \
  'http://localhost:1026/v2/subscriptions/' \
  -H 'Content-Type: application/json' \
  -H 'fiware-service: openiot' \
  -H 'fiware-servicepath: /' \
  -d '{
  "description": "plc_id",
  "subject": {
    "entities": [
      {
        "idPattern": "plc_1"
      }
    ],
    "condition": {
      "attrs": [
        "Assembly_speed"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "Assembly_speed"
    ],
    "metadata": ["dateCreated", "dateModified"]
  },
  "throttling": 1
}'
