from netmiko import ConnectHandler

hosts=["x.x.x.x","x.x.x.x",.....,"x.x.x.x",]
for i in hosts:
    device = {
        "device_type": "ruckus_fastiron",
        "host": i,
        "username": "rohan",
        "password": "@ndr0med@",
        "secret" : "@ndr0med@"
    }

    commands = ["no user ****"]
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_set(commands)
        output += net_connect.save_config()

        print("---------------@",i)
        print("@-------------------")
        print(output)
        print()
