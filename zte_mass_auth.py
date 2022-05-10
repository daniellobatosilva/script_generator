script = ""

print("ZTE Script Generator for Provisioning ONU's | ZTE C320")
slot = input("Insert the slot number: ")
pon = input("Insert the pon number: ")
vlan = input("Insert the vlan: ")
profile_name = input("Insert the profile name: ")
onu_start_index = input("Insert the ONU starting index: ")
onu_type = input("Insert the ONU type: ")

print("Insert the Unauth ONU SN list for slot {} and pon {} and press enter to save:".format(slot, pon))
onu_list = []
while True:
	line = input()
	if line:
		onu_list.append(line)
	else:
		break
cont = 1
for line in onu_list:
	script_line = '''interface gpon-olt_1/{}/{}
onu {} type {} sn {}
exit
interface gpon-onu_1/{}/{}:{}
tcont 1 profile {}
gemport 1 tcont 1
service-port 1 vport 1 user-vlan {} vlan {}
exit
pon-onu-mng gpon-onu_1/{}/{}:{}
service HSI gemport 1 cos 0 vlan {}
vlan port eth_0/1 mode tag vlan {} pri 0
exit
'''.format(slot, pon, str(int(cont) - 1 + int(onu_start_index)), onu_type, line, slot, pon, cont, profile_name, vlan, vlan, slot, pon, cont, vlan, vlan)
	script += script_line
	cont = cont + 1

print("The script will be displayed below:")
print("-----------------------------------")
print(script)