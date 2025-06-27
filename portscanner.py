import socket

def scan_ports(target, start_port, end_port):
    print(f"Scanning {target} from port {start_port} to {end_port}")

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)

            result = s.connect_ex((target, port))
            if result == 0:
                print("Port " + str(port) + " is OPEN")
            s.close()

        except socket.error:
            print("Couldn't connect to "+ str(target))
            break

target_ipaddress = input("Enter target IP or domain: ")
start = int(input("Enter start port: "))
end = int(input("Enter end port: "))

scan_ports(target_ipaddress, start, end)