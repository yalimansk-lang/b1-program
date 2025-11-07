devices = [ ("192.168.1.10", [22, 80, 443]),
("192.168.1.11", [21, 22, 80]), ("192.168.1.12", [23,
80, 3389])]

risky_ports = [21, 23, 3389]

print("scanning network devices...")

risk_count = 0

for ip, open_ports in devices:
    for port in open_ports:
        if port == risky_ports:
            print("WORNING:"+ip+"has risky port"+str(port)+"open")
            risk_count = risk_count + 1 

print("scan is complete" + str(risk_count) + "security risks found")




