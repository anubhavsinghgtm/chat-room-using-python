import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = "192.168.43.57"
port = 1234
s.connect((ip,port))

print("========= Connection is Established =========")
print()

while True:
    msg = input("Enter the message('exit' to close the program): ")
    msg = str.encode(msg)
    s.send(msg)
    if msg.decode() == "exit":
        print()
        print("============ Connection is closed ==============")
        break;
