[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)

# DataModel.ROS2

This repository contains Smart Data Models based on ROS2 (Robot Operating System 2) message types. These data models enable the integration of robotic systems with FIWARE/NGSI-LD platforms.

## Description

The DataModel.ROS2 contains NGSI-LD compliant representations of common ROS2 message types, allowing robotic systems to publish and subscribe to data using standardized FIWARE interfaces.

## Data Models

This subject includes the following data models:

### 1. GeometryMsgsPose
- **Description**: A representation of pose in free space, composed of position and orientation
- **ROS2 Message Type**: `geometry_msgs/Pose`
- **Properties**:
  - `position`: 3D position (x, y, z) in meters
  - `orientation`: Quaternion orientation (x, y, z, w)
  - `frameId`: Reference frame identifier
- **Use Cases**: Robot localization, object tracking, navigation waypoints

### 2. NavMsgsOdometry
- **Description**: Represents an estimate of a position and velocity in free space
- **ROS2 Message Type**: `nav_msgs/Odometry`
- **Properties**:
  - `header`: Timestamp and frame information
  - `childFrameId`: Child frame identifier (typically robot base frame)
  - `pose`: Position and orientation estimate with 6x6 covariance matrix
  - `twist`: Linear and angular velocity estimates with 6x6 covariance matrix
- **Use Cases**: Mobile robot navigation, state estimation, sensor fusion

### 3. SensorMsgsBatteryState
- **Description**: Represents the state of a battery, including voltage, current, charge, capacity, and health status
- **ROS2 Message Type**: `sensor_msgs/BatteryState`
- **Properties**:
  - `voltage`: Battery voltage in Volts (V)
  - `current`: Current in Amperes (A), negative indicates discharging
  - `charge`: Current charge in Ampere-hours (Ah)
  - `capacity`: Total capacity in Ampere-hours (Ah)
  - `percentage`: Charge percentage (0.0 to 1.0)
  - `powerSupplyStatus`: Charging state (UNKNOWN, CHARGING, DISCHARGING, NOT_CHARGING, FULL)
  - `powerSupplyHealth`: Battery health status
  - `powerSupplyTechnology`: Battery chemistry type (LION, LIPO, NIMH, etc.)
  - `cellVoltage`: Individual cell voltages
  - `cellTemperature`: Individual cell temperatures
- **Use Cases**: Battery monitoring, power management, predictive maintenance

## Repository Structure

Each data model follows the Smart Data Models standard structure:

```
<data_model_name>/
├── schema.json              # JSON Schema definition
├── model.yaml              # YAML model definition
├── README.md               # Data model documentation
├── notes.yaml              # Additional notes and specifications
├── CONTRIBUTORS.yaml       # List of contributors
└── examples/
    ├── example.json                    # Key-values NGSI-v2
    ├── example.jsonld                  # Key-values NGSI-LD
    ├── example-normalized.json         # Normalized NGSI-v2
    └── example-normalized.jsonld       # Normalized NGSI-LD
```

## Integration with ROS2

These data models can be used to:
- Bridge ROS2 topics to FIWARE Context Broker
- Enable cloud-based robot monitoring and control
- Integrate robotic data with IoT ecosystems
- Create digital twins of robotic systems
- Implement fleet management solutions

## Usage Example

### Publishing ROS2 data to FIWARE

```python
# ROS2 node publishing geometry_msgs/Pose
import rclpy
from geometry_msgs.msg import Pose
import requests

def ros_to_ngsi(pose_msg, entity_id):
    """Convert ROS2 Pose to NGSI-LD format"""
    return {
        "id": f"urn:ngsi-ld:GeometryMsgsPose:{entity_id}",
        "type": "GeometryMsgsPose",
        "position": {
            "type": "Property",
            "value": {
                "x": pose_msg.position.x,
                "y": pose_msg.position.y,
                "z": pose_msg.position.z
            }
        },
        "orientation": {
            "type": "Property",
            "value": {
                "x": pose_msg.orientation.x,
                "y": pose_msg.orientation.y,
                "z": pose_msg.orientation.z,
                "w": pose_msg.orientation.w
            }
        },
        "@context": [
            "https://smart-data-models.github.io/dataModel.ROS2/context.jsonld"
        ]
    }
```

## Contributing

Contributions are welcome! Please ensure that:
1. Your data model follows the Smart Data Models guidelines
2. All required files are included (schema.json, model.yaml, examples, etc.)
3. Examples are provided in all required formats
4. Documentation is clear and complete

## License

This work is licensed under the Creative Commons Attribution 4.0 International License.

## References

- [Smart Data Models](https://smartdatamodels.org/)
- [ROS2 Documentation](https://docs.ros.org/)
- [FIWARE NGSI-LD](https://www.etsi.org/deliver/etsi_gs/CIM/001_099/009/01.04.01_60/gs_cim009v010401p.pdf)
- [ROS2 Message Types](http://docs.ros.org/en/rolling/Concepts/About-ROS-Interfaces.html)

## Version

Current version: 0.0.1

## Contributors

See individual CONTRIBUTORS.yaml files in each data model directory.

## Support

For questions or issues, please open an issue in the repository or contact the Smart Data Models initiative.

---

Generated on: 2025-12-02
