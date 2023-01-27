# s4syst
Version: 0.0.2

## Description 

List of Types under s4syst
### Types

[Connection](https://github.com/smart-data-models/incubated/SAREF/s4syst//Connection/README.md) - The class of connections between systems. This class qualifies property s4syst:connectedTo. A connection describes potential interactions between systems. Any two connected systems are connected through a connection. A connection can connect more than two systems at the same time.

[ConnectionPoint](https://github.com/smart-data-models/incubated/SAREF/s4syst//ConnectionPoint/README.md) - The class of connection points of systems, at which they may be connected to other systems. This class qualifies properties s4syst:connectsSystem and s4syst:connectedThrough. A connection point belongs to exactly one system. Any system connected through a connection is connected at one of its connection points to the connection. The system of a connection point that is connected through a connection is itself connected through the connection.

[System](https://github.com/smart-data-models/incubated/SAREF/s4syst//System/README.md) - The class of systems, i.e., systems virtually isolated from the environment, whose behaviour and interactions with the environment are modeled. Systems can be connected to other systems. Connected systems interact in some ways. Systems can also have subsystems. Properties of subsystems somehow contribute to the properties of the supersystem.

