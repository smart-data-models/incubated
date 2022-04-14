| Title | Data Type | Min Count | Max Count | Description | Example Value | 
| ------- | ------- | ------- | ------- | ------- | ------- | 
 | hasCPU | xsd:string |  0 |  unlimited | A Gaia-x reference Identifier | gax:Intel-Xeon-Platinum-8280 | 
| hasGPU | xsd:string |  0 |  unlimited | A Gaia-x reference Identifier | gax:NVIDIA-A10 | 
| hasRamsize | gax-core:Measure |  0 |  unlimited | a structured object of type measure, e.g. measure:value=950 and measure:unit=GB | 950 GB | 
| hasHarddrive | xsd:string |  0 |  unlimited | a reference ID to that hard drive | gax:Intel-SSD-DC-P4610 | 
| hasNIC | gax-core:Measure |  0 |  unlimited | a structured object of type measure, e.g. measure:value=10 and measure:unit=GBase-T | 10 GBase-T |