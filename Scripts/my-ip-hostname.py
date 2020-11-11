import socket


print("Computer Host Name is : ", socket.gethostname())
print("Computer IP Address is : ", socket.gethostbyname(socket.gethostname()))
