import socket

IP = socket.gethostbyname(socket.gethostname())
PORT = 4455
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"

def main():
    print("Server is starting.")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(ADDR)
    server.listen()
    print("Server is listening.")

    while True:
        conn, addr = server.accept()
        print(f"{addr} connected.")
        filename = conn.recv(SIZE).decode(FORMAT)
        print(f"Receiving the filename.")
        file = open(filename, "w")
        conn.send("Filename received".encode(FORMAT))
        data = conn.recv(SIZE).decode(FORMAT)
        print(f"Receiving the file data.")
        file.write(data)
        conn.send("File data received".encode(FORMAT))
        file.close()
        conn.close()
        print(f"{addr} disconnected.")

if __name__ == "__main__":
    main()
