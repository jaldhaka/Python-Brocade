from netmiko import ConnectHandler

hosts=["10.12.17.10","10.12.17.21","10.12.17.22","10.12.17.23","10.12.17.24","10.12.17.25","10.12.17.26","10.12.17.27","10.12.17.28","10.12.17.29","10.12.17.30","10.12.17.31","10.12.17.32","10.12.17.33","10.12.17.34","10.12.17.35","10.12.17.36","10.12.17.40","10.12.17.41","10.12.17.42","10.12.17.43","10.12.17.44","10.12.17.128","10.12.17.129","10.12.17.130","10.12.17.131",]
for i in hosts:
    device = {
        "device_type": "ruckus_fastiron",
        "host": i,
        "username": "rohan",
        "password": "@ndr0med@",
        "secret" : "@ndr0med@"
    }

    commands = ["no user balraj"]
    with ConnectHandler(**device) as net_connect:
        output = net_connect.send_config_set(commands)
        output += net_connect.save_config()

        print("---------------@",i)
        print("@-------------------")
        print(output)
        print()
