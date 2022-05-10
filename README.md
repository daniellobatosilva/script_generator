# Script Generator
A script generator for many configs in multi-vendor equipments.

---

Requirements: Python 3+

---
As I develop new scripts, the project will be updated.
Currently the project has the script generator zte_mass_auth.py, which generates a script for authentication and massive provisioning of ONUs in OLT's ZTE c320.

---
zte_mass_auth.py Usage:

1 - Start the application using zte_mass_auth.py

2 - Enter the data requested by the system:
```console
python3 zte_mass_auth.py
ZTE Script Generator for Provisioning ONU's | ZTE C320
Insert the slot number: 2 (change to your slot num)
Insert the pon number: 6 (change to your pon num)
Insert the vlan: 100 (change to your vlan id)
Insert the profile name: PADRAO (change to your profile name)
Insert the ONU starting index: 1 (check your starting index)
Insert the ONU type: BRIDGE (change to your type name)
Insert the Unauth ONU SN list for slot 2 and pon 6 and press enter to save:
PL1901140430
GPON17092331
DD16B3676B06
PL1901140363
c07e406604E2
```
Attention! The list of SN's to be authenticated must follow the model above, placing the SNs in sequence with a line break. After finishing press "enter" twice to finish.

Below is a video of me using the Script Generator...


https://user-images.githubusercontent.com/55722522/167685568-b5c62b17-041b-4c94-bf2b-e3f769d387a1.mp4

