from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pathlib import Path

print("______ ___________")
print("|  ___|_   _| ___ \               ")
print("| |_    | | | |_/ /_____ ___ _ __ ")
print("|  _|   | | |  __/______/ _ \ '__|")
print("| |     | | | |        |  __/ |   ")
print("\_|     \_/ \_|         \___|_|   ")
print("                 made by hackerd25\n")
def pathchecker():
    path = input("The path of the ftp server: ")
    dir = Path(path)
    if dir.is_dir() == 0:
        print("Path doesnt exist.")
        pathchecker()
    return path
def user():
    username = input("Type the name of the username that the server allows: ")
    return username
def ip():
    ip = input("Local computer ip(It is going to crash if it doesnt work): ")
    return ip
def password(passd):
    password = input("Password for " + passd + ": ")
    return password
def portchecker():
    port = int(input("Give a free port higher than 1023(If you dont know just write 2121): "))
    if port < 1023 or port > 65535:
        print("Not in the limits.Try again: ")
        portchecker()
    return port
FTP_HOST = ip()
FTP_PORT = portchecker()

FTP_USER = user()
FTP_PASSWORD = password(FTP_USER)
FTP_DIRECTORY = pathchecker()

def main():
    authorizer = DummyAuthorizer()
    authorizer.add_user(FTP_USER, FTP_PASSWORD, FTP_DIRECTORY, perm='elradfmw')

    handler = FTPHandler
    handler.authorizer = authorizer

    handler.banner = "Lets start pwning!"

    address = (FTP_HOST, FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()

if __name__ == '__main__':
    main()