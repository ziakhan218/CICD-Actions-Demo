import socket

def main():
    s = socket.socket()
    s.connect(("18.168.221.107", 5000))  # Replace this before deploying
    data = s.recv(2048)
    s.close()
    print("Received:", data[:32], "...")  # First 32 bytes + checksum
    with open("received_file.txt", "wb") as f:
        f.write(data.split(b"::")[0])

if __name__ == "__main__":
    main()
