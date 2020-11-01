import os
import socket

ip = socket.gethostbyname(socket.gethostname())

print(f"Serving at http://{ip}:8000")

os.system("python -m http.server")
