Subfolder to collaborate on the data models associated with the STAR DIH^2 Experiment

Here are two folders: dummySensor and OPCUAfromCobot.

### dummySensor ###

Folder dummySensor contains entities in OCB from 3 dummy sensors using SAN from ramp dockerhub: <https://docker.ramp.eu/?page=1#!taglist/opil/opil.iot.san>

In this example 1 digital and 2 analog sensors were used. Data format from SAN has NGSI entities not readable by FIWARE QuantumLeap, see for example *digitalsensor.json*. FIWARE QuantumLeap has a specific format that it "understands". To make use of QuantumLeap and software like Grafana, a translator is needed to convert these entities using the SAN PROXY: <https://hub.docker.com/r/sejego/ql_san_proxy> 

The created entities have a *_ql* postfix in entity id and entity type, see *digitalsensorforquantumleap.json*.


### OPCUAfromCobot ###

Here is config.json generated with the mapping tool from the iotage opcua: <https://github.com/Engineering-Research-and-Development/iotagent-opcua.git>. The OPCUA server is onboard the Omron PLC. This needs to be checked and chosen only needed entities.
