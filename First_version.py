import socket

def Scan(IP, PORTS):
    for port in PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((IP, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

def Edit(IP, PORTS):
    editchoice = input(":")
    if editchoice.lower() == "ip":
        IP = input("Enter new IP address: ")
    elif editchoice.lower() == "ports":
        portschoice = input("Do you want to add or remove a port? (add/remove): ")
        if portschoice.lower() == "add":
            PORTS.append(int(input("Enter new port to add: ")))
        elif portschoice.lower() == "remove":
            port_to_remove = int(input("Enter port to remove: "))
            print(f"Current Ports: {PORTS}")
            if port_to_remove in PORTS:
                PORTS.remove(port_to_remove)
            else:
                print("Port not found.")
    elif editchoice.lower() == "show":
        print(f"Current IP: {IP}")
        print(f"Current Ports: {PORTS}")
    elif editchoice.lower() == "quit":
        return    
    else:
        print("Invalid edit option.")            

PORTS = [21,22,80,443,8080,42000]
IP = "127.0.0.1"


while True:
    choice = input("->")
    if choice.lower() == "scan" or choice.lower() == "run":
        Scan(IP, PORTS)
    elif choice.lower() == "edit":
        Edit(IP, PORTS)
    elif choice.lower() == "help":
        print("Available commands:")
        print("scan/run - Scan the specified ports")
        print("edit - Edit IP address or port list")
        print("help - Show this help message")
        print("exit/quit - Exit the program")
    elif choice.lower() == "exit" or choice.lower() == "quit":
        break
    else:
        print("Invalid command.")